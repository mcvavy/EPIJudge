from typing import List
from collections import Counter

from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    result = []
    
    wordCount = len(words[0])
    wordSize = len(words)
    wordsLength = wordCount * wordSize
    wordsDict = Counter(words)
    
    for i in range(0, len(s) - wordsLength + 1, 1):
        tempDict = wordsDict.copy()
        count = wordSize
        
        for j in range(i, i + wordsLength, wordCount):
            w = s[j:j + wordCount]
            
            if w not in tempDict or tempDict[w] == 0:
                break
            else:
                tempDict[w] -= 1
                count -= 1
        if count == 0:
            result.append(i)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
