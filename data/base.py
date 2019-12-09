import datetime
import re
import string
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
stop_words += ["jellyfish", "jellyfishes"]


class BaseScraper:
    def __init__(self, freq='1111111'):
        self.freq = freq
        self.structure = {
            "date": "",
            "source": "",
            "words": ""
        }

    def run(self):
        weekday = datetime.datetime.now().weekday()
        if int(self.freq[weekday]):
            return self.scrape()
        else:
            return []

    def scrape(self):
        return None


def parse_text(scraped_text):
    punc = string.punctuation + "»–"
    punc += string.digits
    removed_spaces = re.sub('\s+', ' ', scraped_text)
    words = removed_spaces.split()
    words = [word.strip(punc).lower() for word in words]
    words = [word for word in words if word not in stop_words]
    return " ".join(words)
