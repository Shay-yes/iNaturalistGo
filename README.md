# iNaturalistGo

### Running this application and its dependencies:
### Note: This first release contains more or less "wireframe" views of our application's homepage and user registration page. This release lacks functionality outside of presenting these pages to the user.

#### Required software:
See requirements.txt

### To run the application:
1) Download the latest release

2) Open a terminal and navigate to the top-level directory of the release you downloaded. By default, this should be a directory called iNaturalistGo. This directory should contain a file called requirements.txt. **If this is your first time running the application**, run this command: 
pip install requirements.txt
**Otherwise**, skip to step 3.

3) From the root directory, navigate into the iNaturalist_447 directory. This directory should contain the file manage.py. Inside of this directory, run the following command:
python3 manage.py runserver

4) Open a web browser and go to http://127.0.0.1:8000/ to display the app's homepage, which presents an interface for users to navigate the app's (future) functionalities. While in your web browser, go to http://127.0.0.1:8000/register to view the user registration page, which presents a form for users to create an account with. Both of these pages offer trivial functionality at this point, which will be developed during future iterations.


### Running tests for this application:
In a terminal, navigate to the project folder containing manage.py (which should be the same directory referenced in step 3 above) then run this command: 
python3 manage.py test iNaturalist_447

