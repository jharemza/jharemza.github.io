"""
Script to generate a styled blog header image using Pillow.

Usage:
    python generate_blog_header.py "Main Title"
        --subtitle "Optional Subtitle"
        -o assets/img/headers/example.png
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1200, 630
BG_COLOR = (246, 248, 250)
TEXT_COLOR = (29, 29, 29)
SUBTEXT_COLOR = (113, 113, 113)
ACCENT_COLOR = (0, 86, 178)
MARGIN = 60

FONT_DIR = (
    Path(__file__).resolve().parent.parent
    / 'assets' / 'lib' / 'fonts' / 'Source_Sans_Pro'
)
FONT_BOLD = FONT_DIR / 'SourceSansPro-Bold.ttf'
FONT_REGULAR = FONT_DIR / 'SourceSansPro-Regular.ttf'

TITLE_FONT_SIZE = 80
SUBTITLE_FONT_SIZE = 48


def draw_centered_text(draw, text, font, y):
    """
    Wrap and center-align text within the image boundaries.
    Returns updated y-position after rendering text block.
    """
    lines = []
    if not text:
        return y
    words = text.split()
    line = []
    for word in words:
        test_line = " ".join(line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= WIDTH - 2 * MARGIN:
            line.append(word)
        else:
            lines.append(" ".join(line))
            line = [word]
    if line:
        lines.append(" ".join(line))

    for ln in lines:
        bbox = draw.textbbox((0, 0), ln, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        draw.text(((WIDTH - w) / 2, y),
                  ln,
                  fill=TEXT_COLOR if font != SUBTITLE_FONT else SUBTEXT_COLOR,
                  font=font
                  )
        y += h + 10
    return y


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate a blog header image'
        )
    parser.add_argument(
        'title',
        help='Blog post title'
        )
    parser.add_argument(
        '--subtitle',
        help='Optional subtitle',
        default=''
        )
    parser.add_argument(
        '-o',
        '--output',
        help='Output PNG file path',
        required=True
        )
    args = parser.parse_args()

    # Create image canvas
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    title_font = ImageFont.truetype(str(FONT_BOLD), TITLE_FONT_SIZE)
    global SUBTITLE_FONT
    SUBTITLE_FONT = ImageFont.truetype(str(FONT_REGULAR), SUBTITLE_FONT_SIZE)

    # Render text
    y = HEIGHT // 3 - TITLE_FONT_SIZE
    y = draw_centered_text(draw, args.title, title_font, y)
    if args.subtitle:
        y += 20
        draw_centered_text(draw, args.subtitle, SUBTITLE_FONT, y)

    # Draw accent bar at bottom
    draw.rectangle([0, HEIGHT - 20, WIDTH, HEIGHT], fill=ACCENT_COLOR)

    # Save image
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, format='PNG')
