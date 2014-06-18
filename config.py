import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED =  True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'Name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'Name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'Name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'Name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'Name': 'MyOpenID', 'url': 'https://ww.myopenid.com' }]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
