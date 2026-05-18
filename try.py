import json as js

d = {
    "hello":"vyar",
    "vikram": "world"
}

with open("Command_list.json","w") as file:
    js.dump(d,file)
    print("file saved in dist folder")  

with open("Command_list.json","r") as file:
    # file.seek(0)
    d = js.load(file)
          


for ind,keys in enumerate(d.keys() , start=1):
    print(f"{ind} {keys}")

