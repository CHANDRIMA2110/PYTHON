import  json
data='''[
{"name":"chand",
"phone no":"987456123",
"email":{"hide":"yes"}
},
{"name":"kutu",
"phone no":"9558456123",
"email":{"hide":"no"}
}
]'''
info=json.loads(data)
for i in info:

    print("Name :",i["name"])
    print("email :", i["email"])