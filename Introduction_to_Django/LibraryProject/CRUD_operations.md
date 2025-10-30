Script started on 2025-10-30 18:03:52+03:00 [TERM="xterm-256color" TTY="/dev/pts/5" COLUMNS="80" LINES="24"]
[?2004h]0;elyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx: ~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[01;32melyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx[00m:[01;34m~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[00m$ python manage.py shee[Kll
[?2004lCommand 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
[?2004h]0;elyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx: ~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[01;32melyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx[00m:[01;34m~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[00m$ ls
[?2004l[0m[01;34mbookshelf[0m            db.sqlite3      [01;32mmanage.py[0m  Pipfile.lock
CRUD_operations.txt  [01;34mLibraryProject[0m  Pipfile    README.md
[?2004h]0;elyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx: ~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[01;32melyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx[00m:[01;34m~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[00m$ python3 manage.py shell
[?2004lPython 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication _year=1949)
>>> book.save()
>>> books = Book.objects.all()
>>> print(books)
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book)
Nineteen Eighty-Four by George Orwell (1949)
>>> f[Kbook[K[K[K[Kbook = Book.objects.get(title="Nineteen Eighty-Four")
>>> B[Kbook.delete()
(1, {'bookshelf.Book': 1})
>>> print(Book.objects.all())
<QuerySet []>
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
[0m[?2004h]0;elyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx: ~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[01;32melyas@elyas-HP-Pavilion-Gaming-Laptop-15-dk0xxx[00m:[01;34m~/Desktop/projects/ALX/backend development/LibraryProject/Introduction_to_Django/LibraryProject[00m$ exit
[?2004lexit

Script done on 2025-10-30 18:08:29+03:00 [COMMAND_EXIT_CODE="0"]
