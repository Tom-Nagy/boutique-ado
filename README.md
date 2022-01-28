# **What You Need** :seedling:

![Mockup](mockup picture)

**What You Need** is an e-commerce web application that propose a range of indoor and outdoor plants to make your home or office healthier and a bit more special.  
This project is build with growth in mind and offer opportunities to add and improve features as the business develops.

For this project the use of Stripe's test functionality is implemented, rather than actual live payments.
You can make test payment with the following details:

| NUMBER                | BRAND            | CVC          | DATE            |
| --------------------- |----------------- | ------------ | --------------- |
| 4242424242424242      | Visa             | Any 3 digits | Any future date |
| 5555555555554444      | Mastercard       | Any 3 digits | Any future date |
| 378282246310005       | American Express | Any 4 digits | Any future date |

Visit the live Website : **[What You Need :arrow_right:](website link)**

## Table of Content

* [Project](#Project)
  * [Project Goals](#Project-Goals)
  * [Developer and Business Goals](#Developer-and-Business-Goals)
  * [User Goals](#User-Goals)
* [UX](#UX)
  * [Audience Definition](#Audience-Definition)
  * [User Stories](#User-Stories)
  * [Design Choices](#Design-Choices)
  * [Wireframes](#Wireframes)
  * [Different Design](#Different-Design)
* [Features](#Features)
* [Flowchart](#Flowchart)
* [Database](#Database)
  * [Database Design](#Database-Design)
  * [Database Structure](#Database-Structure)
* [Code Structure/Organisation](#Code-Structure/Organisation)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing) [:fast_forward: TESTING.md](TESTING.md)
* [Deployment](#Deployment) [:fast_forward: DEPLOYMENT.md](DEPLOYMENT.md)
* [Bugs](#Bugs)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Aknowledgements)

## Project

### Project Goals

What You Need is an MVP(Model View Project) build for educational purposes that promotes green and healthy homes and offices.

In this year 2022 we can observe a shift in lifestyles needs and organisation. People that use to spend most of their time at work, now work part or full-time from home.

One of today's challenges is mental health. People are more conscious about it, and they are looking for ways to improve their mental health. They want to feel good or better about themselves and about what they do.

Research prove that plants and natural elements provide a positive impact on people increasing well-being and productivity.  
This creates a market opportunity for helping customers improving their workspace and home. At the same time, the e-commerce market is expanding with more people using the web to get what they need every day.

In response to this demand, **What You Need** online shop offers a wide variety of plants. From the most delicate plants to the most indestructible. Customer can browse the website catalog by sorting or searching for specific categories, deals and plants.  
Registered and logged in customer will benefit of the full functionalities of the website including save items into a wishlist, ratings products and leaving reviews as well as reviewing their past order and making request about an order their orders with ease and confidence and accessing community accessible only plants. So get what you need today!

### Developer and Business Goals

* Develop a viable e-commerce web application.
* Provide a user-friendly interface.
* Provide an amazing user-experience across multiple device sizes.
* Improve Wellness and health.

### User Goals

* Easy to use application.
* Getting clear information.
* Quick access to products.
* Buy plants for their homes or offices.

[**:back:** *Table of Content*](#Table-of-Content)

## UX

### Audience definition

1. The primary targeted audience is very broad and address all **online customers**.
2. The secondary targeted audience is **Corporates or Businesses**.

Both targeted audience are looking for plants to buy for their home, office(s) or business. They can be considered as one. The difference will reside in the quantity needed. This is managed with specials deals category for larger orders.

### User stories

#### Customer stories

##### Website navigation and browsing

1. As a user, I want a user-friendly, simple and interactive website.
2. As a user, I want to be able to access the website on different devices with the same experience.
3. As a user, I want to find out what is the website purposes.
4. As a user, I want to search products by category.
5. As a user, I want to search for specific products.
6. As a user, I want to see more details about a product.

##### Shopping experience

1. As a customer, I want to easily identify what is the price of the product.
2. As a customer, I want to easily identify if the product is available.
3. As a customer, I want to choose the size and quantity of a product.
4. As a customer, I want to add/remove/edit product(s) in my shopping bag.
5. As a customer, I want to easily access my shopping bag.
6. As a customer, I want to make a purchase.
7. As a customer, I want the purchase process to be easy and secure.
8. As a customer, I want to be notified of the purchase I have made and be provided with a receipt.
9. As a customer, I want to contact the website owner about a past order.

##### Sign-in and registration

1. As a user, I want to create an account.
2. As registered user, I want to sign-in and sign-out easily.
3. As registered user, I want to change my password if forgotten or not safe anymore.
4. As signed-in user, I want to save/update information to my profile for a better and easier experience.
5. As signed-in user, I want to save products I like for a future purchase.
6. As signed-in user, I want to see/edit my wishlist.
7. As signed-in user, I want to access my previous orders.
8. As signed-in user, I want to leave a review on a product.

#### Site owner/Admin stories

1. As an Admin, I want to add/edit/delete products.
2. As an Admin, I want to add/edit/delete categories.
3. As an Admin, I want to see orders.
4. As an Admin, I want to manage customer queries.

[**:back:** *Table of Content*](#Table-of-Content)

### Design Choices

The approach concerning design choices is that the UX (User experience) should be the same across all platform and devices. Consistency being a key factor for UX.  
For this reason the UI (User Interface) is kept the same across different device sizes. This does not exclude the consideration for any extra or different features, should it improve the user experience.

#### Fonts

Considering the targeted audience, the sans serif type of font is the more appropriate because it is most often associated with simplicity and straightforwardness.  

The website will use well known and popular font that are used online in order to bring to the user a "feeling of knowing".

* *Poppins* for headings.

* *Lato* for main content.

*Sans serif* will be use as a fall back if the fonts do not load. It is common as the main typographies are sans serif type.

#### Icons

* Some Font Awesome icons will be part of the website for better UX.
* The [logo](app/static/images/logo/logo.png) and [favicon](app/static/images/favicon/favicon.ico) are the same image and use the color scheme of the website.

![logo](images/logo/logo.png)

#### Colors

![Color palette](colours-theme.png)

The colours chosen for the website are simple and joyful. They are based on the psychology behind colours ([colour affects](http://www.colour-affects.co.uk/psychological-properties-of-colours), [London Image Institute](https://londonimageinstitute.com/how-to-empower-yourself-with-color-psychology/)).

[Adobe Color](https://color.adobe.com) was used to build the colour scheme, compatibility and accessibility. The color scheme and swatches are said color-blind safe.

![Color accessibility](colours-accessibility.png)

#### Images

The images will be the one uploaded by website owner and/or Admin for products descriptions and website illustrations.  

MAYBE IMAGES WILL BE UPLOADED USING A DATA FROM A WEBSITE 111111111111111111

#### Styling/Feeling

The feel of the website is welcoming and simple to provide a quick access and learning process.  
It makes users comfortable.

#### Audio/Video

No audio or video will be integrated at the moment.

[**:back:** *Table of Content*](#Table-of-Content)

### Wireframes

![Site map](README-images/wireframes/site-map.png)

* [Home page](README-images/wireframes/home.pdf)
* [About page](README-images/wireframes/about.pdf)
* [Contact page](README-images/wireframes/contact.pdf)
* [Terms and Conditions of use page](README-images/wireframes/t-c.pdf)
* [Sign-in page](README-images/wireframes/signin.pdf)
* [create an account page](README-images/wireframes/create-account.pdf)
* [Products page](README-images/wireframes/products.pdf)
* [Product details page](README-images/wireframes/product-details.pdf)
* [Search page](README-images/wireframes/search.pdf)
* [Orders history page](README-images/wireframes/orders-history.pdf)
* [Order details page](README-images/wireframes/order-details.pdf)
* [Order issue page](README-images/wireframes/order-issue.pdf)
* [Account details page](README-images/wireframes/account-details.pdf)
* [Wishlist page](README-images/wireframes/wishlist.pdf)
* [Bag page](README-images/wireframes/bag.pdf)
* [Checkout page](README-images/wireframes/checkout.pdf)
* [Add product page](README-images/wireframes/add-product.pdf)
* [Add category page](README-images/wireframes/add-category.pdf)
* [Error page](README-images/wireframes/error-page.pdf)

For the full version:

* [What You Need website](README-images/wireframes/what-you-need.pdf)

[**:back:** *Table of Content*](#Table-of-Content)

### Different design

After considering deadline and features priority, I decided to leave the support section for future features to implement. I once heard that the project is never finished, we just run out of time!

[**:back:** *Table of Content*](#Table-of-Content)

## Features

To build this project, I use Django framework with the Jinja templating language. For consistency across the website some features will be repeated and functionality will be kept as simple and direct as possible.

* Navigation is always present and fix at the bottom of the page
  * Home
  * Account/profile
  * Bag
  * Search

* Browse product
  * By clicking the callout button on the landing page
  * By clicking the search menu button/icon
  * By category
  * By typing in the search bar

* Shopping bag
  * View the shopping bag
  * Add products to the bag
  * Remove/edit products in the bag

* Checkout
  * Purchase item securely with Stripe payment system
  * Save delivery information
  * Payment confirmation
  * Order confirmation

* Account/Profile
  * Create an account
  * Sign-in and sign-out
  * Update account information
  * Change password if forgotten or unsecure
  * Access orders history
  * File issue regarding an order
  * Access and update wishlist

[**:back:** *Table of Content*](#Table-of-Content)

## Flowchart

![Website flowchart](README-images/design/flowchart.png)

[**:back:** *Table of Content*](#Table-of-Content)

## Database

### Database design

The database design used is a relational database.

* During **development**, sqlite3 was used. It is the database provided by Django and only use for development.
* For **Production**, Postgres is used. It is the database provided by Heroku when deploying the website live.

Below is a representation of the database used for this project.
![Database Design](README-images/design/database-design.png)

### Database Structure

Django, the framework used for the production of this project, is an MVP: Model View Product/Project ??????? This means that the project build with Django is divided in multiple apps. Its structure allows separation of concern and provide many built-in features.  
The models define the data-structure.

* In this project, the following models have been developed:
  * Product
  * Category
  * Order
  * OrderLineItem
  * OrderIssue
  * User
  * UserAccount
  * Review
They can be grouped into three main models : Product, Order, UserAccount

* Models relationship:
  * Product :left_right_arrow: Category: **Many to Many**
    * A Product can be related to many Category, and a Category can be related to many Product.
  
  * Product :left_right_arrow: OrderLineItem: **Many to One**
    * A Product can be related to many OrderLineItem, but an OrderLineItem can be related to one Product.
  
  * Product :left_right_arrow: Review: **Many to One**
    * A Product can be related to many Review, but a Review can be related to one Product.
  
  * Order :left_right_arrow: UserAccount: **One to Many**
    * A Order can be related to one UserAccount, but a UserAccount can be related to many Order.
  
  * Order :left_right_arrow: OrderLineItem: **Many to One**
    * An Order can be related to many OrderLineItem, but an OrderLineItem can be related to one Order.
  
  * Order :left_right_arrow: OrderIssue: **Many to One**
    * An Order can be related to many OrderIssue, but an OrderIssue can be related to one Order.
  
  * UserAccount :left_right_arrow: Review: **Many to One**
    * A UserAccount can be related to many Review, but a Review can be related to one UserAccount.
  
  * UserAccount :left_right_arrow: User: **One to One**
    * A UserAccount can be related to one User, and a User can be related to one UserAccount.
  
  * UserAccount :left_right_arrow: OrderIssue: **Many to One**
    * An UserAccount can be related to many OrderIssue, but an OrderIssue can be related to one UserAccount.

## Technologies Used

### Programming Languages

This project was developed using:

* HTML
* CSS
* JavaScript
* Python
* Jinja templating language.

### Frameworks, Libraries and Programs

* [Django](https://www.djangoproject.com/)  
Framework used to develop the website.

* [Balsamiq](https://balsamiq.com/wireframes/)  
For creating wireframes.

* [lucichart](https://www.lucidchart.com/)  
For producing the flowchart and database design.

* [Google Fonts](https://fonts.google.com/)  
For importing fonts.

* [favicon.io](https://favicon.io/favicon-converter/)  
For generating the favicon.

* [TinyPNG](https://tinypng.com/) or [Squoosh](https://squoosh.app/)  
For resizing all the images.

* [BeFunky](https://www.befunky.com/create/)
For cropping some images.

* [Adobe Color](https://color.adobe.com/create/image)  
For extracting the color scheme used on the website.

* [Am I Responsive?](http://ami.responsivedesign.is/?url=http://ami.responsivedesign.is/#)  
For providing screenshots of the responsiveness of the website across several devices.

* [Autoprefixer CSS online](https://autoprefixer.github.io/)  
For adding prefixer in style.css for cross browser compatibility.

* [Git](https://git-scm.com/)  
For Version control.

* [GitPod](https://www.gitpod.io/)  
For Integrated Development Environment.

* [GitHub](https://github.com/)  
For hosting the repository.

* [Heroku](https://www.heroku.com/home)  
For deploying the website live.

[**:back:** *Table of Content*](#Table-of-Content)

## Testing

Testing information are published in a separate file for better readability.
Please see [TESTING.md](TESTING.md).

## Deployment

Deployment information are published in a separate file for better readability.
Please see [DEPLOYMENT.md](DEPLOYMENT.md).

## Bugs

## Credits

### Code

### Content

[W3schools](https://www.w3schools.com/)  

[W3docs](https://www.w3docs.com/)

[stack overflow](https://stackoverflow.com/)

[GeeksforGeeks](https://www.geeksforgeeks.org/)

[Net Lawman](https://www.netlawman.co.uk/d/website-privacy-policy)  
For privacy policy template.

### Acknowledgements

Special thanks to all Code Institute's team (“Teacher”, Lecturers and Tutors) that are making me more knowledgeable and are making this happen.

Huge thank you to the [Slack](code-institute-room.slack.com) community, all the members and all the leads and tutors for their help and support.

I am hugely grateful to my mentor Chris Quinn for guiding me through this project.

[**:back:** *Table of Content*](#Table-of-Content)
