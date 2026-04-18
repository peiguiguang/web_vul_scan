import argparse
from concurrent.futures import ThreadPoolExecutor,as_completed
from sqli import sqli_scan
from xss import xss_scan

def scan(url):
  sqli_scan(url)
  xss_scan(url)

def multi_scan(url_list,max_workers):
  with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures=[executor.submit(scan,url) for url in url_list]
    for future in as_completed(futures):
      try:
        future.result()
      except Exception as e:
        print(f'扫描异常:{e}')
  

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-u','--url',help='输入要扫描的URL')
    parser.add_argument('-f','--file',help='输入URL列表文件')
    parser.add_argument('-t','--threads',default=5,type=int,help='最大线程数')

    args=parser.parse_args()
    url_list=[]
    if args.url:
      scan(args.url)
    if args.file:
      with open(args.file,'r') as f:
        urls=f.readlines()
        url_list=[url.strip() for url in urls if url.strip()]
    if url_list:
      multi_scan(url_list,args.threads)

        
        


 

  