import requests
def xss_scan(url):
  print('扫描xss漏洞......')
  payload='<script>alert(1)</script>'
  try:
    res=requests.get(url+payload,timeout=5)
    if payload in res.text:
      print("[!] 可能存在 XSS 漏洞")
  except:
    pass

