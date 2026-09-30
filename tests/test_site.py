from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted(
    path
    for path in ROOT.rglob("*.html")
    if not {".git", ".local", ".cache", "node_modules"}.intersection(path.parts)
)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_title = False
        self.has_main = False
        self.resources = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "title":
            self.has_title = True
        elif tag == "main":
            self.has_main = True

        if tag in {"img", "script", "source"} and attributes.get("src"):
            self.resources.append(attributes["src"])
        elif tag == "link" and attributes.get("href"):
            relation = set(attributes.get("rel", "").split())
            if relation & {"stylesheet", "icon", "preload", "apple-touch-icon"}:
                self.resources.append(attributes["href"])


class StaticSiteTests(unittest.TestCase):
    def test_essential_pages_exist(self):
        for page in (
            "index.html",
            "about/index.html",
            "products/index.html",
            "retailers/index.html",
            "contact/index.html",
        ):
            with self.subTest(page=page):
                self.assertTrue((ROOT / page).is_file())

    def test_pages_have_titles_and_main_content(self):
        for page in PAGES:
            with self.subTest(page=str(page.relative_to(ROOT))):
                parser = PageParser()
                parser.feed(page.read_text(encoding="utf-8"))
                self.assertTrue(parser.has_title, "Page is missing a title")
                if page.name != "404.html":
                    self.assertTrue(parser.has_main, "Page is missing a main landmark")

    def test_local_static_resources_exist(self):
        for page in PAGES:
            parser = PageParser()
            parser.feed(page.read_text(encoding="utf-8"))
            for reference in parser.resources:
                url = urlsplit(reference)
                if url.scheme or url.netloc or reference.startswith("//"):
                    continue
                resource = unquote(url.path)
                if not resource:
                    continue
                destination = (
                    ROOT / resource.lstrip("/")
                    if resource.startswith("/")
                    else page.parent / resource
                )
                with self.subTest(page=str(page.relative_to(ROOT)), resource=reference):
                    self.assertTrue(destination.is_file(), "Local resource is missing")


if __name__ == "__main__":
    unittest.main()