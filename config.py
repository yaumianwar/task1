""" Configuration File """
import os

# Development (Debug -> True)
DEBUG =True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' +  os.path.join(PROJECT_DIR,'web.db')