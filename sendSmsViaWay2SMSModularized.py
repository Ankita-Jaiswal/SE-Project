#!/usr/bin/python
import urllib2
import cookielib
import sys

#nmbr from 9731149289
#password P2494F

#nmbr from pragya 9900479820
# password from pragya M3222K

#nmbr for ashhad 7799629099
#pwd for ashhad C2365F

#nmbr for ashhad 8867447967
#pwd for ashhad bismillah1234

#nmbr for anand 9962547546
#pwd for anand K5532Q

#maximum msg size 140 characters
def sendSms(mobNo,msg):

    username = '9731149289'
    passwd   = 'P2494F'
    message  = msg
    number   = mobNo
    print 'Mobile No: ' ,mobNo
    message  = "+".join(message.split(' '))

    cj,opener = openWayToSms(username,passwd)
    sendSmsViaWay2SMS(cj,opener,number,message)

def openWayToSms(username,passwd):
    #Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
  
    #For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  
    # Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
  
    try:
      usock = opener.open(url, data)
    except IOError:
     print "Error while logging in."
     sys.exit(1)
    return cj,opener

def sendSmsViaWay2SMS(cj,opener,number,message):
    
    jession_id = str(cj).split('~')[1].split(' ')[0]

    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
  
    try:
      sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
     print "Error while sending message"
     sys.exit(1)
    print "SMS has been sent."

def main():
    sendSms('8867447967','hello this is a test message')

if __name__=='__main__':
    main()
