# flask app for payroll endp[oint
from flask import Flask, request, jsonify   
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
def create_app():
    """Create and configure an instance of the Flask application."""
    """
    """