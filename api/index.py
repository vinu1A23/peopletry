from fastapi import FastAPI, Depends, HTTPException
from flask import Flask
from sqlalchemy.orm import Session
from typing import List
from model import Task
from schema import task_schema
from session import create_get_session
app = Flask(__name__)

@app.route('/')
def index():
   return 'hello there'

