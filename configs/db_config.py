from __future__ import annotations

import json
import os


class Config:

    def __init__(self, source='json'):

        if source == 'json':
            with open('config.json') as f:
                config = json.load(f)

            db_name = config['CONFIGURATION']['DATABASE_NAME']
            db_type = config['CONFIGURATION']['DB_TYPE']
            db_host = config['CONFIGURATION']['HOST_ADDRESS']
            db_port = config['CONFIGURATION']['PORT']
            db_user = config['CONFIGURATION']['DB_USER']
            db_password = config['CONFIGURATION']['DB_PASSWORD']

        elif source == 'env':
            db_name = os.environ.get('DATABASE_NAME')
            db_type = os.environ.get('DB_TYPE')
            db_host = os.environ.get('HOST_ADDRESS')
            db_port = os.environ.get('PORT')
            db_user = os.environ.get('DB_USER')
            db_password = os.environ.get('DB_PASSWORD')

        self.db_config = f'{db_type}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    def get_config(self):
        return self.db_config
