#!/usr/bin/python
from datetime import timedelta

VERSION='0.1'

## Debug mode. This engages the web-based debug mode
DEBUG = False

## Enable the debug toolbar. DO NOT DO THIS ON A PRODUCTION SYSTEM. EVER. It exposes SECRET_KEY.
DEBUG_TOOLBAR = False

# Key used to sign/encrypt session data stored in cookies.
SECRET_KEY = ''

## File logging
FILE_LOG=True
LOG_FILE='zero.log'
LOG_DIR='/tmp'
LOG_FILE_MAX_SIZE=1 * 1024 * 1024
LOG_FILE_MAX_FILES=10

EMAIL_ALERTS=False
ADMINS=['root']
SMTP_SERVER='localhost'
EMAIL_FROM='root'
EMAIL_SUBJECT='Zero Runtime Error'
EMAIL_DOMAIN='localdomain'

## MySQL
MYSQL_HOST='localhost'
MYSQL_USER='zero'
MYSQL_PASS=''
MYSQL_NAME='zero'
MYSQL_PORT=3306

## Flask defaults (changed to what we prefer)
SESSION_COOKIE_SECURE      = False
SESSION_COOKIE_HTTPONLY    = False
PREFERRED_URL_SCHEME       = 'http'
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

## LDAP AUTH
LDAP_URI            = 'ldaps://localhost.localdomain'
LDAP_SEARCH_BASE    = ''
LDAP_USER_ATTRIBUTE = 'sAMAccountName'
LDAP_ANON_BIND      = True
LDAP_BIND_USER      = ''
LDAP_BIND_PW        = ''
LDAP_ADMIN_GROUP    = "CN=groupname,OU=localhost,DC=localdomain"

## BACKUP STUFF
BACKUP_PORT_MIN = 10000
BACKUP_PORT_MAX = 20000