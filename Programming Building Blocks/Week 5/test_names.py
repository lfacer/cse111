from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name(): 
    #full_name = make_full_name("Sally", "Brown")
    #assert isinstance(full_name, str)
    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones; Ava"
    assert make_full_name("James", "Madison") == "Madison; James"
    assert make_full_name("J", "Ng") == "Ng; J"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    #family_name = extract_family_name("Sally", "Brown")
    #assert isinstance(family_name, str)
    assert extract_family_name("Smith-Jones; Ava") == "Smith-Jones"
    assert extract_family_name("Madison; James") == "Madison"
    assert extract_family_name("Ng; J") == "Ng"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    #given_name = extract_given_name("Sally", "Brown")
    #assert isinstance(given_name, str)
    assert extract_given_name("Smith-Jones; Ava") == "Ava"
    assert extract_given_name("Madison; James") == "James"
    assert extract_given_name("Ng; J") == "J"
    assert extract_given_name("; ") == ""


pytest.main(["-v", "--tb=line", "-rN", __file__])