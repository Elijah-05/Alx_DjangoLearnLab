# Book API — Generic Views Overview

This API is built using Django REST Framework and implements CRUD operations
for the Book model using DRF generic views.

## Available Endpoints

GET /api/books/
    Returns a list of all books (public)

GET /api/books/<id>/
    Returns a book by its ID (public)

POST /api/books/create/
    Creates a new book (authenticated users only)

PUT /api/books/<id>/update/
    Updates a book (authenticated users only)

DELETE /api/books/<id>/delete/
    Deletes a book (authenticated users only)

## Permissions
- List & detail views use AllowAny (public)
- Create, update & delete use IsAuthenticated (restricted)

## Custom Behavior
- BookSerializer validates publication_year to prevent future dates.
- Update and create views can be extended with custom logic in perform_create() or perform_update().
