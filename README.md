# ShopEase – Online Shopping System in C

## Project Overview

ShopEase is a simple and modular online shopping system built using the C programming language. It supports essential e-commerce features such as product browsing, cart management, user authentication, and order processing. The system also includes separate roles for users and admins with different privileges.

## Features

- **User Authentication**
  - Register
  - Login
  - Password Recovery
- **Cart System**
  - Add product by ID
  - Manage product quantity
- **Order System**
  - Place orders
  - Update order status
- **Product Management**
  - Add, view, update products
- **Roles**
  - Separate Admin and User privileges

## System Architecture

- `Main.c`: Entry point, main menu logic
- `Auth.c`: User login, registration, password recovery
- `Product.c`: Product catalog management
- `Cart.c`: Shopping cart functionality
- `Order.c`: Order handling and status tracking
- **Data Storage**: Text files (`products.txt`, `orders.txt`, `users.dat`) for persistence

## Code Highlights

- **Product Display**: Reads from `products.txt` and displays product info with formatting.
- **Add to Cart**: Validates product ID and stock, updates cart.
- **File Operations**: All data interactions are done through text and binary files for persistence.

## Team Contributions

- **Nehith Reddy (B24CY1019)**: User Authentication
- **Bomburi Yaswanth (B24ME1017)**: Product Catalog & Management
- **Dasari Ashish (B24CS1024)**: Cart Functionality
- **Tumma Abhinav (B24BB1041)**: Order System & Admin Features
- **Kushagra Yadav (B24CM1042)**: File Handling and Integration

## Conclusion

ShopEase is a lightweight and user-friendly shopping system demonstrating fundamental concepts in C programming, modular design, and file handling. This project enhanced our team’s understanding of large codebases, collaborative coding, debugging, and practical implementation of real-world systems in C.

---

*Made with dedication by the ShopEase Team.*
