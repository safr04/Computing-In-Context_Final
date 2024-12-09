import os
import sys

# Point to the directory containing the `_config.yml`
sys.path.insert(0, os.path.abspath("."))
from sphinx_config import create_sphinx_config

# Load the configuration from the Jupyter Book `_config.yml`
config = create_sphinx_config("_config.yml")
globals().update(config)
