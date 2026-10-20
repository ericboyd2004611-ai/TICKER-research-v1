"""Render PDFs and check page/text bounds for visual review."""
from pathlib import Path
import json
import pymupdf
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent


def main():
    target = ROOT / 'tmp/pdf-qa'
    target.mkdir(parents=True, exist_ok=True)
    checks = []
    for path in sorted((ROOT / 'output/pdf').glob('*.pdf')):
        doc = pymupdf.open(path)
        images = []
        for index, page in enumerate(doc):
            pix = page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False)
            name = target / f'{path.stem}-{index+1}.png'
            pix.save(name)
            images.append(Image.open(name).convert('RGB'))
            for block in page.get_text('blocks'):
                if block[0] < -1 or block[1] < -1 or block[2] > page.rect.width + 1 or block[3] > page.rect.height + 1:
                    raise ValueError(f'Text outside page: {path.name}, {index+1}')
        if path.name.startswith('Decision-Memo') and len(doc) > 2:
            raise ValueError('Decision memo exceeds two pages')
        width = 700
        height = int(images[0].height * width / images[0].width)
        sheet = Image.new('RGB', (width * 2, (height + 28) * ((len(images)+1)//2)), '#DDE4E8')
        drawing = ImageDraw.Draw(sheet)
        for index, picture in enumerate(images):
            x, y = index % 2 * width, index // 2 * (height + 28)
            drawing.text((x+12, y+7), f'{path.name} - page {index+1}', fill='#173146')
            sheet.paste(picture.resize((width,height)), (x,y+28))
        sheet.save(target / f'{path.stem}-contact.png')
        checks.append(dict(file=path.name, pages=len(doc), text_bounds='PASS', rendered_pages=len(images)))
    (ROOT / 'evidence/pdf-checks.json').write_text(json.dumps(checks, indent=2) + '\n')
    print(json.dumps(checks, indent=2))


if __name__ == '__main__':
    main()
