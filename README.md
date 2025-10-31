🛒 Grocery Store Management System (GSMS)
📘 Overview

The Grocery Store Management System (GSMS) is a web-based inventory and order management platform that allows administrators to efficiently manage grocery items, pricing, and orders.
It provides a clean interface for adding, updating, and deleting products while maintaining a reliable backend for database operations.

This project integrates Flask (Python) on the backend with HTML, CSS, JavaScript, jQuery, and AJAX on the frontend for seamless, real-time interactivity.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Features Implemented by Me

Developed Flask-based REST APIs to manage Products, Orders, and Units of Measurement (UOM) for streamlined backend communication.

Integrated full CRUD functionality for managing products — including adding, updating, and deleting grocery items — improving inventory accuracy.

Implemented order management operations, allowing users to place orders, track order details, and calculate total pricing dynamically.

Utilized SQL queries for inserting, updating, and deleting data in the database, ensuring optimized performance for large datasets.

Applied AJAX and jQuery for real-time updates in the product list, creating smooth dynamic interactions without page reloads.

Automated backend database operations using Python scripts, enhancing efficiency and minimizing manual data entry.

Enhanced application security by applying input validation and safeguards against SQL injection at API endpoints.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧩 Tech Stack

Frontend:

HTML5, CSS3, Bootstrap

JavaScript, jQuery, AJAX

Backend:

Python (Flask Framework)

RESTful API Design

Database:

MySQL

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧠 How It Works

User Interface:
Admins interact via the managed_product.html page to view, add, or modify grocery products.

AJAX + Flask API:
jQuery AJAX calls are sent to Flask routes like /getProducts, /insertProduct, /updateProduct, and /deleteProduct.

Database Operations:
Flask executes corresponding SQL queries to retrieve or modify records in the MySQL database.

Dynamic UI Updates:
AJAX ensures changes appear instantly in the product list — no page refresh required.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

▶️ Running the Project

1. Clone the Repository:

git clone https://github.com/yourusername/grocery-management-system.git
cd grocery-management-system

2. Install Python Dependencies:

pip install flask mysql-connector-pytho

3. Start Flask Server:

python app.py

The app will start running at:
👉 http://127.0.0.1:5000

4. Open in Browser:
Open managed_product.html in your browser to use the interface.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧱 API Endpoints
Method	Endpoint	Description
GET	/getProducts	Fetch all products
POST	/insertProduct	Add a new product
POST	/updateProduct	Update product details
POST	/deleteProduct	Delete a product
GET	/getUOM	Fetch list of units
GET	/getAllOrders	Retrieve all orders

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🛡️ Security Measures

Input validation on all forms.

Parameterized SQL queries to prevent SQL injection.

Restricted API endpoints for backend operations.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Contributions include:
✔ Flask REST API integration
✔ Database CRUD operations
✔ Dynamic UI updates via AJAX
✔ Security and optimization improvements

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
