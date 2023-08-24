import csv
import requests
from bs4 import BeautifulSoup
class BEAHarvester:
    def __init__(self):
        self.base_url = "https://www.bea.gov/data/economic-accounts/gdp-by-industry"
    def get_data(self):
        datasets = []
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        for dataset in soup.find_all("div", class_="dataset-item"):
            datasets.append({
                "id": dataset.find("a")["href"].split("/")[-1],
                "name": dataset.find("h3").text,
                "description": dataset.find("p").text,
                "url": dataset.find("a")["href"]
            })
        with open("bea_data.csv", "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["ID", "Name", "Description", "URL"])
            for dataset in datasets:
                csvwriter.writerow([
                    dataset["id"],
                    dataset["name"],
                    dataset["description"],
                    dataset["url"]
                ])
if __name__ == "__main__":
    scraper = BEAHarvester()
    scraper.get_data()