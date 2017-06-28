#First download PIL
import urllib,urllib2
import json
from PIL import Image
from cStringIO import StringIO
import sys

while 1:
	u="http://www.google.com/recaptcha/api/challenge?k=6LdXvuYSAAAAAJJhkODYw0X09bgn77lC-UXsOKqM&ajax=1&cachestop=0.6509875061456114&lang=en"
	raw = urllib2.urlopen(u).read()
	#print raw
	chal=raw.find("challenge : '")+len("challenge : '");
	finCAP = raw[chal:raw.find("\',",chal)]
	#print finCAP
	u="http://www.google.com/recaptcha/api/image?c="+finCAP
	#print u
	img_file = urllib2.urlopen(u)
	im = StringIO(img_file.read())
	Image.open(im).show()
	#print im
	txtCAP = raw_input().replace(" ","+")
	if txtCAP=="": sys.exit("TY! BYE!");

	fin="curl 'http://lms.usatodayhss.com/atlanta/polls/vote/14-vote-for-the-local-high-school-football-game-of-the-week-for-oct-11' -H 'Cookie: __uvt=; __vrf=1381277711316ZcRXx6OIpRvr0q01Lqf0qNPucwfyE2dA; b1d7798c33bc4b9a357eda91a9dc4cad=5m09gtccv6tcq4ofkaq0ivj6v0; __atuvc=17%7C41; s_cc=true; s_sq=%5B%5BB%5D%5D; uvts=gDM7BCbGCsqGAJy; uvf=1; __vrm=273_1054_1140' -H 'Origin: http://lms.usatodayhss.com' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Host: lms.usatodayhss.com' -H 'Accept-Language: en-US,en;q=0.8,ta;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.8 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: http://lms.usatodayhss.com/atlanta/polls/viewpoll/14-vote-for-the-local-high-school-football-game-of-the-week-for-oct-11' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'answers%5B%5D=58&custom_answer=&recaptcha_response_field="+txtCAP+"&recaptcha_challenge_field="+finCAP+"' --compressed"
	#print fin; sys.exit("Error message");

	# create the request object and set some headers
	path = 'http://lms.usatodayhss.com/atlanta/polls/vote/14-vote-for-the-local-high-school-football-game-of-the-week-for-oct-11'
	data={'answers[]':'58','custom_answer':'','recaptcha_response_field':txtCAP,'recaptcha_challenge_field':finCAP}
	req = urllib2.Request(path,urllib.urlencode(data));
	req.add_header('Origin', 'http://lms.usatodayhss.com')
	req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
	req.add_header('Host', 'lms.usatodayhss.com')
	req.add_header('Accept-Language', 'en-US,en;q=0.8,ta;q=0.6')
	req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.8 Safari/537.36')
	req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
	req.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
	req.add_header('Referer', 'http://lms.usatodayhss.com/atlanta/polls/viewpoll/14-vote-for-the-local-high-school-football-game-of-the-week-for-oct-11')
	req.add_header('X-Requested-With', 'XMLHttpRequest')
	req.add_header('Connection', 'keep-alive')
	req.add_header('DNT', '1')
	req.add_header('Accept', 'aasda')
	# make the request and print the results
	res=urllib2.urlopen(req)
	#print json.load(res)
	#print "done"

"""
curl
'' -H 'Cookie: __uvt=; __vrf=1381277711316ZcRXx6OIpRvr0q01Lqf0qNPucwfyE2dA; b1d7798c33bc4b9a357eda91a9dc4cad=5m09gtccv6tcq4ofkaq0ivj6v0; __atuvc=17%7C41; s_cc=true; s_sq=%5B%5BB%5D%5D; uvts=gDM7BCbGCsqGAJy; uvf=1; __vrm=273_1054_1140'
-H ': ' -H ': ' -H ': ' -H ': ' -H '
 ' -H ': ' -H ': ' -H ': ' -H
 ': ' -H ': ' -H ': 1'
 --data 'answers%5B%5D=58&custom_answer=&recaptcha_response_field=was+reifirs&recaptcha_challenge_field=03AHJ_Vutn7G476sypjCFKRiT2mmkPSBzAQGWcyKBUEeWgYfG6apcbN6pr6R5mMqoF9lqSSintDR7JYbdF3ODjmnqv0Ff4yvppx4JHVCaqLi2CKyVHd9CWQZwKsM4nk3JY0_qc5aHV-28G5wU9c0aOjWt_sDHVTNOqkhk5MJU6epmwNavBH6PSaOA' --compressed








"""