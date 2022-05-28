#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
PROJECT_DIR=$(cd $(dirname $0)/..; pwd)
export $(cat $PROJECT_DIR/.env)

MYSQL_PWD="$DB_PASSWORD" mysql -u $DB_USER -h $DB_HOST $DB_NAME