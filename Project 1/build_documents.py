"""Build review-only PDF artifacts from the matching Markdown records."""
from html import escape
from pathlib import Path
import hashlib
import json
import re
import shutil

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                               TableStyle, PageBreak, Image, KeepTogether)

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'output/pdf'
NAVY = colors.HexColor('#173146')
TEAL = colors.HexColor('#14736B')
GRAY = colors.HexColor('#52616B')
BODY_SIZE, BODY_LEADING = 9.4, 13.1


def ascii_text(text):
    substitutions = {'—': '-', '–': '-', '−': '-', '≤': '<=', '≥': '>=', '→': 'to',
                     'Δ': 'Change ', '×': 'x', '’': "'", '‘': "'", '“': '"', '”': '"',
                     '\u202f': ' ', '\u00a0': ' '}
    for old, new in substitutions.items():
        text = text.replace(old, new)
    return text


def inline(text):
    text = escape(ascii_text(text))
    text = re.sub(r'\[([^]]+)\]\(([^)]+)\)', r'<link href="\2" color="#14736B">\1</link>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'`([^`]+)`', r'<font name="Courier" size="8">\1</font>', text)
    return text


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle('ReportTitle', fontName='Helvetica-Bold', fontSize=25,
                         leading=29, textColor=NAVY, spaceAfter=15))
    s.add(ParagraphStyle('Section', fontName='Helvetica-Bold', fontSize=12,
                         leading=16, textColor=TEAL, spaceBefore=12, spaceAfter=6,
                         keepWithNext=True))
    s.add(ParagraphStyle('BodyCopy', fontName='Helvetica', fontSize=BODY_SIZE,
                         leading=BODY_LEADING, textColor=NAVY, spaceAfter=7,
                         splitLongWords=True))
    s.add(ParagraphStyle('Cell', parent=s['BodyCopy'], fontSize=8, leading=10.5, spaceAfter=0))
    s.add(ParagraphStyle('Source', parent=s['BodyCopy'], fontSize=7.5, leading=10))
    return s


def markdown_story(text, memo=False):
    s = styles()
    lines = text.splitlines()
    story = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith('|'):
            raw = []
            while index < len(lines) and lines[index].strip().startswith('|'):
                row = [x.strip() for x in lines[index].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+', x) for x in row):
                    raw.append(row)
                index += 1
            count = len(raw[0])
            width = 512 / count
            cells = [[Paragraph(inline(x), s['Cell']) for x in row] for row in raw]
            table = Table(cells, colWidths=[width] * count, repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#E4F0ED')),
                ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ('LINEBELOW', (0,0), (-1,0), .7, TEAL),
                ('LINEBELOW', (0,1), (-1,-1), .25, colors.HexColor('#CBD6DC')),
                ('LEFTPADDING', (0,0), (-1,-1), 6),
                ('RIGHTPADDING', (0,0), (-1,-1), 6),
                ('TOPPADDING', (0,0), (-1,-1), 6),
                ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ]))
            story += [Spacer(1,5), table, Spacer(1,7)]
            continue
        if line.startswith('# '):
            story.append(Paragraph(inline(line[2:]), s['ReportTitle']))
        elif line.startswith('## '):
            if memo and line.startswith('## Conditions'):
                story.append(PageBreak())
            story.append(Paragraph(inline(line[3:]), s['Section']))
        else:
            paragraph = [line]
            index += 1
            while index < len(lines) and lines[index].strip() and not lines[index].startswith(('#', '|', '- ')):
                paragraph.append(lines[index].strip())
                index += 1
            content = ' '.join(paragraph)
            st = s['Source'] if content.startswith(('https://', 'Sources:')) else s['BodyCopy']
            story.append(Paragraph(inline(content), st))
            continue
        index += 1
    return story


def footer(canvas, doc):
    canvas.setTitle('FIN 43900 - NuScale')
    canvas.setAuthor('')
    canvas.setStrokeColor(TEAL)
    canvas.setLineWidth(1)
    canvas.line(50, 752, 562, 752)
    canvas.setFillColor(GRAY)
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(50, 762, 'FIN 43900  /  NUSCALE')
    canvas.setFont('Helvetica', 7.5)
    canvas.drawString(50, 28, 'NuScale Power Corporation | Project 1')
    canvas.drawRightString(562, 28, str(doc.page))


def main():
    global BODY_SIZE, BODY_LEADING
    OUTPUT.mkdir(parents=True, exist_ok=True)
    definitions = [
        ('decision-memo.md', 'Decision-Memo.pdf', 'decision-memo.pdf'),
        ('research-evolution.md', 'Research-Evolution.pdf', 'research-evolution.pdf'),
        ('validation-and-ai-use.md', 'Validation-and-AI-Use.pdf', 'validation-and-ai-use.pdf'),
    ]
    records = []
    for source, name, copy in definitions:
        BODY_SIZE, BODY_LEADING = (9.2, 12.6) if source == 'validation-and-ai-use.md' else (9.4, 13.1)
        story = markdown_story((ROOT / 'docs' / source).read_text(), memo=source == 'decision-memo.md')
        if source == 'research-evolution.md':
            story.append(PageBreak())
            s = styles()
            story.append(Paragraph('Supporting lab screenshots', s['ReportTitle']))
            story.append(Paragraph('These images support the dated lab attempt and grade. The student reports professor approval to submit Edition A as text; the supplied text is preserved earlier in this document.', s['BodyCopy']))
            for path in sorted((ROOT / 'docs').glob('Screenshot*.png')):
                width, height = ImageReader(str(path)).getSize()
                scale = min(512 / width, 225 / height)
                story += [Spacer(1,15), Image(str(path), width * scale, height * scale, hAlign='LEFT')]
        doc = SimpleDocTemplate(str(OUTPUT / name), pagesize=(612,792),
                                leftMargin=50, rightMargin=50, topMargin=58,
                                bottomMargin=46, title='NuScale review draft', allowSplitting=True)
        doc.build(story, onFirstPage=footer, onLaterPages=footer)
        shutil.copy2(OUTPUT / name, ROOT / 'docs' / copy)
        records.append(dict(source='docs/' + source,
                            source_sha256=hashlib.sha256((ROOT / 'docs' / source).read_bytes()).hexdigest(),
                            pdf='output/pdf/' + name,
                            pdf_sha256=hashlib.sha256((OUTPUT / name).read_bytes()).hexdigest(),
                            repository_copy='docs/' + copy))
        print(name)
    (ROOT / 'evidence/document-sources.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
