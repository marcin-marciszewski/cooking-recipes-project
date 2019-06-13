<h1>Cooking book</h1>
This website was created to help users add and organize their recipes. The application allows adding all important information about the particular recipe, such as ingredients, cooking method, preparing time, amount of serves, and many more. The created recipe can be later edited and changed. A user can filter available recipes by cuisine name, which list is displayed on the main site. New cuisines can be added to the list and edited. The application also provides a bunch of statistics about the library of the recipes. We can learn the total number of the recipes,  how many of them are assigned to the particular cuisine, also how many were created in a certain year. All the recipes are displayed in a visually attractive way with a picture of the dish and all the information provided. 
A user of the page has to register himself and login to get access to all the functionalities provided by the application. User's password is encrypted for better security and stored in a separated database. 

   
<h2>UX</h2>
 The application allows users to create and maintain a personal library of recipes. The main page is divided into three sections. First of them - About contains a link to the full list of the recipes and a button to create a new one, there is also a search field to find recipes by a keyword. The second section, named Cuisines, displays a list of available cuisines. Beneath, a user can find a link to the manager, where he can and a new cuisine or edit an existing one. In the Cuisines section, we can also find a link to a page with interactive statistics and charts.  The last section at the bottom of the main page - Contact, allows the user to send a message and shows the phone number.  The website is SPA ( single page application ) scaled for a variety of devices for easy access and use. The application was designed in a way to suit all users, and it's relatively easy to translate the content to other languages.
<ul>User stories:
<li>A user who wants to use all functionalities of the application needs to register himself by clicking "Sign Up" button and fill the required fields.</li>
<li>A user who comes back to the website needs to log in by providing the username and password used during the registration process.</li> 
<li>A user can add a new recipe by clicking on the "Add recipe" button, where he can find a form to provide all necessary information.</li> 
<li>A user can browse through all the recipes by clicking on the "All recipes" button.</li>
<li>A user who wants to see recipes from a particular cuisine can click on its name to see the list of them.</li>
<li>A user can add and edit existing cuisines by clicking on "Manage Cuisines" button.</li>
<li>A user who wants to see all the statistics about the library can click the  "Statistics" button.</li>
<li>A user who wants send a message can click "Send a message to us" and fill the form. </li>
</ul>
Pre-implementation mockups: 

https://docdro.id/iLRadZu

<h2>Features</h2>

The project was built for high performance and simplicity. The user interface was put together to allow navigation through the website in an easy and quick way. A picture carousel provides a good first impression and attracts a user visually. Logo in the left top corner is visible all the time to improve the visual identification. Login and registration feature help user protect their privacy. Search field lets a user find a wanted recipe quickly and without hassle. Adding a new recipe and cuisine is intuitive and straightforward for better user experience. The subpage with statistics and charts is clear and simple, and the required information is easy to extract. Contact form lets keep in touch with the administrators of the website and leave valuable feedback. The recipe cards are styled to ease access to all important information. On top of the card is the name of the dish with the cuisine of origin. Next, to the name, we can find a picture of the ready course. Below the picture is the preparation and cooking time, number of serves and date when the recipe was added to the library.  On the card, we can also find the list of necessary ingredients and step-by-step instruction. 
Every recipe card has an "Edit" and "Delete" button. 

<h2>Technologies Used</h2>

Technologies Used:
- HTML
- JavaScript and JQuery
- SASS
- Bootstrap
- Python and Flask



<h2>Testing</h2>
The application was tested on many devices and browsers. The HTML and CSS structures were validated with C3W Markup Validator and C3W CSS Validator. Jasmine and Jasmine-Jquery were used for testing.

1. Using the main site.<br>
a) The main page displays all basic sections and buttons. Images, texts and styles are visible and loading properly.<br>
b) All link to the subpages were tested and working correctly - leading to the subpages.<br>
c)The front page was tested on a variety of devices and resolutions to make sure that the content is adjusting to the different screen sizes.<br>
d) The search functionality working properly and find all the recipes containing wanted keywords.

2. Registering / Login<br>
a) A new user can create a new account by adding username and password to the database.<br>
b) Passwords are encrypted before sending to the database.<br>
c) A user can log in to the website using data information provided during the registration process.<br>

3. Browsing through the recipes.<br>
a) All recipes are displayed correctly either in "All recipes" or in particular cuisine.<br>
b) All information provided by the user is visible on the recipe card, including the picture.<br>
c) Recipes are grouped by three on a single page using pagination.<br>
d) Edit function allows adding new information and modifies the existing one.<br>
e) Delete functionality removes the recipe from the page and the database.<br>

4. Statistics<br>
a) The total number of recipes is displayed properly and change after adding or removing a recipe.<br>
b) All the charts are working correctly, displaying necessary information and updating after changes in the database.
5) Send message.<br>
a) The link to the message form is working correctly.<br>
b) All required fields have to be filled before sending the message.<br>
c) A new message is received instantly on the provided email address.<br>

Jasmine and Jquery-jasmine were used for testing  index.html.<br>
When you run the index.html file, visit:<br>
http://URL.com/jasmine-testing/spec/spec-runner.html<br>
where can be http://localhost:8081/jasmine-testing/spec/spec-runner.html<br>
<br>
All the tests conducted by Jasmine check:
- All the buttons on the main page lead to the subpages.
- The navbar contains the necessary class.
- The collapsing menu is activated by click hamburger button.
- The body of the main page contains three sections: about, cuisines and contact
Some tests were done for the backend using the unittest library in Python 3, and the results can be found in the test.py file.


<h2>Deployment</h2> 

The site was deployed on Heroku.com and can found under this address: https://cooking-recipes-project.herokuapp.com/. The copy of the final version and previous development version can be found on GitHub: https://github.com/szantilas87/cooking-recipes-project. A list of all necessary dependencies is in the requirements.txt file.<br> To run the project, some environment variables are needed:<br> 
IP <br>
PORT <br>
MAIL_USERNAME - email address you want to use<br>
MAIL_PASSWORD - password for the email address<br>
MONGO_URI - set up MongoDB database on https://www.mongodb.com/ or your local environment<br>
SECRET_KEY - any string<br>

<h2>Credits</h2>
<h4>Content</h4>
-Some functionalities were created with Shane Muirhead's help: shanemuirhead.co.uk.<br>
-A lot of ideas and some pieces of code were created thanks to YouTube channels: 
Pretty Printed - https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ
Corey Schafer - https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g

<h4>Media</h4>

-All the pictures used on the website were taken from https://unsplash.com/.<br>
-Recipes and pictures of ready dishes are from https://www.bbc.com/food/recipes.  








