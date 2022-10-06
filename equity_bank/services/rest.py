import frappe
import requests



@frappe.whitelist(allow_guest=True)
def validate_transaction(account, username, password):
    
    bill_information = {
        "amount": 100,
        "billName": "Rent",
        "billNumber": "HAV302",
        "billerCode": "247247",
        "createdOn": "2022-10-07",
        "currencyCode": "KES",
        "customerName": "Geoffrey Karani",
        "customerRefNumber": "HAV302",
        "description": "",
        "dueDate": "",
        "expiryDate": "",
        "type": 1
    }
    
    return bill_information
    

@frappe.whitelist(allow_guest=True, methods='POST')
def register_payment_notification(**kwargs):
    
    if kwargs['billNumber'] == "HAV1234":
        response = {
            "responseCode": "OK",
            "responseMessage": "SUCCESSFUL"
        }
    else:
        response = {
            "responseCode": "OK",
            "responseMessage": "DUPLICATETRANSACTION"
        }
        
    return response