song_name = "TWICE Dance the night away"
input_query1 = 'TWICE – Dance The Night Away (Japanese Ver.)'
input_query2 = 'TWICE – Dance The Night Away'

song_name = set(song_name.split())
input_query1 = set(input_query1.split())
input_query2 = set(input_query2.split())

# song_name = set(['x1','rr','x3','y4'])
# input_query1 = set(['x1','rr','rr','y4'])

# def difference (list1, list2):
#    list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
#    return list_dif

print(song_name,'\n',input_query1,'\n')

difference1 = song_name.difference(input_query1)
print(difference1, len(difference1))

print('\n', song_name,'\n',input_query2,'\n')
difference2 = song_name.difference(input_query2)
print(difference2, len(difference2))

# results = [
#     {"name": "Butterfly", "link": "google.com"},
#     {"name": "Butterfly2", "link": "google2.com"}
# ]
#
# print(results[0]["name"])
