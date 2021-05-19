# Web Scraping Challenge

## Description
I was tasked to build a web application that scrapes various websites that provide data related to Mars and display the collected data in a single HTML page. For more details on the assignment see assignment section.

## How to Run Code
Clone this repository, locate and open the app.py file, run code in terminal, and run the Flask app. Click "Get Mars Data!" to proceed with web scraping and view resulting data. To see the web scraping process, run the mission_to_mars Jupyter notebook.

## Results
The resulting view of the scraped data is shown below:

## Assignment

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.

### Before You Begin


* Create a new repository for this project called web-scraping-challenge. Do not add this homework to an existing repository.


* Clone the new repository to your computer.


* Inside your local git repository, create a directory for the web scraping challenge. Use a folder name to correspond to the challenge: Missions_to_Mars.


* Add your notebook files to this folder as well as your flask app.


* Push the above changes to GitHub or GitLab.



### Step 1 - Scraping
Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.


#### NASA Mars News

Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
https://redplanetscience.com/

#### JPL Mars Space Images - Featured Image


* Visit the url for the Featured Space Image site here.
https://spaceimages-mars.com/image/featured/mars2.jpg

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.


* Make sure to find the image url to the full size .jpg image.


* Make sure to save a complete url string for this image.


