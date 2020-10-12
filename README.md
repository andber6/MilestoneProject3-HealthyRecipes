[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/andber6/MilestoneProject3-HealthyRecipes)

# My Public Recipe List! #

In this project I am creating a python project with flask and using mongoDB as my database to store and update records/recipes.
The goal of this project is simply to get a better understanding of the technologies used (refer to 'Techonologies used' section further down).

## UX ##

In this recipe project I have spent a lot of time getting it all to work correctly, but I am very happy with the end result.
I believe this project has great UX because of the user-friendly transitions, routing and styling with everything being easily accessed.

This website is simply for the purpose of learning, but is also a 'public repository' for recipes that anyone can add their own or find other creative recipes.

### Features ### 

* Smooth transitioning and great UX with the help of materialize
* Included a contact page in case of an employer were to come across my project
* A nice footer where I have mentioned the technologies used in this project as well as a couple links to get in contact or learn more about me
* Included a navbar for easy navigation and user-friendly
* With the help of great navigation, this application prevents several clicks to locate something or somewhere

### Features left to implement ###

* I have yet to fix a proper search option to be able to look through all the recipes in an efficient way in case the list would get long, but I chose to keep the search icon/button
regardless because I think it looked nice and I plan on fixing it in the future
* I left social icons out on purpose because I tried adding them and thought that the footer looked better without it. Hence the reason I just wrote "Github" and "LinkedIn"
and added the respective links instead of keeping the icons
* I have also yet to implement contact me form that sends mail directly to my mail from the form. I'm thinking of maybe solving this with emailjs, 
but thought that I should rather use my time on other things. By clicking submit, the application will open an email that will let them email me directly, 
but unfortunately does not send directly from the form as it is for now

## Technologies used ##

* Python
* HTML5
* CSS3
* JavaScript
* JQuery
* MongoDB
* Materialize
* Flask

## Testing ##

I have run numerous tests and I am positive that things finally work as they should.
I have conducted tests over a long period of time and struggled forever with getting all routing correctly set up, but as a result of all the troubling the routing has caused me, 
it also made me learn a great deal about routing and exactly what is going on. One of many things that took me forever to solve was when I was trying to update my recipes, 
I was running: 
recipes = mongo.db.recipes.find() instead of mongo.db.recipes. Or all the hours spent because I wrote:
{{url_for('update_recipe', recipe_id=recipe_id)}} instead of:
{{url_for('update_recipe', recipe_id=recipe._id)}}. 
I also encountered some problem with chache that made my css not apply even in inkognito mode, which I ended up finding a solution to: 'ctrl + shift + r' in inkognito mode has
helped me a lot in this project and saved me from numerous headaches.

I also had some trouble with git branches when trying to push to github, but a friend of mine was of great help.

### Deployment ###

* I deployed this project with heroku through github.
* Run the program with the command "python3 app.py" in the terminal
* I added the live link to my github repository so that anyone can just click that and easily see the final result in case of running the program through 
the terminal would be a little bit complicated for some
* I used an environment variable to be able to access my mongoDB, which I included in my .gitignore in order to keep it secret of course

### Acknowledgements ### 

I received the idea of a recipe list from code institute's milestone project suggestions and thought it was a great idea for me since I am very interested in fitness and living a
healthy lifestyle. 
I want to thank Google for all the help along the way, as well as Code Institute's tutors, and of course the stackOverflow community.