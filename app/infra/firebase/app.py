from firebase_admin import initialize_app, credentials

cred = credentials.Certificate('key/key-firebase.json')

app = initialize_app(cred)