# Timing Example
import time
import requests
from bs4 import BeautifulSoup

def timer(function):

    # can add *args and **kwargs to the function
    # but it is not necessary for this example
    def wrapper():
        before = time.time()
        function()
        after = time.time()
        funcName = function.__name__
        print(f"{funcName} took {after - before} seconds")

    return wrapper

@timer
def scrapeGoogle():
    r = requests.get("https://www.google.com")
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup.title.text)

scrapeGoogle()