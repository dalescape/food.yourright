# my_personal_project

Planning stage complete up to a certain point.

I will first set up the backend with Django. I will first focus on getting the Plaid api connected to be able to get user signed into the Plaid interface - this is because this will be the majority of the data being worked with on the backend. I did not find great docs on the Plaid website for connecting to a Django backend but I did find refrences to other indivdual projects that were able to get me started on the user banking login. 

Once this is setup my next task will be getting the bones of react laid out, not going to look pretty, just something to be able to visually see my data.

Next I will go back to my backend and finish structuring sql for the raw transaction data. 




I am concerned using the example django plaid project, it is 3 years old. 
Each tool in the toolbox will need to be seperate apps. 

Will need to update plaid_keys in order to run.
Verify plaid_app views and templates



STEPS TAKEN -->

1. pre everything. created a repository in github with this readme. Added the excalidraw file in github. 
2. cloned this project (my_personal_project) to my local machine (desktop -> programming_ish -> my_personal_project) and began working in this readme. 
3. created a virtual environment (.venv) AND activated it. lol
4. installed needed packages (pip install django, python -m pip install --upgrade pip, pip install "psycopg[binary]", pip install djangorestframework, pip install django-cors-headers)
5. created a db in postgresql (money_db)
6. set up a django project (myapi) & connected db in settings.py
7. created first django app (plaid_app) and went to settings and added it to the installed apps list along with rest_framework
8. updated myapi urls.py with plaid_app import views and added needed url patterns (from example)
9. updated plaid app from example. (migrations, init, admin, apps, models, and tests had no change) views updated. created new file (plaid_keys) this is needed to get info from plaid *WILL NEED TO UPDATE!*. created template folder with index.html file copied from example.
9. (b) creeated a seperate folder (example_to_delete). most will be deleted but static/admin stuff will stay. potentailly the requirments too. this wasnot used ad wass then deleted.
10. git cloned the example project into api testing to copy over needed files(static/admin & requirments) and test project (worried about outdated pieces.. )
11. almost ready to run web server. decieded to check the example file first. this was a good idea. one major change was noticed. the previous public key was still implemented, this needs to change to the new link token. a different example oes include this change. i will check this other code base out after running the server to catch other errors. 
12. updated plaid_keys and installed plaid-python. ran ./manage.py runserver. did not work, too many errors.
        /Users/dale./Desktop/programming-ish/my_personal_project/.venv/lib/python3.9/site-packages/urllib3/__init__.py:34: NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(

        File "/Users/dale./Desktop/programming-ish/my_personal_project/myapi/urls.py", line 19, in <module>
            from plaid_app import views
        File "/Users/dale./Desktop/programming-ish/my_personal_project/plaid_app/views.py", line 5, in <module>
            from plaid import Client
        ImportError: cannot import name 'Client' from 'plaid' (/Users/dale./Desktop/programming-ish/my_personal_project/.venv/lib/python3.9/site-packages/plaid/__init__.py)

13. after looking over docs and other example projects i have chosen to begin by updating views. the quickstart guide provided by plaid is in python but its flask? 

Note: uhg attempting to convert flask to django and update the example code is really really sucky. me no like. so. thought. what if i instead, run this in the frontend with react from the provided tiny quickstart and then pass the data, the transactions ONLY, to the backend to store? idk where exactly to start... but. it seems like that might be the better route because im getting a headache. 

DECIDED TO TRY AGAIN BY RECLONING MY PROJECT AND RENAMING THE FIRST ATTEMPT BUT KEEPING IT AS A LOCAL VERSION

Plan 2.0 --> I have recolned the project and copied over the contents of this readme. I will now be testing out the tiny quickstart from react in my api_testing folder. this example is in react as the frontend but the minimal backend is with Express/Node. my plan is to play with the react front end and set up all things needed with the server. i will then in the api testing folder change the app to get transactions instead, then eventually changing the backend to django for the full project when moving over to this folder. this is a small minimal app so i should be able to handle this conversion and will be able to reference the previous django example projects if i get really stuck. the other concern is that this project example is using yarn instead of npm. from my understanding it will be easier to just learn how to work with yarn ? ew ok lets start. 

1. recloned project and cloned tiny quickstart. (following the react readme instructions) cd'ed into the react folder, installed yarn (npm install --global yarn) and copied over the env file to where it was needed(cp .env.example .env). the filled out the .env with the credentials. -- it did not have pproducts or country codes, this could be an issue if i am trying to get the transactions... -- then i started up the server -- jk it wasn't working. went and installed yarn in terminal otside of all folders. went to yarn package and did the following (sudo corepack enable, yarn set version stable) -- went back into the react folder (yarn set version stable) wouldn't work. went back to main place and removed the package.json file. In the react terminal folder i ran (yarn install-- it worked?, yarn start) the server is now up and running but has uncaught runtime errors i need to figure out. 

2. sorting out server errors. inserted a console.log into the react app.jsx now line 30. checked errors with chatgpt and did the following (npm install eslint --save-dev
 did get the following "9 vulnerabilities (3 moderate, 6 high)" ,yarn start -- got an error an it said to install yarn again?, yarn install, yarn start -- this work to open the server in chrome but had uncaught runtime errors) 
 
 in console:
        App.jsx:31 Response data: {"expiration":"2023-08-11T23:33:44Z","link_token":"link-sandbox-3555debc-4fcb-4f5e-866b-93e6d97f1313","request_id":"LSqsZTq01hJ01u6"}
        App.jsx:32 Uncaught (in promise) TypeError: Failed to execute 'json' on 'Response': body stream already read
            at App.jsx:32:1
        App.jsx:31 Response data: {"expiration":"2023-08-11T23:33:44Z","link_token":"link-sandbox-510cdbdc-3793-473c-a2ff-c47c43a64b9b","request_id":"HNBzHt3vhtFzCzK"}
        App.jsx:32 Uncaught (in promise) TypeError: Failed to execute 'json' on 'Response': body stream already read
            at App.jsx:32:1

in terminal: 
        Compiled with warnings.

        [eslint] 
        src/App.jsx
        Line 20:6:  React Hook useCallback has a missing dependency: 'getBalance'. Either include it or remove the dependency array     react-hooks/exhaustive-deps
        Line 68:6:  React Hook useEffect has a missing dependency: 'createLinkToken'. Either include it or remove the dependency array  react-hooks/exhaustive-deps

        Search for the keywords to learn more about each warning.
        To ignore, add // eslint-disable-next-line to the line before.

        WARNING in [eslint] 
        src/App.jsx
        Line 20:6:  React Hook useCallback has a missing dependency: 'getBalance'. Either include it or remove the dependency array     react-hooks/exhaustive-deps
        Line 68:6:  React Hook useEffect has a missing dependency: 'createLinkToken'. Either include it or remove the dependency array  react-hooks/exhaustive-deps

        webpack compiled with 1 warning

    But!! the link account button is able to be seen after closing the errors.

3. continuing to figure out errors. ctrl c to close server and did npm update then npm audit fix twice and then npm audit fix --force. now i have 88 vulnerabilities (14 low, 23 moderate, 43 high, 8 critical). uhg. thinking about just recloning and only using npm, not yarn. everything broken. sad. sad. 

4. renamed the tiny-quickstart to tint-quickstart-attempt-1. cloned the project again. went into react folder and did (npm install, npm audit fix, cp .env.example .env ) then went to .env and filled contents. then (npm run dev -- missing script "dev", npm run, npm run start ) OMG !!!! ITS RUNNING AND NO RUNTIME ERRORS! button works! i finshed reading the tutorial setup and while it is working i might have more issues when trying the app in development with a real bank. but for now im happy.

5. now im going to open the individual files and begin to change them to what i need. currently a json is printing to my screen. this includes accounts and then balances. there is also a item obj but not sure where that is coming from. 

NOTE: continuing to get frusrated and im learning a lot more but while the tiny react thingy is working im going to try something else. i want to get a clone of this other example project where it has a react frontend, backend with nodejs and express (might adjust to django..) and then a database with postgresql. it does also use ngrok tunnel to get webhooks. considering this example already is getting transactions and will only require a change of the backend, im hoping this is a better jumping off point. im tired lol. 

1. trying something different again. okay i have downloaded the ngrok thingy after creating an account and then installed it with brew. then gave it the authtoken. cloned the pattern github thingy and went into the folder. copied the .env and then updated the .env file with creds. updated the ngrok.yml file with auth code.

2. ran (make start -- took a while) everything is up and working!! now to change things for my stuff. checked the (make logs -- dont know what this is tbh) was able to run (http://localhost:3001/admin) and can see users. in order to do development enviroment i need https with localhost and the instructions fot this are in the pattern readme. not yet doing this.

3. began playing with react devtools and reading thrpugh files. for some reason in a lot of the files, there are a bunch of red squiggle errors that things cant be found. i tried npm install but only got errors. decied to do make stop and then do make start agian in a bit. currently want to fiure out a bit more about typescript since that is what is being used. yikes. oh well. tried (npm install --save @types/react) - this seemed to have fixed a decent few of these issues! still some are there but idk. 

4. added a console.log in transactions.tsx and then did make start again. this did not help as i got this weird array thing that looked similar to a promise, not ideal but eh i shall keep trying. tried to add a console.log to items.js when transactions are fetched and this seems to have worked. now i am going to to the transactions.js db query page and play with the transactions there. i have now added a console log in the update transactions.js. 

5. well nothing is working and im going in circles trying to sort stuff out. looking at other options. likely too complicated to use the tabula bindings for python. the csv from the bank website does not have all the data i want even if it is more organized and more simple to handle. bank to looking at getting data directly from bank statemnts. 

welp. i think i need to change projects for now. i want to and will do this project at a later point but for now to meet the requirments for CP i need to do something different. 


[0-9][0-9]/[0-9][0-9]  reg ex to find date
(... to find card num used
[$][0-9], to find numbers with comma that needs to be ignored
