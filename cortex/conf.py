# -*- coding: utf-8 -*-
#
# test documentation build configuration file, created by
# sphinx-quickstart on Thu Nov 16 11:07:03 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_parsers = {
}
source_suffix = '.rst'

pygments_style = 'monokai'

# The master toctree document.
master_doc = 'docs-home'

# General information about the project.
project = u'PROS for Cortex'
copyright = u'{}, Purdue ACM SIGBots. Released under the MPL 2.0 license'.format(datetime.now().year)
author = u'Purdue ACM SIGBots'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'Cortex (2.12.1)'
# The full version, including alpha/beta/rc tags.
release = u'2.12.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# Modifications to the default Sphinx-quickstart output
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["../sphinx_rtd_theme"]
html_context = {
    'display_github': True,
    'github_user': 'purduesigbots',
    'github_repo': 'pros-docs',
    'github_version': 'master/'
}
html_theme_options = {
    #'analytics_id': INSERT GOOGLE ANALYTICS CODE
    'versions': {
        'V5': '../v5/docs-home',
        'Cortex': 'docs-home',
    }
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "../common/images/logo.svg"
html_favicon = "../common/_static/favicon.ico"

# html_title = ""
html_additional_pages = {
    #'index': 'index.html'
}

html_show_sphinx = False
highlight_language = "c"
