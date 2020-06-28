from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

for path in Path("level_words").glob("*"):
    print(path)

    soup = BeautifulSoup(open(path).read())

    level_words = []

    for word in soup.find_all("div",{"class":"thing text-text"}):
        romanian = word.find("div", {"class": "col_a"}).text.strip()
        english = word.find("div", {"class": "col_b"}).text.strip()
        level_words.append({"romanian": romanian, "english": english})

        pd.DataFrame(level_words).to_csv(f"output/{path.name.split('.html')[0]}.csv", index=False)


