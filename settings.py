#!/usr/bin/env python
"""
This program is just an example API
Copyright (C) 2017 Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of N360 Sample API.

N360 Sample API is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

N360 Sample API is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with N360 Sample API.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

employees_schema = {
    'internalcode': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
        'required': True,
        'unique': True
    },
    'firstname': {
        'type': 'string'
    },
    'lastname': {
        'type': 'string'
    }
}

DOMAIN = {
    'employees': {
        'item_title': 'employee',
        # Allow GET requests at '/employees/<internalcode>'
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'internalcode'
        },
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PUT', 'PATCH', 'DELETE'],
        'schema': employees_schema
    }
}

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'n360-sample-api')

#X_DOMAINS = '*'

# Disable etag concurrency control (for now anyway)
IF_MATCH = False
