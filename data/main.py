from data.scrapers import *
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def model_run(model, freq='1111111', existing=None):
    scraper = model(freq)
    dfs = scraper.run()
    for df in dfs:
        existing.append(df)
    return existing


def generate_wordcloud(text, year=None):
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    if year:
        plt.savefig("../assets/img/jellyfish_{}.png".format(str(year)), format="png")
    plt.show()


if __name__ == "__main__":
    dfs = list()
    model_run(SmithsonianScraper, freq='1111111', existing=dfs)
    model_run(FastCompanyScraper, freq='1111111', existing=dfs)
    model_run(WorldEconomicForumScraper, freq='1111111', existing=dfs)
    model_run(NewScientistScraper, freq='1111111', existing=dfs)
    model_run(TimeScraper, freq='1111111', existing=dfs)
    model_run(JStorScraper, freq='1111111', existing=dfs)
    model_run(QuartzScraper, freq='1111111', existing=dfs)
    model_run(MarineScienceScraper, freq='1111111', existing=dfs)
    model_run(BBCEarthScraper, freq='1111111', existing=dfs)
    model_run(BBCNewsScraper, freq='1111111', existing=dfs)
    model_run(TheGuardianScraper, freq='1111111', existing=dfs)
    dfs = pd.DataFrame(dfs).sort_values(by="date")

    grouped_df = dfs.groupby(dfs['date'].dt.year)['words'].agg(['sum', 'count']).reset_index()
    print(grouped_df)

    for index, row in grouped_df.iterrows():
        generate_wordcloud(row['sum'], row['date'])

