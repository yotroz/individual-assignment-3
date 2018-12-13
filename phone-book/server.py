#%%

from flask import Flask, jsonify


server = Flask("Online Phonebook Running")

phonebook = {"pepe": "53535353",
             "lukas": "8888888",
             "agata": "7777777",
             "octavio": "88888",
             "david": "99999"}


@server.route("/phonebook")
def get_phonebook():
    return jsonify(phonebook)

    
@server.route("/add-contact/<phone>/<name>", methods=["POST"])
def add_contact_post(phone, name): 
    

    if name not in phonebook: 
        
        phonebook.update({name:phone})
        return jsonify("you have added " + name + " with the phone number: " + phone)
    
    else: 
        return jsonify("you have already added " + name)


@server.route("/get-phone/<name>")
def get_phone_by_name(name): 
    
    if name in phonebook: 
        return jsonify(name + "'s  phone number is " + phonebook[name])
    
    else: 
        return jsonify("there is no " + name + " in your phonebook")


@server.route("/delete-contact/<name>", methods=["DELETE"])
def delete_contact_by_name(name):   
    if name not in phonebook: 
        
        return jsonify("there is no " + name + " in your phonebook")
    else:
        del phonebook[name]
        
        return jsonify(name + " has been deleted from your phonebook :( ")         


                  
@server.route("/update-contact/<name>/<phone>", methods=["PUT"])
def update_contact(name, phone): 
    
    if name not in phonebook: 
        return jsonify("There is no one in you phonebook with that name")
    
    else: 
        phonebook[name] = phone
        return jsonify(name + " has been updated to: " + phone)
    
        
    
server.run()
