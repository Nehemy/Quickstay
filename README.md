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

- **Enquiries & Reviews:**  
  - Enquiry form for guests to contact property owners.
  - Reviews with ratings and comments on properties.

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
quickstay/                  # Main project folder
├── accounts/               # Accounts app (user authentication and profile)
│   ├── migrations/         # Database migrations for the accounts app
│   ├── models.py           # Models for user profiles and related logic
│   ├── views.py            # Views handling account-related endpoints
│   ├── forms.py            # Forms for registration and profile updates
│   └── urls.py             # URL routes specific to the accounts app
├── listings/               # Listings app (property listings, images, reviews, enquiries)
│   ├── migrations/         # Database migrations for the listings app
│   ├── models.py           # Models for Property, PropertyImage, Review, Enquiry, etc.
│   ├── views.py            # Views handling property listing endpoints
│   ├── serializers.py      # (Optional) DRF serializers if using Django Rest Framework
│   └── urls.py             # URL routes specific to the listings app
├── quickstay/              # Django project configuration folder
│   ├── __init__.py         # Makes this directory a Python package
│   ├── settings.py         # Global settings for the Django project
│   ├── urls.py             # Root URL configuration for the project
│   ├── wsgi.py             # WSGI configuration for deployment
│   └── asgi.py             # ASGI configuration for asynchronous support
├── media/                  # Media files (uploaded images, etc.)
├── static/                 # Static files (CSS, JS, images)
├── manage.py               # Command-line utility for interacting with the Django project
└── README.md               # Project overview and documentation
