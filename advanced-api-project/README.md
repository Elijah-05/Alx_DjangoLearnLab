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


# Filtering, Searching, and Ordering

The Book API supports advanced query features using Django REST Framework.

## Filtering

You can filter results using exact field matches:

- /api/books/?title=Dune
- /api/books/?publication_year=1965
- /api/books/?author=1

## Searching

Search text across title and author name:

- /api/books/?search=dune
- /api/books/?search=orwell

## Ordering

Sort results by any of the allowed fields:

- /api/books/?ordering=title
- /api/books/?ordering=-publication_year

Negative sign `-` indicates descending order.

## Combined Examples

- `/api/books/?search=dune&ordering=-publication_year`
- `/api/books/?author=2&ordering=title`
