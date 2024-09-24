#!/usr/bin/env python3
""" Flask class
"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect, make_response

AUTH = Auth()
app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ GET /
    Return:
      - welcome
    """
    return jsonify({"message": "Bienvenue"}), 200

@app.route('/users', methods=['POST'], strict_slashes=False)
def user() -> str:
    """ POST /users
    Return:
      - message
    """
    email = request.form.get('email')
    password = request.form.get('password')
    # Insert user creation logic here
    return jsonify({"message": "User created"}), 201

@app.route('/sessions', methods=['POST'], strict_slashes=False)
def logout() -> str:
    """ POST /sessions
    Logout a user by destroying their session.
    Return:
      - Redirect to GET /
      - 403 if session does not exist
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)  # No session ID provided

    user = AUTH.get_user_by_session_id(session_id)  # Adjust this method to find user by session ID

    if user:
        AUTH.destroy_session(user.id)  # Adjust this method to destroy the session
        response = make_response(redirect('/'))  # Redirect to GET /
        response.delete_cookie('session_id')  # Optional: Remove the session cookie
        return response
    else:
        abort(403)  # User not found, respond with 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
