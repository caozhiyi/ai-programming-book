from setuptools import setup

setup(
    name="mkdocs-seo-canonical",
    version="0.1.0",
    description="Honor frontmatter canonical key as page canonical URL",
    py_modules=["seo_canonical"],
    entry_points={
        "mkdocs.plugins": ["seo-canonical = seo_canonical:SeoCanonicalPlugin"],
    },
)
