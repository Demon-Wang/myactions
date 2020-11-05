import http.client
import mimetypes
conn = http.client.HTTPSConnection("god-welfare.gameyw.netease.com")
payload = "{\"rewardBagId\":\"5b557b14550f0256f7620be3\",\"appKey\":\"g37\",\"roleId\":\"58db9dc455a961299a0647f9\",\"server\":\"15024\",\"gameId\":\"\"}"
headers = {
  'Host': 'god-welfare.gameyw.netease.com',
  'Connection': 'keep-alive',
  'Content-Length': '122',
  'gl-checksum': '',
  'Sec-Fetch-Mode': 'cors',
  'gl-version': '2.11.0',
  'Origin': 'https://welfare.ds.163.com',
  'gl-source': 'URS',
  'gl-curtime': '1604563599059',
  'gl-deviceid': '04c95fa1622443d2b8c0e4c42dcbbf6a',
  'content-type': 'application/json;charset=UTF-8',
  'gl-token': 'c513864277b04a7dac790f13b0bb8255',
  'accept': 'application/json;charset=UTF-8',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6010 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045410 Mobile Safari/537.36 Godlike/2.11.0',
  'gl-clienttype': '50',
  'gl-nonce': '134961979100862568',
  'gl-uid': '0f5b218bb760459abf79415490571bdb',
  'X-Requested-With': 'com.netease.gl',
  'Sec-Fetch-Site': 'cross-site',
  'Referer': 'https://welfare.ds.163.com/g37/',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}
conn.request("POST", "/v1/welfare/applyRewardV2?ts=1604563599&uf=2cf89fcce8cb4438b7d50a936bab82b200&ab=d0de6ff590433236a7ccd32e81dd462a8a&ef=5af887a2718532b3647ec15c79f620b05f", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))