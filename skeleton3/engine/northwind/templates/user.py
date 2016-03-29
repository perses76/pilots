class UserTemplate(object):
    def render(self, data):
        user = data['user']
        return 'Northwind!!! Hello: {user_name}, at age: {age}'.format(**{'user_name': user.name, 'age': user.age})
