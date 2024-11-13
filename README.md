# Medical Inventory Management System

A robust medical inventory management system built using Python and Django, designed to streamline the organization, tracking, and management of medical supplies in healthcare facilities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

## Features
- **Inventory Tracking**: Easily track and manage medical items with real-time updates.
- **User Authentication**: Secure access with user login and roles.
- **CRUD Operations**: Create, read, update, and delete medical items.
- **Search Functionality**: Quick search for items by name or category.
  
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/RUKUNDO-Prince/medical-inventory-management-system.git
   ```
2. **Navigate into the project directory**:
   ```bash
   cd medical-inventory-management-system
   ```
3. **Set up a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Open a web browser and go to `http://127.0.0.1:8000/`.
2. Log in or register to access the inventory management features.
3. Use the interface to add, view, edit, or delete medical inventory items.

## Project Structure

- **medical_inventory**: Contains Django app files for inventory functionalities.
- **db.sqlite3**: SQLite database file for development.
- **manage.py**: Django command-line utility.

## Dependencies
- **Django** (see `requirements.txt` for full list)

## License
This project is open-source and available under the MIT License.
