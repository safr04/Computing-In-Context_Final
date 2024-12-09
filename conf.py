import os
import sys

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath("."))

# Project information
project = "Computing in Context - Shazia Rehman"
author = "Shazia Rehman"

# General Sphinx configuration
extensions = [
    "myst_parser",  # Add support for Markdown files with MyST
    "sphinx.ext.mathjax",  # Math support
    "sphinx.ext.autodoc",  # Documentation for Python code
]

# Source file parsers
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Master document (main entry point for Sphinx)
master_doc = "intro"  # Set this to the name of your main file (e.g., "intro.md")

# MyST-specific settings
myst_enable_extensions = [
    "colon_fence",  # Support for ::: directives
    "dollarmath",  # Support for inline and block math
]

# Suppress warnings to handle unknown directives like `tableofcontents` or `code-cell`
suppress_warnings = [
    "myst.directive_unknown",
    "myst.role_unknown",
]

# HTML settings
html_theme = "sphinx_rtd_theme"
