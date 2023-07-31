"""
Users API

This module provides functionality for App Users.
"""

# pylint: disable=E0401
from flask_restx import Namespace, Resource, fields

api = Namespace("users", description="User related operations")

user = api.model(
    "User",
    {
        "id": fields.String(required=True, description="The user identifier"),
        "username": fields.String(required=True, description="The user username"),
        "name": fields.String(required=False, description="The user Name"),
        "email": fields.String(required=True, description="The user email"),
        "password": fields.String(required=True, description="The user password"),
        "books": fields.List(fields.String, required=False, description="The user books"),
        "libraries": fields.List(
            fields.Nested(
                api.model(
                    "Library",
                    {
                        "library_name": fields.String(
                            required=True, description="The library name"
                        ),
                        "books": fields.List(
                            fields.String,
                            required=False,
                            description="List of library book ids",
                        ),
                    },
                )
            ),
            required=False,
            description="The user libraries",
        ),
    },
)

USERS = [
    {
        "id": "123",
        "username": "john_doe",
        "name": "John Doe",
        "email": "john@example.com",
        "password": "mypassword",
        "books": ["book1", "book2", "book3", "book4", "book5"],
        "libraries": [
            {
                "library_name": "Library A",
                "books": ["book1", "book2", "book3"]
            },
            {
                "library_name": "Library B",
                "books": ["book4", "book5"]
            }
        ]
    }
]


@api.route("/")
class UserList(Resource):
    @api.doc("list_users")
    @api.marshal_list_with(user)
    def get(self):
        """List all users"""
        return USERS


@api.route("/<id>")
@api.param("id", "The user identifier")
@api.response(404, "User not found")
class User(Resource):
    @api.doc("get_user")
    @api.marshal_with(user)
    def get(self, id):
        """Fetch a user given its identifier"""
        for user in USERS:
            if user["id"] == id:
                return user
        api.abort(404)

