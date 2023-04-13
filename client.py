import requests

# response = requests.post('http://127.0.0.1:5000/user/',
#                          json={
#                              'username': 'User_1',
#                              'password': 'Some_password',
#                              'email': 'user_email'
#                          })

# response = requests.get('http://127.0.0.1:5000/user/1')

# response = requests.delete('http://127.0.0.1:5000/post/1')

response = requests.post('http://127.0.0.1:5000/post/',
                         json = {
                             'creator': 3,
                             'post_header': 'Заголовок',
                             'post_text': 'Здесь текст объявления'
                         })

# response = requests.patch('http://127.0.0.1:5000/post/6',
#                          json = {
#                              'post_header': 'Новый заголовок',
#                              'post_text': 'Другой текст'
#                          })

print(response.status_code)
print(response.json())