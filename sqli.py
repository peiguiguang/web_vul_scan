import requests
def sqli_scan(url):
  print(url)
  payload="'"
  error=['syntax error',
         'warning',
         'mysql',
         'sql syntax']
  try:
    res=requests.get(url+payload,timeout=5)
    for err in error:
      if err.lower() in res.text.lower():
        print("[!] 可能存在 SQL 注入漏洞")
        return
  except:
    pass
