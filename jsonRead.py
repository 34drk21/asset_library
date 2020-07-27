import json

def main():
	json_open = open("/Users/shotakimura/Desktop/test.json", 'r')
	json_load = json.load(json_open)

	assetName = json_load["AssetName"]
	description = json_load["Description"]
	date = json_load["Date"]

	print("AssetName: " + assetName + "/nDescription: " + description + "/nDate: " + date)

if __name__=="__main__":
	main()