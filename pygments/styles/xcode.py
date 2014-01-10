# -*- coding: utf-8 -*-
"""
    pygments.styles.xcode
    ~~~~~~~~~~~~~~~~~~~~~~

    Style similar to the `Xcode` default theme.

    :copyright: Copyright 2006-2013 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Text, Other, Literal, Punctuation


class XcodeStyle(Style):
    """
    Style similar to the Xcode default colouring theme.
    """

    default_style = ''

    styles = {
        Comment:                '#177500',
        Comment.Preproc:        '#633820',

        String:                 '#C41A16',
        String.Char:            '#2300CE',
        
        Operator:               '#000000',

        Keyword:                '#AA0D92',

        Name:                   '#000000',
        Name.Attribute:         '#836C28',
        Name.Class:             '#000000',
        Name.Function:          '#000000',
        Name.Builtin:           '#AA0D92',
        Name.Builtin.Pseudo:    '#5B269A',          # In Obj-C code this token is used to colour Cocoa types
        Name.Variable:          '#000000',
        Name.Tag:               '#000000',
        Name.Decorator:         '#000000',
        Name.Label:             '#000000',          # Workaround for a BUG here: lexer treats multiline method signatres as labels

        Number:                 '#2300CE',
        Error:                  '#000000',
    }