import mysql.connector
from mysql.connector import errorcode
from flask import flash

try:
    # Establish a connection with the MySQL database
    # Password here is hardcoded for simplicity.
    # For all practical purposes, use environment variables or config files.
    cnx = mysql.connector.connect(user='test_user', password='password',
                                  host='127.0.0.1',
                                  database='phone_directory')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


def add_contact(contact):
    status = None
    cursor = cnx.cursor()
    insert_query = "INSERT INTO contacts (name, mobile_no, email) VALUES (%s, %s, %s)"
    contact = (contact.get("name"), contact.get(
        "mobile_no"), contact.get("email"))
    try:
        cursor.execute(insert_query, contact)
        status = True
    except Exception as e:
        print(e)
        status = False
    finally:
        cnx.commit()
        cursor.close()

    return status


def get_contacts():
    try:
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        cursor.close()
        return contacts
    except Exception as e:
        print(e)
        flash("Error occured while reading from the database")
        return None


def delete_contact(contact_id):
    cursor = cnx.cursor()
    try:
        cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id, ))
        flash("Contact deleted successfully")
    except Exception as e:
        print(e)
        flash("Error occured while deleting from the database")
    cursor.close()
