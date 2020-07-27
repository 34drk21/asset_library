import json
import collections as cl
import datetime

def main():
	dataList = ["AssetName", "Description", "Date"]
	assetName = "firstTest"
	description = "this is a first test /nthis is a first test. "
	d_today = datetime.date.today()
	date = str(d_today)

	ys = cl.OrderedDict()

	ys[dataList[0]] = assetName
	ys[dataList[1]] = description
	ys[dataList[2]] = date

	fw = open("/Users/shotakimura/Desktop/test.json", "w")

	json.dump(ys, fw, indent=4)

	print("done!")

if __name__=="__main__":
	main()