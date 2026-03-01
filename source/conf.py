# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Blog'
copyright = '2025, Wufei Ma'
author = 'Wufei Ma'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys
from pathlib import Path
sys.path.append(str(Path('_ext').resolve()))

extensions = [
    # 'sphinx_rtd_theme',
    'sphinx_design',
    # 'sphinx_tags',
    'mybadges',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = 'Blog'

# sphinx-tags
# tags_create_tags = True

rst_prolog = """
.. |area-llm| replace:: :bdg-blue-line:`LLM`
.. |area-vlm| replace:: :bdg-lightblue-line:`VLM`
.. |area-rl| replace:: :bdg-purple-line:`RL`
.. |area-3d| replace:: :bdg-orange-line:`3D`
.. |area-pt| replace:: :bdg-green-line:`Pretraining`
.. |area-dl| replace:: :bdg-amber-line:`DL`
.. |area-video| replace:: :bdg-pink-line:`Video`
.. |area-robot| replace:: :bdg-indigo-line:`Robotics`
.. |area-gen| replace:: :bdg-deeporange-line:`Generation`
.. |area-math| replace:: :bdg-teal-line:`Math`
.. |area-dl| replace:: :bdg-lime-line:`Deep Learning`
.. |area-vision| replace:: :bdg-lightblue-line:`Vision`
.. role:: ul
   :class: ul
.. role:: bul
   :class: bul
.. role:: orange
"""


def setup(app: Sphinx) -> None:
    app.add_css_file('css/mycss.css')
