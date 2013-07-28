from boto.dynamodb2.table import Table

class Message(object):
    table = Table('message')

    def __init__(self, message, name, email):
        self.message = message
        self.name = name
        self.email = email

    def save(self):
        data = {'message': self.message,
                'name': self.name,
                'email': self.email}

        self.table.put_item(data=data)
        
    @staticmethod
    def all():
        table = Table('message')
        all_users = table.scan()

        for user_db in all_users:
            yield Message(user_db['message'], user_db['name'], user_db['email'])
