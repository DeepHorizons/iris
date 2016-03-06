"""
The function to parse through the string
"""

import iris.plugins.loader
import nltk


def evaluate(string):
    """
    Given a string, return a response or None

    :param string:
    :return:
    """

    grammars = iris.plugins.loader.get_all_grammars()

    passed = []
    for grammar in grammars:
        wer = error_rate(string, grammar)

        if wer <= 5:
            passed += (wer, grammar, grammars[grammar])
    if not passed:
        raise Exception("No matching grammar found")
    chosen_grammar = choose(passed)
    pos = get_positions(string, chosen_grammar[0])

    return chosen_grammar[1](*pos, text=string)


def choose(lst):
    """
    Choose one and only one grammar from a list
    :param lst: a three tuple containing the word error, grammar, and function
    :return:
    """
    m = ("", None)
    for i in lst:
        if len(i[1]) > len(m):
            m = (len(i[1]), i[2])  # drop the WER
    return m


def error_rate(string, grammar):
    """
    Calculate the Word Error Rate of a grammar from a string

    :param string: The
    :param grammar:
    :return:
    """
    # TODO implement this
    return nltk.edit_distance(string, grammar)


def get_positions(string, grammar):
    """
    Get the positional values in a grammar from a string

    :param string: The
    :param grammar:
    :return:
    """
    # TODO implement this
    return ()


def expand_grammar(grammar, grammar_func):
    lst = [grammar]
    while '[' in lst[0]:
        for elm in lst:
            l = elm.find('[')
            r = elm.find(']', l+1)
            splice = 0  # needed to commit
