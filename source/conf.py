# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'benchmark-docs'
copyright = '2025, J Mitchell'
author = 'J Mitchell'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions =  [
    "sphinx_design",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    ]

templates_path = ['_templates']
exclude_patterns = []


pygments_style = "manni"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_material"
html_title = "NEST Benchmark Documentation"
html_logo = "_static/img/nest_logo.png"

html_theme_options = {
    # Set the name of the project to appear in the navigation.
    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',
    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    "base_url": "https://nest-simulator.readthedocs.io/en/stable/",
    "html_minify": False,
    "html_prettify": False,
    "css_minify": True,
    # Set the color and the accent color
    "color_primary": "orange",
    "color_accent": "white",
    "theme_color": "ff6633",
    "master_doc": False,
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/nest/nest-simulator/",
    "repo_name": "NEST Simulator",
    "nav_links": [{"href": "https://nest-simulator.org/documentation", "internal": False, "title": "NEST Docs Home"}],
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": True,
    "version_dropdown": False,
}

html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
    "css/pygments.css",
]

html_js_files = [
    "js/custom.js",
]
html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}

html_favicon = "_static/img/nest_favicon.ico"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "nest": ("https://nest-simulator.readthedocs.io/en/stable/", None),
    "nestml": ("https://nestml.readthedocs.io/en/latest/", None),
    "desktop": ("https://nest-desktop.readthedocs.io/en/latest/", None),
    "gpu": ("https://nest-gpu.readthedocs.io/en/latest/", None),
    "neat": ("https://nest-neat.readthedocs.io/en/latest/", None),
    "pd14": ("https://microcircuit-pd14-model.readthedocs.io/en/latest", None),
    "extmod": ("https://nest-extension-module.readthedocs.io/en/latest/", None),
}

