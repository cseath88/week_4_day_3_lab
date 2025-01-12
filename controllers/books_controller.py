from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/book_list.jinja", all_books = books)

@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/single_book.jinja', book = book)

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')



