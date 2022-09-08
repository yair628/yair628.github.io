# https://github.com/mohd-akram/base16-pygments/blob/master/pygments_base16/base16-tomorrow.py

from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, String, Text
)


class Base16Style(Style):
    base00 = '#ffffff'
    base01 = '#e0e0e0'
    base02 = '#d6d6d6'
    base03 = '#8e908c'
    base04 = '#969896'
    base05 = '#4d4d4c'
    base06 = '#282a2e'
    base07 = '#1d1f21'
    base08 = '#c82829'
    base09 = '#f5871f'
    base0a = '#eab700'
    base0b = '#718c00'
    base0c = '#3e999f'
    base0d = '#4271ae'
    base0e = '#8959a8'
    base0f = '#a3685a'

    default_style = ''

    background_color = base00
    highlight_color = base02

    styles = {
        Text: base05,
        Error: base08,  # .err

        Comment: base03,  # .c
        Comment.Preproc: base0f,  # .cp
        Comment.PreprocFile: base0b,  # .cpf

        Keyword: base0e,  # .k
        Keyword.Type: base08,  # .kt

        Name.Attribute: base0d,  # .na
        Name.Builtin: base0d,  # .nb
        Name.Builtin.Pseudo: base08,  # .bp
        Name.Class: base0d,  # .nc
        Name.Constant: base09,  # .no
        Name.Decorator: base09,  # .nd
        Name.Function: base0d,  # .nf
        Name.Namespace: base0d,  # .nn
        Name.Tag: base0e,  # .nt
        Name.Variable: base0d,  # .nv
        Name.Variable.Instance: base08,  # .vi

        Number: base09,  # .m

        Operator: base0c,  # .o
        Operator.Word: base0e,  # .ow

        Literal: base0b,  # .l

        String: base0b,  # .s
        String.Interpol: base0f,  # .si
        String.Regex: base0c,  # .sr
        String.Symbol: base09,  # .ss
    }


from string import capwords  # noqa: E402
Base16Style.__name__ = 'Base16{}Style'.format(
    capwords('tomorrow', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
