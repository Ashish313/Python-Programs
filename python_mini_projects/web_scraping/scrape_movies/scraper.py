from bs4 import BeautifulSoup as soup 
import pandas as pd 
import requests
from time import time, sleep
from random import randint
from warnings import warn
from IPython.core.display import clear_output
import re


# declaring the lists to store the data
names = []
imdb_ratings = []
release = []
taglines = []
rated = []
runtimes = []
countries = []
genres = []
summary = []
director = []
cast = []
posters = []
screenshot1 = []
screenshot2 = []
screenshot3 = []

# preparing the monitoring of the loop
start_time = time()
req = 0

# loop over the three pages
for i in range(1,3):
    
    # make the get request
    page= requests.get(f'https://fzmovies.uno/release/2019/page/{i}/')

    # pause the loop
    sleep(randint(5,10))

    # monitor the requests
    req += 1
    elapsed_time = time()-start_time
    print('Request: {}; Frequency: {} requests/s'.format(req,req/elapsed_time))
    clear_output(wait=True)

    # throw warning if status code is not equal to 200
    if page.status_code != 200:
        warn('Request: {}; Status_code: {}'.format(req,page.status_code))

    # Break the loop if number of requests exceed 90
    if req > 90:
        warn('Requests are greater than we expected.')
        break

    # parse the content of the request
    page_soup = soup(page.text,'html.parser')

    # select all the movies on the page and loop through each movie
    mv_containers = page_soup.find_all('article',class_='item movies')
    for container in mv_containers:

        # scrape the name of the movie
        name = container.h3.a.text
        names.append(name)

        # scrape the IMDB rating of the movie
        rating = container.find('div',class_='rating').text
        imdb_ratings.append(rating)

        # scrape the release date of the movie
        release_date = container.h3.find_next_sibling().text
        release.append(release_date)

        # scrape the genre of the movie
        genre = set()
        mta_tag = container.find('div',class_='mta')
        if mta_tag:
            for tag in mta_tag:
                genre.add(tag.text)

        genres.append(tuple(genre))


        # remove punctuations from name of the movie for the url
        name = name.lower()
        name = re.sub(r"[(),@#!:’\*]","",name)
        name = '-'.join(name.split())

        # make the request to each movie page
        page2 = requests.get('https://fzmovies.uno/movies/download-'+str(name)+'-2019-full-movie-in-hd-fzmovies/')

        sleep(randint(5,10))
        req += 1
        elapsed_time = time()-start_time
        print('Request: {}; Frequency: {} requests/s'.format(req,req/elapsed_time))
        clear_output(wait=True)

        if page2.status_code != 200:
            warn('Request: {}; status_code: {}'.format(req,page2.status_code))

        if req > 90:
            warn('Requests are greater than we expected')
            break

        # parse the content of the request
        page_soup_2 = soup(page2.text,'html.parser')


        # scrape the poster of the movie
        poster = page_soup_2.find('div',class_='poster')
        posters.append(poster.img['src'])


        extra_data = page_soup_2.find('div',class_='extra')

        # scrape the tagline of the movie
        try:
            tagline = extra_data.find('span',class_='tagline').text
        except:
            taglines.append('')
        else:
            taglines.append(tagline)
        

        # scrape the origin of the movie
        try:
            country = extra_data.find('span',class_='country').text
        except:
            countries.append('N/A')
        else:
            countries.append(country)
        

        # scrape the runtime/length of the movie
        try:
            runtime = extra_data.find('span',class_='runtime').text
        
        except:
            runtimes.append('N/A')
        else:
            runtimes.append(runtime)

        
        # scrape the rating of the movie(G, PG, PG-13, R, NC-17)
        try:
            rated_tag = extra_data.find('span',class_='rated').text
        
        except:
            rated.append('N/A')
        else:
            rated.append(rated_tag)


        # scrape the summary of the movie
        neighbor_tag = page_soup_2.find('h2',attrs={'style':'text-align: center;'})
        if neighbor_tag:
            summary_tag = neighbor_tag.find_previous_sibling().text
            summary.append(summary_tag)

        # cast and director
        person = page_soup_2.find_all('div',class_='person')

        # scrape the director of the movie
        person_name = person[0].find('div',class_='name').text
        director.append(person_name)
        

        # scrape the names of the cast
        movie_cast = set()
        
        for actor in range(1,len(person)):
            person_name = person[actor].find('div',class_='name').text
            movie_cast.add(person_name)
            
        cast.append(tuple(movie_cast))


        # scrape the screenshots of the movie
        slider_tag = page_soup_2.find_all('div',class_='g-item')
        
        if len(slider_tag) >= 3:
            screenshot1.append(slider_tag[0].a['href'])
            screenshot2.append(slider_tag[1].a['href'])
            screenshot3.append(slider_tag[2].a['href'])       

        else:
            screenshot1.append('N/A')
            screenshot2.append('N/A')
            screenshot3.append('N/A')




# create a dictionary of the scraped values
movies_data = {'name':names,'taglines':taglines,'imdb_rating':imdb_ratings,'release_date':release,
             'runtimes':runtimes,'countries':countries,'rated':rated,'genre':genres,
             'summary':summary,'director':director,'cast':cast,'poster':posters,
             'screenshot1':screenshot1,'screenshot2':screenshot2,'screenshot3':screenshot3}


# create a pandas dataframe
df = pd.DataFrame(movies_data)

# make the csv file of the scraped data
df.to_csv('scraped_data.csv',sep='\t',encoding='utf-8',index=False)

print('Done')
