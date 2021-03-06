import hashlib 
class Customer:
    password = 'defaultPassword'
    def __init__(self, local_uid, name, phoneNumber, address, email, shoppingCart):
        self.local_uid = hashlib.sha256(email.encode()) 
        self.name = name
        self.phoneNumber = phoneNumber
        self.address = address
        self.email = email
        self.shoppingCart = shoppingCart

    def __dict__():
        """ returns the all class attributes in dictionary format """
        returnDict = {'Local_uid' : self.local_uid, 'Name': self.name, 'PhoneNumber': self.phoneNumber, 'Address' : self.address, 'Email' : self.email, 'Shopping Cart' : self.shoppingCart}
        return returnDict

    def setPassWord (self, password):
        """ sets the password for the user"""
        self.password = password
    