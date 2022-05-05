import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
import mysql
import _mysql_connector

DATABASE_URL = f"mysql+mysqlconnector://root@localhost:3306/sayu"