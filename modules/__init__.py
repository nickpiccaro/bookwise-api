"""
Module Description

This module provides functionality for XYZ.

Author: Your Name
"""

# pylint: disable=E0401
from flask_restx import Api

from .user import api as users_api
from .gbooks import api as books_api
from .yolo import api as yolo_api

api = Api(
    title='BookWise API',
    version='1.0',
    description='Powerful book id tool',
)

api.add_namespace(users_api)
api.add_namespace(books_api)
api.add_namespace(yolo_api)
