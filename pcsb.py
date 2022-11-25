import click

import typing
import enum
import string


class SpecialCharacters(enum.Enum):
    exclamation = "!"
    ampersand = "&"
    period = "."
    comma = ","
    semicolon = ";"
    colon = ":"
    question = "?"

    plus = "+"
    minus = "-"
    equals = "="

    pipe = "|"
    underscore = "_"
    at = "@"
    octothorpe = "#"
    dollar = "$"
    percent = "%"
    caret = "^"
    asterisk = "*"
    tilde = "~"
    backtick = "`"

    single = "'"
    double = '"'

    forward = "/"
    back = "\\\\"


class Brackets(enum.Enum):
    curly = "{}"
    square = "[]"
    parens = "()"
    angle = "<>"


class CharacterSets(enum.Enum):
    letters = set(string.ascii_letters)
    lower = set(string.ascii_lowercase)
    upper = set(string.ascii_uppercase)

    digits = set(string.digits)

    special = {character.value for character in SpecialCharacters}.union(
        *(set(brackets.value) for brackets in Brackets)
    )


def make_include_exclude(characters: typing.Union[CharacterSets, SpecialCharacters]):
    """Construct a callback to handle including or excluding a character or set"""
    if characters in CharacterSets:
        character_set = characters.value
    elif characters in Brackets:
        character_set = set(characters.value)
    else:
        character_set = set([characters.value])

    def include_exclude(
        context: click.Context, parameter: click.Parameter, value: typing.Optional[bool]
    ) -> None:
        if value is not None:
            if value:
                context.obj |= character_set
            else:
                context.obj -= character_set

    return include_exclude


def canonical_set_representation(character_set: set[str], join: str = "") -> str:
    """Sort and display a set of characters"""
    return "".join(sorted(list(character_set)))


def render_help_text(value: typing.Union[str, set[str]]) -> str:
    if isinstance(value, str):
        return value
    else:
        return canonical_set_representation(value, " ")


default_sets = [CharacterSets.letters, CharacterSets.digits, CharacterSets.special]


@click.command(context_settings={"obj": set()})
@click.pass_obj
def cli(characters: set[str]):
    """Generate a character set for use with `pass` password generation (or `tr` generally).

    By default, every character is included. Exclusions and additions are processed
    in order, so e.g. `-special +at` would result in the character set containing
    letters, digits, and the at symbol.

    Override the `pass` character set with:

        PASSWORD_STORE_CHARACTER_SET=$(pcsb [OPTIONS]) pass generate [OPTIONS]
    """
    click.echo(canonical_set_representation(characters))


for character in list(CharacterSets) + list(Brackets) + list(SpecialCharacters):
    name = character.name
    click.option(
        f"+{name}/-{name}",
        default=True if character in default_sets else None,
        expose_value=False,
        callback=make_include_exclude(character),
        help=render_help_text(character.value),
    )(cli)
