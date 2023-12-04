#!/usr/bin/python3
def multiple_returns(sentence):
    f = "None"
    if len(sentence) != 0:
        f = sentence[0]
    return (len(sentence), f)
