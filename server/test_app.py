import pytest
import json
from app import app, BOOKS

@pytest.fixture
def client():
    with app.test_client() as client:
        # Reset BOOKS à chaque test pour éviter les effets de bord
        BOOKS.clear()
        BOOKS.extend([
            {
                'id': '1',
                'title': 'On the Road',
                'author': 'Jack Kerouac',
                'read': True
            },
            {
                'id': '2',
                'title': 'Harry Potter and the Philosopher\'s Stone',
                'author': 'J. K. Rowling',
                'read': False
            }
        ])
        yield client

# Tests pour la route /ping
def test_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.json == 'pong!'

# Tests pour les routes /books
def test_get_books(client):
    res = client.get('/books')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'success'
    assert len(data['books']) == 2

# Tests pour la route /books avec un livre ajouté
def test_post_book(client):
    new_book = {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
    res = client.post('/books', data=json.dumps(new_book), content_type='application/json')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'success'
    assert data['message'] == 'Book added!'
    assert any(book['title'] == 'Green Eggs and Ham' for book in BOOKS)

# Tests pour la route /books/<book_id> pour mettre à jour un livre
def test_put_book(client):
    update_data = {
        'title': 'Updated Title',
        'author': 'Updated Author',
        'read': False
    }
    book_id_to_update = '1'
    res = client.put(f'/books/{book_id_to_update}', data=json.dumps(update_data), content_type='application/json')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'success'
    assert data['message'] == 'Book updated!'
    # Vérifie que le livre n'a plus l'ancien id (car il est supprimé et remplacé)
    assert not any(book['id'] == book_id_to_update for book in BOOKS)
    # Vérifie que le livre a bien les nouvelles données
    assert any(book['title'] == 'Updated Title' for book in BOOKS)

# Tests pour la route /books/<book_id> pour supprimer un livre
def test_delete_book(client):
    book_id_to_delete = '2'
    res = client.delete(f'/books/{book_id_to_delete}')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'success'
    assert data['message'] == 'Book removed!'
    assert not any(book['id'] == book_id_to_delete for book in BOOKS)
