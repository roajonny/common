# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hardware-as-Software'
copyright = '2025, Jonathan Roa'
author = 'AUTHOR'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx-needs didn't include this command as part of the install procedure
import os

# Sphinx-needs directions needed syntax correction to get this working
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
else:
    plantuml = 'java -jar %s' % (os.path.join(os.path.dirname(__file__), "utils", "plantuml.jar"))

    plantuml_output_format = 'png'

extensions = [
    'sphinxcontrib.mermaid',
    'sphinxcontrib.plantuml',
    'sphinx_needs'
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = 'Hardware-as-Software (v0.1)'
#html_static_path = ['_static']

# Also required by sphinx-needs to render objects properly but not explained
# that well in the install procedure
needs_css = 'dark.css'
