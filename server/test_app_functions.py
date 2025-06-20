import pytest
from app import BOOKS, remove_book

@pytest.fixture(autouse=True)
def setup_books():
    BOOKS.clear()
    BOOKS.extend([
        {
            'id': '1',
            'title': '1984',
            'author': 'George Orwell',
            'read': True
        },
        {
            'id': '2',
            'title': 'Brave New World',
            'author': 'Aldous Huxley',
            'read': False
        }
    ])
    yield

# Tests pour la fonction de suppression de livre
def test_remove_book():
    remove_book("2")
    assert len(BOOKS) == 1
    assert not any(b["id"] == "2" for b in BOOKS)
