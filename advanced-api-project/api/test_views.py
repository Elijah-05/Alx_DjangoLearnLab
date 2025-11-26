from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .models import Author, Book


"""
This test suite validates all API behavior for the Book model:

1. CRUD (Create, Retrieve, Update, Delete)
2. Filtering, Searching, Ordering
3. Permissions (authenticated vs unauthenticated users)

We use Django REST Framework's APITestCase and APIClient to simulate
real HTTP requests to the API.
"""


class BookAPITestCase(APITestCase):
    """Main test class for Book API."""

    def setUp(self):
        """
        Create test data and authentication setup.
        Runs before each test.
        """

        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Create an API client
        self.client = APIClient()

        # Create Authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create Books
        self.book1 = Book.objects.create(
            title="Book A",
            publication_year=2000,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="Book B",
            publication_year=1995,
            author=self.author2
        )
        self.book3 = Book.objects.create(
            title="Another Book",
            publication_year=2020,
            author=self.author1
        )

    # -----------------------------------------------------
    # CRUD TESTS
    # -----------------------------------------------------

    def test_list_books(self):
        """Ensure that the list endpoint returns all books."""
        url = reverse("book-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_single_book(self):
        """Test retrieving a single book by ID."""
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book A")

    def test_create_book_unauthenticated(self):
        """Unauthenticated users must not create books."""
        url = reverse("book-create")
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated users can create books."""
        self.client.login(username="testuser", password="testpassword")

        url = reverse("book-create")
        data = {
            "title": "Created Book",
            "publication_year": 2021,
            "author": self.author1.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book(self):
        """Test updating a book."""
        self.client.login(username="testuser", password="testpassword")

        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Updated Book A",
            "publication_year": 2005,
            "author": self.author1.id
        }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book A")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username="testuser", password="testpassword")

        url = reverse("book-delete", args=[self.book1.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    # -----------------------------------------------------
    # FILTERING, SEARCHING, ORDERING
    # -----------------------------------------------------

    def test_filter_books_by_author(self):
        """Filter books by author ID."""
        url = reverse("book-list")
        response = self.client.get(url, {"author": self.author1.id})

        self.assertEqual(len(response.data), 2)  # book1 & book3

    def test_search_books(self):
        """Search books by title or author's name."""
        url = reverse("book-list")
        response = self.client.get(url, {"search": "another"})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Another Book")

    def test_order_books_by_publication_year(self):
        """Order books ascending by publication year."""
        url = reverse("book-list")
        response = self.client.get(url, {"ordering": "publication_year"})

        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

    # -----------------------------------------------------
    # PERMISSIONS
    # -----------------------------------------------------

    def test_permission_protection(self):
        """Ensure write operations require authentication."""
        url = reverse("book-create")
        data = {
            "title": "Unauthorized Create",
            "publication_year": 2022,
            "author": self.author1.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
