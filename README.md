# Scubasport International
(Developer: Daniel Richards)

![Mockup of Scubasport International](readme/mockup.jpg)

[View live site](https://scubasport.herokuapp.com/)

## Table of Content

1. [Strategy](#project-goals)
    1. [Site Owner Goals](#site-owner-goals)
    2. [User Goals](#user-goals)
    3. [Target Audience](#target-audience)
    3. [Business Model](#business-model)
    4. [SEO](#seo)
    5. [Marketing](#marketing)
2. [Structure](#structure)
    1. [Website pages](#website-pages)
    2. [Code Structure](#code-structure)
    3. [Database](#database)
    4. [Physical database model](#physical-database-model)
    5. [Models](#models)
        1. [User Model](#user-model)
        2. [UserProfile Model](#userprofile-model)
        3. [Product Model](#product-model)
        4. [Category Model](#category-model)
        5. [Brand Model](#brand-model)
        6. [Size Model](#size-model)
        7. [Color Model](#color-model)
        8. [Inventory Model](#inventory-model)
        10. [Course Model](#contact-model)
        11. [Contact Model](#reason-model)
        12. [Faq Model](#about-model)
    3. [Scope](#scope)
        1. [User Stories](#user-stories)
    4. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    5. [Surface](#surface)
        1. [Design Choices](#design-choices)
        2. [Colour](#colours)
        3. [Fonts](#fonts)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
6. [Features](#features)
7. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [JS Validation](#JS-validation)
    4. [Python Validation](#py-validation)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    7. [Device testing](#performing-tests-on-various-devices)
    8. [Browser compatibility](#browser-compatibility)
    9. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

# User Experience
## Strategy

### Site Owner Goals

The primary goal of the website from the site owners perspective is as follows:
- To enable customers to purchase products listed on the site
- To allow a user to navigate the website and view product details
- To allow a user to create an account & log in to an existing account
- To allow a user to view their order history and account details
- To allow users to keep updated with a newsletter signup
- To be able to edit, add and remove products from the site

### User Goals
- The primary goal of the website from a site users perspective is as follows:
- To view products and product details
- To easily search for products
- To filter products 
- To register for an account
- To log into/out of an existing account
- To be able to view and edit their account profile
- To add a product to bag and purchase order
- To be able to view order history
- To contact the site owner
- To sign up to a newsletter

### Target Audience
- Diving enthusiasts
- Active people
- People who want to learn to dive
- Qualified divers
## User Requirements and Expectations
- An easy navigation system with instant learning.
- Able to navigate the site quickly and easily.
- No broken links.
- Responsive and visually appealing on all devices.
- Ability to view products and complete purchases
- Ability to contact the business

## Business Model

For this project, as the primary goal is to sell products direct to consumers, I have chosen a B2C business model.  To align with this all considerations have been made on imagery, ability to search, an instructor recommends section on the home page, speed and ease to purchase, a product inventory with out of stock visibilty, and restrictions on purchasing more items than in stock.

The business model would be that scubasport buys products from wholesalers and then retails those products to the end customer at increased margin.


Alternatively, the business could arrange sale or return from the the supplier or sell driect from supplier stock in the online store and carry physical stock in thier own warehouse.

For the nature of this project, the stock is held pysically in the business.

## SEO

Long tag and short tag keyword were searched for in regards to SEO using Google tools and other online resources.  These tags have been used in the main HTML head and throughout the project to name images and within main body text.

![SEO keywords HTML](readme/misc/seo-keywords-html.png)

## Marketing

### Facebook Business Page

To assist with marketing the website, it has a link to its own social media page in the footer and that has a recipricol link to the site.

Facebook site can be viewed [here](https://www.facebook.com/Scubasport-103293935757804). 

![Facebook Screenshot](readme/misc/facebook-screenshot.png)
![Facebook Screenshot2](readme/misc/facebook-screenshot-2.png)

### Newsletter Signup

The site includes a signup form to a newsletter so the business can keep in touch with it's vistors.
![Sign-up](readme/misc/mailchimp-signup.png)

![Email-success](readme/misc/email-success.png)

## Structure
### Code Structure
The project is organised into a variety of applications, as is constructed using the Django Framework.

App details as follows:
- Home - this app contains information about the dive centre home page with quick links to the dive courses and product page, contact-us and about us via the nav bar.

It contains a footer with links to external sites and a mailchimp signup form.
- Products - this app contains the the product listings and detail views, users can add items to a shopping cart, filter for items in categories and hosts the results of the product search.  Clicking individual items opens a sub  page where users can see detailed product information.  The product app has a stock inventory so customers cannot add more to the bag than what is physically in stock.  When items are out of stock at that time this is rendered to the user.  
    - Staff can create, read, update and delete product and inventory items.
    - Staff can fully manage brands, sizes, categories and add and remove items to inventory.
- Courses - Users can view course listings and details and be redirected to the contact form to get in touch and enquire.
- About - this app contains information relating to the business and frequently asked questions.
- Contact - this app is for users to be able to submit a message to the site owners and recieve acknowledgment. For users with a profile, when logged in, the form prepopulates profile data to remove friction to the user.
- Profile - Users can choose to have a profile either when checking out or when authenticated.  Edit functionality exists and users can view thier purchase history.
- Bag - User can view, add and remove products that they have added to the bag
- Checkout - Users can use the checkout app to purchase selected items.  They can see items in the cart and have the option to save profile data during the checkout process.

To complement the apps there are
- project: Project level files - settings.py for project level settings and urls.py to route the website URLS
- templates: Containing the base.html, allauth(django authentication)
- templates (app level): each app has it's own templates directory for HTML to consider portability and re-use.
- urls (app level): each app has it's own url.py file to consider portability and re-use.
- static: Base css and Javascript files
- manage.py: This file is used to start the site and perform funcions during development
- README.md: Readme documentation
- Procfile: To run the application on Heroku
- Requirements.txt: Containing the project dependencies
Note: Environment variable values are not exposed in the source code, they are stored locally in env.py that is not checked in(and listed in .gitignore, and on Heroku in app settings

### Database
#### Physical database model

This model contains all fields stored in the database collections with their data type and mimics the structure of what is actually stored in the Postgres database 
<br>![Database model](readme/misc/database_schema.png)

#### Models
- The following models were created to represent the database model structure for the website

##### User Model
- The User model contains information about the user. It is part of the Django allauth library
- The model contains the following fields: username, password, first_name, last_name, email, is_staff, is_active, is_superuser, last_login, date_joined

##### UserProfile Model
- The UserProfile model contains information about the users address.  This can be created at anytime through the nav link or automatically added post checkout.  The UserProfile Model contains the following fields: userdefault_phone_number,default_street_address1,default_street_address2,default_town_or_city,default_county,default_postcode,default_country.

##### Product Model
- The Product model contains information about products available within each of the categories
- It contains Category as a foreign-key.
- It contains holding(Inventory) as a Many-toMany relationship.
- The model contains the following fields:  name, friendly_name, description,  category, gender, brand, holding, color, price, promoted, image, slug.

##### Category Model
- The category model contains the available categories for a product item
- The model contains the following fields: name, friendly_name

##### Brand Model
- The Brand model contains brands for the products.
- The model contains the following fields: name

##### Size Model
- The Size model contains a the sizes available for each product. This is linked to the product model through a custom intermediate model as a many to many relationship.
- It acts as a foreign-key for Inventory model and through to Product
- The model contains the following fields: name, friendly_name

##### Color Model
- The Color model contains viable colors for the products.
- It acts as a foreign-key for Product model
- The model contains the following fields: name

##### Inventory Model
- The Inventory model is a custom intermediate model that between Size Model and Product model as a many to many relationship.  It has an inventory count as an additional field and self generates a unique SKU on save
- The model contains the following fields: product, size, sku, count

##### Course Model
- The Course model contains a courses that customers can enquire about.  There is a subclass for different difficulty levels.
- The model contains the following fields: name, friendly_name, description, extra_details, price, duration ,level, image, slug

##### Contact Model
- The Contact model contains a collection of data submitted by the user when messaging the site owner.
- It contains Reasons subclass as a with preconfigured choices for the user to select
- The model contains the following fields: reason, name, email, phone, postcode, street_address, message.

##### Faq Model
- The Faq model contains a collection of frequently asked questions and answers for users to be able to get commonly sought information from the site without having to get in touch.
- The model contains the following fields: name, friendly-name, question, answer.


## Scope
### User stories:

1. As an unauthenticated user, I want to be able to navigate the website quickly and easily 
2. As an unauthenticated user, I want to have the option to view all products on the site
3. As an unauthenticated user, I want to be able to search the website for specific products and brands
4. As an unauthenticated user, I want to be able to view detailed descriptions and prices of the products
5. As an unauthenticated user, I want to be able to order the product pages by price, and alphabetically
6. As an unauthenticated user, I want to be able to sort and view products by category
7. As an unauthenticated user, I want to be able to view specific brands' products sold on the site
8. As an unauthenticated user, I want to be able to add a product to my bag
9. As an unauthenticated user, I want to be able to quickly navigate through product listing pages
10. As an unauthenticated user, I want to be able to view how many products are in my shopping bag at all times
11. As an unauthenticated user, I want to be able to navigate back to the products page after viewing product details
12. As an unauthenticated user, I want to be able to view products added to my shopping bag
13. As an unauthenticated user, I want to be able to increase quantities and remove items from my shopping bag
14. As an unauthenticated user, I want to be able to checkout and purchase products
15. As an unauthenticated user, I want to be able to create an account
16. As an unauthenticated user, I want to be able to log in to / sign out of an existing account
17. As an authenticated user, I want to be able to view and update my personal information in my profile
18. As an authenticated user, I want to be able to view my order history
19. As an unauthenticated user, I want to be able contact the business
20. As an unauthenticated user, I want to be able to receive news and updates from the business
21. As an unauthenticated user, I want to be able to view the business location
22. As a site owner, I want users to be able to navigate the website quickly and easily
23. As a site owner, I want users to be sign up to a newsletter to capture user information
24. As a site owner, I want users to be able to view the business social media
25. As a staff user, I want to be able to update and edit product descriptions, details and prices
26. As a staff user, I want to be able to add a brands to the brand list
27. 7As a staff user, I want to be able to update the brands listed
28. 7As a staff user, I want to be able to remove any brands listed
29. As a staff user, I want to be able to view and update products 
30. As a staff user, I want to be able to add products
31. As a staff user, I want to be able to delete products
32. As a staff user, I want to be able to manage product inventory
33. As a staff user, I want to be able to view and update product categories
34. As a staff user, I want to be able to add product categories
35. As a staff user, I want to be able to delete product categories
36. As an authenticated user, I want confirmation that I have signed out of my account
37. As a site owner, I want to make sure that customers aren’t able to purchase more products than what is listed in the inventory
38. As a site owner, I want to make sure that customers can see which products are out of stock
39. As an unauthenticated user, I want to be able to browse available courses
40. As an unauthenticated user, I want to be able to view course details and request a booking
41. As a staff user, I want to be able to view and update the courses listed
42. As a staff user, I want to be able to add a course
43. As a staff user, I want to be able to delete a course
44. As an unauthenticated user, I want to be able to find answers to frequently asked questions without having to wait for an answer from the site owner by filling in the contact form
45. As a user, I want to have confirmation that my order has been successful
46. As admin, I want to be able to create batch actions and manipulate all the data tables in one place
47. As a user, I want to be shown messages that my actions have been successful and unsuccessful*

#### Error Flow
45. As first time, I user should be able to navigate back through the site structure in case of page not found without using the browser back button.
46. As a site owner, I want error pages that enables users to be able to return to valid areas of the site without using browser controls.

## Skeleton

### Wireframes

<details><summary>About Us</summary>
<img src="readme/wireframes/about-us.png">
</details>

<details><summary>All-course</summary>
<img src="readme/wireframes/all-courses.png">
</details>

<details><summary>All-Products</summary>
<img src="readme/wireframes/all-products.png">
</details>

<details><summary>Checkout</summary>
<img src="readme/wireframes/checkout.png">
</details>

<details><summary>Contact Us</summary>
<img src="readme/wireframes/contact-us.png">
</details>

<details><summary>Course Details</summary>
<img src="readme/wireframes/course-details.png">
</details>

<details><summary>Error Page</summary>
<img src="readme/wireframes/error.png">
</details>

<details><summary>Home</summary>
<img src="readme/wireframes/home-page.png">
</details>

<details><summary>Order History</summary>
<img src="readme/wireframes/order-history.png">
</details>

<details><summary>Payment Confirmation</summary>
<img src="readme/wireframes/payment-confirmation.png">
</details>

<details><summary>Product Details</summary>
<img src="readme/wireframes/product-details.png">
</details>

<details><summary>Profile Edit</summary>
<img src="readme/wireframes/profile-edit.png">
</details>

<details><summary>Profile</summary>
<img src="readme/wireframes/profile.png">
</details>

<details><summary>Register</summary>
<img src="readme/wireframes/register.png">
</details>

<details><summary>Cart</summary>
<img src="readme/wireframes/shopping-cart.png">
</details>

<details><summary>Sign-in</summary>
<img src="readme/wireframes/sign-in.png">
</details>

<details><summary>Sign-out</summary>
<img src="readme/wireframes/sign-out.png">
</details>

<details><summary>Manage Categories</summary>
<img src="readme/wireframes/staff-manage-categories.png">
</details>

<details><summary>Manage Brands</summary>
<img src="readme/wireframes/staff-manage-brands.png">
</details>

## Surface

### Design choices
The aim of the design of the website was to create a clean and modern website, photography imagery is used to show business values and create an enticing site that the visitor wants to explore. 
The fonts are bold, clear and modern, with clear headings to enable easy navigation.

### Colours
The colour scheme is primarily blues to represent water which matches the business theme. 
#FFFFFF – Titles & subtitles
#FFFFFF - Body text
##315673- Buttons
##5392C2– Button highlight & search bar
#000000 – Image overlay text
insert colour palette image
After choosing a colour scheme I tested a number of palette options to make sure the it met accessibility standards.
<br>![Color](readme/misc/color.png)
<br>![Accessible Color](readme/misc/accessible-color.png)

### Typography
Poller One is the font uses for the logo, this font is from the Google Fonts.
Urbanist is the font used across all of the headings and text across the website, it has been used in different 
weights and different cases to highlight titles. This font is from the Google Fonts Library.

## Features

The site consists of 12 pages, with the features detailed under each page.

1. Home page
2. Shop
3. Brands
4. Courses
5. Log in
6. Log out
7. Register
8. Profile page
9. Shopping Cart
10. Contact
11. About
12. Admin

### Page 1 – Home page
<br>![Home page](readme/features/home-page-nav-bar.png)

The home page consists of the following features:

#### Feature 1 – Header and navigation bar
The header contains the logo, products link, brands link, search bar, user account and shopping bag. The header is visible across all pages.

This feature covers the following user stories:

*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily *

*2 As an unauthenticated user, I want to have the option to view all products on the site.*

*3 As an unauthenticated user, I want to be able to search the website for specific products and brands.*

*7 As an unauthenticated user, I want to be able to view specific brands' products sold on the site.*

*10 As an unauthenticated user, I want to be able to view how many products are in my shopping bag at all times.*

*12 As an unauthenticated user, I want to be able to view products added to my shopping bag.*

*15 As an unauthenticated user, I want to be able to create an account.*

*16 As an unauthenticated user, I want to be able to log in to / sign out of an existing account.*

*22 As a site owner, I want users to be able to navigate the website quickly and easily*

#### Feature 2 – Search bar
<br>![Home page](readme/features/search-bar.png)

The search bar is part of the header and features across all pages. This allows the user to easily search products by brand, product type, colour. For this first release the functionality is limited to only one keyword per search, for future releases the search would include multiple keyword search functionality.

This feature covers the following user stories:

*3 As an unauthenticated user, I want to be able to search the website for specific products and brands.*

#### Feature 3 – Image carousel
<br>![Home page](readme/features/home-page-carousel.png)

The image carousel is the first image the user is presented with, the carousel provides an aesthetic to engage the user through activity, rather than just having static images

This feature covers the following user stories:
*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily*

#### Feature 4 – Mailing list
<br>![Home page](readme/features/mailing-list.png)

The mailing list appears across all pages, to make it as visible as possible and encourage the user to sign up to the newsletter.

This feature covers the following user stories:

*20 As an unauthenticated user, I want to be able to receive news and updates from the business*

*23 As a site owner, I want users to be sign up to a newsletter to capture user information*

#### Feature 5 – Footer
<br>![Home page](readme/features/footer.png)

The footer appears across all pages, and contains links to direct the user to all main pages – shop, information, account. As well as links to social media pages and the address of the business. It also ensures the mailing list sign up features across all pages to prompt user engagement.

This feature covers the following user stories:

*2 As an unauthenticated user, I want to have the option to view all products on the site*

*7 As an unauthenticated user, I want to be able to view specific brand’s products sold on the site*

*15 As an unauthenticated user, I want to be able to create an account*

*16 As an unauthenticated user, I want to be able to log in to / sign out of an existing account*

*19 As an unauthenticated user, I want to be able contact the business*

*20 As an unauthenticated user, I want to be able to receive news and updates from the business*

*21 As an unauthenticated user, I want to be able to view the business location*

*23 As a site owner, I want users to be sign up to a newsletter to capture user information*

*24 As a site owner, I want users to be able to view the business social media*


### Page 2 – Products

The product listing menu consists of the following features:

#### Feature 1 – All products
<br>![products page](readme/features/all-products-menu.png)
<br>![products page](readme/features/all-products.png)

When the user first selects the shop link, they have an option to view ‘all products’ or select one of the product categories. On selecting the all products page, every product listing appears in an automatic alphabetical order.

This feature covers the following user stories:

*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily*

*2 As an unauthenticated user, I want to have the option to view all products on the site*

#### Feature 2 – Product details
<br>![products page](readme/features/product-details.png)

The user has the option to view details of any product listing. They have to select this to be able to purchase the product. The product details appear in a new window and gives the user the product name and brand, detailed product description, an option to select size and quantity. The user can then add the product to their cart, and either go to the bag or continue shopping.

When the user adds a product to the cart, they are unable to add more than is listed in inventory.

When an item becomes out of stock, the size selection automatically shows out of stock, and the user will be unable to select this product for purchase.

This feature covers the following user stories:

*4 As an unauthenticated user, I want to be able to view detailed descriptions and prices of the products*

*9 As an unauthenticated user, I want to be able to add a product to my bag*

*12 As an unauthenticated user, I want to be able to navigate back to the products page after viewing product details*

*37 As a site owner, I want to make sure that customers aren’t able to purchase more products than what is listed in the inventory*

*38 As a site owner, I want to make sure that customers can see which products are out of stock*

#### Feature 3 – Managing product details

When logged in as a staff user or admin, the user has the ability to create and update any product from the product details page. Upon selection the staff user can edit the title, description, friendly name, category, brand, sizing options, colour options, price and image. The staff user has the option to save or cancel any changes.

This feature covers the following user stories.

*25 As a staff user, I want to be able to update and edit product descriptions, details and prices*

*29 As a staff user, I want to be able to view and update products*

*30 As a staff user, I want to be able to add products*

#### Feature 4 – Page order
<br>![products page](readme/features/product-order.png)

The user has the option to select the order in which to view the products are listed. They can order by price (ascending or descending) or alphabetically (ascending or descending). 

This feature covers the following user stories:

*5 As an unauthenticated user, I want to be able to order the product pages by price, and alphabetically*

#### Feature 6 – Pagination
<br>![products page](readme/features/pagination.png)

The pagination appears at the top and bottom of the products page, it shows the user which product page they are on, and gives the user the ability to easily navigate through the product pages.

This feature covers the following user stories:

*1 As an unauthenticated user, I want to be able to navigate the website quickly and easily *

*10 As an unauthenticated user, I want to be able to quickly navigate through product listing pages*

#### Feature 7 – Create product
<br>![products page](readme/features/create-product.png)

The option to create a product appears in the shop dropdown menu when logged in as a staff user or admin. It enables a staff user to create a new product with blank required fields. 

This feature covers the following user stories:

*30 As a staff user, I want to be able to add products*


#### Feature 8 – Update product
<br>![products page](readme/features/update-product.png)

When logged in as a staff user or admin, when on any product details page, the user has the ability to update the selected item.

This feature covers the following user stories:

*29 As a staff user, I want to be able to view and update products*

#### Feature 9 – Deleting a product
<br>![products page](readme/features/delete-product.png)

When logged in as a staff user or admin, when they select any product the user has the ability to delete the selected item. They are taken to a new page for them to confirm the deletion.

This feature covers the following user stories:

*31 As a staff user, I want to be able to delete products*

#### Feature 10 – Categories
<br>![products page](readme/features/categories-header.png)
<br>![products page](readme/features/categories-all-products.png)

The category list appears when the user selects the shop link in the header, as well as on the all product page / products pages. The categories allow the user to filter and browse certain products.

This feature covers the following user stories:

*2 As an unauthenticated user, I want to have the option to view all products on the site*

*3 As an unauthenticated user, I want to be able to search the website for specific products and brands*

*6 As an unauthenticated user, I want to be able to sort and view products by category*

#### Feature 11 – Category management
<br>![products page](readme/features/category-management.png)

The category management features in the shop dropdown menu when logged in as a staff user or admin. It enables a staff user to view, add, update or remove product categories.

This feature covers the following user stories: 

*33 As a staff user, I want to be able to view and update product categories*

*34 As a staff user, I want to be able to add product categories*

*35 As a staff user, I want to be able to delete product categories*

#### Feature 12 – Inventory management
<br>![products page](readme/features/inventory-management.png)
<br>![products page](readme/features/update-inventory.png)
<br>![products page](readme/features/out-of-stock.png)

The inventory management features in the shop dropdown menu when logged in as a staff user or admin. It enables the user to view all products listed alphabetically, or they can search by SKU, product name and brand name.

After selecting adjust quantity, the user is taken to an update inventory page where they can adjust the quantity of stock.

This feature covers the following user stories:

*32 As a staff user, I want to be able to manage product inventory*

*37 As a site owner, I want to make sure that customers aren’t able to purchase more products than what is listed in the inventory*


### Page 3 – Brands

This page consists of the following features:

#### Feature 1 - Brands link 
<br>![brands page](readme/features/brands-header.png)

The brand link is featured on the header, this page allows the user to organise products solely by brand via a dropdown menu. 

This feature covers the following user stories:

*7 As an unauthenticated user, I want to be able to view specific brand’s products sold on the site*

#### Feature 2 – Brand management
<br>![brands page](readme/features/brand-management.png)

When a staff user is logged in the option to manage brands appears in the brand menu. The brand management page appears when selected and allows the staff user to view, add, update or remove brands.

This feature covers the following user stories:

*26 As a staff user, I want to be able to add a brands to the brand list*

*27 As a staff user, I want to be able to update the brands listed*

*28 As a staff user, I want to be able to remove any brands listed*

#### Feature 3 - Update brands
<br>![brands page](readme/features/update-brand.png)

When a staff user selects update from the brand management page, they are able to update the brand name.

This feature covers the following user stories:

*27 As a staff user, I want to be able to update the brands listed*

#### Feature 4 - Add brands
<br>![brands page](readme/features/add-brand.png)

When a staff user selects update from the brand management page, they are able to add a brand to the brand list.

This feature covers the following user stories:

*26 As a staff user, I want to be able to add a brands to the brand list*

#### Feature 4 - Delete brands
<br>![brands page](readme/features/delete-brand.png)

When a staff user selects update from the brand management page, they are able to add a brand to the brand list.

This feature covers the following user stories:

*28 As a staff user, I want to be able to remove any brands listed*


### Page 4 – Courses

This page consists of the following features:

#### Feature 1 – Course list
<br>![courses page](readme/features/course-list.png)
The course link is located in the header, and the dropdown menu lists all available courses. Each courses has it's descriptions and an option to view more details or enquire to book.

This feature covers the following user stories:

*19 As an unauthenticated user, I want to be able contact the business*

*39 As an unauthenticated user, I want to be able to browse available courses*

*40 As an unauthenticated user, I want to be able to view course details and request a booking*

*41 As a staff user, I want to be able to view and update the courses listed*

*42 As a staff user, I want to be able to add a course*

*43 As a staff user, I want to be able to delete a course*

#### Feature 2 – course details
<br>![course page](readme/features/course-details.png)

The course details page shows the selected course with a more detailed description, and options to reserve or go back to the previous page.

This feature covers the following user stories:

*19 As an unauthenticated user, I want to be able contact the business*

*39 As an unauthenticated user, I want to be able to browse available courses*

*40 As an unauthenticated user, I want to be able to view course details and request a booking*

#### Feature 3 - Update courses
<br>![courses page](readme/features/update-course.png)

When a staff user selects update details from the course details page, they are able to update the course in any required field.

This feature covers the following user stories:

*41 As a staff user, I want to be able to view and update the courses listed.*

#### Feature 4 - Add courses
<br>![courses page](readme/features/create-course.png)

When a staff user selects create a course from the dropdown menu in the header, they are able to add a course.

This feature covers the following user stories:

*42 As a staff user, I want to be able to add a course*

#### Feature 4 - Delete courses
<br>![courses page](readme/features/delete-course.png)

When a staff user selects update details from the course details page, they are able to delete the course.

This feature covers the following user stories:

*43 As a staff user, I want to be able to delete a course*


### Page 5 - Log in
<br>![login page](readme/features/sign-in.png)

The user can access the log in via the links in the header and footer, they are taken to a sign in page that also features a link to create a new account.
A confirmation box appears above the login links to tell the user they have logged in successfully.

If the user has forgotten their password, there is a link to perform a password reset where an email is sent to the user's requested email address.

This page covers the following user stories:

*16 As an unauthenticated user, I want to be able to log in to / sign out of an existing account*

*48 As a user, I want to be able to reset my password if I have forgotten it*



### Page 6 - Log out
<br>![logout page](readme/features/sign-out.png)

The user can access the log out via the links in the header and footer, they are taken to a log out page and confirmation box appears above the login links to tell the user they have logged in successfully.

This page covers the following user stories:

*16 As an unauthenticated user, I want to be able to log in to / sign out of an existing account*

*36 As an authenticated user, I want confirmation that I have signed out of my account*


### Page 7 – Register
<br>![register page](readme/features/sign-up.png)

The register page can be accessed from the header link across all pages. The user is asked to create a username for future logins. 
The user gains benefits such as saving shipping details and viewing past orders.

This page covers the following user stories:

*15 As an unauthenticated user, I want to be able to create an account*

*36 As an authenticated user, I want to receive an email confirmation to verify my account and confirmation the registration is successful*


### Page 8 - Profile page

#### Feature 1 – Profile information 
<br>![profile page](readme/features/profile-info.png)
<br>![profile page](readme/features/edit-profile.png)

When the user is logged in or registered, they are able to view their profile. This features their personal details which they are able to update and change.

This feature covers the following user stories:

*17. As an authenticated user, I want to be able to view and update my personal information in my profile*

#### Feature 2 – Order history 
<br>![profile page](readme/features/profile-info.png)
<br>![profile page](readme/features/order-history.png)

When the user is logged in, they are able to view their previous order history. They are given the option to view any order in more detail. This page includes order number, product and cost, delivery address and billing information.

The user is then given the option to return to profile or continue shopping.

This page covers the following user stories:

*17 As an authenticated user, I want to be able to view and update my personal information in my profile*

*18 As an authenticated user, I want to be able to view my order history*


### Page 9 - Shopping Cart

The shopping cart is always visible in the header on each page. The quantity is always visible and updates whenever a product is added.

#### Feature 1 – Shopping cart
<br>![shopping page](readme/features/shopping-cart.png)
<br>![shopping page](readme/features/cart-item-removed.png)

When the user chooses to view their cart all items, they can adjust the quantities of the products, selecting minus to take the quantity to zero removes the item from the bag altogether. The user has confirmation that the product has then been removed.

This feature covers the following user stories:

*10 As an unauthenticated user, I want to be able to view how many products are in my shopping bag at all times*

*12 As an unauthenticated user, I want to be able to view products added to my shopping bag*

*13 As an unauthenticated user, I want to be able to increase quantities and remove items from my shopping bag*

#### Feature 2 – Checkout
<br>![shopping page](readme/features/checkout.png)

When the user is happy with the items placed in the bag they can choose to checkout. This takes them to the checkout page which displays the items in their bag, as well as payment details.

When the user is logged in the form is prepopulated with their delivery and contact information.

When the user is not logged in the form is empty for the user to complete, and they are given the option to create an account or log in.
<br>![shopping page](readme/features/checkout-unauthenticated.png)

When the card details have been entered correctly a confirmation page is displayed and the order confirmation is sent the to the user’s email address.
<br>![shopping page](readme/features/order-confirmation.png)

This feature covers the following user stories:

*14 As an unauthenticated user, I want to be able to checkout and purchase products*

*45 As a user, I want to have confirmation that my order has been successful*


### Page 10 – Contact
<br>![contact page](readme/features/contact.png)

The contact page contains a form for any user to complete to enable them to contact the business. It features different subject matters for the user to select from which helps the staff user / site owner deal with customer messages.

This form is also the form users are taken to when they wish to reserve a dive course placement. 

This page covers the following user stories:

*19 As an unauthenticated user, I want to be able contact the business*


### Page 11 - About
<br>![about page](readme/features/about-us.png)

The about page features an overview of the business to engage users and help build trust to make them purchase products from the site. 
It contains an easy to use FAQ menu with questions, the aim of this is to resolve customer queries so the staff users can focus on other messages via the contact form, and enable users to quickly resolve common questions.

This page covers the following user stories:

*44 As an unauthenticated user, I want to be able to find answers to frequently asked questions without having to wait for an answer from the site owner by filling in the contact form*


### Page 12 – Administration
<br>![admin page](readme/features/admin-panel.png)

The Django admin panel is a built in tool that enables the admin users to create batch actions and manipulate all the data tables in one place.

This page covers the following user stories:
*46 As admin, I want to be able to create batch actions and manipulate all the data tables in one place*


### Feature 13 - Messaging
<br>![admin page](readme/features/success-message.png)

After certain actions, success confirmation messages are shown at the top of the screenn to confirm the user's action has been applied.
After certain actions, error messages are shown at the top of the screenn to confirm the user's action has been not been applied.

This page covers the following user stories:
*47 As a user, I want to be shown messages that my actions have been successful and unsuccessful*

## Technologies Used

### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JS ES6](https://en.wikipedia.org/wiki/JavaScript)
- [Django](https://www.djangoproject.com/)
- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

#### Python Libraries

- astroid==2.11.4
- boto3==1.24.15
- asgiref==3.5.1
- botocore==1.27.15
- certifi==2021.10.8
- cffi==1.15.0
- charset-normalizer==2.0.12
- cryptography==37.0.2
- defusedxml==0.7.1
- dill==0.3.4
- Django==4.0.5
- django-allauth==0.50.0
- django-bootstrap-form==3.4
- django-countries==7.3.2
- django-crispy-forms==1.14.0
- django-database-url==1.0.3
- django-extensions==3.1.5
- django-filter==21.1
- django-storages==1.12.3
- djhtml==1.5.0
- gunicorn==20.1.0
- idna==3.3
- isort==5.10.1
- jmespath==1.0.1
- lazy-object-proxy==1.7.1
- mccabe==0.7.0
- oauthlib==3.2.0
- Pillow==9.1.0
- platformdirs==2.5.2
- psycopg2-binary==2.9.3
- pycparser==2.21
- pydot==1.4.2
- PyJWT==2.3.0
- pylint==2.13.8
- pylint-django==2.5.3
- pylint-plugin-utils==0.7
- pyparsing==3.0.9
- python-dateutil==2.8.2
- python3-openid==3.2.0
- pytz==2022.1
- requests==2.27.1
- requests-oauthlib==1.3.1
- s3transfer==0.6.0
- six==1.16.0
- sqlparse==0.4.2
- stripe==3.3.0
- tomli==2.0.1
- typing_extensions==4.2.0
- urllib3==1.26.9
- wrapt==1.14.1

### Frameworks & Tools
- [Bootstrap 5.0](https://getbootstrap.com/docs/5.0) - for general site layout, grid, flex, carousel.
- [Bootstrap Icons 1.8](https://getbootstrap.com/) - for various icons in the site
- [Postgres](https://www.postgresql.org/) - the site is deployed on Heroku using a Postgress database.
- [SQLLite](https://www.sqlite.org/index.html) - this database was used in local development.
- [VSCode](https://code.visualstudio.com/) - my IDE of choice for this project.
- [Gitpod](https://gitpod.io/) - used occasionally for tutor support.
- [Github](https://github.com/) - used as the code repository.
- [Google Fonts](https://fonts.google.com/) - used for the main body font and some headings.
- [Balsamiq](https://balsamiq.com/) -  used to create the website wireframes.
- [Font Awesome](https://fontawesome.com/) - Font awesome was used to provide the relevant fonts/icons for the website social media icon links.
- [JQuery](https://jquery.com) - JQuery was used in some javascript files for DOM manipulation
- [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - for validation of the css in the project.
- [HTML Markup Validation Service](https://validator.w3.org/) - for validation the HTML in the project.
- [Firefox dev tools](https://firefox-source-docs.mozilla.org/devtools-user/index.html) - troubleshooting and debugging of the project code.
- [Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) - for performance, accessibility, progressive web apps, SEO analysis of the project code.
- [Responsive Design](http://ami.responsivedesign.is/) - for website mockup.
- [JSHint](https://jshint.com/) - for javascript validation.
- [PEP8](https://www.python.org/dev/peps/pep-0008/) - for python validation.
- [Quick Database diagrams](https://www.quickdatabasediagrams.com)- for the database schema diagram.
- [Facebook](https://www.facebook.com) - for social media marketing
- [Stripe](https://stripe.com/gb) - For payments
- [Amazon Web Services](https://aws.amazon.com/) - For static file hosting

## Validation

### HTML Validation
The HTML of the each page of the site was validated using [W3C Markup Validation Service](https://validator.w3.org/).  All pages returned a pass with 0 errors and 0 warnings.

<details><summary>Home</summary>
<img src="readme/validation/html-validation/html-validation-home-index.png">
</details>
<details><summary>Products</summary>
<img src="readme/validation/html-validation/html-validation-products.png">
</details>
<details><summary>Product Detail</summary>
<img src="readme/validation/html-validation/html-validation-product-detail.png">
</details>
<details><summary>Courses List</summary>
<img src="readme/validation/html-validation/html-validation-courses-list.png">
</details>
<details><summary>Course Detail</summary>
<img src="readme/validation/html-validation/html-validation-course-details.png">
</details>
<details><summary>Checkout</summary>
<img src="readme/validation/html-validation/html-validation-checkout.png">
</details>
<details><summary>Bag</summary>
<img src="readme/validation/html-validation/html-validation-bag.png">
</details>
<details><summary>Checkout Success</summary>
<img src="readme/validation/html-validation/html-validation-checkout-success.png">
</details>
<details><summary>Contact Us</summary>
<img src="readme/validation/html-validation/html-validation-contact.png">
</details>
<details><summary>About</summary>
<img src="readme/validation/html-validation/html-validation-contact.png">
</details>


### CSS Validation
The [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/validator) was used to validate the CSS of the website. 

The custom CSS file for the site passed with 0 errors.

<details><summary>base.css</summary>
<img src="readme/validation/css-validation/base-css-validation.png">
</details>

<details><summary>checkout.css</summary>
<img src="readme/validation/css-validation/checkout-css-validation.png">
</details>

<details><summary>contact.css</summary>
<img src="readme/validation/css-validation/contact-css-validation.png">
</details>

<details><summary>courses.css</summary>
<img src="readme/validation/css-validation/courses-css-validation.png">
</details>

<details><summary>colors.css</summary>
<img src="readme/validation/css-validation/colors-css-validation.png">
</details>

<details><summary>products.css</summary>
<img src="readme/validation/css-validation/products-css-validation.png">
</details>

### JS Validation
The Javascript of the each page of the site was validated using [JSHint validation tool](https://jshint.com/).  All pages returned a pass with 0 errors and 0 warnings.

<details><summary>bag.js</summary>
<img src="readme/validation/js-validation/js-validation-bag.png">
</details>

<details><summary>checkout.js</summary>
<img src="readme/validation/js-validation/js-validation-js-stripe.png">
</details>

<details><summary>courses.js</summary>
<img src="readme/validation/js-validation/js-validation-courses.png">
</details>

<details><summary>inventory.js</summary>
<img src="readme/validation/js-validation/js-validation-inventory.png">
</details>

<details><summary>products.js</summary>
<img src="readme/validation/js-validation/js-validation-products.png">
</details>

### Py Validation
The Python of the each page of the site was validated using [Python validation tool](http://pep8online.com/).  All pages returned a pass with 0 errors and 0 warnings.

#### Admin py-validation

<details><summary>about/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-about-admin.png">
</details>
<details><summary>checkout/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-checkout-admin.png">
</details>
<details><summary>contact/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-admin.png">
</details>
<details><summary>courses/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-courses-admin.png">
</details>
<details><summary>product/admin.py</summary>
<img src="readme/validation/py-validation/py-validation-products-admin.png">
</details>

#### Forms py validation

<details><summary>checkout/forms.py</summary>
<img src="readme/validation/py-validation/py-validation-checkout-forms.png">
</details>
<details><summary>products/forms.py</summary>
<img src="readme/validation/py-validation/py-validation-products-forms.png">
</details>
<details><summary>contact/forms.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-forms.png">
</details>
<details><summary>profiles/forms.py</summary>
<img src="readme/validation/py-validation/py-validation-profiles-forms.png">
</details>

#### Models py validation

<details><summary>about/models.py</summary>
<img src="readme/validation/py-validation/py-validation-about-models.png">
</details>
<details><summary>checkout/models.py</summary>
<img src="readme/validation/py-validation/py-validation-checkout-models.png">
</details>
<details><summary>contact/models.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-models.png">
</details>
<details><summary>courses/models.py</summary>
<img src="readme/validation/py-validation/py-validation-course-models.png">
</details>
<details><summary>products/models.py</summary>
<img src="readme/validation/py-validation/py-validation-products-models.png">
</details>

#### Urls py validation

<details><summary>bag/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-bag-urls.png">
</details>
<details><summary>about/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-about-urls.png">
</details>
<details><summary>checkout/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-checkout-urls.png">
</details>
<details><summary>contact/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-urls.png">
</details>
<details><summary>courses/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-courses-urls.png">
</details>
<details><summary>products/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-products-urls.png">
</details>
<details><summary>profiles/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-profiles-urls.png">
</details>
<details><summary>project/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-project-urls.png">
</details>

#### Context py validation

<details><summary>bag/context_processor.py</summary>
<img src="readme/validation/py-validation/py-validation-bag-context.png">
</details>

<details><summary>products/urls.py</summary>
<img src="readme/validation/py-validation/py-validation-products-context.png">
</details>

#### Views py validation

<details><summary>about/views.py</summary>
<img src="readme/validation/py-validation/py-validation-about-views.png">
</details>
<details><summary>bag/views.py</summary>
<img src="readme/validation/py-validation/py-validation-bag-views.png">
</details>
<details><summary>contact/views.py</summary>
<img src="readme/validation/py-validation/py-validation-contact-views.png">
</details>
<details><summary>checkout/views.py</summary>
<img src="readme/validation/py-validation/py-validation-checkout-views.png">
</details>
<details><summary>courses/views.py</summary>
<img src="readme/validation/py-validation/py-validation-courses-views.png">
</details>
<details><summary>products/views.py</summary>
<img src="readme/validation/py-validation/py-validation-products-views.png">
</details>
<details><summary>profiles/views.py</summary>
<img src="readme/validation/py-validation/py-validation-profiles-views.png">
</details>
<details><summary>home/views.py</summary>
<img src="readme/validation/py-validation/py-validation-home-views.png">
</details>

### Accessibility
The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/ was used to ensure the website met high accessibility standards. All pages returned 0 errors.

<details><summary>Home</summary>
<img src="readme/validation/wave-validation/wave-validation-index.png">
</details>
<details><summary>Products</summary>
<img src="readme/validation/wave-validation/wave-validation-products.png">
<img src="readme/validation/wave-validation/wave-validation-products-detail.png">
<img src="readme/validation/wave-validation/wave-validation-products-edit.png">
<img src="readme/validation/wave-validation/wave-validation-products-delete.png">
<img src="readme/validation/wave-validation/wave-validation-products-create.png">
<img src="readme/validation/wave-validation/wave-validation-categories-list.png">
<img src="readme/validation/wave-validation/wave-validation-categories-add.png">
<img src="readme/validation/wave-validation/wave-validation-brands-list.png">
<img src="readme/validation/wave-validation/wave-validation-brands-update.png">
<img src="readme/validation/wave-validation/wave-validation-brands-remove.png">
<img src="readme/validation/wave-validation/wave-validation-brands-remove.png">
<img src="readme/validation/wave-validation/wave-validation-colors-list.png">
<img src="readme/validation/wave-validation/wave-validation-colors-update.png">


</details>
<details><summary>About</summary>
<img src="readme/validation/wave-validation/wave-validation-about.png">
</details>
<details><summary>Contact</summary>
<img src="readme/validation/wave-validation/wave-validation-contact.png">
</details>
<details><summary>Accounts</summary>
<img src="readme/validation/wave-validation/wave-validation-logout.png">
<img src="readme/validation/wave-validation/wave-validation-profile.png">
</details>

<details><summary>Bag/Checkout</summary>
<img src="readme/validation/wave-validation/wave-validation-cart.png">
</details>

### Performance 
[Google Lighthouse](https://developers.google.com/web/tools/lighthouse/) was used to measure the performance and speed of the website -performance, accessibility, best practice and SEO with results below:

<details><summary>Home</summary>
<img src="readme/validation/lighthouse-validation/lighthouse-validation-index.png">
</details>
<details><summary>Products</summary>
<img src="readme/validation/lighthouse-validation/lighthouse-validation-products.png">
<img src="readme/validation/lighthouse-validation/lighthouse-validation-product-detail.png">
</details>
<details><summary>Courses</summary>
<img src="readme/validation/lighthouse-validation/lighthouse-validation-course-list.png">
<img src="readme/validation/lighthouse-validation/lighthouse-validation-course-detail.png">
</details>
<details><summary>About</summary>
<img src="readme/validation/lighthouse-validation/lighthouse-validation-about.png">
</details>
<details><summary>Contact</summary>
<img src="readme/validation/lighthouse-validation/lighthouse-validation-contact.png">
</details>
<details><summary>Accounts</summary>
<img src="readme/validation/lighthouse-validation/lighthouse-validation-accounts.png">
</details>

## Testing

### Manual Testing
### Testing user stories

1. As an unauthenticated user, I want to be able to navigate the website quickly and easily 


| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|   nav bar   | Select any nav link from the main nav bar           |     selected page is displayed with images and information | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-1-navigation.jpg">
</details>

2. As an unauthenticated user, I want to have the option to view all products on the site

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  nav bar           |  from any page, select all products from product link in nav bar         |  all products page is displayed            | Works as expected |
|  footer          | from any page, select the products link in the footer          |  all products page is displayed                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-2-all-products.jpg">
</details>

3. As an unauthenticated user, I want to be able to search the website for specific products and brands

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  search bar          |   from any page enter a keyword relating to a product, or a brandname into the search bar        |    products matching keywords are displayed                 | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-3-searchbar.jpg">
</details>

4. As an unauthenticated user, I want to be able to view detailed descriptions and prices of the products

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product listing page            | From any product listing page, select the details button            | taken to product details page, images and description displayed                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-4-product-details.jpg">
</details>

5.	As an unauthenticated user, I want to be able to order the product pages by price, and alphabetically

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product listing page            | select order by button and choose option in which to sort and view products, then select search          | products are organised in the selected order               | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-5-product-order.jpg">
</details>

6.	As an unauthenticated user, I want to be able to sort and view products by category

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| nav bar          | From any page, select the shop button in the header           | product catergories are displayed in dropdown menu, when selected taken to the correct page                   | Works as expected |
| product listing page            | select any product category listed in side category menu         | correct product category page is displayed               | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-6-product-category.jpg">
</details>

7.	As an unauthenticated user, I want to be able to view specific brands' products sold on the site

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| nav bar            | select any brand from brand link dropdown menu in header          | products matching brand criteria are displayed                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-7-view-brands.jpg">
</details>

8.	As an unauthenticated user, I want to be able to add a product to my bag

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product details page           |  when product size and quantity have been selected, select add to cart         | product is added to bag and success message is displayed                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-8-add-to-bag.jpg">
</details>

9.	As an unauthenticated user, I want to be able to quickly navigate through product listing pages

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  product listing page           | selected desired pagination buttons            | taken to first or last page and can easily skip to next or previous page        | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-9-pagination.jpg">
</details>

10.	As an unauthenticated user, I want to be able to view how many products are in my shopping bag at all times

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| nav bar           | add product to cart and observe shopping icon on any page          | cart icon and product count is displayed in header         | Works as expected |


<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-10-view-bag-count.jpg">
</details>

11.	As an unauthenticated user, I want to be able to navigate back to the products page after viewing product details

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product details        | from product details page, select continue shopping          | taken back to all products page         | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-11-continue-shopping.jpg">
</details>

12.	As an unauthenticated user, I want to be able to view products added to my shopping bag
    
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| nav bar - shopping cart           | From any page, select shopping cart icon in nav bar           | shopping bag is displayed with added products                     | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-12-view-bag.jpg">
</details>

13.	As an unauthenticated user, I want to be able to increase quantities and remove items from my shopping bag

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| shopping cart            | when in shopping cart, select the increase or decrease buttons to adjust product quantity           | product quantity is updated                     | Works as expected |
| shopping cart            | when in shopping cart, decrease buttons to adjust product quantity to zero         | product is removed from bag and visual confirmation message appears                     | Works as expected |
| shopping cart            | when in shopping cart, select the bin icon to remove product from bag           | product is removed from bag and visual confirmation message appears                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-13-updating-bag-quantities.jpg">
</details>

14.	As an unauthenticated user, I want to be able to checkout and purchase products

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| checkout     | from shopping cart, select proceed to checkout          | checkout page is displayed                    | Works as expected |
| checkout     | from checkout page, complete all required fields and select complete order       | order confirmation page is displayed showing order has been successful, confirmation email sent to user                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-14-checkout.jpg">
</details>

15. As an unauthenticated user, I want to be able to create an account

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| account            | From any page observe profile icon in navbar and select register, sign up page displayed and complete required fields           | account is created and verification email sent to user            | Works as expected |
| account            | From any page select register link in footer, sign up page displayed and complete required fields           | account is created and verification email sent to user            | Works as expected |
| account            | From the checkout page select option to register link, sign up page displayed and complete required fields           | account is created and verification email sent to user            | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-15-register-1.jpg">
<img src="readme/validation/us-testing/us-15-register-2.jpg">
<img src="readme/validation/us-testing/us-15-register-3.jpg">
</details>
    

16. As an unauthenticated user, I want to be able to log in to / sign out of an existing account

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| account     | From navbar select profile icon and enter details in sign in page        | User is logged in and success message displayed                  | Works as expected |
| account     | From navbar select profile icon, select sign out buton on sign out page        | User is logged out and success message displayed                  | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-16-login.jpg">
<img src="readme/validation/us-testing/us-16-logout.jpg">
</details>

17. As an authenticated user, I want to be able to view and update my personal information in my profile

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  profile           | From update section of profile page, change personal details and select save          | details saved and confirmation displayed that details have been updated                    | Works as expected |
| profile           | From any page, select profile icon           | profile page is displayed with user details visible                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-17-view-update-profile.jpg">
</details>

18.  As an authenticated user, I want to be able to view my order history

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| profile         | when logged in select profile icon, profile page is displayed and observe order history           | all order history is displayed                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-18-order-history.jpg">
</details>

19.As an unauthenticated user, I want to be able contact the business

| nav bar         | from any page select the contact link in the header         | contact form is displayed                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-19-contact.jpg">
</details>

20.	As an unauthenticated user, I want to be able to receive news and updates from the business

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| mailing list           |  From any page, observe mailing list as part of footer and enter email address        |  email added to mailing list and success message is displayed                  | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-20-mailing-list">
</details>

21.	As an unauthenticated user, I want to be able to view the business location
    
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| footer            | From any page, observe business address in footer            | business address is displayed                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-21-business-location.jpg">
</details>

22.	As a site owner, I want users to be able to navigate the website quickly and easily
    
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| checkout     | from shopping cart, select proceed to checkout          | checkout page is displayed                    | Works as expected |
| checkout     | from checkout page, complete all required fields and select complete order       | order confirmation page is displayed showing order has been successful, confirmation email sent to user                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-14-checkout.jpg">
</details>

23. As a site owner, I want users to be sign up to a newsletter to capture user information

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| mailing list           |  From any page, observe mailing list as part of footer and enter email address        |  email added to mailing list and success message is displayed                  | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-20-mailing-list">
</details>

24.	As a site owner, I want users to be able to view the business social media
    
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| footer           | From any page, select any social media link in footer          | taken to correct social media page        | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-24-social-media.jpg">
</details>

25.	As a staff user, I want to be able to update and edit product descriptions, details and prices

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product details           | from product details page, select update product details and create/update product page is displayed          | able to update required fields, once saved product is updated                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-25-product-details">
</details>

26.	As a staff user, I want to be able to add a brands to the brand list

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| brand management            |  from brand management page, select add and add brand page is displayed where name can be inputted, select save          | name is saved and brand appears in brand list                  | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-26-add-brand.jpg">
</details>

27.	As a staff user, I want to be able to update the brands listed

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  brand management          | from brand management page select update, update brand page is displayed where name can be updated, select save | name is updated and visual confirmation message is displayed                           | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-27-update-brand.jpg">
</details>

28.	As a staff user, I want to be able to remove any brands listed

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| brand management          | from brand management page select remove, delete brand page is displayed where confirmation of deletion is required         | after confirming yes brand is successfully removed         | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-28-delete-brand.jpg">
</details>

29.	As a staff user, I want to be able to view and update products 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product details page          | from product details page, select update, edit required fields and select save           | visual confirmation message is displayed that product has been updated                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-29-update-product.jpg">
</details>

30.	As a staff user, I want to be able to add products
    
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| create/update product page            | from create/update product page, complete required fields and select save         | visual confirmation message is displayed that product has been added successfully                      | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-30-add-product.jpg">
</details>

31.	As a staff user, I want to be able to delete products

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product details page            | from product details page, select remove and confirm deletion of product           | product is deleted and visual confirmation message is displayed                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-31-delete-product.jpg">
</details>

32. As a staff user, I want to be able to manage product inventory

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  manage inventory           |   from shop link in header select manage inventory, observe product to update or search for product using search function, select adjust inventory to adjust quantity          |   inventory quantity is updated and visual confirmation message is displayed                 | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-32-manage-inventory.jpg">
</details>

33. As a staff user, I want to be able to view and update product categories

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| category management       | from category management page, select update and edit required fields           | category is updated and visual confirmation is displayed                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-33-update-category.jpg">
</details>

34. As a staff user, I want to be able to add product categories

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| category management             | from category management page, select add and enter required fields, select save           | category is successfully added and visual confirmation is displayed            | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-34-add-category.jpg">
</details>

35. As a staff user, I want to be able to delete product categories
    
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| category management             | from category management page, select delete on category to remove, confirm that category is to be deleted           | category is successfully deleted and visual confirmation is displayed            | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-35-delete-category.jpg">
</details>

36. As an authenticated user, I want confirmation that I have signed out of my account

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  account           | from profile icon in header, select sign out and confirm on sign out page that is displayed          | user is signed out and confirmation message is displayed                    | Works as expected |


37.As a site owner, I want to make sure that customers aren’t able to purchase more products than what is listed in the inventory

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product details page            | from the product details page, using the increase button you are unable to increase the quantity past the max inventory           | observe product quantity will increment no further than inventory                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-37-product-inventory-max.jpg">
</details>

38. As a site owner, I want to make sure that customers can see which products are out of stock

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| product details page             | from product details page, select sizing options, observe any sizes that are out of stock            | sizes that are out of stock are displayed and unable to be added to bag                    | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-38-out-of-stock.jpg">
</details>

39. As an unauthenticated user, I want to be able to browse available courses

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| nav bar          | from any page, select course link in nav bar and observe courses        | available courses are displayed in dropdown menu                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-39-view-courses.jpg">
</details>

40. As an unauthenticated user, I want to be able to view course details and request a booking

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| courses         | from courses page select more details, course details are displayed and select reserve now button to book        | detailed course description is displayed, taken to contact form after selecting reserve now                  | Works as expected |
| courses         | from courses page select enquire now, contact form displayed      | contact form page displayed to complete                  | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-40-book-courses.jpg">
<img src="readme/validation/us-testing/us-40-book-courses-2.jpg">
</details>

41. As a staff user, I want to be able to view and update the courses listed

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| courses         | from course details page, select update details, complete required fields and select save      | course details are updated and visual confirmation is displayed                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-41-update-course.jpg">
</details>

42. As a staff user, I want to be able to add a course

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| courses         | select create course from course link in header, complete required fields and select save      | course is created and visual confirmation is displayed                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-42-add-course.jpg">
</details>

43. As a staff user, I want to be able to delete a course

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| courses         | from course details page, select delete course, confirm deletion when prompted      | after confirmation course is deleted and visual confirmation is displayed                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-43-delete-course.jpg">
</details>

44. As an unauthenticated user, I want to be able to find answers to frequently asked questions without having to wait for an answer from the site owner by filling in the contact form

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| about page         | from about page, observe FAQ section with questions displayed in accordian menu      | FAQ questions and answers are visible                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-44-faq.jpg">
</details>

45. As a user, I want to have confirmation that my order has been successful

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| checkout     | from checkout page, complete all required fields and select complete order       | order confirmation page is displayed showing order has been successful, confirmation email sent to user                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-14-checkout.jpg">
</details>

47. As a user, I want to be shown messages that my actions have been successful and unsuccessful

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| account     | on any page where fields are required, if completed incorrectly form won't be submitted      | error message displayed and form isn't submitted                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-47-action-error.jpg">
</details>

48. As a user, I want to be able to reset my password if I have forgotten it

 **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| account     | on sign in page, select forgotten password link and enter recovery email into password reset page      | email is sent to recover email to reset password                   | Works as expected |

<details><summary>Images</summary>
<img src="readme/validation/us-testing/us-48-password-reset.jpg">
</details>
 
## Automated Testing

### Unit testing

As part of the project I have used a number of automated tests using the built in Django testing framework which is based on python unittest.

I have demonstrated some proficiency in using these tests however due to the tight time constraints on this project, the code does not have full coverage.  For future releases and project I could endeavor to increase the number of unit tests and coverage of the code.

#### About

+ Testing Models
<code>
1. Test str method
</code>

#### Bag

+ Testing Views
<code>
1. Check bag page is displayed
2. Add product to empty Bag
3. Adjust qty to zero
4. Remove product from Bag
5. Remove product from bag exception
</code>

#### Checkout

+ Testing Models
<code>
1. Test str method
</code>

+ Testing Views
<code>
1. Test empty cart is displayed
</code>

+ Testing Forms
<code>
1. Tests the orderform object
</code>

#### Contact

+ Testing Models
<code>
1. Test str method
</code>

+ Testing Forms
<code>
1. Tests the contact form
</code>

#### Courses

+ Testing Models
<code>
1. Test str method
</code>

#### Home

+ Testing Views
<code>
1. Test home page loads
2. Test 404 returned if url error
</code>

#### Products

+ Testing Models
<code>
1. Test str method
</code>

+ Testing Views
<code>
1. Test List View with one record
2. Test search all products no query string
3. Test get product detail page and Verify
4. Test add product as a superuser
5. Test add product as a non superuser
6. Test add product post as a superuser
7. Test get product edit page
8. Test delete product as a superuser
9. Test delete product as a non super user
10. Test list view with no records
</code>

<br>![Auto test results](readme/validation/atest/results.png)

### Coverage

To show code coverage a python test plugin called coverage was used to generate the following results

<details><summary>Images</summary>
<img src="readme/validation/atest/coverage1.png"><br>
<img src="readme/validation/atest/coverage2.png"><br>
<img src="readme/validation/atest/coverage3.png">
</details>

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| Site images not rendering on Heroku | Change source path from relative to static directory |
| Transluscent overlay remaining after resevervation request has been received  | Applied style to form instead of parent div |
| Comment edit does not show awaiting approval | Fix would be to require additional view, bout out of scope for projectt timebox |
 -->

<!-- Deployement steps modified from Paul Meeny Love Rugby -->
## Google emails
To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
2. Turn on 2-step verification and follow the steps to enable
3. Click on app passwords, select Other as the app and give the password a name, for example Django
<br>![App password](readme/misc/gmail_app_password.png)
4. Click create and a 16 digit password will be generated, note the password down
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
7. Set and confirm the following values in the settings.py file to successfully send emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>
8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

## Stripe
1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in
3. Under Developers, click on the API keys section
<br>![API keys](readme/misc/stripe_keys1.png)
4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>
6. Back in the Developers section of your stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://scubasport.herokuapp.com/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
<br>![Webhook](readme/misc/stripe_keys2.png)
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Feel free to test out the webhook and note the success/fail attempts for troubleshooting

# Deployment
There are a number of applications that need to be configured to run this application locally or on a cloud based service, for example Heroku

## Amazon WebServices
1. Create an account at aws.amazon.com
2. Open the S3 application and create an S3 bucket named "scubasport"
3. Uncheck the "Block All Public access setting"
4. In the Properties section, navigate to the "Static Website Hosting" section and click edit
5. Enable the setting, and set the index.html and the error.html values
<br>![AWS Static](readme/misc/aws_static.png)
6. In the Permissions section, click edit on the CORS configuration and set the below configuration
<br>![AWS CORS](readme/misc/aws_cors.png)
7. In the permissions section, click edit on the bucket policy and generate and set the below configuration(or similar to your settings)
<br>![AWS Bucket Policy](readme/misc/aws_bucket_policy.png)
8. In the permissions section, click edit on the Access control list(ACL)
9. Set Read access for the Bucket ACL for Everyone(Public Access)
10. The bucket is created, the next step is to open the IAM application to set up access
11. Create a new user group named "manage-scubasport"
12. Add the "AmazonS3FullAccess" policy permission for the user group
<br>![AWS Bucket Policy](readme/misc/aws_user_group.png)
13. Go to "Policies" and click "Create New Policy"
14. Click "Import Managed Policy" and select "AmazonS3FullAccess" > Click 'Import'.
15. In the JSON editor, update the policy "Resource" to the following
<br><code>"Resource": [</code>
<br><code>"arn:aws:s3:::scubasport",</code>
<br><code>"arn:aws:s3:::scubasport/*"</code>
<br><code>]</code>
16. Give the policy a name and click "Create Policy"
17. Add the newly created policy to the user group
<br>![AWS Bucket Policy](readme/misc/aws_policy.png)
18. Go to Users and create a new user
19. Add the user to the user group manage-scubasport
20. Select "Programmatic access" for the access type
21. Note the AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID variables, they are used in other parts of this README for local deployment and Heroku setup
22. The user is now created with the correct user group and policy
<br>![AWS Bucket Policy](readme/misc/aws_user.png)
23. Note the AWS code in settings.py. Note an environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage
<br>![AWS Settings](readme/misc/aws_settings.PNG)
24. These settings set up a cache policy, set the bucket name, and the environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY that you set in your aws account
25. The configuration also requires the media/static folders that must be setup in the AWS S3 bucket to store the media and static files 

## Local Deployment
To run this project locally, you will need to clone the repository
1. Login to GitHub (https://wwww.github.com)
2. Select the repository dannymagnus/CI-MS5-EComm
3. Click the Code button and copy the HTTPS url, for example: https://github.com/dannymagnus/CI-MS5-EComm.git
4. In your IDE, open a terminal and run the git clone command, for example 

    ```git clone https://github.com/dannymagnus/CI-MS5-EComm.git```

5. The repository will now be cloned in your workspace
6. Create an env.py file(do not commit this file to source control) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values<br>
<br><code>import os</code>
<br><code>os.environ["SECRET_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["STRIPE_PUBLIC_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["STRIPE_SECRET_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["STRIPE_WH_SECRET"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["AWS_ACCESS_KEY_ID"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["AWS_SECRET_ACCESS_KEY"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["EMAIL_HOST_USER"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["EMAIL_HOST_PASS"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["USE_AWS"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["DATABASE_URL"]= 'TO BE ADDED BY USER'</code>
<br><code>os.environ["DEVELOPMENT"] ='True'</code>
7. Some values for the environment variables above are described in different sections of this readme
8. Install the relevant packages as per the requirements.txt file
9. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
10. Ensure debug is set to true in the settings.py file for local development
11. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
12. Run "python3 manage.py showmigrations" to check the status of the migrations
13. Run "python3 manage.py migrate" to migrate the database
14. Run "python3 manage.py createsuperuser" to create a super/admin user
15. Run manage.py loaddata db.json to load the product data into the database
18. Start the application by running <code>python3 manage.py runserver</code>
19. Open the application in a web browser, for example: http://127.0.0.1:8000/

## Heroku and Postgres Database
To deploy this application to Heroku, run the following steps.
1. Create an account at heroku.com
2. Create an app, give it a name for example scuabasport, and select a region
3. Under resources search for postgres, and add a Postgres database to the app

![Heroku Postgres](readme/misc/heroku_postgres.png)
    
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
5. Install the plugins dj-database-url and psycopg2-binary.
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text: web: gunicorn scubasport.wsgi:application for example
8. In the settings.py ensure the connection is to the Heroku postgres database
9. Ensure debug is set to false in the settings.py file
10. Add localhost/127.0.0.1, and scuabasport.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Run python3 manage.py loaddata db.json
16. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
17. From the CLI login to Heroku using the command heroku git:remote -a scubasport
18. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a scubasport
19. Push the code to Heroku using the command git push heroku master
20. Ensure the following environment variables are set in Heroku
<br>![Heroku Env variables](readme/misc/heroku_env_variables.png)
21. Connect the app to GitHub, and enable automatic deploys from main
<br>![Heroku Postgres](readme/misc/heroku_deployment.png)
22. Click deploy to deploy your application to Heroku for the first time
23. Click on the link provided to access the application
24. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

## Credits
- Paul Meeny for readme deployment and some unit tests for CI
- Code Institute for the bag and checkout app as a basis for my checkout and bag apps
- CSS Tricks for much help with flex
- Stack overflow for guidance on many of my bug fixes.

*All credit also included in the page files.*

### Media

Media from the following was used throughout the site.

- [Adobe Stock Images](www.stock.adobe.com)
- [Creative Market](https://creativemarket.com/)
- [Unsplash](https://unsplash.com/)
- Oleksandr Sushko

- [Pexels](https://www.pexels.com/)
- [Shutterstock](https://www.shutterstock.com/discover/stock-assets-uk-0220?kw=free%20images&c3apidt=p44044564070&gclid=CjwKCAjwloCSBhAeEiwA3hVo_aWCMHb_myvjFHu9hDOK2H8NkLvJ2OUMurc0or0G-aCEET7y-l4RdhoCnyQQAvD_BwE&gclsrc=aw.ds)
- [Postgress-Deployment](https://github.com/pmeeny/CI-MS4-LoveRugby#deployment)
- [Site-Concept-base-models](https://www.udemy.com/course/build-a-restuarnt-site-with-python-and-django/learn/lecture/13170634?start=15#questions)
- Code for comments adapted from Code Institute Django blog

### Acknowledgements: 

- To my wife Rebecca Richards for her testing, support, feedback, permissions for content and images on this project. 
- To my mentor Mo Shami for his invaluable guidance and direction.
- To the Code Institute slack community of students.
- Code Institute Tutors

