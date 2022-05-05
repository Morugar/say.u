import os
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

DATABASE_URL = f"mysql+mysqlconnector://root@localhost:3306/sayu?charset=utf8mb4"