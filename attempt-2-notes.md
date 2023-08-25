Plan 897 -->

Alrighty. This time around I have a project plan for a **food access web application**. 
User will be able to create account, sign in, and sign out. (username, password, name, zipcode)
Once signed in the user will be able to see the main homepage where they can add the tiles that are going to be options from the other pages, they can also delete these tiles if they want. There will be a few prepopulated tiles based on user location. (snap info for state)
The other webpages are going to be:
    **SNAP Calculator** - self developed calculator for determining amount of SNAP benefits the   user is eligible for. once completed it will be a tile added to the homepage.


*API's*

To use the APIs, you must register for a key using the form below. Registering is simple—just provide your name and valid email address. You’ll gain universal access to any Open Government data using the service, and receive notification of updates and new releases.

For additional support, please contact us. When contacting us, please tell us what API you're accessing and provide the following account details so we can quickly find you:

Account Email: kdalelewis@yahoo.com
Account ID: 76f7c91e-6537-4eab-a6d5-8eb5ddb8010a

Your API key for kdalelewis@yahoo.com is:

Sbykz8AqkuoPy9LkITDpR87uCQARZlavbypEkN2d

Thomas Kane
IT Specialist
thomas.kane@usda.gov

**ARMS Data API** : USDA’s Economic Research Service (ERS) is making data from USDA’s Agricultural Resource Management Survey (ARMS) available through an Application Programming Interface (API) to better serve customers. The data in the API are available in JSON format and provide attribute-based querying. The data are also available in bulk files.

This documentation provides a brief explanation of the API to get you started. For user convenience, we provide demos using R: open source statistical programming language.

*Local Food Directories*
I want to use https://www.usdalocalfoodportal.com/fe/datasharing/ for an api, I have requested to get a key but my backup if I am unable to do so is to download the directories data. There are five APIs for you to obtain directory data:
        Agritourism Business Directory: https://www.usdalocalfoodportal.com/api/agritourism/
        CSA: https://www.usdalocalfoodportal.com/api/csa/
        Farmers Market: https://www.usdalocalfoodportal.com/api/farmersmarket/
        Food Hub: https://www.usdalocalfoodportal.com/api/foodhub/
        On-farm Market: https://www.usdalocalfoodportal.com/api/onfarmmarket/

*SNAP Retailer Locator Data*
I want to use https://usda-fns.hub.arcgis.com/datasets/USDA-FNS::snap-store-locations/api for an api. I can also have the data downloaded in case im unable to access it for whatever reason. 

**USDA ERS GIS Map Services and API User Guide**  
https://catalog.data.gov/dataset/usda-ers-gis-map-services-and-api-user-guide
Metadata Updated: May 17, 2021 

All of the ERS mapping applications, such as the Food Environment Atlas and the Food Access Research Atlas, use map services developed and hosted by ERS as the source for their map content. These map services are open and freely available for use outside of the ERS map applications. Developers can include ERS maps in applications through the use of the map service REST API, and desktop GIS users can use the maps by connecting to the map server directly.





What defines a front end api? if im calling a random government website for info that i display, does that count?


Name: Food.YourRight

Objective: Allow users to see different points of food access in the local area. This will include SNAP and WIC program info by state, a snap eligiblity calculator, SNAP retialers locally, summer food service programs locally, food bank/pantries/distributions nearby, food hubs/markets/farms locally and hunting/fishing opprotunities. There will also be the option to save indivdual tiles to the users homepage for the user to have easy access to.

UI: Front page will have create account and sign in buttons, a mission statement and a map of the US with clickable states/territories that when clicked populate a card with information from the state's SNAP and WIC programs. Allow users to create an account, sign in, and sign out from the application. Once signed in the user will be able to have a populated homepage conatining a tile of the blank snap benefit calculator and a tile of general info about food access. There will be a signout button always visable as well as the name. There will be folder tabs to click from:
    Home: 
    Help By State Map:
    SNAP Calculator:
    SNAP Retailers:
    Summer Food Services:
    Free Food Options:
    Healther Local Food Options:
    Get Your Own Food Options:

API's used: 
            frontend:    using svg stuff, hopefully this counts.
                "http://www.w3.org/2000/svg"
            backend:


Databases:  





Note - got the raw html of all info by state for food and nutrition services. will need to figure out how to grab it... I also got the state map up and running to be able to work hopefully. 




 1607  python -m venv .venv
 1608  source ./.venv/bin/activate
 1609  pip install django djangorestframework django-cors-headers
 1610  python -m pip install --upgrade pip
 1613  pip install django #installs django\npip install "psycopg[binary]" #installs psycopg3 which allows django to talk to postgresql\npip install djangorestframework #install rest_framework to allow us to utilize Response, APIView, and TokenAuthentication\npip install django-cors-headers
 1616  django-admin startproject foodyourright .
 1618  createdb foodyourright_db


Steps:

1. got Django up. my virtual envrioment is '.venv'. activated it. installed dependencies. created project. created database. added   'rest_framework',
    'corsheaders', to settings installed apps. added 'corsheaders.middleware.CorsMiddleware', to middleware in settings. added db to settings and changed it to postgreSQL. added another item to settings, "# i added this one  to disable CORS feature while working full localhost
CORS_ORIGIN_ALLOW_ALL = True" i also created the first app, users. i added  this to settings in apps. 

2. updated admin.py. filled out basics of models.py. created urls.py and filled in. created views. added name to models. then did some migrations. well attempted. currently having a lot of errors...
well i just noticed my app isn't actually in the django project. moved users into foodyourright from finder. getting error that there is no module users. going to retry and see why my directories are being weird. 

3. needed packages already installed. created project as foodyourright_proj and app for users as users_app. updated views, models, admin with models, added rest framework to settings, added auth user to settings and upded urls agian. trying migrations... still got error
ModuleNotFoundError: No module named 'users_app' but am continuing with it. was not working, made sure i had requirments installed from previous assesment. messed it up more. just recloning and starting again uhg. 




