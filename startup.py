import sys
import json
from pprint import pprint

import re,sys
import mechanize
#for irctc pnr

import time
#for sleep

from googlemaps import Client
from HTMLParser import HTMLParser
from Route import get_route
#above to help get route

import urllib2
import cookielib
#for way2sms
from sendSmsViaWay2SMSModularized import sendSms



#from geopy.geocoders import Nominatim
#the above library helps to convert lat long to address

import geocoder
#pythons simple geo techniques

#takes command line arguments
#number then message
#example
#8867447967 destination#lat#lon# to go
def main():
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    client_number=str(sys.argv[1])
    client_message=str(sys.argv[2])
    print 'sender is ',  client_number
    print 'message is ', client_message
    if client_number[0]=='+':
        client_number=client_number[3:]
    print 'sender is ',  client_number
    #split the message and produce the different parameters
    parameters=client_message.split('#')
    #1st parameter is destination
    #2nd parameter is longitude
    #3rd parameter is latitude
    
    #1st check if all three elements have come
    if len(parameters) == 3:
	print parameters[1]
	print parameters[2]
	get_pnrStatus(parameters[2])
	return
    if len(parameters) != 5:
        #send message saying co ordinates not received
        #please re send
        print "incorrect parameters"
        return
    dest=  parameters[1]
    lat =  parameters[2]
    lon =  parameters[3]


    

    print 'lat is ',lat,' and lon is ',lon,' and dest is ',dest
    client_city,client_address=get_client_address(lat,lon)  
    print "the address is", client_address
    print "the city is ",client_city


    source=client_address
    if client_city == None:
        print "city could not be extracted.exiting"
        return
    dest=dest+', '+client_city
    the_route=get_route(source,dest)
    print 'the route is ',the_route
    #now send the route
    send_route(the_route,client_number)
                



    #print(location.city)

def send_route(the_route,nmbr):
    
    #now send the_route as a message line by line
    listOfSentences=the_route.split('\n')
    list_to_be_sent=[]
    for sentence in listOfSentences:
        if len(sentence)<135:
            list_to_be_sent.append(sentence)
    total_count=len(list_to_be_sent)
    count=total_count
    print 'total number of messages to be sent for this route is ',total_count


    #print recepient=',str(nmbr)
    #sendSms(str(nmbr),'hello from startup')       

    for sentence in list_to_be_sent:
        count-=1
        remaining=str(count)
        message_text="#"+remaining+sentence
        print 'sending '+message_text
        sendSms(str(nmbr),message_text)
        #time.sleep(3)

    
def get_client_address(lat,lon):
    #geolocator = Nominatim()
    #co_ord=lat+","+lon
    #reverse(latitude,longitude)
    print 'getting client address'
    print 'lat is ', lat
    print 'lon is ', lon
    location = geocoder.google([lat, lon], method='reverse')
    #location = geolocator.reverse("52.52, 13.4050")
    # bangalore is 12.9716 N, 77.5946 E
    #north and east are positive
    print "address is",location
#    print "city is ",location.city
#    print "various attributes maybe"
#    print (vars(location))
    the_city=location.city
    the_address=str(location)
    the_address=the_address[24:]
    the_address=the_address[:len(the_address)-2]

    return the_city,the_address


#to get pnr status:

def get_pnrStatus(pnrnum):
	pnr=pnrnum
	br = mechanize.Browser()
	br.open("http://www.indianrail.gov.in/index.html")

	req = br.click_link(text='PNR Status')
	br.open(req)

	br.select_form(nr=0)
	br["lccp_pnrno1"]= pnr
	br.submit()
	html = br.response().read()
	with open('/home/ankita/seProj/internals/output.txt', 'w') as f:
		f.write(html)

if __name__=='__main__':
    main()
