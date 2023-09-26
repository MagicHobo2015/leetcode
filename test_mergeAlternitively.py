# A class to get practice writting tests.

import pytest
import mergeAlternitively

solution = mergeAlternitively.Solution()

def test_one():
    assert solution.mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr"

def test_two():
    assert solution.mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs"

def test_three():   
    assert solution.mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd"