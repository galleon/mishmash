from mishmash.lib import KittApi, TextParser

DATA = ((
    "La liberté est pour la Science ce que l'air est pour l'animal.",
    "la liberte est pour la science ce que l'air est pour l'animal.",
    "la liberte est pour science ce que l'air est pour l'animal",
    "la liberte est pour la science ce que l'air est pour l'animal",
), (
    "À vaillant coeur rien d'impossible.",
    "a vaillant coeur rien d'impossible.",
    "a vaillant coeur rien d'impossible",
    "a vaillant coeur rien d'impossible",
), (
    "Quand on a pas ce que l'on aime, il faut aimer ce que l'on a.",
    "quand on a pas ce que l'on aime, il faut aimer ce que l'on a.",
    "quand on a pas ce que l'on aime il faut aimer ce que l'on a",
    "quand on a pas ce que l'on aime il faut aimer ce que l'on a",
), (
    "Il n'y a rien de négatif dans le changement, si c'est dans la bonne direction.",
    "il n'y a rien de negatif dans le changement, si c'est dans la bonne direction.",
    "il n'y a rien de negatif dans changement si c'est dans bonne direction",
    "il n'y a rien de negatif dans le changement si c'est dans la bonne direction",
))


def test_flatten_text():
    tp = TextParser()
    for x in DATA:
        assert tp.flatten_text(x[0]) == x[1]


def test_segment_text():
    tp = TextParser()
    for x in DATA:
        print(tp.parsing_flow(x[0]))


def test_remove_punctuation():
    tp = TextParser()
    for x in DATA:
        assert tp.remove_punctuation(x[1]) == x[3]


def test_parsing_flow():
    tp = TextParser()
    for x in DATA:
        assert tp.parsing_flow(x[0]) == x[2]


def test_kitt_api_get_user_ide():
    ka = KittApi()
    assert ka.get_user_id() == 11764
