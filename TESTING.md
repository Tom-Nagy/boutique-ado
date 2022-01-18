# TESTING

**[:leftwards_arrow_with_hook: *README.md*](README.md)**

Visit the live Website : **[What You Need :arrow_right:](https://what-you-need.herokuapp.com/)**.

## Table of Content

* [Code Validation](#Code-Validation)
  * [W3C](#W3C)
  * [JSHint](#JSHint)
  * [PEP8](#PEP8)
  * [Regex](#Regex)
* [Lighthouse](#Lighthouse)
* [Cross Browsers Testing](#Cross-Browsers-Testing)
* [Manual Testing](#Manual-Testing)
  * [Functionality Testing](#Functionality-Testing)
    * [Home](#Home)
    * [Contact us](#Contact-us)
    * [Products](#Products)
    * [Product Details](#Product-Details)
    * [Review](#Review)
    * [Search](#Search)
    * [Shopping Bag](#Shopping-Bag)
    * [Checkout](#Checkout)
    * [Create an account / Sign in](#Create-an-account-/-Sign-in)
    * [Account details](#Account-details)
    * [Orders history](#Orders-history)
    * [Report an issue](#Report-an-issue)
    * [Wishlist](#Wishlist)
    * [Product management](#Product-management)
    * [Category](#Category)
    * [Product](#Product)
    * [Orders](#Orders)
  * [Conclusions and Notations](#Conclusions-and-Notations)
* [User Stories Testing](#User-Stories-Testing)
  * [Customer stories](#Customer-stories)
  * [Site owner/Admin stories](#Site-owner/Admin-stories)
* [Further Testing](#Further-Testing)

## Code Validation

All code validation has been done using text input. The code was copied from the source code of the browser inspect page. This allows to check HTML without getting error because of Jinja template.

### W3C

W3C Markup Validation Service and W3C CSS Validation Service have been used to check all the pages of the website for semantic and syntax errors.
The results show no errors and the code is valid.

* [W3C Markup Validation Service](https://validator.w3.org/)

* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
  * ![W3C CSS Validation Result](app/static/images/README-images/TESTING-images/code-validation/css-validator.png)

[**:back:** *Table of Content*](#Table-of-Content)

### JSHint

[JSHint](https://jshint.com/) was used to validate the JavaScript code for semantic and syntax errors. No warnings or error were found.  
The results are positive, and the code is valid.

### PEP8

[PEP8 online](http://pep8online.com/) was used to validate the Python code for semantic and syntax errors. No warnings or error were found.  
The results are positive, and the code is valid.

Exception:  
one line of code is too long and correspond to the regex pattern variable for password validation.

### Regex

[Regex101](https://regex101.com/) to check implementation of regex pattern.

## Lighthouse

[Lighthouse](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools) is a tool provided by Google Chrome DevTools and allows to identify the site performance, accessibility and user experience on Mobile and Desktop.  
All the pages from the website have been tested with Lighthouse.

* The scores given by Lighthouse for:

  * **SEO** (Search Engine Optimization) show **Crawling and Indexing** issues with invalid robots.txt file. I have done some research but found the subject out of scope and myself in the complete dark, running out of time I decided to leave it the way it is.

  * **Accessibility** show issues regarding contrast. Those apply to some material icons that are only esthetic element and provide no information to the user. ``aria-hidden="true"`` has been added to those elements

  * **Accessibility** show issue regarding form label. This is raised by the fact that Materializecss used javascript to change the ``select`` tag to an input that does not have a corresponding label. So error is shown even though the select tag has a corresponding label. As well the date and time input have a default label and therefor through an error.

  * **Best Practice** show issues regarding image size and more precisely the favicon size expectation against the size produced on the website. Even after changing to the expected size shown by the error, the issue still exist with different sizes. This is not a major issue and I decided to leave it that way at the moment.

[**:back:** *Table of Content*](#Table-of-Content)

## Manual Testing

* Manual testing was executed on several browsers (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari and Opera) and shows good functionality across them all.
* The responsiveness of the website for different viewport sizes was tested by dragging the window up, down, left and right.  
* The following tests have been executed several times at different viewport breakpoints and on different devices.  
* Friends, fellow Code Institute students and family members tested the website on different devices.

### Functionality Testing

#### General features

* Buttons change state/style
  * on hover :heavy_check_mark:
  * on focus :heavy_check_mark:
  * on active :heavy_check_mark:
  * on click and expected behavior happens :heavy_check_mark:
* Link change state/style
  * on hover :heavy_check_mark:
  * on focus :heavy_check_mark:
  * on active :heavy_check_mark:
  * on click and expected behavior happens :heavy_check_mark:
* Forms validation
  * inputs/ content :heavy_check_mark:
  * on submit :heavy_check_mark:
* Modal Triggers :heavy_check_mark:

#### Home

* Clicking on the callout button brings the user to see all the products available on the website.
* The contact-us button is functional and redirect the user to the correct page.
* The About-us button is functional and redirect the user to the correct location.
* The Terms and Conditions of Use button is functional and redirect the user to the correct location.

[**:back:** *Table of Content*](#Table-of-Content)

#### Contact us

* Clicking on contact us direct the user to the contact us page correctly.
* The contact us form information fields are prefilled is the user is registered and signed-in.
* If the form is not filled correctly, the user cannot submit/send.
  * Feedback is given to the user for requested fields and incorrect values.
* When the form is filled in correctly the user can submit/send.
  * Feedback is given for successfully sending message.
  * An email is sent to the website owner successfully.

[**:back:** *Table of Content*](#Table-of-Content)

#### Products

* Stacking and display of the products is responsive.
* The total number of products is displayed and adjust accordingly.
  * A message informs the user that more detailed search is available through the search menu.
* The sorting button is displayed and toggles when clicked.
  * Sorting options are functional and display the correct and appropriate content.
    * Price low to hight :heavy_check_mark:
    * Price hight to low :heavy_check_mark:
    * Rating hight to low :heavy_check_mark:
    * Name Abc :heavy_check_mark:
    * Name Zyx :heavy_check_mark:

[**:back:** *Table of Content*](#Table-of-Content)

#### Product Details

* Clicking on a product brings the user on the product details page.
* All information are displayed.
* The quantity button to adjust the number of items is functional
  * User can adjust quantity by direct input.
  * User can adjust quantity by clicking the plus or minus button.
  * Quantity limits are functional the minimum being 1. EVEN BY DIRECT INPUT ??????????
* Add to bag button is functional.
  * When clicked A feedback popup gives information to the user with the product name and quantity.
  * When the quantity of the product is adjusted, the correct amount is added to the bag.
* Reviews are displayed correctly.
  * To leave a review the user must be registered and signed-in.
* A heart icon, for adding to the wishlist, is displayed correctly.
  * To add an item to the wishlist, the user must be registered and signed-in.
* A back button allows the user to return the all products or the corresponding category search.
  * Upon clicking the user is redirected to the correct page.

[**:back:** *Table of Content*](#Table-of-Content)

#### Review

* Reviews are displayed correctly.
  * Reviews are displayed from the most recent to the oldest.
  * If there is no review for a product, a message is displayed to the user.
* Submit a review is only available and displayed if signed-in.
  * A message informs the user that leaving a review is possible if signed-in.
* Submitting a review is functional.
  * Rating must be given to submit.
  * Content must be filled with a minimum of four characters.
  * If the above is not conditions are not fulfilled, an error message appear and the review will not be submitted.
* Feedback is given on submit.
* The product rating is updated successfully on submit.

[**:back:** *Table of Content*](#Table-of-Content)

#### Search

* Search bar is displayed.
  * When a user input a keyword, correct products are presented.
  * When a user is clicking search with no input, an error message is displayed for feedback and user redirected ???????????///
  * The total number of products per search is displayed and adjust accordingly.
* Search categories are displayed.
  * All categories are displayed.
    * Each category present the correct information.
    * When a category is selected, it displays the correct products.
* Sorting button is displayed with the search result page.
  * Sorting options are functional and display the correct content.

[**:back:** *Table of Content*](#Table-of-Content)

#### Shopping Bag

* Clicking on the Shopping bag icon brings the user to the correct page.
* Products and related information are displayed correctly.
* The quantity button to adjust the number of items is functional
  * User can adjust quantity by direct input.
  * User can adjust quantity by clicking the plus or minus button.
  * Quantity limits are functional the minimum being 1. EVEN BY DIRECT INPUT ??????????
  * Product quantity adjusts when clicking on the update button.
  * Feedback is given when quantity is changed.
* The delete item(s) button is displayed correctly.
  * On click item(s) are successfully removed.
  * Feedback is given when item(s) are removed.
* Subtotal is displayed correctly.
  * The subtotal adjusts with the quantity accordingly.
* Delivery cost and Grand Total are displayed correctly.
  * Delivery cost and Grand Total adjust with items and quantity accordingly.
* EXPLAIN DELIVERY COST METHOD / THRESHOLD ECT...
* Keep shopping button is displayed correctly.
  * When keep shopping button is clicked, the user is directed to the all products page.
* Proceed to checkout button is displayed correctly.
  * When proceed to checkout is clicked, the user is directed to the checkout page.
* The shopping bag content remains in the browser unless the cache is clear or a purchase is made.

[**:back:** *Table of Content*](#Table-of-Content)

#### Checkout

* The checkout page is displayed correctly.
* The order summary/details correspond to the shopping bag content.
  * Products information with quantity and price are displayed correctly.
  * Delivery cost and Grand Total are displayed correctly.
* If the user is signed-in and had previously added its details, the checkout form is correctly prefilled.
* If the form is not filled in correctly the user is given feedback, and he will not be able to submit the form.
* An option to save the delivery details is available.
* When the form is correctly filled and the user clicks on the complete order button, he is directed to the order confirmation page.
  * Payment is processed.
    * The payment intent is successfully created on Stripe.
    * The payment amount corresponds to the shopping bag and order amount.
  * A feedback message is displayed.
  * A summary of the order is correctly displayed with the items, prices and delivery details.
  * A confirmation email is correctly sent to the customer.
  * The order is correctly added to the database.
  * If the user close the page before the order is completed:
    * The payment is processed correctly on Stripe using a webhook.
    * The order is created correctly in the database.
    * The email confirmation is correctly sent.

[**:back:** *Table of Content*](#Table-of-Content)

#### Create an account / Sign in

* Clicking on the profile icon toggles different options depending on the user status:
  * If unregistered or logged-out customer: the options of Creating an account or signing-in are given.
    * PICTURE
  * If the customer is logged-in: the options of Account details, Orders history, My wishlist and Sign-out are given.
    * PICTURE
* Create an account page is displayed correctly.
  * An option to sign-in is provided if already a customer.
  * If the form is not filled correctly the user will not be able to submit.
    * If the username/email already exist the user will have to choose a different one.
    * Feedback is given to the user.
  * When the form is filled correctly, the user is directed to the verify email page and a feedback message appears.
    * The email confirmation is correctly sent to the email provided upon registration.
    * Clicking the link provided in the email confirmation directs the user to the confirm email address page.
    * When clicking on confirmation, the user is directed to the sign-in page.
    * A confirmation feedback message is displayed.
* Sign-in page is displayed correctly.
  * If the form is not filled correctly the user will not be able to submit.
    * Username/email and password have to match for the user to sign-in.
    * An option to reset the password is provided if forgotten.
  * When the form is correctly filled, the user is successfully signed-in.
  * A successful feedback message is displayed.
  * If forgotten password is clicked, the user is directed to the password reset page.
    * When clicking on reset password, upon giving a correct and existing email/username, the user receive an email to reset their password.
    * Feedback is given to the user if the username/email does not exist or if successful.
    * In the email received, clicking on the link given to reset the password, the user will be directed to the change password page.
    * Clicking on change password upon entering a new correct password twice, a message informs the user that the password was successfully changed.
    * Signing-in with the new credentials will allow the user to access his account successfully.
    * If the user try to change his password with a previously used link he will be redirected to the bad token page explaining that the link was invalid. A new link is provided and directs the user to the reset password page.
* Signing-out directs the user to the home page.
  * Feedback is message is displayed.

[**:back:** *Table of Content*](#Table-of-Content)

#### Account details

* Account details page is displayed correctly.
* If the user has not previously saved any information an empty form is displayed inviting the user to enter his information.
  * The user has the option to save or delete his details.
  * When saved information button is clicked, the user is given a feedback message.
    * The details are correctly saved in the database.
  * When delete information button is clicked, the user is given a feedback message.
    * The details are correctly deleted from the database.
* If the user has previously saved delivery information a prefilled form is displayed.
  * The user has the option to update or delete his details.
  * When update information button is clicked, the user is given a feedback message.
    * The details are correctly updated in the database.
  * When delete information button is clicked, the user is given a feedback message.
    * The details are correctly deleted from the database.

[**:back:** *Table of Content*](#Table-of-Content)

#### Orders history

* Orders history page is displayed correctly.
* Orders are displayed from the most recent to the oldest.
* Clicking on the Order details button directs the user to the order details page correctly.
  * The order details page is displayed correctly.
  * Report an issue button is displayed correctly.
  * The back button is displayed correctly and directs the user back to the orders history page.

[**:back:** *Table of Content*](#Table-of-Content)

#### Report an issue

* Clicking on the report an issue button directs the user to the report an issue page correctly.
  * The report an issue page is displayed correctly.
  * If the form is not filled correctly the user will not be able to submit.
    * Issue type must be selected.
    * Issue description must be filled with a minimum of 25 characters.
  * When the form is correctly filled the user is directed to the orders history page correctly.
    * Feedback is given to the user.
    * The issue status is displayed correctly on the corresponding order.
    * The issue status is correctly changed when updated by the Admin.
    * The issue is correctly saved in the database.

[**:back:** *Table of Content*](#Table-of-Content)

#### Wishlist

* To add an item to the wishlist, the user must be registered and signed-in.
* A heart icon, for adding to the wishlist, is displayed correctly on the products.
* The wishlist page is displayed correctly.
* The user can remove an item from the wishlist.
  * Feedback is given to the user for successfully removing the item from the wishlist.
* The user can buy an item by clicking buy know.??????????????????????????????????????????????????????????????????????????????????
  * When clicking buy now, the user is directed to the shopping bag page correctly and the item is correctly added to the bag.
* The user can add an item to the bag by clicking the add to bag button.
  * When clicking on add to bag button, the item is successfully added to the bag.
  * A feedback popup gives information to the user with the product name.

[**:back:** *Table of Content*](#Table-of-Content)

#### Product management

When clicking on the profile icon, if the user is a superuser/Admin an extra link is displayed: Products management.

* Clicking on the products management link directs the superuser to the products management page correctly.
  * The products management page is displayed correctly.
  * Options are presented to the superuser:
    * Category: Add category / Manage category
    * Product: Add product / Manage product
    * Orders: All orders / Reported issues

[**:back:** *Table of Content*](#Table-of-Content)

##### Category

* When add category is selected, the superuser is correctly directed to the add category page.
  * If the form is not filled correctly the superuser will not be able to submit.
    * Feedback is given to the superuser for requested fields and incorrect values.
  * When the form is filled in correctly the superuser can submit.
    * Feedback is given for successfully adding category.
    * The category is correctly created in the database.
    * Superuser is directed to products management page.

* When manage category is selected, the superuser is correctly directed to the manage category page.
* The page displayed all categories correctly.
* If a category is selected the superuser is correctly directed to the category details page.
* The category can be modified or deleted by clicking on Modify or Delete button.
  * If the form is modified and not filled correctly the superuser will not be able to submit.
    * Feedback is given to the superuser for requested fields and incorrect values.
  * When the form is filled in correctly the superuser can submit.
    * Feedback is given for successfully modifying category.
    * The category is correctly modified in the database.
    * Superuser is directed to the manage category page.
  * When clicking on the delete button, the superuser will be prompted with a modal (defensive design) for confirming the action.
    * The superuser can delete or cancel the action taken.
    * If delete is selected, feedback is given for successfully deleting category.
    * The category is correctly deleted from the database.
    * Superuser is directed to the manage category page.

[**:back:** *Table of Content*](#Table-of-Content)

##### Product

When clicking on the manage product button, the superuser is directed to the all products page of the website. The search and sort options are the same as a user, so the superuser can browse the products exactly the same way. The difference is that with superuser credentials, when selecting a product, other options are available: Modify and Delete.

* When add product is selected, the superuser is correctly directed to the add product page.
  * If the form is not filled correctly the superuser will not be able to submit.
    * Feedback is given to the superuser for requested fields and incorrect values.
  * When the form is filled in correctly the superuser can submit.
    * Feedback is given for successfully adding product.
    * The product is correctly created in the database.
    * Superuser is directed to products management page.

* When manage product is selected, the superuser is correctly directed to the all products page.
* The page displayed all products correctly.
* If a product is selected the superuser is correctly directed to the product details page.
* The product can be modified or deleted by clicking on Modify or Delete button.
  * When clicking on the Modify button, the superuser is correctly directed to the modify product page.
  * If the form is not filled correctly the superuser will not be able to submit.
    * Feedback is given to the superuser for requested fields and incorrect values.
  * When the form is filled in correctly the superuser can submit.
    * Feedback is given for successfully modifying product.
    * The product is correctly modified in the database.
    * Superuser is directed to the product details page.
  * When clicking on the delete button, the superuser will be prompted with a modal (defensive design) for confirming the action.
    * The superuser can delete or cancel the action taken.
    * If delete is selected, feedback is given for successfully deleting the product.
    * The product is correctly deleted from the database.
    * Superuser is directed to the all products page or the category of the current search.

[**:back:** *Table of Content*](#Table-of-Content)

##### Orders

* When selecting all orders, the superuser is correctly directed to all orders page.
  * Orders are displayed correctly with all the relevant information.
  * When selecting an order, the superuser is directed to the order details page.
    * Order details are displayed correctly.

* When selecting reported issues, the superuser is correctly directed to the Reported order page.
  * All order with an issue status other than "none" or "resolved" is displayed correctly.
  * When selecting an order, the superuser is directed to the order details page.
    * Order details are displayed correctly.
    * The superuser can modify the order and change the issue status of the order.
    * The superuser can select "solving" or "resolved"
    * Changing the issue status updates the order details of the user accordingly.
    * If changed to "resolved", the order is correctly moved from all orders.

[**:back:** *Table of Content*](#Table-of-Content)

### Conclusions and Notations

All the features and functionality works very well across browser.

Noted issues on ...:

Noted general issue:

All those points are not major bugs to fix and will be implemented in the near future with the support section of the website.

[**:back:** *Table of Content*](#Table-of-Content)

## User Stories Testing

### Customer stories

#### Website navigation and browsing

1. As a user, I want a user-friendly, simple and interactive website.

    * The website is build with simplicity and consistency.
    * The website uses clean and spacious design.
    * The website applies all the accessibility protocols for an easy and good user experience for all.
    * The Navigation bar is fixed and always accessible providing quick access to the main features of the website.
    * The Navigation bar is designed to provide users with feedback on where they are "located" on the website.
    * All action taken by the user is met with feedbacks providing an interactive interface and playful content.

2. As a user, I want to be able to access the website on different devices with the same experience.

    * Content size and arrangement is adjusted with the viewport size without compromising features.
    * All features are kept the same regardless viewport sizes, providing the same experience no matter the device.

3. As a user, I want to find out what is the website purposes.

    * The home page provides all the information that a new user needs.
    * The About section of the home page describes the website goals and motivation.
    * The home page content provides information on the website focus.
      * The colours are a visual clue for plants and nature.
      * The statement and phrasing on the home page indicates what is the website content in a clear manner.
      * The callout button invites customers to find what they need.

4. As a user, I want to search products by category.

    * The menu provides a search button that opens the search options.
    * Categories are presented clearly in cards format including:
      * A clear title.
      * An image/icon for content representation.
      * Products number providing the number of items per category.

5. As a user, I want to search for specific products.

    * The menu provides a search button that opens the search options.
    * The search options include a search bar that provide the user with the mean of search per keywords or for a specific item.

6. As a user, I want to see more details about a product.

    * When browsing the website products, user can click on a product to see the product details.
    * The details include:
      * Price
      * Rating
      * Description
      * Availability
      * Reviews

#### Shopping experience

1. As a customer, I want to easily identify what is the price of the product.
2. As a customer, I want to easily identify if the product is available.
    * When browsing products, the user can find the most important information about an item without clicking on details:
      * Price / Rating / Stock availability.

3. As a customer, I want to choose the size and quantity of a product.

    * Most of the products are available in two sizes: small and large.
    * Users can choose their prefer size on the product details page or in the shopping bag.

4. As a customer, I want to add/remove/edit product(s) in my shopping bag.

    * The shopping bag provides the user with all the features needed.
    * Users can add items to their bag from products, product details and wishlist page.
    * Users can modify the quantity of an item using plus or minus button or by direct input and clicking update.
    * Users can remove product from their bag with the remove button.

5. As a customer, I want to easily access my shopping bag.

    * The shopping bag is accessible via the navigation menu in one click.

6. As a customer, I want to make a purchase.
7. As a customer, I want the purchase process to be easy and secure.

    * The website provides a full payment system implemented with stripe payment system.
    * By clicking on the Secure Checkout button of the shopping bag, the user will access the checkout payment and delivery page.
    * Completing the checkout by clicking on Complete Order on the checkout page will place the order and process the payment.
    * The process is secure and quick.
    * All relevant information will be prefilled if the user is register, signed-in and had previously provided and saved those details. This will potentially be true for a second purchase or purchase made after searching the website content.

8. As a customer, I want to be notified of the purchase I have made and be provided with a receipt.

    * Feedback is provided via a popup message to the user on a successful purchase.
    * An email confirmation is sent to the user with the order details and delivery address.

9. As a customer, I want to contact the website owner about a past order.

    * A contact us section is available on the home page or via the home button in the navigation menu.
    * An unregistered user can report an issue by answering the email confirmation of the order received when purchasing a product.
    * If the user is registered and signed-in, orders history is accessible via the profile button in the navigation menu.
      * Report an issue button is available on the order details for the user to report any queries or issue regarding this order.

#### Sign-in and registration

* Secure registration features are available on the Django framework.
  * Those features have been implemented and user can securely create/access an account.

1. As a user, I want to create an account.

    * Create an account is accessible from the profile button of the navigation menu.

2. As registered user, I want to sign-in and sign-out easily.

    * Signing-in and out of the website is easily accessible from the profile button of the navigation menu.

3. As registered user, I want to change my password if forgotten or not safe anymore.

    * When signing-in, the user have the option to click on reset password in order to generate a different password if it became unsecure or forgotten.

4. As signed-in user, I want to save/update information to my profile for a better and easier experience.

    * Account details is accessible from the profile button of the navigation menu.
    * The account details page stores all the delivery information about the user and prefilled all relevant fields accordingly when the user is signed-in.

5. As signed-in user, I want to save products I like for a future purchase.

    * Signed-in users have the possibility to saved products to their wishlist by clicking the heart icon available on a product.

6. As signed-in user, I want to see/edit my wishlist.

    * Signed-in user can access their wishlist via the profile button of the navigation menu.
    * Users can delete item from their wishlist.

7. As signed-in user, I want to access my previous orders.

    * Signed-in users can access their order history via the profile button of the navigation menu.

8. As signed-in user, I want to leave a review on a product.

    * Signed-in users can write review on a product from the review form available on the product details page.

### Site owner/Admin stories

* When a user with admin credentials sign-in, a Product management page is accessible from the profile button of the navigation menu.
  * The admin/superuser status provides access to extra features.

1. As an Admin, I want to add/edit/delete products.

    * Admin can access modify or delete features from the product details page.
    * Admin can add a product with the add product button of the Product management page.

2. As an Admin, I want to add/edit/delete categories.

    * Admin can add a category with the add category button of the Product management page.
    * Admin can edit or delete a category from the category list of category section of the Product management page.

3. As an Admin, I want to see orders.
4. As an Admin, I want to manage customer queries.

    * Admin can access and deal with customer queries from the orders section of the Product management page.
    * Admin can select from all orders or reported issue.
    * Reported issue will provide all order with an issue status other than "none" and "resolved".

[**:back:** *Table of Content*](#Table-of-Content)
