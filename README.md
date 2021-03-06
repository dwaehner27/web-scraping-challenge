# Web Scraping Challenge

## Description
I was tasked to build a web application that scrapes various websites that provide data related to Mars and display the collected data in a single HTML page. For more details on the assignment see assignment section [here](https://github.com/dwaehner27/web-scraping-challenge/blob/main/README.md#assignment).

## How to Run Code
Clone this repository, locate and open the app.py file, run code in terminal, and run the Flask app. Click "Get Data!" to proceed with web scraping and view resulting data. To see the web scraping process, run the mission_to_mars Jupyter notebook.

## Results
The resulting view of the scraped data is shown below:

![image](https://user-images.githubusercontent.com/61367502/121986471-25cfe900-cd5c-11eb-9a8f-6687c859f85f.png)


## Assignment

In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do.


### Step 1 - Scraping
Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

#### NASA Mars News

Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
https://redplanetscience.com/

#### JPL Mars Space Images - Featured Image


* Visit the url for the Featured Space Image site here.
https://spaceimages-mars.com/image/featured/mars2.jpg

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.


* Make sure to find the image url to the full size .jpg image.


* Make sure to save a complete url string for this image.

#### Mars Facts


* Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
https://galaxyfacts-mars.com/


* Use Pandas to convert the data to a HTML table string.

#### Mars Hemispheres

* Visit the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

### Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


- - -

### Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.

2. Screenshots of your final application.

3. Submit the link to your new repository to BootCampSpot.

4. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

### Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.


