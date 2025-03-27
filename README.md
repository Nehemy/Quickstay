# QuickStay - Short Let Web App

QuickStay is a Django-powered short let web application that connects hosts (property owners) with guests seeking short-term rentals. Hosts can list properties with detailed descriptions, images, pricing, and amenities, while guests can view listings and send enquiries.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
<!-- - [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license) -->

## Overview

This project is built using Django and implements key functionalities including:
- User authentication and registration
- Profile management with role selection (Host vs. Renter)
- Property listings with a cover image and additional images
- Amenity selection via a multi-select field
- Enquiries and Reviews for properties

## Features

- **User Management:**  
  - Registration and login using Django's built-in User model.
  - Extended Profile with bio, profile picture, and user type (Host or Renter).

- **Property Listings:**  
  - CRUD operations for property listings.
  - Prepopulated property types (Apartment, House, Condo, Studio, Hotel, Hostel).
  - Amenity selection using a multi-select field.
  - Cover image and additional images support.

- **Enquiries**  
  - Enquiry form for guests to contact property owners.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/quickstay.git
   cd quickstay

**Create and Activate a Virtual Environment:**

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

- **Install the Dependencies:**

pip install -r requirements.txt

- **Apply Migrations:**

python manage.py makemigrations
python manage.py migrate

- **Run the Development Server:**

python manage.py runserver


## Project Structure

```plaintext
quickstay/
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── account_form.html
│   │       └── profile.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── listings/
│   ├── migrations/
│   ├── templates/
│   │   └── listings/
│   │       ├── confirm_delete.html
│   │       ├── property_detail.html
│   │       └── property_form.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── quickstay/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── images/
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── base.html
│   └── home.html
├── db.sqlite3
├── manage.py
└── README.md
