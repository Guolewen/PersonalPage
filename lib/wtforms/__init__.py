"""
WTForms
=======

WTForms is a flexible forms validation and rendering library for python web
development.

:copyright: Copyright (c) 2008 by the WTForms team.
:license: BSD, see LICENSE.rst for details.
"""
from . import validators, widgets
from .fields import *
from .form import Form
from .validators import ValidationError

__version__ = '2.2.1'
