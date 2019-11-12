from suds.client import Client
wsdl="http://ws.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl"
client=Client(wsdl)
res=client.service.getWeather("成都")
print(res)



