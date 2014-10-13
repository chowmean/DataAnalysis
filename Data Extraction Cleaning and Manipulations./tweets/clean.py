import json

with open("outfile_1.json") as json_file:
	json_data = json.load(json_file)
	i=0
	while json_data[i]!="" :
		text=json_data[i]["text"]
		print("tweet=> "+ json_data[i]["text"])
		print("favorite_count=> "+ str(json_data[i]["favorite_count"]))
		print("retweet_count=> "+str(json_data[i]["retweet_count"]))    
		print("Followers=> "+str(json_data[i]["user"]["followers_count"]))   
		print("friends=> "+str(json_data[i]["user"]["friends_count"]))   
		print("Location=> "+json_data[i]["user"]["location"])   
		print("Description of user=>"+json_data[i]["user"]["description"]) 
		print("\n\n ")
		i=i+1
