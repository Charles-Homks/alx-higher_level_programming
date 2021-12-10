#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val = -1
    vad = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > val:
            val = a_dictionary[key]
            vad = key
    return vad
