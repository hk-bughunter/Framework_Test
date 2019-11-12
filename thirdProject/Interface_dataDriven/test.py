from urllib.parse import unquote
source_str = "redirectURL=%2Ftinyshop%2Findex.php%3Fcon%3Dindex%26act%3Dflash&email=2%401.com&password=123456"

source_list = source_str.split("&")

data = {}

for source in source_list:
    data_str = unquote(source).split("=")
    data[data_str[0]] = data_str[1]