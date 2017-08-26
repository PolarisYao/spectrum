"""Based on Sphinx configuration example with the proper extensions


"""
# -*- coding: utf-8 -*-
#
# documentation build configuration file, created by
# sphinx-quickstart on Wed Dec  2 17:50:25 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import sphinx

sys.path.insert(0, os.path.abspath('sphinxext'))
import sphinx_gallery

###########################ADDON############################
try:
    import easydev
    from easydev import get_path_sphinx_themes
except Exception, e:
    print "Install easydev or set your PYTHONPATH properly"
    raise Exception


import pkg_resources
version = pkg_resources.require("spectrum")[0].version
release = version
author = "Thomas Cokelaer"
title = "spectrum"
copyright = author + ", 2012-2017"
project = "spectrum"




#NOTHING to change below in principle
##########################################################


# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc',

    ('sphinx.ext.imgmath'  # only available for sphinx >= 1.4
                  if sphinx.version_info[:2] >= (1, 4)
                  else 'sphinx.ext.pngmath'),
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    "numpydoc.numpydoc",
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.autosummary',
    'sphinx_gallery.gen_gallery',
    ]
# note that the numpy directives is buggy. Example: class and init are not recognised as two entities for the autoclass_content=both here below


todo_include_todos=True
jscopybutton_path = easydev.copybutton.get_copybutton_path()
autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = project
copyright = copyright


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']
exclude_patterns = []



# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.

# -- sphinx gallery ------------------------------------------------------------
plot_gallery = True
sphinx_gallery_conf = {
    "doc_module": "spectrum",
    "examples_dirs": "../../examples",
#    "gallery_dirs": "auto_examples",
    "backreferences_dir": "True"
}

# Get rid of spurious warnings due to some interaction between
# autosummary and numpydoc. See
# https://github.com/phn/pytpm/issues/3#issuecomment-12133978 for more
# details
numpydoc_show_class_members = False


# solution from nilearn
def touch_example_backreferences(app, what, name, obj, options, lines):
    # generate empty examples files, so that we don't get
    # inclusion errors if there are no examples for a class / module
    examples_path = os.path.join(app.srcdir, "modules", "generated",
                                 "%s.examples" % name)
    if not os.path.exists(examples_path):
        # touch file
        open(examples_path, 'w').close()



# Add the 'copybutton' javascript, to hide/show the prompt in code
# examples
def setup(app):
    app.add_javascript('copybutton.js')
    app.connect('autodoc-process-docstring', touch_example_backreferences)





# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = "standard"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# the user theme contains the otpions 'homepage', which is populated here
#html_theme_options = {'homepage': init_sphinx.url}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [easydev.get_path_sphinx_themes()]


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = "spectrum" + ' ('+version +')'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = "spectrum"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.join('logo.png')


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = os.path.join(openalea, 'images', 'oaicon.ico')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static', os.path.join(extensionPath, '_static')]
#html_style = 'mine.css'
# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_index = 'index.html'

#Custom sidebar templates, maps page names to templates.
html_sidebars = {
                    'index': [ 'indexsidebar.html'], 
                    'contents':'indexsidebar.html',


}
# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {   'index': 'index.html'}


# If false, no module index is generated.
html_use_modindex = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True
#html_copy_source = False


# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'doc'


# -- Options for LaTeX output --------------------------------------------------

# NOT in original quickstart
pngmath_use_preview = True

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'main.tex', title,
   author, 'manual'),
]

latex_elements = { 'inputenc': '\\usepackage[utf8]{inputenc}' }

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = 

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False
# If true, show page references after internal links.
#latex_show_pagerefs = False

# Additional stuff for the LaTeX preamble.
latex_preamble = r"""
   \usepackage{amsmath}
   \usepackage{amsfonts}
   \usepackage{amssymb}
   \usepackage{txfonts}

\definecolor{VerbatimColor}{rgb}{.9,1,0.9}
\definecolor{VerbatimBorderColor}{rgb}{0,0,0}

   \setlength{\fboxrule}{2pt}
 
 \renewcommand{\Verbatim}[1][1]{%
   % list starts new par, but we don't want it to be set apart vertically
   \bgroup\parskip=0pt%
   \smallskip%
   % The list environement is needed to control perfectly the vertical
   % space.
   \list{}{%
   \setlength\parskip{5pt}% space between verbatim and previous paragraph
   \setlength\itemsep{0ex}%
   \setlength\topsep{1ex}%
   \setlength\partopsep{0pt}%
   \setlength\leftmargin{10pt}%
   }%
   \item\MakeFramed {\FrameRestore}%
      \small%
     \OriginalVerbatim[#1]%
 }

"""

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', project, project,
     [author], 1)
]


# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://docs.python.org/': None}
intersphinx_mapping = {}
