from operator import ge
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    #test the single nouns
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(4):
        word = get_noun(1)
        assert word in single_nouns
    
    #test the plural nouns
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_noun(quantity)
        assert word in plural_nouns

def test_get_verb():

    #test the past verbs
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(4):
        word = get_verb(1, "past")
        assert word in past_verbs
    
    #test the present verbs
    present_verbs_singular = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    present_verbs_plural = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    for _ in range(4):
        word = get_verb(2, "present")
        assert word in present_verbs_singular

    for _ in range(4):
        word = get_verb(1, "present")
        assert word in present_verbs_plural

    #test the future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    for _ in range(4):
        word = get_verb(1, "future")
        assert word in future_verbs

def test_get_preposistion():
    preposistion = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()
        assert word in preposistion

def test_get_prepositional_phrase():
    preposistion = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["two", "some", "many", "the"]
    single_noun = ["bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"]
    plural_noun = ["birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        word = get_prepositional_phrase(1)
        words = word.split(" ")
        assert words[0] in preposistion

    for _ in range(4):
        word = get_prepositional_phrase(1)
        words = word.split(" ")
        assert words[1] in single_determiners

    for _ in range(4):
        word = get_prepositional_phrase(2)
        words = word.split(" ")
        assert words[1] in plural_determiners

    for _ in range(4):
        word = get_prepositional_phrase(1)
        words = word.split(" ")
        assert words[2] in single_noun
    
    for _ in range(4):
        word = get_prepositional_phrase(2)
        words = word.split(" ")
        assert words[2] in plural_noun

        
        

pytest.main(["-v", "--tb=line", "-rN", __file__])