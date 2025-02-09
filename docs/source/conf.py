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
    'sphinx_needs',
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

# Needs object configuration
needs_types = [
    {
        "directive": "tutorial-project",
        "title": "Project",
        "prefix": "P_",  # prefix for auto-generated IDs
        "style": "rectangle", # style for the type in diagrams
        "color": "#BFD8D2", # color for the type in diagrams
    }
]
needs_types = [dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"),
               dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="node"),
               dict(directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"),
               # Kept for backwards compatibility
               dict(directive="need", title="Need", prefix="N_", color="#9856a5", style="node"),

               # Custom
               dict(directive="tutorial-project", title="Project", prefix="P_", color="#BFD8D2", style="rectangle"),
           ]
need_extra_links = [
  {
    "option": "tutorial_required_by",
    "incoming": "requires",  # text to describe incoming links
    "outgoing": "required by",  # text to describe outgoing links
    "style": "#00AA00"  # color for the link in diagrams
  }
]
