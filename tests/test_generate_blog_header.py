"""Command-line smoke tests for the blog header generator."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = REPOSITORY_ROOT / 'tools' / 'generate_blog_header.py'


class GenerateBlogHeaderSmokeTest(unittest.TestCase):
    def run_generator(self, *arguments):
        """Run the generator as a user would from the repository root."""
        return subprocess.run(
            [sys.executable, str(GENERATOR), *map(str, arguments)],
            cwd=REPOSITORY_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def assert_valid_header(self, output_path):
        """Check stable PNG properties rather than renderer-specific pixels."""
        self.assertTrue(output_path.is_file())
        with Image.open(output_path) as image:
            image.verify()
        with Image.open(output_path) as image:
            self.assertEqual(image.format, 'PNG')
            self.assertEqual(image.size, (1200, 630))
            self.assertEqual(image.mode, 'RGB')
            self.assertIsNotNone(image.getbbox())

    def test_title_only_creates_missing_output_directory(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / 'missing' / 'header.png'

            result = self.run_generator(
                'A representative blog title', '-o', output
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_valid_header(output)

    def test_title_with_subtitle_creates_valid_header(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / 'header-with-subtitle.png'

            result = self.run_generator(
                'A representative blog title',
                '--subtitle',
                'A useful explanatory subtitle',
                '--output',
                output,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_valid_header(output)

    def test_missing_fonts_fail_with_clear_message(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            temporary_generator = temporary_root / 'tools' / GENERATOR.name
            temporary_generator.parent.mkdir()
            shutil.copy2(GENERATOR, temporary_generator)
            output = temporary_root / 'header.png'

            result = subprocess.run(
                [
                    sys.executable,
                    str(temporary_generator),
                    'Title',
                    '-o',
                    str(output),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn('Required font asset is missing:', result.stderr)
            self.assertFalse(output.exists())

    def test_incompatible_fonts_fail_with_clear_message(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            temporary_generator = temporary_root / 'tools' / GENERATOR.name
            temporary_generator.parent.mkdir()
            shutil.copy2(GENERATOR, temporary_generator)
            font_directory = (
                temporary_root / 'assets' / 'lib' / 'fonts' / 'Source_Sans_Pro'
            )
            font_directory.mkdir(parents=True)
            for font_name in ('SourceSansPro-Bold.ttf',
                              'SourceSansPro-Regular.ttf'):
                (font_directory / font_name).write_text('not a font')

            result = subprocess.run(
                [
                    sys.executable,
                    str(temporary_generator),
                    'Title',
                    '-o',
                    str(temporary_root / 'header.png'),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                'Required font asset is incompatible or unreadable:',
                result.stderr,
            )


if __name__ == '__main__':
    unittest.main()
