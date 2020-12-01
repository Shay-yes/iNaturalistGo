# iNaturalistGo

### Running this application and its dependencies:
Our application has been deployed via Heroku! To run the application, simply head to inaturalistgo.herokuapp.com.
The current Heroku deployment has a few migrations pending, so all features may not be available at the above link. To explore the full functionality of the app,
complete the follwoing steps:

1. Download the repository to a Linux machine
2. In a terminal, navigate to the root directory of the repository
3. While in the terminal, run the command pip3 install -r requirements.txt
4. Run the command python3 manage.py makemigrations
5. Run the command python3 manage.py migrate
5. Run the command python3 manage.py runserver

You should now be able to navigate to the iNaturalistGo website at the IP address 127.0.0.1:8000
To test the login/account creation functionality, click the "Create Account" button from the iNaturalistGo homepage. Fill out the registration form to create
an account. Then, head over to 127.0.0.1:8000/login (or navigate there via the link on the registration screen) to login to this account. Enter your newly created
account credentials into the login screen, then click the Login button. You should now see the "logged-in" homepage, which presents the user with more options than
just the default "Sign in" or "Create account." Click on "Upload a Species" to be presented with a form that lets you upload a picture of an animal, along with its 
names (common and scientific) and location. Once you upload a species, click on "Species Gallery" from the homepage to view any uploaded species.

### Running tests for this application:
In a terminal, navigate to the project folder containing manage.py (which should be the same directory referenced in step 3 above) then run this command: 
python3 manage.py test
