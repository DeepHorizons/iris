"""
The function to parse through the string
"""

import iris.plugins.loader
import nltk


def evaulate(string):
    """
    Given a string, return a response dict or raise an error

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
    while any('[' in i for i in lst):
        new_lst = []
        for elm in lst:
            if '[' in elm:
                l = elm.find('[')

                # ignore nested brackets
                if elm.find('[', l+1) < elm.find(']', l+1) and elm.find('[', l+1) != -1:
                    tmp_l = elm.find('[', l+1)
                    while elm.find('[', tmp_l+1) < elm.find(']', l+1):
                        if elm.find('[', tmp_l+1) == -1:
                            tmp_l = elm.find(']', tmp_l+1)  # We have found the last '[', find the matching ']'
                            break
                        else:
                            tmp_l = elm.find('[', tmp_l+1)
                    r = elm.find(']', tmp_l+1) # find the one we want
                else:
                    r = elm.find(']', l+1)
                splice = elm[l+1:r]
                ''' No nested  brackets
                if '[' in splice:
                    opts = [i.strip() for i in splice[:splice.rfind('|', splice.find('['))].split('|')] + \
                           [splice[splice.find('['): splice.rfind(']') + 1]] + \
                           [i.strip() for i in splice[splice.find('|', splice.rfind(']') + 1) + 1:].split('|')]
                    opts = [i for i in opts if i]
                else:
                    opts = [i.strip() for i in splice.split('|')]
                    '''
                opts = [i.strip() for i in splice.split('|')]
                for j in opts:
                    new_lst.append(elm[:l] + ' ' + j + ' ' + elm[r+1:])
            else:
                new_lst.append(elm)
        lst = new_lst
    dic = {}
    for i in lst:
        dic[i] = grammar_func

    return dic
