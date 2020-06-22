#https://www.youtube.com/watch?v=tb8gHvYlCFs&feature=share
import requests

#r = requests.get('https://0.soompi.io/wp-content/uploads/2019/07/13072305/Chuu1.jpg')

#print(dir(r)) #prints out accessible variables/functions
#print(help(r)) #prints out details of accesible data
#print(r.text) #prints out HTML code
#print(r.content) #prints out content in bytes

#### Downloading Image by requesting bytes - Syntax similar to A1 ####
# with open('chuu.png','wb') as w: #wb = write bytes
#     w.write(r.content)

#### A1 ####
# w = open('chuu.png', 'wb')
# w.write(r.content)
# w.close()

#print(r.status_code) #2XX = success, 3XX = redirects, 4XX = client errors, 5XX = server errors
#print(r.ok) #returns True if no error
#print(r.headers) #returns dictionary of labels

#### HTTPbin Get ####
# url_par = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=url_par)
# print(r.url)

#### HTTPbin Post ####
# url_par = {'username': 'query', 'password': 'test'}
# r = requests.post('https://httpbin.org/post', data=url_par)
# print(r.text)

#### JSON Method HTTPbin Post ####
# url_par = {'username': 'chuu', 'password': 'test'}
# r = requests.post('https://httpbin.org/post', data=url_par)
# print(r.json()) #returns a dictionary of parameters from HTTPbin post
#
# r_dict = r.json()
# print(r_dict['form']) #to obtain which data are needed for form to test authorization routes


#### Sample Authentication Testing ####
r = requests.get("https://httpbin.org/basic-auth/chuu/test", auth=('chuu', 'test')) #creates a link which requires specific username/password combination to be authenticized

print(r.text)
#print(r) returns status code
