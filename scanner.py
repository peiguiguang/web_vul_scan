import argparse
from sqli import sqli_scan
from xss import xss_scan


if __name__=='__main__':
  parser=argparse.ArgumentParser()
  parser.add_argument('-u','--url',required=True,help='输入要扫描的URL')
  args=parser.parse_args()
  sqli_scan(args.url)
  xss_scan(args.url)

  