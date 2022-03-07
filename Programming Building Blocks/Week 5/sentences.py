import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman", "sussy baka", "boba", "weeb"]
    else:
        noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women", "sussy bakas", "bobas", "weebs"]
    
    # Randomly choose and return a determiner.
    noun = random.choice(noun)
    return noun

def get_verb(quantity, tense):
    if tense == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote", "twerked"]
        
    elif tense == "present" and quantity == 1:
        verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes", "twerks"]

    elif tense == "present" and quantity != 1:
        verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write", "twerk"]

    elif tense == "future":
        verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write", "will twerk"]

    # Randomly choose and return a determiner.
    verb = random.choice(verb)
    return verb

def get_preposition():
    preposition = [
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    preposition = random.choice(preposition)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    preposistion = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return f"{preposistion} {determiner} {noun}"

def get_adjective():
    adjective = ["smelly", "big", "small", "hungry",
    "funny", "tasty", "suspicious", "skinny", "fat",
    "beautiful", "bright", "radiant", "sneaky", ""]
    adjective = random.choice(adjective)
    return adjective

def make_sentences(tense):
    for i in range(1,3):
        word = get_determiner(i)
        adjective = get_adjective()
        noun = get_noun(i)
        verb = get_verb(i, tense)
        print(f"{word.capitalize()} {adjective} {noun} {verb}.")

def make_preposition_sentences(tense):
    for i in range(1,3):
        preposition = get_prepositional_phrase(i)
        determiner =  get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, tense)
        adjective = get_adjective()
        print(f"{determiner.capitalize()} {adjective} {noun} {verb} {preposition}.")

def main():
    make_sentences("past")
    make_sentences("present")
    make_sentences("future")
    print()

    make_preposition_sentences("past")
    make_preposition_sentences("present")
    make_preposition_sentences("future")

main()