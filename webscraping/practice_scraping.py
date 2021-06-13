from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver=webdriver.Chrome(ChromeDriverManager().install())

url="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
driver.get(url)
time.sleep(1)

main_area = driver.find_element_by_css_selector("tbody.lister-list")
movie_titles = main_area.find_elements_by_css_selector("td.titleColumn")
movie_ratings = main_area.find_elements_by_css_selector("td.ratingColumn.imdbRating")

data = []
for title,rating in zip(movie_titles,movie_ratings):
    title_and_year = title.text
    name = title_and_year.rsplit(maxsplit=1)[0]
    year = title_and_year.rsplit(maxsplit=1)[1][1:-1]
    rating=rating.text
    data.append({
        "name":name,
        'year':year,
        'rating':rating.text
        
    })

driver.close()
pd.DataFrame(data).to_csv("most_popular_movies.csv")

 