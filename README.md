# wallcraft-scraper

## Scraping Site :- https://wallpaperscraft.com/


# Change category and resolution you want to scrape
48. category = "cars" (https://github.com/rushipatel7/wallpaperscraft-scraper/blob/03d1cd02066f747c3f10548a31f6a557c1d826e6/wallpaper-scraper.py#L48)
49. resolution = "1280x1024" (https://github.com/rushipatel7/wallpaperscraft-scraper/blob/03d1cd02066f747c3f10548a31f6a557c1d826e6/wallpaper-scraper.py#L49)

# change number of page you want to scrape
28. for i in tqdm(range(1,5), desc='Loading...'):
  put diffrent number instend of 5 (https://github.com/rushipatel7/wallpaperscraft-scraper/blob/03d1cd02066f747c3f10548a31f6a557c1d826e6/wallpaper-scraper.py#L28)
  
  example:- for i in tqdm(range(1,100), desc='Loading...'):
