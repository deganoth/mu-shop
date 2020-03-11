# MuShop - Ecommerce platform
### [MuShop on Heroku]
### What is this?
MuShop is a Django based online music shop. It makes use of Stripe for taking payments(test payments only), Amazon S3 for cloud based file storage, and Heroku for app and database hosting. It provides the user the ability to create, edit or delete products, manage orders, monitor reviews and manage users. The customer can browse,  purchase products and receive a receipt, leave product reviews and compare products .
### UX
The app front end is designed to be used by consumers of music instruments. With a simple, clean layout and color palette, each element is obvious and accessible. It displays well on all platforms with collapsable elements and appropriate size changes per platform. As actions are taken, such as adding an item to the compare function, or the shopping cart, messages display confirming the action has taken place. Colour associated Counters for both compare and cart tell the customer quantity levels per page. Stock levels are visible per product, informing the customer of availability.
In the admin section, 4 model groups can be seen. Each has associated sub models grouped to the parent model. Each model is searchable apart from the Order model. It is set by date, so only the most recent orders shows at the top. For front end styling and design, [Materialize] was used. Much like Bootstrap, it uses flexible containers set in a grid of 12 per row. This makes layouts already functional and quick to design
### Functionality
Front end functionality is flexible in appearance by design. Components resize to suit the user chosen platform. The navigation menu details all available products grouped by category. A user account feature is available on this app. When un registered or logged out, a "Register", and "Login" menu item are shown. Once logged in, these change to "Profile", and "Logout". This is known as Business Logic. While an account is not required to browse the site, it is required to make purchases. This saves the customer profile details for future purchases. Following this in the navigation bar are Compare and Cart. Both of these use the browser session context to store model items respectively. Compare only allows one of each Product model to be stored, while the Cart can have multiple. Contexts don't store data for future use, it is only present in the current browser session. Items can be removed from the Compare function, and quantities can be updated in the Cart. A search bar is the final Navigation element. It can find results by searching through the Product model fields for words associated with the navbar input. The Checkout function requires a user profile to access. All items from the cart are added to the checkout. Postage details are requested, along with a Stripe payment form for processing payments. The dummy card used is a US based card, and so has a US based ZIP code. Dummy card details are below. Once Payment is complete, an order details page is presented. This page is then emailed to the associated user account email.
| Stripe Field Name | Value |
| ------ | ------ |
| Card Number | 4242 4242 4242 4242 |
| CVV | Any 3 digits will do |
| Expiry Date | Any future date and year |
| Post Code | Any 5 digits will do |

### Feature
**Home page**
This is a summary page designed to tell the customer about news and current activities of the shop. Banner ads appear featuring product highlights or events, and new products are listed below.

**Pagination**
This feature is attached to the Product model. For flexibility purposes, different product quantities are shown per page on the home page, and the products page. It makes use of the Paginator function from Django. It sets the number of items per page and allows the user to click through each page until the database has been cycled through. On the home page, 4 products must be visible before pagination becomes available. On the product pages (All products for example), 5 products are shown before pagination is visible. This can be changed based on the database size.

**Stock counter** 
Available on each product is a stock quantity counter. It displays current stock quantities available of that product. If a quantity of the product is purchased, the stock level changes to reflect it. When the quantity reaches 0, the "Add to Cart" button is disabled. This protects the shop and customer. The quantity check is performed on each product in the html template with the Django Templating language. 

**Search Function**
Available in the navbar, this function searches through each product model field. It takes an input from the user, and checks each field against this input. If the input value is present in any field, a result is shown. If not, a page declaring "0 results found" is shown offering the user to browse or try to search again.

**Product display**
The navbar offers different product model display options. As the model is split into categories, each category is available to view by selecting the name from the navbar. This is achieved by filtering by category in the product views. In the admin panel, categories can be created. Each category has an associated number. Each product in turn has an associated category. The category model is paired with the product model by setting the category field in the product to the a Foreign Key, the Category model. This allows filtering of the product models through the category field.

**Reviews**
A feature that allows the customer to rate and review any product in the database. Reviews are stored in the admin section. Each review is presented at the bottom of the single product template. An average rating is displayed also. This is based on a calculation that counts the number of ratings present, and gets the average number. This is then presented in the review section as a float. Each review can be expanded by clicking the "read more" link below the comment. This leads to a full review page for each review.

**Compare function**
This allows users to compare a number of products in detail. It makes use of the browser session context to add only one product of each type to the compare tab. This is then updated visually with a counter that is colour associated with the compare button on each product. When in the compare page, each product is displayed in detail. To do this, a contexts python file must be created in Django, along with a context processor in the settings python file middleware section. This allows Django to create lists in the browser session. In the contexts python file function, a reference to the selected product is created, along with a list and quantity variable. These updated as products are added.

**Cart function**
Much like the compare function, the cart makes use of a context python file for creating lists in the browser session, however in the cart function, each product has a quantity that can be updated on the cart template page. A check is in place to make sure the user cannot add a quantity greater than the available quantity in the product model. This model is required to fill the checkout template with the required product quantities and information. 

**User accounts**
Using the built in Django Authorisation and Authentication feature, user accounts were created. These make use of the custom backends available by specifying "AUTHENTICATION BACKENDS" in the settings. python file to be the associated models. Custom forms and and views with form validation were required to verify user details. To allow a user to sign in with both username and password, a backends python file was created. This sets the username to the user email, allowing sign in with either. This is registered in the settings python file also. Custom styled user account templates were created to keep the user associated with the front end shop. The ability for the user to edit their profile, or reset their password are also available. A request is made via the user profile, or login page to reset the user password. A password reset page loads requesting the user email. Once entered and sent, a custom email with a unique token is received by the user to reset their password. This is generated in the url_reset.py file using python regular expressions.

**Stripe Payments**
As a checkout demo, Stripe payments has been added. This requires a Stripe account, and for the current version of stripe (V3), [Stripe Elements]. Both a custom JavaScript file and html form with specific tags are required for this to function. Once an account is setup with Stripe, a Test Publishable key and Secret Key are provided. The secret key must be set as an environment variable in the Django backend to ensure payment security. It along with the stripe app are registered in the settings python file . The publishable key must be present in the custom JavaScript file for the checkout to complete. Security issues are discussed here - [Stripe Elements Publishable Key Security Query] - Within this file, card elements are created and "mounted" in the checkout template by referencing div id names specific to each element. A unique "Token" is then created as the transaction takes place. It is set in a hidden div on the card details form. This is injected via the Django checkout views file. Once complete, a payment is sent to stripe, and a receipt page loads in the MuShop app

**Email Receipt**
Making use of [Sendgrid], A copy of the receipt page is sent to the user account email. Send grid was used as an alternative to gmail, as there is a known bug with Django and the smtp server of gmail. It is implemented in much the same way in the settings python file. Differences are the need for an API key from sendgrid via the sendgrid admin panel. Additionally, two sendgrid options must be declared. Sandbox mode must be False, so emails send, and "SENGRID_ECHO" must be set to false. This stops any other output being sent other than the browser.
 
### Technologies Used for Development
* [Windows 10]
* [Command prompt]
* [Sublime]
* [Python 3.8]
* [HTML/CSS]
* [JavaScript]
* [Django]
* [Stripe Payments]
* [Amazon S3 Buckets]
* [Heroku App Hosting]
* [Heroku Postgres Database]
* [Github]
* [Sendgrid]
* [Dilliner Markdown Editor]

### Testing
A full write up is available in the UX folder in the github repository. Below is a summary of all testing performed.
- Virtual environment used for testing SQLite3 database, as postgres on Heroku was unavailable. 
- Tests written to test views, forms and models.
- Code validation was achieved using coverage html.
- Manual Testing and feedback provided by work colleagues. 
### Deployment
**Local build**
To work on this project locally, navigate to your chosen folder, clone the repository in your chosen os terminal (cmd.exe, git bash, powershell) and use the following commands:
```sh
git init
git clone https://github.com/deganoth/mu-shop.git
```
Git init creates a new git repository. Once cloned, install the requirements.txt using this command:
```sh
pip install -r requirements.txt
```
Then migrate the model database using this command:
```sh
python manage.py migrate
```
Accounts from third party services required to use this app are:
- [Sendgrid]
- [Stripe Payments]

Once created, make an env.py file with the following content. Replace each item with the required key.This file is required to secure these private keys.
```sh
import os

os.environ.setdefault("STRIPE_PUBLISHABLE", "your_stripe_publishable_key")
os.environ.setdefault("STRIPE_SECRET", "you_test_stripe_secret_key")
os.environ.setdefault("SECRET_KEY", "your_django_secret_key")
os.environ.setdefault("SENDGRID_API_KEY", "your_sendgrid_api_key")
```
Update your checkout.js file in the static/js directory with your stripe publishable key:
```sh
var stripe = Stripe('your_stripe_publishable_key');
```
An important step to access the admin panel of this project is to create a super user in Django. This area of the site is access by adding "/admin" to the end of the homepage url when viewing in the browser. Add a super user with the folling command:
```sh
python manage.py createsuperuser
```
To run the server, use the command below:
```sh
python manage.py runserver
```
As a local build, SQLite3 will be the database. When creating products, image sizes should be 750 x 850 for best results. The large banner should be 800 x 400, and the two small banners should be 400 x 150. Image files will be stored in the media/images folder. 

**Heroku build**
Accounts and services from third party services required to use this app are. :
- [Heroku Postgres Database]
- [Amazon S3 Buckets]

Amazon S3 buckets is not required, as heroku whitenoise can be used instead. The latter however stores files for a limited time

For Heroku, Sign up, create an app with a unique name. For postgres, heroku has an add-ons section in the overview of your created app. Click on the add-on search bar and search for "postgres". Add the hobby dev as your pricing plan, it's free.
A database url will now be present in your settings tab under the hidden configs. Once revealed, add each line in your env.py to the hidden configs, as they will be read by heroku when your app is uploaded.

Amazon S3 has a detailed setup. A tutorial can be found at the link below detailing each step of the process.
- [Amazon S3 Buckets Tutorial]

Once activated, go to the settings.py file and update the "AWS_STORAGE_BUCKET_NAME" with your chosen name, and update the env.py as follows, replacing each new key with your respective keys:
```sh
import os

os.environ.setdefault("STRIPE_PUBLISHABLE", "your_stripe_publishable_key")
os.environ.setdefault("STRIPE_SECRET", "you_test_stripe_secret_key")
os.environ.setdefault("SECRET_KEY", "your_django_secret_key")
os.environ.setdefault("DATABASE_URL", "your_heroku_postgres_url")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "your_amazon_access_key")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "your_amazon_secret_access_key")
os.environ.setdefault("SENDGRID_API_KEY", "your_sendgrid_api_key")
```
Head back over to Heroku and add each new line to the hidden config variables. Update your database to postgres on heroku using the command:
```sh
python manage.py makemigrations
```
Then migrate to postgres using:
```sh
python manage.py migrate
```
To update any static files from now on, use the command below. They will be stored on Amazon:
```sh
python manage.py collectstatic
```
This will collect all required static files to a folder called "staticfiles". This is read by the settings in setting.py and uploaded once the command is complete. Finally, use the commands below to push your project to heroku for hosting:
```sh
git add .
git commit -m "Your comment here"
git push heroku master
```
### Solutions found
- [Custom widget field class names - for use with Stripe Elements]
- [Stripe Elements Separation]
- [DjangoMoney - currency selector]
### Tutorials
- [Vitor Freitas - Django Migrations Tutorial]
- [Vitor Freitas - Django Forms Tutorial]
- [Vitor Freitas - Django Pagination Tutorial]
- [Max Goodridge - Django Forms]
- [Jose A Dianes - Review models Tutorial]
- [TestDriven Stipe Elements with Django Tutorial]
- [Marcelo Canina - Sending emails in Django Tutorial]
- [DjangoBook - Admin panel customization]
### Ideas
- [Stripe Elements Examples]
- [Stripe Payments with Django Tutorial]
- [Using Google for Django Storages]
### Credits
My Mentor, [Spencer Barriball] for showing me the ropes, and being a great teacher.
[Code Institute] - For making this possible.
[Vitor Freitas] - Amazing Django Tutorials
[Max Goodridge] - Django Maestro
[Jose A Dianes] - Extremely well made Django Review Model Tutorial

**End of doc.**
    
   [Sendgrid]:<https://sendgrid.com/>
   [Windows 10]:<https://docs.microsoft.com/en-us/windows/apps/>    
   [Command prompt]:<https://www.computerhope.com/issues/chusedos.htm>
   [Sublime]:<https://www.sublimetext.com/>
   [Python 3.8]:<https://www.python.org/>
   [HTML/CSS]:<https://www.w3schools.com/html/html_css.asp>    
   [Javascript]:<https://www.w3schools.com/js/>
   [Django]:<https://www.djangoproject.com/>
   [Stripe Payments]:<https://stripe.com/ie>
   [Stripe Elements]:<https://stripe.com/docs/js>
   [Amazon S3 Buckets]:<https://aws.amazon.com/s3/>
   [Heroku App Hosting]:<https://www.heroku.com/>
   [Heroku Postgres Database]:<https://www.heroku.com/postgres>
   [Github]:<https://github.com/>
   [Materialize]:<https://materializecss.com/>
   [Dilliner Markdown Editor]:<https://dillinger.io/>
   
   [MuShop on Heroku]:<https://mu-shop.herokuapp.com/>
   [Jenkins Continous Integration Tutorial]: <https://medium.com/@mondaini/assembling-a-continuous-integration-service-for-a-django-project-on-jenkins-5f979d4c4184>
   [CircleCi Continuous Integration Tutorial]:<https://circleci.com/blog/continuous-integration-with-code-climates-automated-code-review/>
   [Pagination of Product Models]:<https://stackoverflow.com/questions/2266554/paginating-the-results-of-a-django-forms-post-request>
   [DjangoBook - Admin panel customization]:<https://djangobook.com/mdj2-django-admin/>
   [DjangoMoney - currency selector]:<https://github.com/django-money/django-money>
   [Stripe Elements Separation]:<https://jsfiddle.net/ywain/o2n3js2r/>
   [Vitor Freitas - Django Migrations Tutorial]:<https://simpleisbetterthancomplex.com/tutorial/2017/09/26/how-to-create-django-data-migrations.html>
   [Vitor Freitas - Django Forms Tutorial]:<https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html>
   [Vitor Freitas - Django Pagination Tutorial]:<https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html>
   [Weasyprint for Django Templates]:<https://github.com/fdemmer/django-weasyprint>
   [Weasyprint Tutorial]:<https://micropyramid.com/blog/generate-pdf-files-from-html-in-django-using-weasyprint/>
   [Dillinger online Markdown Editor]: <https://dillinger.io/>
   [TestDriven Stipe Elements with Django Tutorial]:<https://testdriven.io/blog/django-stripe-tutorial/>
   [Stripe Elements Examples]:<https://github.com/stripe-samples>
   [Stripe Payments with Django Tutorial]:<https://www.youtube.com/watch?v=6aQanCJZx04>
   [Using Google for Django Storages]:<https://django-storages.readthedocs.io/en/latest/backends/gcloud.html>
   [Max Goodridge - Django Forms]:<https://www.youtube.com/watch?v=JmaxoPBvp1M>
   [Jose A Dianes - Review models Tutorial]:<https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a>
   [Custom widget field class names - for use with Stripe Elements]:<https://stackoverflow.com/questions/41189852/cant-set-attrs-in-integerfield-widget-in-model-form>
   [Stripe Elements Publishable Key Security Query]:<https://github.com/stripe/react-stripe-elements/issues/359>
   [Gmail with Django bug]:<https://stackoverflow.com/questions/46020703/smtp-authentication-error-with-django-on-heroku#46020719>
   [Marcelo Canina - Sending emails in Django Tutorial]:<https://simpleit.rocks/python/django/adding-email-to-django-the-easiest-way/>
   [Amazon S3 Buckets Tutorial]:<https://medium.com/@manibatra23/setting-up-amazon-s3-bucket-for-serving-django-static-and-media-files-3e781ab325d5>
  
   [Vitor Freitas]:<https://simpleisbetterthancomplex.com/>
   [Max Goodridge]:<https://www.youtube.com/channel/UCAx4nmhI7S1RcPiaG-Uw0tg>
   [Jose A Dianes]:<https://github.com/jadianes>
   [Spencer Barriball]:<https://github.com/5pence>
   [Code Institute]:<https://codeinstitute.net/>


   
   
