import  json
data='''{
"name":"chand",
"phone no":"987456123",
"email":{"hide":"yes"}
}'''
info=json.loads(data)
print(info)
print("Name :",info["name"])
print("email :", info["email"])[]