# Remmisma-Gallery

## Author
[Stephen remmi](https://github.com/Stephenremmi)

## Description
An application which lists and previews news articles from various sources using the [News API](https://newsapi.org/), made by python web framework, Flask.This web app keeps
you up-to-date anytime and anywhere around the globe given you have a device able to connect to internet,internet access and free time to spare.

## Features
Here are the features in summary:
* A minimalistic landing page showing trending world news and a variety of news sources
* Clickable news sources which direct the user to a page with article highlights from the particular source.

#
## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: 
    * **`pip install flask`**

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/Stephenremmi/Articnews.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install <name>`**
* **Step 5** : Go to the [news API]() WEBSITE, sign up for a free account and generate an API key. 
    * Create a file in your root directory called start.sh and store the API key like so **`export API_KEY="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`** 
* **Step 6** : On your terminal, run the following command, **`chmod a+x start.sh`**
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.

## Known Bugs
* overlap of scroll features

## Versioning
Articnews version 1.0
Future releases should have the following features:
* Ability to search news
* Ability to favorite specific articles
* Pagination.
* be responsive
* Bottom screen-Allows user to scroll down the page infinitely
* Include various news categories such as sport,science and tech.



## Technologies Used
* Python 3.6
* HTML  
* CSS

## Support and contact details
You can provide feedback or raise any issues/ bugs via email:
* stephenremmi@gmail.com

## [License](https://github.com/Stephenremmi/Articnews/blob/master/LICENSE)
MIT license Copyright(c) 2020 **Stephen Remmi**
