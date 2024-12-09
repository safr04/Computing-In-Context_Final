import os
import sys

sys.path.insert(0, os.path.abspath("."))

project = "Computing in Context - Shazia Rehman"
author = "Shazia Rehman"

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "alabaster"
