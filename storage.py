import pickle
from models import AddressBook

FILENAME = "addressbook.pkl"

def save_data(book, filename=FILENAME):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename=FILENAME):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()