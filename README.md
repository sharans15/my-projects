# my-projects


INTRO:This project demonstrates a FastAPI which enables the user to store the location or addrees of a place in form of coordinates and then helps the user 
choose the range of coordinates (latitude and longitude) and shows all the places registered in that range of
coordinates.


Requirements:
1) python 3.7 or 3.8
2) sql database application (get it from "https://sqlitebrowser.org/dl/") : This will help you to see which data has gone in which table and so accordingly you can
test and run
3) open the DB browser and chose "open database" and choose the db file (named "database") which is present in "\my-projects-master\my-projects-master"


For running and Understand the flow of project:
Step 1 : clone this repository or simply download in zip file
step 2: run the command "pip install -r requirements.txt (this installs all the necessary libraries needed)
step 3: then in terminal run "uvicorn main:app --reload"
step 4: you will see this message on terminal "Application startup complete."
step 5: then on your webbrowser just open "http://localhost:8000/docs#/"

step 6: you will see the built in Swagger UI open with the following opt

        1)Gems (This contains the location detials,that is "location" and its coordinates (latitude and longitude))
        
            1) get method: here you can enter the range of latitudes (lte_lat = Highest range of latitude and gta_lat = Lowest range of latitude) and longitudes (lte
            _lon = highest range of longitude and gte_lon = lowest range of longitude) .
             And then the locations matching the criteria will show up .
             No authentication needed for this and initially i have stored a few places like mumbai delhi etc along with some test places saved with the default name 
             "string" .
               
             2) post method : here you can add places (like mumbai,delhi,bangalore,amritsar etc) and the latitude and longitude value will be set to 0 by default and you
             need not change that because afer you choose the city or place or address the corresponsing latitudes and longitudes will be assigned to the respective id
             by the help of geopy library, and id is the city which you are entering.
             This needs AUTHENTICATION
             
             3)put method : Here you can update the address. So for a given id you can put any address and any latitude and longtitude as desired.
             This needs AUTHENTICATION and also the entered ID should exist.
             
             4) delete : Here you can enter the ID and delete the same.
             This needs AUTHENTICATION and also the entered ID should exist.

          2)User
          
             1) Post registration : here you can register and password should be atleast 6 characters and username should be unique and unused.
             is_auth parameter shall be true by default and not be changed.
             
             2) Post login : here you will login with correct credentials as entered during registration and then you will see a token generated and then you will click on the
             lock sign and enter the token to get authenticated.
             
             3) get users: you can see your user credentials
             This needs AUTHENTICATION.
