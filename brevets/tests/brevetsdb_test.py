"""
Nose tests for storing and accessing information in the brevets database
"""
import nose
import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.testdb


def _clean():
    mycol = db.km
    mycol.delete_many({})


def insert_retrieval():
    """
    Tests both insertion and retrieval of data
    """
    _clean()
    control_point = {
        'km': 100,
        'open_time': 200,
        'close_time': 250
    }
    db.test.insert_one(control_point)
    print(db.test.find())
    assert db.test.find()[0].km == 100
    assert db.test.find()[0].open_time == 200
    assert db.test.find()[0].close_time == 250
    _clean()


def clean_up():
    """
    Tests deletion of data
    """
    _clean()
    for i in range(5):
        control_point = {
            'km': (i + 1) * 10,
            'open_time': (i + 3) * 20,
            'close_time': (i + 4) * 20
        }
        db.test.insert_one(control_point)
    db.test.delete_many({})
    assert len(db.test.find()) == 0
    _clean()


def mass_retrieval():
    """
    Tests retrieval of many values from database
    """
    _clean()
    for i in range(20):
        control_point = {
            'km': i * 10,
            'open_time': (i + 1) * 15,
            'close_time': (i + 3) * 20
        }
        db.test.insert_one(control_point)
    assert len(db.test.find()) == 20
    _clean()
