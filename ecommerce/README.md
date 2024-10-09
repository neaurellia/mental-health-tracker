assignment 6
1. JavaScript can be used to create dynamic and interactive web applications.
- JS allows developers to create interactive user interfaces that respond to user actions in real time without refreshing the page
- JS works on all modern browsers, hence it is more accessible to a wider audience
- The JS ecosystem includes libraries and frameworks like React, Vue.js and Angular to help streamline development and provide reusable components
- Can also be used for server-side programming

2. We need the await keyword to wait for a Promise to resolve or reject before continuing execution. We want to wait for the response when calling fetch() before proceeding with further logic. Otherwise, it can lead to undefined values or errors or async challenges.

3. csrf_exempt disables Django's Cross-Site Request Forgery protection for the specific view it's applied to. This is needed for AJAX POST requests because:
- AJAX requests might not include the necessary CSRF token
- Simplifies testing by bypassing the CSRF check in development or when external clients are involved.

4. - Front-end validation can be easily bypassed by attackers using Postman or by disabling JavaScript
- Backend sanitization ensures that even if malicious data is sent, it will be cleaned or rejected
- Ensures consistent processing of data across all platforms because different browsers may interpret front-end validation differently

5. First we add error message to Login, then we create a function to Add Product Order with AJAX. Next, we add routing for said function and display the Product Entry data with fetch() API. After that, we create Modal as a form to Add Product and we add data product with AJAX. Next, we protect the app from XSS by adding strip_tags to "clean up" new data and sanitize data with DOMPurify.


























assignment 5
1. 1. Inline styles (applied directly in the HTML element using style attribute)
  2. ID selectors (#id_name), must be unique within the entire document
  3. Class selectors(.class_name) or attribute selectors(ex: [type="text]) and pseudo-classes(ex: :hover)
  4. Element selectors(ex: p, div, etc.), applies to all elements of specified type
If selectors have the same specificity, the last one defined in the CSS file will be applied

2. Responsive design makes web applications adapt to different screen and device sizes by using flexible layouts, images, and CSS media queries.
Applications with responsive design: Twitter, TikTok, Instagram, YouTube
Applications without responsive design: older government sites

3. ![alt text](image-1.png)
margin: the transparent area outside the border, the margin property also affects the total space that the box will take up on the page, but the margin is not included in the actual size of the box. The box's total width and height stops at the border.
border: border that goes around the padding and content
padding: transparent area around content

div {
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
}

4. Flexbox (Flexible Box Layout) is a one-dimensional CSS layout model that allows you to arrange items in a row or column. It designs complex layouts with ease. It provides a more efficient way to align, distribute, and order items within a container, even when their sizes are unknown or dynamic, ideal for navigation bars, buttons, and lists.

Core Concepts of Flexbox:
1. Flex Container and Items
- Flex container: The parent element that has display: flex or display: inline-flex. It defines a flex context for its direct children.
- Flex items: The direct child elements of a flex container, which are laid out according to the flexbox rules.
2. Main and Cross Axis
- Main: Primary axis
- Cross: perpendicular to main axix (if main is horizontal, cross is vertical and vice versa)
3. Flex Properties for Container
- Flex-direction: Defines the direction in which flex items are placed within the container. (row, row-reverse, column, column-reverse)
- Flex-wrap: Controls whether flex items wrap onto multiple lines (nowrap, wrap, wrap-reverse)
- Justify-content: Aligns items along the main axis (horizontal by default). (flex-start, flex-end, center, space-between, space-around, space-evenly)
- Align-items: Aligns items along the cross axis(flex-start, flex-end, center, baseline)
- Align-content: Aligns rows of flex items when there is extra space on the cross axis (flex-start, flex-end, center, space-between, space-around, stretch)
4. Flex Properties for Items
- Order: Changes the order of individual flex items.
- flex-grow: Specifies how much a flex item should grow relative to the others in the container
- flex-shrink: Specifies how much a flex item should shrink relative to the others when space is limited
- flex-basis: Defines the initial size of the flex item before growing or shrinking is applied.
- align-self: Overrides the align-items property for individual flex items. (auto, flex-start, flex-end, center, baseline, stretch)
5. Flex shorthand: combines flex-grow, flex-shrink, and flex-basis into one property

Uses of Flexbox:
- Responsive design: Easily adapts elements to different screen sizes.
- Centering elements (both vertically and horizontally) without much complexity.
- Creating navigation bars, flexible galleries, card layouts, and other UI components.
- Ordering and aligning elements regardless of HTML structure.

The CSS Grid Layout is a two-dimensional layout system designed to handle both rows and columns. Unlike Flexbox, which is primarily one-dimensional (either row-based or column-based), Grid allows you to control the placement of items along both the horizontal and vertical axes.

Core Concepts of Grid Layout:
1. Grid Container: The parent element that holds grid items. You define a grid container by applying display: grid or display: inline-grid.
2. Grid Items: The children of the grid container. Each child automatically becomes a grid item.
3. Grid Lines: The dividing lines that define the rows and columns.
4. Grid Tracks (Rows and Columns): A grid track is the space between two grid lines. Grid tracks are defined using grid-template-rows and grid-template-columns.
5. Grid Cells: The space between any four grid lines (the intersection of a row and a column) is a grid cell.
6. Grid Areas: You can name areas of your grid, which allow you to place items into those predefined areas using the grid-area property.
7. Gaps: The space between rows and columns, which can be adjusted using grid-gap, grid-row-gap, and grid-column-gap.
8. Auto-placement: Items are automatically placed on the grid in available cells unless otherwise specified using explicit positioning.
9. Explicit Grid: You explicitly define the number of rows and columns.
10. Implicit Grid: Grid can automatically generate additional rows or columns if the content requires it.
11. Grid Template: Allows you to define the structure of the grid using the grid-template property, which sets up the rows, columns, and grid areas all at once.
12. Justify and Align Items: Align items along the horizontal and vertical axes within the grid container using justify-items, align-items, and similar properties for individual items like justify-self, align-self.

Uses of Grid Layout:
- Complex web layouts (e.g., page layouts with headers, footers, sidebars, and main content areas).
- Building fully responsive designs with precise control over how elements are sized and positioned.
- Creating dashboard-style layouts with multiple, aligned components.
- Layouts where both horizontal and vertical placement of items is needed.

Flexbox vs. Grid Layout: Key Differences
- Flexbox is a one-dimensional layout model (row or column), while Grid is two-dimensional (rows and columns).
- Flexbox is generally better for simple layouts or aligning items along a single axis. Grid is more powerful for complex, large-scale layouts where control over both axes is needed.
- Flexbox is often used inside components, while Grid is typically used for structuring the overall page layout. However, they can be combined for more flexibility in design.

When to Use Flexbox:
- When you need to align items along a single row or column.
- When you need to control the order of items based on screen size.
- Ideal for navigation bars, button groups, and centering elements.

When to Use Grid:
- When you need a complex, multi-dimensional layout.
- When you want to control both row and column positioning.
- Useful for page layouts, card-based designs, and organizing content-heavy pages.


5. First we add tailwind, then add features such as edit and delete product, then we add navigation bar, then configure static files then edit css to our liking.



















assignment 4
1. HttpResponseRedirect() is a class in Django that is used to perform a manual redirect to a different URL. It takes a URL as an argument and sends a response telling the browser to navigate to that URL.

redirect() is a convenience function provided by Django that abstracts away the lower-level HttpResponseRedirect(). It can accept not only a URL string but also a view name or even an object, making it more flexible.

2. In Django, a foreign key relationship can link MoodEntry model and User model as so:
user = models.ForeignKey(User, on_delete=models.CASCADE)
This creates a relationship where each mmood entry is related to a specific user to retrieve all mood entries made by user.

3. Authentication: process of verifying who a user is
Authorization: process of determining what an authenticated user is allowed to do

4. Django stores data on the server and a session ID in a cookie on the user's browser. Every time the user makes a request, the session ID is sent along with it, allowing Django to recognize the user as logged in.

Other uses of cookies:
- Tracking user preferences: Cookies can be used to store user preferences, such as language settings or dark mode preferences.
- Cart functionality: In e-commerce sites, cookies can track the items added to a user's shopping cart.
- Analytics and tracking: Cookies are used for analytics purposes to track user behavior and activity on a website.

Not all cookies are safe, especially when dealing with sensitive information. 

5. First I implemented function and registration forms by adding the registration form and created the register mechanism. This is done by editing views.py and urls.py and creating register.html.

Next, I implemented a login function by importing authenticate, login and AuthenticationForm (built-in Django functions) in views.py and adding a login_user function to authenticate users to log in. Then, I created login.html and edited urls.py as needed.

After that, I implemented a logout function by editing and importing logout in views.py. I also implemented the logout mechanism by creating a logout_user function, then I edited main.html so that it would link to the URL based on app_name and name defined in urls.py. I then edited urls.py as needed

I also restricted access to the main page then used data from cookies by importing HttpResponseRedirect, reverse and datetime and modified a few functions in views.py

Finally, I connected ProductEntry model to the User model by linking each ProductEntry object created to the user who made it so that an authorized user only sees entries they created.



















assignment 3
1. Enables communication between different parts of the system and between platforms and users. It forms the backbone of communication in any platform, ensuring that information flows seamlessly across all components.

2. JSON is generally better for web applications because it is:
- simpler, more compact syntax compared to XML.
- easier and faster to parse, especially in JavaScript.
- JSON data is easy for both humans and machines to read.

XML may be better for complex documents and data interchange where the structure needs to be more rigorous:
- more flexible with its support for attributes and nested elements, making it useful for defining complex data structures.
- XML supports namespaces, which helps in differentiating similar data fields in large documents.

JSON is more popular than XML because:
- JSON is faster to parse and generate than XML.
- JSON's minimal syntax makes it easier to write, read, and debug. This is a key reason for its widespread adoption in modern APIs.
- JSON is directly compatible with JavaScript, the most widely used language for web development, making it a natural choice for web applications.
-  JSON is more concise, requiring fewer characters to represent data than XML

3. The is_valid() method in Django forms checks whether the form data is valid by:
- Validating Data: It runs through all field validators and ensures that the data conforms to the rules defined in the form’s fields (e.g., required fields, data types, and length constraints).
- Cleaning Data: After validation, the is_valid() method stores the cleaned data in form.cleaned_data for further processing (e.g., saving to the database).
- Returns a Boolean: If the data is valid, it returns True; otherwise, it returns False and stores error messages in form.errors.

Why Do We Need is_valid()?
- Error Handling: It prevents invalid or incomplete data from being processed and provides users with informative error messages to fix issues in form submission.
- Security: Validating data before processing ensures that only clean, expected data is accepted, reducing the risk of malicious input or data corruption.

4. - prevent attackers from submitting forms on behalf of users.
- avoid exploitation of authenticated user's session and take over sensitive operations

5. Compare them with tutorial 2 and implement them. First I implemented the Skeleton of a View, then changed the Primary Key from integer to UUID, then I created as form input data and displayed data on HTML. Next I returned data in both XML and JSON format and did it based on an ID, then I used Postman as a data viewer and deployed to PWS

![WhatsApp Image 2024-09-18 at 11 21 39_39d33e01](https://github.com/user-attachments/assets/0d7c5adb-a8ab-4c6a-a41e-a48a0ff8ca58)
![WhatsApp Image 2024-09-18 at 11 22 04_87fd11b8](https://github.com/user-attachments/assets/a1c0bdab-6607-4e32-8ac7-ff4706507863)
![WhatsApp Image 2024-09-18 at 11 22 45_e458d2f4](https://github.com/user-attachments/assets/7fcac5c7-78f9-4ca2-99db-c6fe57466c67)
![WhatsApp Image 2024-09-18 at 11 23 14_1c26978f](https://github.com/user-attachments/assets/c5ea2597-bafb-478f-970e-651ba471b8c8)






















assignment 2
1. First, I figured out to combine Tutorial 0 and 1 for this assignment, then after comparing the checklist and the tutorial, I simply followed the tutorials with the checklist as my guideline and made changes where necessary. I created a new repository for the new project and many folders and files inside folders as shown in the checklist, I then performed routing and created a model. I had to adjust here and for the function in views.py as well. I then created a routing in urls.py for the application main to map the function created in views.py then deployed to PWS.

2. <img width="286" alt="image" src="https://github.com/user-attachments/assets/c88d1e20-4970-46e5-bdc2-6fdececffa90">

   urls.py -> maps URLs to specific views (which view should handle that request)
   views.py -> contains the logic to execute request, communicates with models.py to fetch or update data from database, if necessary, it will pass data to HTML template for rendering
   models.py -> defines models (data structure), interacts with database
   HTML file -> view passes data to HTML file, dynamically generates a webpage using the provided data, and this page is then returned to the client as a response

4. Git can track changes made. Git keeps track of changes made so that developers can review or go back to the previous code when needed. Git can allow developers to collaborate as it allows merging without conflict and also branch so that if anything happens to one branch, the others will not be affected. Git can also back up data.
   
5. I find it seamless that it uses chunks of python and HTML so that we can learn something new and strengthen previous knowledge as well. Despite many new things to learn, I did not struggle as much as I had been familiar with Python.
  
6. It allows developers to interact with the database using Python objects rather than writing raw SQL queries. This way, it reduces errors in database interactions.