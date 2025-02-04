# tests for the functions in pss.py

import pytest

@pytest.fixture
def test_string():
   tstring = "National Center for Supercomputers Applications"
   return tstring

from pss import *

def test_vowel_to_number_uppercase():
    assert vowel_to_number("A") == "1"

def test_vowel_to_number_lowercase():
    assert vowel_to_number("a") == "1"

def test_modify_string(test_string):
    assert modify_string(test_string) == "N1t915n1l C5nt5r f15r S21p5rc15mp21t5rs 1ppl9c1t915ns"

def test_consonant_count(test_string):
    assert consonant_count(test_string) == 26
