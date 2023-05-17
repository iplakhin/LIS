from flask import Flask, render_template, request, redirect
from mysql.connector import connect, Error
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()

connection = connect(host="localhost", user="root", password="derparol", database="patients")
cursor = connection.cursor()

######################################## Class dictionary
class create_dict(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value
########################################################

#########---patient queries---##############

def all_patients():
    mydict = create_dict()
    try:
        with connection:
            query = "SELECT p_name, birthday, gender, ssn FROM patients.patients"
            with cursor:
                cursor.execute(query)
                patients = cursor.fetchall()
                for i in range(len(patients)):
                    for patient in patients:
                        mydict.add(i, (
                        {"name": patient[0], "birthday": str(patient[1]), "gender": patient[2], "ssn": patient[3]}))
    except Error as e:
        print("An error occured: ", e)
    finally:
        cursor.close()
        connection.close()
    return mydict

def patient_ssn():
    pass #"SELECT * FROM patients WHERE ssn = {ssn}"

def new_patient():
    try:
        with connection:
            query = "INSERT INTO patients.patients(p_name, birthday, gender, ssn) VALUES (Ivan, 1991-07-16, 1, 0987654321)"
            with cursor:
                cursor.execute(query)
    except Error as e:
        print("An error occured: ", e)
    finally:
        cursor.close()
        connection.close()
    return ""

def update_patient():
    pass # UPDATE

#########---END patient queries---##############

class Patient(Resource):
    def get(self):
        return all_patients()

    def post(self):
        return new_patient()

api.add_resource(Patient, f"/api/patient/")
api.init_app(app)




if __name__ == '__main__':
    app.run(debug=True)
