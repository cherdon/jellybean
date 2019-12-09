import re
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from data.base import BaseScraper, parse_text
with open('../links.json', 'r') as infile:
    links = json.load(infile)
data_structure = {
            "date": None,
            "source": None,
            "words": None
}


def log(text):
    print(text + " scraper...done")


class SmithsonianScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['smithsonian']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("time").text
            try:
                time = datetime.strptime(time_str, "%B %Y")
            except:
                time = datetime.strptime(time_str, "%B %d, %Y")
            source = re.sub('\s+', ' ', soup.find("span", {"class": "pub-edition"}).text)
            try:
                source = source.split("|")[0].strip()
            except:
                pass
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("Smithsonian")
        return data


class FastCompanyScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['fast-company']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("time")['datetime']
            time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
            source = re.sub('\s+', ' ', soup.find("a", {"class": "masthead__title"}).text)
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("Fast Company")
        return data


class WorldEconomicForumScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['we-forum']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("div", {"class": "article-published"}).text
            time = datetime.strptime(time_str, "%d %b %Y")
            source = re.sub('\s+', ' ', soup.find("title").text)
            source = source.split("|")[1].strip()
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("World Economics Forum")
        return data


class NewScientistScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['new-scientist']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = re.sub('\s+', ' ', soup.find("span", {"class": "published-date"}).text).strip(" ")
            time = datetime.strptime(time_str, "%d %B %Y")
            source = re.sub('\s+', ' ', soup.find("title").text)
            source = source.split("|")[1].strip()
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("New Scientist")
        return data


class TimeScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['time']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("span", {"class": "entry-date"}).text
            time = datetime.strptime(time_str.replace("Sept", "Sep"), "%b. %d, %Y")
            source = re.sub('\s+', ' ', soup.find("title").text)
            source = source.split("|")[1].strip()
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("Time.com")
        return data


class JStorScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['jstor']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("time", {"class": "timestamp--published"})['datetime']
            time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)
            source = re.sub('\s+', ' ', soup.find("title").text)
            source = source.split("|")[1].strip()
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("JStor")
        return data


class QuartzScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['quartz']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("time")['datetime']
            time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.000Z")
            source = re.sub('\s+', ' ', soup.find("title").text)
            source = source.split("—")[1].strip()
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("Quartz")
        return data


class MarineScienceScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['marine-science-today']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("span", {"class": "meta-date"}).text.replace("on", "")
            time_str = re.sub('\s+', ' ', time_str).strip(" ")
            time = datetime.strptime(time_str, "%B %d, %Y")
            source = re.sub('\s+', ' ', soup.find("title").text)
            source = source.split("|")[1].strip()
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("Marine Science")
        return data


class BBCEarthScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['bbc-earth']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("span", {"class": "publication-date"}).text
            time = datetime.strptime(time_str, "%d %B %Y")
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": "BBC Earth",
                "words": paragraphs
            })
        log("BBC Earth")
        return data


class BBCNewsScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['bbc-news']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("div", {"class": "date--v2"})['data-datetime']
            time = datetime.strptime(time_str, "%d %B %Y")
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": "BBC News",
                "words": paragraphs
            })
        log("BBC News")
        return data


class TheGuardianScraper(BaseScraper):
    def scrape(self):
        data = list()
        url_links = links['the-guardian']
        for link in url_links:
            html = requests.get(link).text
            soup = BeautifulSoup(html, 'html.parser')
            time_str = soup.find("time", {"class": "content__dateline-wpd"})['datetime']
            time = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z").replace(tzinfo=None)
            source = re.sub('\s+', ' ', soup.find("title").text)
            source = source.split("|")[-1].strip()
            paragraphs = [para.text for para in soup.find_all("p")]
            paragraphs = parse_text(" ".join(paragraphs))
            data.append({
                "date": time,
                "source": source,
                "words": paragraphs
            })
        log("The Guardian")
        return data


if __name__ == "__main__":
    df = TheGuardianScraper().run()
    print(df)
