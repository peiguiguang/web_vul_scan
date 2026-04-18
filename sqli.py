import requests
def sqli_scan(url):
  print('扫描sql注入漏洞......')
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
