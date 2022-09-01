from pip._vendor import requests
from types import SimpleNamespace
import time
import csv

url = 'https://api.twitter.com/2/users/1174426031010152448/mentions'


queryparams={
    "expansions":"author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
    "user.fields":"created_at,description,entities,id,location,name,profile_image_url,url,username",
}

headers = {
  "accept": "application/json",
  "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAAPrcwEAAAAATFz6hzNYHoLC8eZwXTfpfg6b91g%3DWFo7w5XAhKraUHMjVcpZFn5myhecOaUVdk2OO4ZsfKKmAFBRiY"
}

fieldnames = ['text', 'author_id', 'id', 'username','location']

# csv data
filename = "/Users/udhaysubramanian/Documents/dataset.csv"

response = None
next_token = None
while response is None or next_token:
  response = requests.request("GET", url, headers=headers, params=queryparams).json()
  list1=[]
  list2=[]  
#print(response)
 
    
  for key, value in response.items():
    print("kt",key)
   # print(type(value))
   #print(value)
    seconddict = {}
    if value == "429" or value == "Too Many Requests":
      print("time is currently at an interval of 15!")
      print(next_token)
      print(value)
      time.sleep(15 * 60)
    if key == "errors":
      print("eror")
      print(value)     
      response = requests.request("GET", url, headers=headers, params=queryparams).json() 
    if key == "data":
      print(type(value))
      for index in range(len(value)):
        c=0
        firstdict = {}
        for key1 in value[index]:  
          #print(key1)
          if key1 == "id" or key1 == "text" or key1 == "author_id":
            #print(value[index][key1])
            c+=1
            firstdict[key1] = value[index][key1]
            if c == 3:
              list1.append(firstdict)
              firstdict = {}
              c=0
    if key == "includes": 
      for k1,v1 in value.items():
        for index in range(len(v1)):
          c1=0
          seconddict = {}
        # print(v1[index])
          for key2 in v1[index]:
            if key2 == "id" or key2 == "username" or key2 == "location":
              c1+=1
              seconddict[key2] = v1[index][key2] 
              if(c1 == 3):
               #print(seconddict)
                list2.append(seconddict)
                seconddict={}
                c1=0
    if key == "meta":
      #print("meta")
      for k3,v3 in value.items():
        if k3 == "next_token":
          next_token = v3
          #print("v3",v3)
    for val1 in list1:
      #print(type(val1["author_id"]))
      for val2 in list2:
        #print(type(val2["id"]))
        if(val1["author_id"] == val2["id"]):
          #print("kenannn")
          val1["username"] = val2["username"]
          val1["location"] = val2["location"]
  if next_token:
    #print("nexttoken")
    queryparams={
   # "pagination":next_token,
    "expansions":"author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
    "user.fields":"created_at,description,entities,id,location,name,profile_image_url,url,username",
    #"max_results":"100"
    }
  else:
    queryparams={
    "expansions":"author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
    "user.fields":"created_at,description,entities,id,location,name,profile_image_url,url,username",
    #"max_results":"100"
    }

  
  #print(list1)
  with open(filename, 'a', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(list1)
  # temp = temp + 1
  # print("temp",temp)
  #if temp >= 50000:
    


