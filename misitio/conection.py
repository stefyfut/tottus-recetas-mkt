import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def conectionFB():
    cred = credentials.Certificate('./tottus-recetas-firebase.json')

    return cred
