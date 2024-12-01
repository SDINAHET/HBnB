#!/bin/bash

DB_FILE="development.db"

# Remove the old database
if [ -f $DB_FILE ]; then
    rm $DB_FILE
fi

# Create the database schema
sqlite3 $DB_FILE < create_tables.sql

# Insert initial data
sqlite3 $DB_FILE < insert_initial_data_admin.sql

echo "Database has been recreated and populated with initial data."

// chmod +x reset_db.sh
// ./reset_db.sh
