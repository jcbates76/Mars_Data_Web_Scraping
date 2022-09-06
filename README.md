# Mars_Data_Web_Scraping

![Webpage Image 2022-03-26](https://user-images.githubusercontent.com/94392882/188524069-08d9e728-61c9-455f-b5dd-762e6387db98.png)  

## Mission to Mars Project
This project utilizes web scraping to collect various forms of information on the Nasa Mars project, and displays that information on an HTML template utilizing a Flask Application.   

## Step 1 - Scraping
Using a Jupyter Notebook, perform the following information was collected using web scraping techniques.  

### NASA Mars News
* Scrape the Mars News Site (https://redplanetscience.com/) and collect the latest News Title and Paragraph Text.   

### JPL Mars Space Images - Featured Image
* Visit the site https://spaceimages-mars.com/ and capture the full size image of the feature_image_url.  

### Mars Facts
* Visit the Mars facts webpage https://galaxyfacts-mars.com/ and use Pandas to scrape the table containing facts about the planet.  Use Pandas to conver the data to a HTML table sting.  

### Mars Hemispheres
* Visit the astrogeology site https://marshemispheres.com/ and obtain the high resolution images of each of Mars's hemispheres.  Save poth the image URL strong and the hemisphere title in a Python dictionary.  

## Step 2 - MongoDB and Flask Application
* Converted the Jupyter notebook into a Python script with a function that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.  
* Created a route called "/Scrape" that imports the script, calls the function, and stores the return value in Mongo as a Python dictionary.
* Created a root route "/" that queries the Mongo database and passes the mars data into an HTML template to display the data.
* An HTML template takes the mars data dictionary and displays all of the data in appropriate HTML elements.  
