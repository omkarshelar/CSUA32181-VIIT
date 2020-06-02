from flask import Flask, render_template, redirect, url_for, flash
from forms import addContactForm
import db_utils

# initialize the Flask app
app = Flask(__name__)

# Note: This is a demo application hence secret is hardcoded for simplicity.
# For all practical purposes, take the key from OS environment variables or config files.
app.secret_key = 'any random string'

# Route to list all phone contacts of the user.
@app.route('/', methods=["GET"])
def list_contacts():
    contacts = db_utils.get_contacts()
    if contacts is None:
        return "Error conecting to database. Ensure that the database is installed properly."
    return render_template('list_contacts.html', contacts=contacts)

# Add a contact to phonebook
@app.route('/add/', methods=["GET", "POST"])
def add_contact():
    form = addContactForm()
    if form.validate_on_submit():  # Validate the form for CSRF etc.
        # Extract form information
        name = form.name.data
        mobile_no = form.mobile_no.data
        email = form.email.data
        add_response = db_utils.add_contact({  # Add to database
            "name": name,
            "mobile_no": mobile_no,
            "email": email
        })
        if add_response:
            flash("Added!")  # Show acknowledge to user
            # Redirect to list_contacts page
            return redirect(url_for("list_contacts"))
        else:
            flash("Error occured while adding contact. Try Again!")

    return render_template('add_contact.html', form=form)

# Delete Channel from the database
@app.route('/delete/<contact_id>/', methods=["GET"])
def delete_contact(contact_id):
    db_utils.delete_contact(contact_id)
    return redirect(url_for('list_contacts'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
