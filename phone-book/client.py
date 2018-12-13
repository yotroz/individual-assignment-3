#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:30:27 2018

@author: yotroz
"""

#%%


import requests

def get_phonebook_client(): 
    request = requests.get('http://127.0.0.1:5000/phonebook')
    
    return request.json() 


def add_contact_client_post(phone, name): 
    request = requests.post('http://127.0.0.1:5000/add-contact/{}/{}'.format(phone, name))
    
    return request.json()


def get_phone_by_name_client(name): 
    request = requests.get('http://127.0.0.1:5000/get-phone/{}'.format(name))
    
    return request.json()


def delete_contact_by_name_client(name): 
    request = requests.delete('http://127.0.0.1:5000/delete-contact/{}'.format(name))
    
    return request.json()

def update_contact_client(name, phone):
    request = requests.put('http://127.0.0.1:5000/update-contact/{}/{}'.format(name, phone))
    
    return request.json()
    

    