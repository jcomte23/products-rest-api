# Products REST API

This is a simple REST API built with Flask, designed for managing a product inventory. It allows users to perform CRUD operations (Create, Read, Update, Delete) on a list of products.

## Features

- **GET** `/products`: Retrieve all products in the inventory.
- **POST** `/products`: Add a new product to the inventory.
- **PUT** `/products/{id}`: Update an existing product by ID.
- **DELETE** `/products/{id}`: Delete a product by ID.

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository:
```bash
git clone https://github.com/jcomte23/product-api.git
```

### 2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
```

### 3. Activate the virtual environment:

+ On Windows
```bash
venv\Scripts\activate
```

+ On macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install dependencies:
```bash
pip install -r requirements.txt
```

### 5. Run the API:
```bash
python app.py
```