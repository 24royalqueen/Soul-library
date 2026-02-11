from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Data
books = []
members = []
fines = []
reservations = []

# Books Endpoints
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return jsonify(book), 200 if book else 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        updated_book = request.json
        book.update(updated_book)
        return jsonify(book), 200
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 204

# Members Endpoints
@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

@app.route('/members', methods=['POST'])
def add_member():
    new_member = request.json
    members.append(new_member)
    return jsonify(new_member), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = next((member for member in members if member['id'] == member_id), None)
    return jsonify(member), 200 if member else 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member = next((member for member in members if member['id'] == member_id), None)
    if member:
        updated_member = request.json
        member.update(updated_member)
        return jsonify(member), 200
    return jsonify({'message': 'Member not found'}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    global members
    members = [member for member in members if member['id'] != member_id]
    return jsonify({'message': 'Member deleted'}), 204

# Borrowing Endpoints
@app.route('/borrow', methods=['POST'])
def borrow_book():
    # Implement borrowing logic
    return jsonify({'message': 'Book borrowed'}), 201

@app.route('/return', methods=['POST'])
def return_book():
    # Implement return logic
    return jsonify({'message': 'Book returned'}), 201

# Fines Endpoints
@app.route('/fines', methods=['GET'])
def get_fines():
    return jsonify(fines), 200

@app.route('/fines', methods=['POST'])
def add_fine():
    new_fine = request.json
    fines.append(new_fine)
    return jsonify(new_fine), 201

@app.route('/fines/<int:fine_id>', methods=['DELETE'])
def delete_fine(fine_id):
    global fines
    fines = [fine for fine in fines if fine['id'] != fine_id]
    return jsonify({'message': 'Fine removed'}), 204

# Reservations Endpoints
@app.route('/reservations', methods=['POST'])
def reserve_book():
    new_reservation = request.json
    reservations.append(new_reservation)
    return jsonify(new_reservation), 201

@app.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = next((res for res in reservations if res['id'] == reservation_id), None)
    return jsonify(reservation), 200 if reservation else 404

@app.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    global reservations
    reservations = [res for res in reservations if res['id'] != reservation_id]
    return jsonify({'message': 'Reservation canceled'}), 204

if __name__ == '__main__':
    app.run(debug=True)