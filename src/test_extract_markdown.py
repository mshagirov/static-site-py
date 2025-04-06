import unittest
from converter import extract_markdown_images, extract_markdown_links

class TestExtractFromMarkdown(unittest.TestCase):
    def test_extract_link(self):
        matches = extract_markdown_links(
            "Normal text with a [link anchor text](https://my.blog.com/abcd123!@#$%^&*_-+=)"
        )
        answer = [('link anchor text', 'https://my.blog.com/abcd123!@#$%^&*_-+=')]
        self.assertEqual(answer, matches)

        # ignore images
        img_matches = extract_markdown_links(
            "Normal text with an ![image_alt_text](https://img.source.com/abcd123!@#$%^&*_-+=.png)"
        )
        self.assertEqual([], img_matches)


    def test_extract_images(self):
        # extract image alt text and link
        matches = extract_markdown_images(
            "Normal text with an ![image_alt_text](https://img.source.com/abcd123!@#$%^&*_-+=.png)"
        )
        answer = [('image_alt_text', 'https://img.source.com/abcd123!@#$%^&*_-+=.png')]
        self.assertEqual(answer, matches)

        # should ignore normal links
        link_matches = extract_markdown_images(
            "Normal text with a [link anchor text](https://my.blog.com/abcd123!@#$%^&*_-+=)"
        )
        self.assertEqual([], link_matches)


