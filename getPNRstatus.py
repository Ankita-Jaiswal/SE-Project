import re,sys
import mechanize
#for irctc pnr

def fun(pnr):
	#pnr=sys.argv[1]
	br = mechanize.Browser()
	br.open("http://www.indianrail.gov.in/index.html")

	req = br.click_link(text='PNR Status')
	br.open(req)

	br.select_form(nr=0)
	br["lccp_pnrno1"]= pnr
	br.submit()
	#print br.response().read()
	html = br.response().read()
	with open('/home/ankita/seProj/internals/output.txt', 'w') as f:
		f.write(html)
	

fun("2319107478")
