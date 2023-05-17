import requests


resp = requests.get("http://127.0.0.1:5000/api/patient/")
print(resp.json())


#########---order queries---##############

def orders_list():
    pass  # SELECT * FROM orders


def order_barcode():
    pass # SELECT * FROM orders WHERE barcode == "{barcode}"

def orders_by_patient():
    pass #SELECT id FROM patients WHERE name == {name}
    # SELECT * FROM orders WHERE patient_id == {id}

def closed_order():
    pass

def not_closed_order():
    pass

def new_order():
    pass  # INSERT INTO orders


def update_order():
    pass  # UPDATE


#########---END order queries---##############


### SAMPLE FUNCTION ###

def SAMPLE():
    try:
        with connection:
            query = ""
            with cursor:
                cursor.execute(query)
    except Error as e:
        print("An error occured: ", e)
    finally:
        cursor.close()
        connection.close()
    return ""
