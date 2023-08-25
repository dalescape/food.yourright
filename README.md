# my_personal_project

re cloned project. (to note: i got this to work only!! when i created a project within a project. )

created a requirments.txt file and pasted in from assesment and tutorial.
created virtual envriroment and activated it
did:
pip install -r requirements.txt
python -m pip install --upgrade pip
pip install django-cors-headers 
django-admin startproject foodyourright_proj .
django-admin startapp user_app 

settings:
'rest_framework'
'ENGINE': 'django.db.backends.postgresql', #<== Points to PostgreSQL
        'NAME': 'foodyourright_db',
'user_app'
AUTH_USER_MODEL = 'users_app.Client'
 'rest_framework.authtoken',
 'corsheaders',


added to admin.py in user_app

added to models.py in user_app

added to views.py in user_app

created and added to urls.py in user_app

created super user after adding username field to models.py 

superuser
1234

finally got the superuser server up, need to connect the urls tho. i did this correctly and accesed the admin site

created practice user -->
esmeraldaviolet
1234
esmeraldaviolet@gmail.com

ready to start up react. created new branch (fe)

npm created vite and installed. the npm run dev seems to be working?

updated the index.css with what i had, will need to edit obviously
added to main.jsx, well tried

created router.jsx 
created components folder and added a few with the basic bones. 
 created pages added those features in. 






