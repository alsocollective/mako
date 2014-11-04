import requests,os,re,json
from xml.dom import minidom

def getdata():
	with open("data.xml") as inputFileHandle:
		return inputFileHandle.read()

def parseEachdatapoint(data,dType):
	if not dType.find("Wind Direction"):
		return int(re.findall(r"\d+",data)[0])
	if not dType.find("Wind Speed") or not dType.find("Average Period") or not dType.find("Mean Wave Direction") or not dType.find("Dominant Wave Period") or not dType.find("Wind Gust") or not dType.find("Atmospheric Pressure")or not dType.find("Significant Wave Height"):
		return float(re.findall(r"[0-9\.]+",data)[0])
	if not dType.find("Water Temperature") or not dType.find("Air Temperature") :
		return float(re.findall(r"[0-9\.]+",data)[2])
	if not dType.find("Pressure Tendency"):
		return re.findall(r"[\+0-9\.]+",data)[1]
	if not dType.find("Location"):
		return re.findall(r"[\+0-9\.A-Z]+",data)				
	return "|||| none parsed ||||%s"%data

def parseContents(data):
	data = re.findall('<strong>([a-zA-Z0-9#;+\.\(\)\&,: +W]*)</strong>([a-z A-Z 0-9 #;+\.\(\)\&]*)',data,re.DOTALL)
	out = {}
	for point in data[1:]:
		out["unparsed_%s"%point[0].replace(":","")] = point[1]
		out[point[0].replace(":","")] = parseEachdatapoint(point[1],point[0])
	return out

def getbouydata(id):
	r = requests.get("http://www.ndbc.noaa.gov/data/latest_obs/%s.rss"%id)
	r = r.text
	# r = minidom.parse("%s/data.xml"%os.path.dirname(os.path.realpath(__file__))) #parseString(r)
	r = minidom.parseString(r)
	r = r.getElementsByTagName('item')[0]
	out = {
		"date":r.getElementsByTagName('pubDate')[0].firstChild.nodeValue,
		"title":r.getElementsByTagName('title')[0].firstChild.nodeValue,
		"contents_nonparse":r.getElementsByTagName('description')[0].firstChild.nodeValue		
	}
	out["contents"] = parseContents(out["contents_nonparse"])
	return out

location = ['45008','45149','45137']#,'45143','45132','45167','45142','45159','45012','45135','45003']

out = []
for loc in location:
	out.append({"loc":loc,"data":getbouydata(loc)})
text_file = open("fulldataset.json", "w")
text_file.write(json.dumps(out))
text_file.close()
# data = getbouydata(location[0])["contents"]

