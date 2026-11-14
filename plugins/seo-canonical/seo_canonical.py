"""mkdocs plugin: honor a `canonical` frontmatter key as the page canonical URL.

Pages duplicated from the main site (essay appendices published first at
caozhiyi.cc/zh|en/articles/...) set `canonical:` in frontmatter; this plugin
rewrites `page.canonical_url` so the theme emits rel=canonical pointing at
the original article instead of the book copy.
"""
import mkdocs.plugins


class SeoCanonicalPlugin(mkdocs.plugins.BasePlugin):
    def on_page_context(self, context, page=None, config=None, nav=None):
        canonical = (page.meta or {}).get("canonical") if page else None
        if canonical:
            page.canonical_url = canonical
        return context
