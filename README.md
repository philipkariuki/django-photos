# Django Photos
My first Django app that involves creating a photo gallery.

#### By **Philip Kariuki**


## Description
This is a my first Django web application that entails creating a photo gallery website where you users get to see my collection of photos and they can click on the image to zoom it and also be able to compy the image link.

Live link : https://phillmatic.herokuapp.com

## User Stories
As a user, I would like to be able to do the following:
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
| Display all photos | On home page load | Loads all the available photos |
| Zoom in on image | Click on a particular image | Single image zooms in |
| View image details | Click on the particular image | Image descriptions display on top of and below the image |
| Search for image | Enter image description in search box | Matching images return as search results else 0 matching images found |


## Setup/Installation Requirements
To clone this repo, open terminal in your desired folder then run:

        $ git clone https://github.com/philipkariuki/django-photos/
        $ cd /django-photos

To create and activate the virtual environment and install pip:

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python


To install all the required pip modules for proper functionality:

        (virtual)$ python3.6 -m pip install -r requirements.txt

To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
To run unittests:

        $ python3.6 manage.py test philmatic

## Known Bugs

No known bugs

## Technologies Used

* HTML
* CSS
* Python3.6
* Pip
* Django v 2.2.3
* MDBootstrap
* Postgres Database
* gunicorn


## Contributors
<a href="https://github.com/philipkariuki">philipkariuki</a>

## Support and contact details
To support me, you can contact me at <a href="https://www.gmail.com">philippokar@hotmail.co.uk</a>

## License
[MIT © 2019](https://github.com/philipkariuki/django-photos/blob/master/LICENSE)

