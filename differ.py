from termcolor import colored, cprint
import difflib


def diff(orig_data ,diff_data, color=None, attrs=None):
    minuses = 0
    position = 0
    stdout = ""
    for i, s in enumerate(difflib.ndiff(orig_data, diff_data)):
        if s[0] == ' ':
            stdout += diff_data[i-minuses]
        elif s[0] == '-':
            minuses += 1
        elif s[0] == '+':
            stdout += colored(diff_data[i-minuses], color, attrs=attrs)

    print stdout
