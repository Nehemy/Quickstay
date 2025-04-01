# QuickStay - Short Let Web App

QuickStay is a Django-powered short let web application that connects hosts (property owners) with guests seeking short-term rentals. Hosts can list properties with detailed descriptions, images, pricing, and amenities, while guests can view listings and send enquiries.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)


## Overview

This project is built using Django and implements key functionalities including:
- User authentication and registration
- Profile management with role selection (Host vs. Renter)
- Property listings with a cover image and additional images
- Amenity selection via a multi-select field
- Enquiries and Reviews for properties

## Features

- **User Management:**  
  - Registration with account type selection (host or renter)
  - Login with token authentication
  - Profile management (view/update)

- **Property Listings:**  
  - CRUD operations for property listings. (host-only for create, update, and delete)
  - Prepopulated property types (Apartment, House, Condo, Studio, Hotel, Hostel).
  - Amenity selection using a multi-select field.
  - Cover image and additional images support.

- **Enquiries**  
  - Enquiry form for guests to contact property owners.
  - Enquiries are also accessible via a dedicated endpoint

- **Public Profile View:**  
  - Public endpoint for viewing host profiles without sensitive data

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/quickstay.git
   cd quickstay

**Create and Activate a Virtual Environment:**

python -m venv venv
source env/bin/activate   # On Windows use `env\Scripts\activate`


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
│   │       └── public_profile.html
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
│   │       ├── host_enquiries.html
│   │       ├── property_details.html
│   │       └── properties.html
│   │       └── property_form.html
│   │       └── property.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── api/
│   ├── __init__.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
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
│   │   └── registration/
│   │       ├── logged_out.html
│   │       ├── login.html
│   │       ├── signup.html
│   ├── base.html
│   └── home.html
├── db.sqlite3
├── manage.py
└── README.md
```

## API Endpoints

## 1. User Registration
**Endpoint:**  
`POST /api/register/`

**Purpose:**  
Register a new user by providing a username, name (mapped to the User’s first_name), email, password, password confirmation, and account type.

**Body:**
```json
{
  "username": "chinedu123",
  "name": "Chinedu",
  "email": "chinedu@example.com",
  "password": "SecurePassword1",
  "password2": "SecurePassword1",
  "user_type": "host"
}
```

**Expected Response:**
```json
{
  "message": "User successfully registered."
}
```

## 2. User Login
**Endpoint:**  
`POST /api/login/`

**Purpose:**  
Authenticate the user and return an authentication token.

**Body:**
```json
{
  "username": "chinedu123",
  "password": "SecurePassword1"
}
```

**Demo Expected Response:**
```json
{
  "token": "11111111000aethnd12345678925y2f01234567"
}
```

Use the token in the Authorization header for all authenticated endpoints.
Example:

Authorization: Token 11111111000aethnd12345678925y2f01234567

## 3. Profile (Logged-in User)
**Endpoint:**  
`GET /api/profile/`

**Purpose:**  
Retrieve, update, or delete the profile of the authenticated user.

**Demo Headers:**  
Authorization: Token 11111111000aethnd12345678925y2f01234567


**Demo Expected Response:**
```json
{
  "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "username": "chinedu123",
  "name": "Chinedu",
  "email": "chinedu@example.com",
  "bio": "",
  "profile_picture": "/images/profile_images/default.png",
  "user_type": "host",
  "date_joined": "2025-03-31T14:30:00Z",
  "updated_at": "2025-03-31T14:30:00Z"
}
```

## 4. Properties

**a. List Properties**  

**Endpoint:**  
`GET /api/properties/`

**Purpose:**  
Retrieve a list of all properties.


**Demo Expected Response:**
```json
[
  {
    "id": "4a9e56c9-aef8-4187-91ca-45d72a6ac35f",
    "description": "Modern apartment in the heart of Lagos",
    "address": "No. 12, Iyana Ipaja, Lagos",
    "city": "Lagos",
    "state": "Lagos",
    "country": "Nigeria",
    "price": "1500000.00",
    "property_type": "apartment",
    "amenities": ["wifi", "ac", "kitchen"],
    "cover_image": "/images/cover_images/lagos.jpg",
    "images": [],
    "enquiries": []
  }
]
```

**b. Retrieve Single Property**  

**Endpoint:**  
`GET /api/properties/<property_id>/`

**Purpose:**  
Retrieve detailed information for a specific property, including nested images and enquiries (if the authenticated user is the property owner).

**c. Create Property (Host Only)**  

**Endpoint:**  
`POST /api/properties/`

**Purpose:**  
Create a new property (only hosts can create properties).

**Body**
```json
{
  "description": "Modern apartment in the heart of Lagos",
  "address": "No. 12, Iyana Ipaja, Lagos",
  "city": "Lagos",
  "state": "Lagos",
  "country": "Nigeria",
  "price": "1500000.00",
  "property_type": "apartment",
  "amenities": ["wifi", "ac", "kitchen"],
  "cover_image": "/images/cover_images/lagos.jpg"
}
```

**d. Update/Delete Property**  

**Endpoint:**  
`PUT/PATCH /api/properties/<property_id>/`
`DELETE /api/properties/<property_id>/`

**Purpose:**  
Update or delete a property (only allowed if the authenticated user is the property owner).

## 5. Enquiries

**Endpoint:**  
`GET, POST /api/enquiries/`

**Purpose:**  
Authenticated users can create enquiries and view them.


**Demo for Creating an Enquiry:**
```json
{
  "property": "<property_id>",
  "name": "Emeka",
  "phone": "08012345678",
  "email": "emeka@example.com",
  "message": "I would like more details about your property."
}
```

**Demo Expected Response**
```json
{
  "id": 1,
  "property": "<property_id>",
  "name": "Emeka",
  "phone": "08012345678",
  "email": "emeka@example.com",
  "message": "I would like more details about your property.",
  "created_at": "2025-03-31T15:00:00Z"
}
```

## 6. Public Profile

**Endpoint:**  
`GET /api/public-profile/<profile_id>/`

**Purpose:**  
Retrieve the public profile of a host, showing non-sensitive data (name, bio, profile_picture, user_type) and nested properties.


**Demo Expected Response**
```json
{
  "name": "Chinedu",
  "bio": "",
  "profile_picture": "/images/profile_images/default.png",
  "user_type": "host",
  "properties": [
    {
      "id": "property_uuid",
      "description": "Modern apartment in the heart of Lagos",
      "address": "No. 12, Iyana Ipaja, Lagos",
      "city": "Lagos",
      "state": "Lagos",
      "country": "Nigeria",
      "price": "1500000.00",
      "property_type": "apartment",
      "amenities": ["wifi", "ac", "kitchen"],
      "cover_image": "/images/cover_images/lagos.jpg",
      "images": [],
      "enquiries": []
    }
  ]
}
```