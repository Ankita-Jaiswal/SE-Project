from googlemaps import Client
from HTMLParser import HTMLParser


def getLandMarks(text):
    landMarkList=[]
    listOfSentences=text.split('\n')    
    for sentence in listOfSentences:
        words=sentence.split()
        count=0
        for word in words:
            #print word            
            if count==0:
                count=1
                continue                        
            #keeping only the words with capital letters
            if word[0].isupper():
                newWord=word
                indx=newWord.find("Pass")
                if(indx>=0):
                    newWord=newWord[:indx]                
                landMarkList.append(newWord.strip())
        landMarkList.append('\n')
    return landMarkList

class MLStripper(HTMLParser):
        def __init__(self):
                self.reset()
                self.fed=[]
        def handle_data(self,d):
                self.fed.append(d)
        def get_data(self):
                return ''.join(self.fed)

def get_route(src,dest):
    print 'from ',src,' to ',dest
  # Add you API key here
    mapService = Client(key='AIzaSyASPXj-p2W-z3N1KEcbCOd9mrvZEOQrCcM ')

    directions = mapService.directions(src, dest)
    directions = directions[0]

    htmlText=""

    i=1
    for leg in directions['legs']:
        startAddress = leg['start_address']
        print "Start Address:", startAddress
        endAddress = leg['end_address']
        print "End Address:", endAddress
        for step in leg['steps']:
            html_instructions = step['html_instructions']
        #    print "STEP {} {}".format(i ,html_instructions)
            htmlText=htmlText+html_instructions+"\n"
            i = i+1
    #print htmlText
    smStrip=MLStripper()
    smStrip.feed(htmlText)
    text=smStrip.get_data()
    print 'the route is as follows' 
    print
    print text
    print
    print 'end of route'

    #a function to get only the proper nouns
    #that too after ignoring the first word in each line
    landMarkList=getLandMarks(text)
    print('landmarks list is')
    print(landMarkList)
    landMarkListText=" "
    landMarkListText=landMarkListText.join(landMarkList)


    #for now store in file
    fileLine="\n"+text
    #fo = open("/home/pi/myproject/app/message","a")
    fo = open("/home/ankita/seProj/message","a")
    fo.write(landMarkListText)
    fo.close()
    return text


def main():
    theRoute=get_route('Electronics City, Bangalore','Marathalli,Bangalore')
    print theRoute

if __name__=='__main__':
    main()
