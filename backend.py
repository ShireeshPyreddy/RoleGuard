import mysql.connector
from mysql.connector import Error
from datetime import datetime


class InfocomOrg:
    """
    This class will handle the backend of the application which performs operations like add, update, delete and
    get records to view.
    """

    def __init__(self):
        """
        Initializes the database connection using mysql.connector. The connection parameters include the host name,
        database name, user_name, and user password. These parameters are set to connect to a local MySQL server with
        the 'organization' database using the 'root' user and 'root' password. A connection object is created and
        stored in self.connection.
        """
        self.host_name = 'localhost'
        self.db_name = 'organization'
        self.user_name = 'root'
        self.user_password = 'root'

        self.connection = mysql.connector.connect(
            host=self.host_name,
            user=self.user_name,
            passwd=self.user_password,
            database=self.db_name
        )

    def execute_query(self, query, flag=False):
        """
        Executes a given SQL query on the connected database and fetches all the resulting records. Optionally formats
        the results as a list of dictionaries if the 'flag' parameter is set to True, with each dictionary representing
        a row and keys as column names.

        :param query: The SQL query string to be executed.
        :param flag: If set to True, the result is formatted as a list of dictionaries. Default is False, which returns
                     a list of tuples.
        :return: A list of tuples representing the fetched rows from the database. If 'flag' is True, returns a list of
                 dictionaries with keys corresponding to column names.
        """
        result = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            if flag is True:
                column_names = cursor.column_names
                result = [dict(zip(column_names, row)) for row in result]

            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

        return result

    def add_additional_details(self, user_details, logger):
        """
        Adds additional user details into the database based on the user role. Depending on the role ('HR', 'SE', or 'PR'),
        different sets of data are inserted into specific tables. The function checks for existing records before inserting
        new data to avoid duplicates. The process involves generating unique IDs for new records, validating and inserting
        data into respective tables, and logging the outcome.

        :param user_details: A dictionary containing the details of the user such as name, department, role, etc.
        :param logger: Logger instance for logging messages regarding the process outcomes.
        :return: A message indicating the result of the operation, whether it was successful, if duplicates exist, or
                 if an error occurred.
        """
        if user_details['role'].lower() == 'hr':
            message = ""

            check_records = "select * from emp_hr"
            records_check = self.execute_query(check_records)

            if records_check:
                get_latest_record = "select id from emp_hr order by id"
                res = self.execute_query(get_latest_record, flag=True)
                UID = res[-1]['id'][:-1] + str(int(res[-1]['id'][-1]) + 1)
                print("get_latest_record", res, UID)
            else:
                UID = "INFOCOMHR1"

            name = user_details['name']
            department = user_details['department']
            supervisor = user_details['supervisor']
            address = user_details['address']
            phone_no = user_details['phone_no']
            rank = user_details['rank']

            check_hr_data = "select * from hr_data where name = '" + name + "' and department = '" + department + "'"
            res = self.execute_query(check_hr_data)
            flag, flag2 = False, False

            if not res:
                user_data_insert_query = f"INSERT INTO hr_data (id, name, department, supervisor) VALUES ('{UID}', '{name}', '{department}', '{supervisor}')"
                self.execute_query(user_data_insert_query)
                print("New User Data Added")
                message = "New HR User Details Added Successfully"
                flag = True

            check_emp_hr = "select * from emp_hr where phone_no = '" + phone_no + "'"
            res = self.execute_query(check_emp_hr)
            if not res:
                user_data_insert_query = f"INSERT INTO emp_hr (id, address, phone_no, user_rank) VALUES ('{UID}', '{address}', '{phone_no}', '{rank}')"
                self.execute_query(user_data_insert_query)
                print("New User Data Added")

                message = "New HR User Details Added Successfully"
                flag2 = True

            if flag is False and flag2 is False:
                message = "HR User Details Already Exists"

        elif user_details['role'].lower() == 'se':
            message = ""

            check_records = "select * from emp_se"
            records_check = self.execute_query(check_records)

            if records_check:
                get_latest_record = "select id from emp_se order by id"
                res = self.execute_query(get_latest_record, flag=True)
                UID = res[-1]['id'][:-1] + str(int(res[-1]['id'][-1]) + 1)
                print("get_latest_record", res, UID)
            else:
                UID = "INFOCOMSE1"

            name = user_details['nameOne']
            projectname = user_details['projectname']
            supervisor = user_details['supervisorOne']
            deadline = user_details['deadline']
            deadline = datetime.strptime(deadline, "%m/%d/%Y")
            address = user_details['addressOne']
            phone_no = user_details['phone_no_one']
            salary = user_details['salary']

            if salary.strip() == "":
                salary = -1

            blood_group = user_details['blood_group']

            check_se_data = "select * from se_data where projectname = '" + projectname + "'"
            res = self.execute_query(check_se_data)
            flag, flag2 = False, False

            if not res:
                user_data_insert_query = f"INSERT INTO se_data (id, name, projectname, supervisor, deadline) VALUES ('{UID}', '{name}', '{projectname}', '{supervisor}', '{deadline}')"
                self.execute_query(user_data_insert_query)
                print("New User Data Added")
                message = "New SE User Details Added Successfully"
                flag = True

            check_emp_se = "select * from emp_se where phone_no = '" + phone_no + "'"
            res = self.execute_query(check_emp_se)
            if not res:
                user_data_insert_query = f"INSERT INTO emp_se (id, address, phone_no, salary, bloodgroup) VALUES ('{UID}', '{address}', '{phone_no}', '{salary}', '{blood_group}')"
                self.execute_query(user_data_insert_query)
                print("New User Data Added")

                message = "New SE User Details Added Successfully"
                flag2 = True

            if flag is False and flag2 is False:
                message = "SE User Details Already Exists"

        elif user_details['role'].lower() == 'pr':
            message = ""

            check_records = "select * from emp_pr"
            records_check = self.execute_query(check_records)

            if records_check:
                get_latest_record = "select id from emp_pr order by id"
                res = self.execute_query(get_latest_record, flag=True)
                UID = res[-1]['id'][:-1] + str(int(res[-1]['id'][-1]) + 1)
                print("get_latest_record", res, UID)
            else:
                UID = "INFOCOMPR1"

            firstname = user_details['firstname']
            lastname = user_details['lastname']
            dob = user_details['dob']
            dob = datetime.strptime(dob, "%m/%d/%Y")
            address = user_details['addressTwo']
            phone_no = user_details['phone_no_two']
            salary = user_details['salaryOne']

            if salary.strip() == "":
                salary = -1

            check_pr_data = "select * from pr_data where firstname = '" + firstname + "' and lastname = '" + lastname + "'"
            res = self.execute_query(check_pr_data)
            flag, flag2 = False, False

            if not res:
                user_data_insert_query = f"INSERT INTO pr_data (id, firstname, lastname, dob) VALUES ('{UID}', '{firstname}', '{lastname}', '{dob}')"
                self.execute_query(user_data_insert_query)
                print("New User Data Added")
                message = "New PR User Details Added Successfully"
                flag = True

            check_emp_pr = "select * from emp_pr where phone_no = '" + phone_no + "'"
            res = self.execute_query(check_emp_pr)
            if not res:
                user_data_insert_query = f"INSERT INTO emp_pr (id, address, phone_no, salary) VALUES ('{UID}', '{address}', '{phone_no}', '{salary}')"
                self.execute_query(user_data_insert_query)
                print("New User Data Added")

                message = "New PR User Details Added Successfully"
                flag2 = True

            if flag is False and flag2 is False:
                message = "PR User Details Already Exists"
        else:
            message = "Error In Adding The User"

        logger.info(message)
        return message

    def add_or_update_user(self, user_details, logger):
        """
        Adds a new user or updates an existing user's details in the 'login_credential' table of the database. It checks
        for the existence of a user with the given username. If the user exists, it logs a message indicating that the user
        is already created. If the user does not exist, it inserts a new record with the provided username, password, and
        role into the table and logs a message indicating a new user has been added.

        :param user_details: A dictionary containing the user's details, including 'username', 'role', 'pass', and 'name'.
        :param logger: Logger instance for logging the outcomes of the operation.
        :return: None
        """
        try:
            username = user_details['username']
            role = user_details['role'].upper()
            password = user_details['pass']
            name = user_details['name']

            user_check_query = f"SELECT * FROM login_credential WHERE username = '{username}'"
            res = self.execute_query(user_check_query)
            if res:
                print("User Found")
                message = "User Already Created"
            else:
                user_insert_query = f"INSERT INTO login_credential (username, password, role) VALUES ('{username}', '{password}', '{role}')"
                self.execute_query(user_insert_query)
                print("New User Added")
                message = "New User Added"

            return message
        except Exception as e:
            message = "Error Encountered While Adding New User"

        logger.info(message)

    def check_admin(self, username, password):
        """
        Checks if the given username and password combination exists in the 'login_credential' table, and returns the role
        of the last matching entry if found. This function is particularly used to verify if a user is an administrator or
        has some specific role based on the login credentials provided.

        :param username: The username to check in the 'login_credential' table.
        :param password: The corresponding password for the username to validate.
        :return: The role of the user if the username and password match an entry in the database; otherwise, an empty
                 string is returned to indicate no match found.
        """
        query = "select * from login_credential where username = '" + username + "' and password = '" + password + "'"
        res = self.execute_query(query)
        print("res", res)
        if res:
            return res[-1][-1]
        else:
            return ""

    def get_records_count(self):
        """
        Retrieves the count of records from six different tables: 'hr_data', 'pr_data', 'se_data', 'emp_hr', 'emp_pr',
        and 'emp_se'. Each table represents a different category of employees or related data in the organization. This
        function executes a COUNT query for each table and stores the result in a dictionary where keys are the table
        names and values are the respective counts.

        :return: A dictionary with keys as table names ('hr', 'pr', 'se', 'emp_hr', 'emp_pr', 'emp_se') and values as the
                 count of records in each table. This provides a quick summary of the data volume in each category.
        """

        counts = {"hr": 0, "pr": 0, "se": 0, "emp_hr": 0, "emp_pr": 0, "emp_se": 0}
        query = " select count(*) from hr_data"
        counts["hr"] = self.execute_query(query)[0][0]
        query = " select count(*) from pr_data"
        counts["pr"] = self.execute_query(query)[0][0]
        query = " select count(*) from se_data"
        counts["se"] = self.execute_query(query)[0][0]
        query = " select count(*) from emp_hr"
        counts["emp_hr"] = self.execute_query(query)[0][0]
        query = " select count(*) from emp_pr"
        counts["emp_pr"] = self.execute_query(query)[0][0]
        query = " select count(*) from emp_se"
        counts["emp_se"] = self.execute_query(query)[0][0]

        return counts

    def get_hr_records(self):
        """
        Fetches all records from the 'hr_data' table, which includes information specific to HR employees. The results
        are formatted as a list of dictionaries, each representing one HR record with keys corresponding to the table's
        column names.

        :return: A list of dictionaries each representing an HR record from 'hr_data', or an empty dictionary if no
                 records are found.
        """
        query = "select * from hr_data"
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    def get_se_records(self):
        """
        Retrieves all records from the 'se_data' table, containing details on Software Engineering (SE) employees.
        The results are formatted as a list of dictionaries, with each dictionary including keys for the column names.

        :return: A list of dictionaries each representing an SE record from 'se_data', or an empty dictionary if there
                 are no records.
        """
        query = "select * from se_data"
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    def get_pr_records(self):
        """
        Gathers all records from the 'pr_data' table, which holds information on Public Relations (PR) employees. The
        data is returned as a list of dictionaries, where each dictionary represents a PR record, including column names
        as keys.

        :return: A list of dictionaries each representing a PR record from 'pr_data', or an empty dictionary if no records
                 exist.
        """
        query = "select * from pr_data"
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    def get_emp_hr_records(self):
        """
        Retrieves all records from the 'emp_hr' table, containing details of HR (Human Resources) employees. The data is
        returned as a list of dictionaries, with each dictionary representing one employee record, including column names
        as keys.

        :return: A list of dictionaries each representing an HR employee record from 'emp_hr', or an empty dictionary if
                 there are no records.
        """
        query = "select * from emp_hr"
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    def get_emp_se_records(self):
        """
        Retrieves all records from the 'emp_se' table, which holds information on Software Engineering (SE) employees.
        The results are formatted as a list of dictionaries, where each dictionary corresponds to one employee record,
        including keys for each column in the table.

        :return: A list of dictionaries with each dictionary representing an SE employee record from 'emp_se', or an
                 empty dictionary if no records exist.
        """
        query = "select * from emp_se"
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    def get_emp_pr_records(self):
        """
        Fetches all records from the 'emp_pr' table, which contains details about Public Relations (PR) employees.
        The result is formatted as a list of dictionaries for easier data manipulation, with each dictionary representing
        a single record and containing keys corresponding to the table's column names.

        :return: A list of dictionaries, each representing a PR employee record from 'emp_pr', or an empty dictionary if
                 no records are found.
        """
        query = "select * from emp_pr"
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    def get_usernames(self):
        """
        Retrieves all usernames and their associated roles from the 'login_credential' table. It formats the results
        as a list of dictionaries, with each dictionary containing 'username' and 'role' keys.

        :return: A list of dictionaries with 'username' and 'role' for each record in 'login_credential', or an empty
                 dictionary if no records are found.
        """
        query = "select username, role from login_credential"
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    @staticmethod
    def get_table(rt):
        """
        Determines the database table name based on a given role type abbreviation ('rt'). Maps common role type
        abbreviations to their corresponding database table names.

        :param rt: A string representing the role type abbreviation (e.g., 'empse', 'se', 'hr', 'emphr', 'pr', 'emppr').
        :return: The corresponding database table name as a string. If the role type does not match any predefined
                 abbreviations, an empty string is returned.
        """
        if rt == "empse":
            table = "emp_se"
        elif rt == "se":
            table = "se_data"
        elif rt == "hr":
            table = "hr_data"
        elif rt == "emphr":
            table = "emp_hr"
        elif rt == "pr":
            table = "pr_data"
        elif rt == "emppr":
            table = "emp_pr"
        else:
            table = ""

        return table

    def delete(self, details):
        """
        Deletes a record from either the 'login_credential' table or another specified table based on the role type ('rt')
        provided in 'details'. If 'rt' is not specified, it targets 'login_credential' using 'username' and 'role' from
        'details'. Otherwise, it uses 'rt' to determine the correct table and 'uid' for the specific record.

        :param details: Dictionary containing necessary information for deletion, including 'username', 'role', and
                        optionally 'rt' for role type and 'uid' for user ID in other tables.
        :return: The result of the delete operation if successful; an empty dictionary if no record was deleted.
        """
        if 'rt' not in details:
            query = "delete from login_credential where username = '" + details['username'] + "' and role = '" + \
                    details[
                        'role'] + "'"
        else:
            table = self.get_table(details['rt'])
            query = "delete from " + table + " where id= '" + details['uid'] + "'"
        res = self.execute_query(query, flag=True)
        if res:
            return res
        else:
            return {}

    def update_user(self):
        """
        Retrieves all user records from the 'login_credential' table. It executes a SELECT query to fetch all existing
        user data, with the option to format the results as a list of dictionaries for easier data manipulation and
        access.

        :return: A list of dictionaries, each representing a user record with keys as column names if records exist;
                 an empty dictionary is returned if there are no records.
        """
        query = "select * from login_credential"
        print(query)
        res = self.execute_query(query, flag=True)
        print("res", res)
        if res:
            return res
        else:
            return {}

    def change_role(self, details, logger):
        """
        Changes the role of a user in the 'login_credential' table based on provided details. It first checks for the
        existence of a record with the given username. If found, it updates the role to the new one specified in 'details'.
        Logs the outcome.

        :param details: Dictionary containing 'username' and the new 'role' to update to.
        :param logger: Logger for documenting the change.
        :return: Message indicating the success of the role update, or failure if the record was not found or an error occurred.
        """
        message = ""
        try:
            check_record = "select * from login_credential where username='" + details['username'] + "'"
            print(check_record)
            res = self.execute_query(check_record)
            if res:
                update_statement = "update login_credential set role = '" + details[
                    'role'].upper() + "' where username = '" + details['username'] + "'"
                print(update_statement)
                self.execute_query(update_statement)
                message = "Role Updated Successfully"
                print("Message", message)
            else:
                message = "Record Not Found"
        except Exception as e:
            print("ERROR", e)
            message = "Error Occurred While Updating The Record"

        logger.info(message)
        return message

    def get_data(self, uid, rt):
        """
        Fetches data for a given user ID (uid) from the appropriate table determined by the role type (rt). The function
        first determines the correct table to query from based on the role type, then constructs and executes a SQL
        query to fetch all records matching the given user ID.

        :param uid: The unique identifier for the user whose data is to be retrieved.
        :param rt: The role type that determines which table to fetch the data from.
        :return: A list of dictionaries representing the retrieved records, with keys as column names.
        """
        table = self.get_table(rt)
        query = "select * from " + table + " where id= '" + uid + "'"
        print("query get_data", query)
        res = self.execute_query(query, flag=True)
        return res

    def update_emp_se_details(self, user_details, logger):
        """
        Updates details for a Software Engineer (SE) employee in 'emp_se'. It checks if an SE record exists for the
        provided 'username' (UID), then updates 'address', 'phone_no', 'salary', and 'blood_group'. Updates are logged.

        :param user_details: Dictionary with SE's updated details.
        :param logger: Logger for update logging.
        :return: Message indicating the update outcome.
        """
        message = ""
        uid = user_details['username']
        address = user_details['addressOne']
        phone_no = user_details['phone_no_one']
        salary = user_details['salary']
        blood_group = user_details['blood_group']

        # check_se_data = "select * from se_data where id = '" + uid + "'"
        # res = self.execute_query(check_se_data)
        # flag, flag2 = False, False
        #
        # if res:
        #     # user_data_insert_query = f"INSERT INTO se_data (id, name, projectname, supervisor, deadline) VALUES ('{UID}', '{name}', '{projectname}', '{supervisor}', '{deadline}')"
        #
        #     user_data_update_query = "update se_data set name = '" + name + ", projectname = '"+projectname+", supervisor='"+supervisor+", deadline='"+deadline+" where id = '"+uid+"'"
        #     # self.execute_query(user_data_update_query)
        #     print("New User Data Added")
        #     message = "SE User Details Updated Successfully"
        #     flag = True

        check_emp_se = "select * from emp_se where id = '" + uid + "'"
        res = self.execute_query(check_emp_se)

        if res:
            user_data_update_query = "update emp_se set address = '" + address + "', phone_no = '" + phone_no + "', salary = '" + salary + "', bloodgroup = '" + blood_group + "' where id = '" + uid + "'"
            print("user update query", user_data_update_query)
            self.execute_query(user_data_update_query)
            print("New User Data Added")
            message = "EMP SE User Details Updated Successfully"
            logger.info(message)

        return message

    def update_se_data_details(self, user_details, logger):
        """
        Updates software engineer (SE) details in 'se_data' based on 'user_details'. Checks for an existing SE record
        using 'username' (UID), then updates 'name', 'projectname', 'supervisor', and 'deadline'. The update is logged.

        :param user_details: Dictionary containing SE user's updated data.
        :param logger: Logger for recording update actions.
        :return: Notification message of the update result.
        """
        message = ""
        uid = user_details['username']
        name = user_details['nameOne']
        project_name = user_details['projectname']
        supervisor = user_details['supervisorOne']
        deadline = user_details['deadline']

        check_se_data = "select * from se_data where id = '" + uid + "'"
        res = self.execute_query(check_se_data)

        if res:
            user_data_update_query = "update se_data set name = '" + name + "', projectname = '" + project_name + "', supervisor='" + supervisor + "', deadline='" + deadline + "' where id = '" + uid + "'"
            self.execute_query(user_data_update_query)
            print("New User Data Added")
            message = "SE User Details Updated Successfully"
            logger.info(message)
            flag = True

        return message

    def update_pr_data_details(self, user_details, logger):
        """
        Updates PR employee data in 'pr_data' table with given 'user_details'. Checks if record exists for 'username'
        (UID), then updates 'firstname', 'lastname', and 'dob'. Logs the update process.

        :param user_details: Dictionary with PR user's updated information.
        :param logger: Logger for update notifications.
        :return: Message regarding update status.
        """
        message = ""
        uid = user_details['username']
        f_name = user_details['firstname']
        l_name = user_details['lastname']

        dob = user_details['dob']
        # dob = datetime.strptime(dob, "%m/%d/%Y")

        check_pr_data = "select * from pr_data where id = '" + uid + "'"
        res = self.execute_query(check_pr_data)

        if res:
            user_data_update_query = "update pr_data set firstname = '" + f_name + "', lastname = '" + l_name + "', dob='" + dob + "' where id = '" + uid + "'"
            self.execute_query(user_data_update_query)
            print("New User Data Added")
            message = "PR User Details Updated Successfully"
            logger.info(message)
            flag = True

        return message

    def update_hr_data_details(self, user_details, logger):
        """
        Updates HR data in 'hr_data' with provided 'user_details'. Checks for an existing record with the given 'username'
        (UID), then updates 'name', 'department', and 'supervisor'. Outcome is logged.

        :param user_details: Dictionary containing updated HR details.
        :param logger: Logger for documenting the update result.
        :return: Update outcome message.
        """
        message = ""
        uid = user_details['username']
        name = user_details['nameOne']
        dept = user_details['dept']
        sup = user_details['sup']

        # dob = user_details['dob']
        # dob = datetime.strptime(dob, "%m/%d/%Y")

        check_hr_data = "select * from hr_data where id = '" + uid + "'"
        res = self.execute_query(check_hr_data)

        if res:
            user_data_update_query = "update hr_data set name = '" + name + "', department = '" + dept + "', supervisor='" + sup + "' where id = '" + uid + "'"
            self.execute_query(user_data_update_query)
            print("New User Data Added")
            message = "HR User Details Updated Successfully"
            logger.info(message)
            flag = True

        return message

    def update_emp_pr_details(self, user_details, logger):
        """
        Updates PR employee details in 'emp_pr' using 'user_details'. Verifies the presence of a record with the specified
        'username' (UID), then updates 'address', 'phone_num', and 'salary'. Logs the result.

        :param user_details: Dictionary with PR user's updated details.
        :param logger: Logger for result logging.
        :return: Result message.
        """
        message = ""
        uid = user_details['username']
        address = user_details['address']
        phone_num = user_details['phone_num']
        salary = user_details['salary']

        check_pr_data = "select * from emp_pr where id = '" + uid + "'"
        res = self.execute_query(check_pr_data)

        if res:
            user_data_update_query = "update emp_pr set address = '" + address + "', phone_no = '" + phone_num + "', salary='" + salary + "' where id = '" + uid + "'"
            self.execute_query(user_data_update_query)
            print("New User Data Added")
            message = "PR User Details Updated Successfully"
            logger.info(message)
            flag = True

        return message

    def update_emp_hr_details(self, user_details, logger):
        """
        Updates the details of an HR employee in the 'emp_hr' table based on the provided user details. It checks if a
        record with the specified username (treated as the unique ID in this context) exists in the table. If the record
        exists, it updates the address, phone number, and rank of the employee with the provided values.

        :param user_details: A dictionary containing the HR user's details to be updated, including 'username' (used as
                             unique ID), 'address', 'phone_num', and 'user_rank'.
        :param logger: Logger instance for logging the outcome of the update operation.
        :return: A message indicating the result of the update operation, specifically if the HR user's details were
                 successfully updated or not.
        """

        message = ""
        uid = user_details['username']
        address = user_details['address']
        phone_num = user_details['phone_num']
        u_rank = user_details['user_rank']

        check_hr_data = "select * from emp_hr where id = '" + uid + "'"
        res = self.execute_query(check_hr_data)

        if res:
            user_data_update_query = "update emp_hr set address = '" + address + "', phone_no = '" + phone_num + "', user_rank='" + u_rank + "' where id = '" + uid + "'"
            self.execute_query(user_data_update_query)
            print("New User Data Added")
            message = "HR User Details Updated Successfully"
            logger.info(message)
            flag = True

        return message

# if __name__ == '__main__':
#     obj = InfocomOrg()
#     obj.get_emp_pr_records_count()
#     obj.get_emp_se_records_count()
#     obj.get_emp_hr_records_count()
#     obj.get_pr_records_count()
#     obj.get_se_records_count()
#     obj.get_hr_records_count()
