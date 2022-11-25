# `pcsb`: A `pass` character set builder

    Usage: pcsb [OPTIONS]

      Generate a character set for use with `pass` password generation (or `tr`
      generally).

      By default, every character is included. Exclusions and additions are
      processed in order, so e.g. `-special +at` would result in the character set
      containing letters, digits, and the at symbol.

      Override the `pass` character set with:

          PASSWORD_STORE_CHARACTER_SET=$(pcsb [OPTIONS]) pass generate [OPTIONS]

    Options:
      +letters / -letters          ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu
                                   vwxyz
      +lower / -lower              abcdefghijklmnopqrstuvwxyz
      +upper / -upper              ABCDEFGHIJKLMNOPQRSTUVWXYZ
      +digits / -digits            0123456789
      +special / -special          !"#$%&'()*+,-./:<=>?@[\\]^_`{|}~
      +curly / -curly              {}
      +square / -square            []
      +parens / -parens            ()
      +angle / -angle              <>
      +exclamation / -exclamation  !
      +ampersand / -ampersand      &
      +period / -period            .
      +comma / -comma              ,
      +semicolon / -semicolon      :
      +question / -question        ?
      +plus / -plus                +
      +minus / -minus              -
      +equals / -equals            =
      +pipe / -pipe                |
      +underscore / -underscore    _
      +at / -at                    @
      +octothorpe / -octothorpe    #
      +dollar / -dollar            $
      +percent / -percent          %
      +caret / -caret              ^
      +asterisk / -asterisk        *
      +tilde / -tilde              ~
      +backtick / -backtick        `
      +single / -single            '
      +double / -double            "
      +forward / -forward          /
      +back / -back                \\
      --help                       Show this message and exit.
