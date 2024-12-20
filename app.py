from flask import Flask, render_template, request, redirect, url_for, jsonify
import backend
from logger import logging

obj = backend.InfocomOrg()

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    """
    This function is used to load the login page

    :return: Redirecting to index.html
    """
    logging.info('Homepage Loaded')
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    """
    This function takes the username and password, verifies the user credentials and login to the specific user page.

    :return: Redirecting to the user homepage based on the role. Ex: Admin, HR, PR, SE, General
             OR error page if the user is not found
    """

    data = request.get_json()

    username = data.get('username')  # Use data.get() to avoid KeyError if the key is missing
    password = data.get('password')

    flag = obj.check_admin(username, password)

    if flag == "Admin":
        # return render_template('admin.html')
        redirect_url = url_for('admin', username=username)
        logging.info('Admin ' + username.upper() + ' Logged In')
        return jsonify({'redirect_url': redirect_url})
    elif flag == "HR":
        # return render_template('admin.html')
        redirect_url = url_for('hr', username=username)
        logging.info('HR User ' + username.upper() + ' Logged In')
        return jsonify({'redirect_url': redirect_url})
    elif flag == "PR":
        # return render_template('admin.html')
        redirect_url = url_for('pr', username=username)
        logging.info('PR User ' + username.upper() + ' Logged In')
        return jsonify({'redirect_url': redirect_url})
    elif flag == "SE":
        # return render_template('admin.html')
        redirect_url = url_for('se', username=username)
        logging.info('SE User ' + username.upper() + ' Logged In')
        return jsonify({'redirect_url': redirect_url})
    elif flag == "GENERAL":
        # return render_template('admin.html')
        redirect_url = url_for('general', username=username)
        logging.info('General User ' + username.upper() + ' Logged In')
        return jsonify({'redirect_url': redirect_url})
    else:
        redirect_url = url_for('error')
        logging.info('Error While Logging In, User ' + username.upper() + ' Not Found')
        return jsonify({'redirect_url': redirect_url})


@app.route('/error')
def error():
    """
    This function goes to the error page if the user is not found.

    :return: Redirecting to error.html page
    """

    return render_template('error.html')


@app.route('/admin/<username>')
def admin(username):
    """
    This function goes to the admin page if the user role is Admin.

    :return: Redirecting to admin.html page
    """

    return render_template('admin.html', username=username)


@app.route('/se/<username>')
def se(username):
    """
    This function goes to the se page if the user role is SE.

    :return: Redirecting to se.html page
    """
    return render_template('se.html', username=username)


@app.route('/hr/<username>')
def hr(username):
    """
    This function goes to the hr page if the user role is HR.

    :return: Redirecting to hr.html page
    """
    return render_template('hr.html', username=username)


@app.route('/pr/<username>')
def pr(username):
    """
    This function goes to the pr page if the user role is PR.

    :return: Redirecting to pr.html page
    """
    return render_template('pr.html', username=username)


@app.route('/general/<username>')
def general(username):
    """
    This function goes to the general page if the user role is General.

    :return: Redirecting to general.html page
    """
    return render_template('general.html', username=username)


@app.route('/new_user')
def new_user():
    """
    This function purpose to go to new_user page to add the details.

    :return: Redirects to new_user.html
    """

    return render_template('new_user.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    This function purpose is to add a new user or update the existing user.

    :return: message saying success or fail.
    """
    logging.info('Adding New User Named ' + request.form['username'])
    message = obj.add_or_update_user(request.form, logging)
    return jsonify({"Status": message})


@app.route('/get_records_count')
def get_records_count():
    """
    This function purpose is to get the records count ready from all the tables for the admin to view them.

    :return: Counts from all the tables
    """

    # Assume get_hr_records_count() is a function that returns the count of HR records
    count = obj.get_records_count()
    return jsonify(count=count)


@app.route('/logout', methods=['POST'])
def logout():
    """
    This function is to log out from the user page.

    :return: Redirects to the index.html which is a login page.
    """

    logging.info('User Logged Out')
    redirect_url = url_for('index')
    return jsonify({'redirect_url': redirect_url})


@app.route('/get_hr_records', methods=['GET'])
def get_hr_records():
    """
    This function purpose is to get the records count ready from the accessible tables for the HR to view them.


    :return: dictionary containing hr records
    """
    logging.info('Getting HR Records')
    # Fetch HR records from your database or service
    hr_records = obj.get_hr_records()
    return jsonify(hr_records)


@app.route('/get_se_records', methods=['GET'])
def get_se_records():
    """
    This function purpose is to get the records count ready from the accessible tables for the SE to view them.


    :return: dictionary containing se records
    """
    logging.info('Getting SE Records')
    # Fetch HR records from your database or service
    se_records = obj.get_se_records()
    return jsonify(se_records)


@app.route('/get_pr_records', methods=['GET'])
def get_pr_records():
    """
    This function purpose is to get the records count ready from the accessible tables for the PR to view them.


    :return: dictionary containing pr records
    """
    logging.info('Getting PR Records')
    # Fetch HR records from your database or service
    pr_records = obj.get_pr_records()
    return jsonify(pr_records)


@app.route('/get_emphr_records', methods=['GET'])
def get_emp_hr_records():
    """
    This function purpose is to get the records count ready from the accessible tables for the EMP HR to view them.


    :return: dictionary containing emp hr records
    """
    logging.info('Getting EMP HR Records')
    # Fetch HR records from your database or service
    hr_records = obj.get_emp_hr_records()
    return jsonify(hr_records)


@app.route('/get_empse_records', methods=['GET'])
def get_emp_se_records():
    """
    This function purpose is to get the records count ready from the accessible tables for the EMP SE to view them.


    :return: dictionary containing emp se records
    """
    logging.info('Getting EMP SE Records')
    # Fetch HR records from your database or service
    emp_se_records = obj.get_emp_se_records()
    return jsonify(emp_se_records)


@app.route('/get_emppr_records', methods=['GET'])
def get_emp_pr_records():
    """
    This function purpose is to get the records count ready from the accessible tables for the EMP PR to view them.


    :return: dictionary containing emp pr records
    """
    logging.info('Getting EMP PR Records')
    # Fetch HR records from your database or service
    emp_pr_records = obj.get_emp_pr_records()
    return jsonify(emp_pr_records)


@app.route('/get_usernames', methods=['GET'])
def get_usernames():
    """
    Retrieves list of usernames.

    :return: dictionary containing list of usernames
    """
    logging.info('Getting Users List')
    # Fetch HR records from your database or service
    records = obj.get_usernames()
    return jsonify(records)


@app.route('/delete', methods=['POST'])
def delete():
    """
    This function deletes a specific record from specific table

    :return:  A message of success or failure
    """

    logging.info('Deleting ' + request.json['username'].upper() + ' Record')
    # Fetch HR records from your database or service
    records = obj.delete(request.json)
    return jsonify(records)


@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    """
    Redirects to the update user page.

    :return: returns URL
    """
    # Assuming `get_user_by_id` is a function that fetches user data from your database
    if 'rt' not in request.json:
        username = request.json.get('username')
        role = request.json.get('role')
    else:
        username = request.json.get('uid')
        role = request.json.get('rt')

    redirect_url = url_for('get_update_user_page', username=username, role=role)
    return jsonify({'redirect_url': redirect_url})


@app.route('/update_user_page/<username>/<role>')
def get_update_user_page(username, role):
    """
    Loads the update user page based on username and role.

    :param username:
    :param role:
    :return: HTML template based on the role
    """
    if not username.startswith("INFO"):
        return render_template('update_user.html', username=username, role=role)
    else:
        details = obj.get_data(username, role)
        if role == "empse":
            return render_template('update_details.html', username=username, role=role, address=details[0]['address'],
                                   phone_num=details[0]['phone_no'], salary=details[0]['salary'],
                                   bg=details[0]['bloodgroup'])
        elif role == "pr":
            return render_template('update_pr_data.html', username=username, role=role,
                                   firstname=details[0]['firstname'],
                                   lastname=details[0]['lastname'], dob=details[0]['dob'])
        elif role == "emppr":
            return render_template('update_emp_pr_data.html', username=username, role=role,
                                   address=details[0]['address'],
                                   phone_num=details[0]['phone_no'], salary=details[0]['salary'])
        elif role == "emphr":
            return render_template('update_emp_hr_data.html', username=username, role=role,
                                   address=details[0]['address'],
                                   phone_num=details[0]['phone_no'], user_rank=details[0]['user_rank'])
        elif role == "hr":
            return render_template('update_hr_data.html', username=username, role=role, name=details[0]['name'],
                                   department=details[0]['department'], supervisor=details[0]['supervisor'])
        else:
            return render_template('update_se_data.html', username=username, role=role, name=details[0]['name'],
                                   pn=details[0]['projectname'], sp=details[0]['supervisor'],
                                   dl=details[0]['deadline'])


@app.route('/change_role', methods=['POST'])
def change_role():
    """
    This function purpose is to change the user role which is only allowed by the admin.

    :return: A message saying the operation successful or not.
    """

    logging.info('Changed a user role to ' + request.form.to_dict()['role'] + ' for the user ' + request.form.to_dict()[
        'username'])
    message = obj.change_role(request.form.to_dict(), logging)

    return jsonify({"Status": message})


@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    """
    Redirects to add data page.


    :return: Method to redirect.
    """
    username = request.json.get('username')
    role = request.json.get('role')

    redirect_url = url_for('add_user_data', username=username, role=role)
    return jsonify({'redirect_url': redirect_url})


@app.route('/user_details/<username>/<role>')
def add_user_data(username, role):
    """
    Loads the add user data page.

    :param username:
    :param role:
    :return: HTML Page: add_user_data.html
    """
    return render_template('add_user_data.html', username=username, role=role)


@app.route('/add_additional_details', methods=['POST'])
def add_additional_details():
    """
    Adds additional user details.

    :return: message saying success or fail.
    """
    logging.info('Adding additional details')
    message = obj.add_additional_details(request.form.to_dict(), logging)

    return jsonify({"Status": message})


@app.route('/update_se_details', methods=['POST'])
def update_se_details():
    """
    Updates all user details.

    :return: message saying success or fail.
    """
    logging.info('Updating the details for a provided user.')

    if "table" in request.form.to_dict() and request.form.to_dict()['table'] == "empse":

        message = obj.update_emp_se_details(request.form.to_dict(), logging)

    elif "table" in request.form.to_dict() and request.form.to_dict()['table'] == "pr":
        message = obj.update_pr_data_details(request.form.to_dict(), logging)
    elif "table" in request.form.to_dict() and request.form.to_dict()['table'] == "emppr":
        message = obj.update_emp_pr_details(request.form.to_dict(), logging)
    elif "table" in request.form.to_dict() and request.form.to_dict()['table'] == "hr":
        message = obj.update_hr_data_details(request.form.to_dict(), logging)
    elif "table" in request.form.to_dict() and request.form.to_dict()['table'] == "emphr":
        message = obj.update_emp_hr_details(request.form.to_dict(), logging)
    else:
        message = obj.update_se_data_details(request.form.to_dict(), logging)

    return jsonify({"Status": message})


if __name__ == '__main__':
    app.run(host='localhost', port=3333, debug=False)
