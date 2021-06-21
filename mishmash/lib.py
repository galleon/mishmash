import re
from unidecode import unidecode
# Example of stopwords
STOPWORD = ('le', 'la', 'les', 'mais', 'où', 'et', 'donc', 'or', 'ni', 'car')


class TextParser:
    """Handle the parsing of the text written by the user.
    Extract the significative words that could relate to a location.
    """
    def __init__(self):
        self.stopwords = [self.flatten_text(word) for word in STOPWORD]

    def flatten_text(self, wording):
        """Normalize the characters of a text,
        by ensuring that the whole string is in lowercase,
        and by striping every accent in it.
        """
        # Ensure that the attribute in a string
        wording = str(wording)
        # Lower cases
        wording = wording.lower()
        # Strip accents
        wording = unidecode(wording)
        return wording

    def segment_text(self, wording):
        """Try to extract the significative words of the question from the text,
        with the use of various rational expressions.
        """
        # List of rational expressions used to search the text
        regex = [
            r"((adresse|chemin|direction|itineraire|trajet)( \b\w+\b))(?P<segment>[\w '-]+)",
            r"(ou (est|sont|(se \b\w+\b)))(?P<segment>[\w '-]+)",
            r"((indiqu|localis|position|trouv|situ)\w*)(?P<segment>[\w '-]+)"
        ]
        # Search the text with each rational expression, and stop at the first match
        match = None
        for expression in regex:
            if re.search(expression, wording):
                match = re.search(expression, wording)
                return match.group('segment')
        # Return whole text, if the rational expressions gave no result
        if match is None:
            return wording

    def remove_punctuation(self, wording):
        """Remove every punctuation from the text."""
        try:
            re.search(r"[^' a-zA-Z0-9-]", wording)
        except TypeError:
            pass
        else:
            if re.search(r"[^' a-zA-Z0-9-]", wording):
                wording = re.sub(r"[^' a-zA-Z0-9-]", "", wording)
        return wording

    def filter_text(self, wording):
        """Remove stopwords from the text."""
        try:
            for word in self.stopwords:
                wording = wording.replace(f' {word} ', ' ')
        except AttributeError:
            pass
        return wording

    def parsing_flow(self, text):
        """Apply all the functions of the parser on the string, in a staged process.
          -  put every characters of the string in lowercase, and strip every accent
          -  try to extract the significative words of the string, with regex
          -  remove the punctuation in the string
          -  remove a list of stopwords from the string
        """
        flow_funcs = [
            self.flatten_text, self.segment_text, self.remove_punctuation,
            self.filter_text
        ]
        # Chain the call to the functions in the list
        for func in flow_funcs:
            text = func(text)
        return text
