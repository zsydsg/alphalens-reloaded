# -*- coding: utf-8 -*-
import sys
import os

from alphalens import __version__ as version

sys.path.insert(0, os.path.abspath("../.."))

extensions = ["sphinx.ext.autodoc", "numpydoc"]

templates_path = ["_templates"]

source_suffix = ".rst"

master_doc = "index"

project = "Alphalens"
copyright = "2016, Quantopian, Inc."
author = "Quantopian, Inc."

release = version
language = None

exclude_patterns = []

pygments_style = "sphinx"

todo_include_todos = False

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

htmlhelp_basename = "Alphalensdoc"

latex_elements = {}

latex_documents = [
    (
        master_doc,
        "Alphalens.tex",
        "Alphalens Documentation",
        "Quantopian, Inc.",
        "manual",
    )
]

man_pages = [(master_doc, "alphalens", "Alphalens Documentation", [author], 1)]

texinfo_documents = [
    (
        master_doc,
        "Alphalens",
        "Alphalens Documentation",
        author,
        "Alphalens",
        "One line description of project.",
        "Miscellaneous",
    )
]
