#purpose: process the output of twitter-log to create a CSV (for graphing) and
#         and a TXT file for wordcloud creation

#use twitter-log to create the raw material

from optparse import OptionParser 
import time

usage = "usage: %prog -i INPUTFILE -c OUTPUTCSV -t OUTPUTTXT [Comma Seperated list of words to search for]"
parser = OptionParser(usage=usage)
parser.add_option("-u", "--user", dest="user",
                  help="twitter user without @", metavar="USER") 
parser.add_option("-i", "--input", dest="inputfile",
                  help="input data from INPUT", metavar="INPUTFILE") 
parser.add_option("-c", "--outputcsv", dest="outputcsv",
                  help="write CSV to OUTPUTCSV", metavar="OUTPUTCSV") 
parser.add_option("-t", "--outputtxt", dest="outputtxt",
                  help="write tweets to OUTPUTTXT", metavar="OUTPUTTXT")                              
(options, args) = parser.parse_args()

DateArr={}
with open(options.inputfile,'r') as f:
    for read_data in f.readlines():
        if not(options.user in read_data) and not(read_data[0]=="\n"):
            if 'Date:' in read_data:
                t=time.strptime(read_data[6:36],"%a %b %d %H:%M:%S +0000 %Y")
                k=str(t.tm_year) + "/" + ("00" + str(t.tm_yday))[-3:]
                if not DateArr.has_key(k): 
                    DateArr[k] = {'Total':1, 'Tweet':' '}
                    if len(args)>0:
                        for txtval in args:
                            DateArr[k][txtval]=0
                else:DateArr[k]['Total']=DateArr[k]['Total']+1
            else:
                if len(args)>0:
                    for txtval in args:
                        if txtval in read_data: 
                            DateArr[k][txtval]=DateArr[k][txtval]+1
                            DateArr[k]['Tweet']=DateArr[k]['Tweet'] + read_data
                            bInTweet=False #only count ABC once
                        elif len(read_data)>2 and not ('In-Reply-To' in read_data): 
                            DateArr[k]['Tweet']=DateArr[k]['Tweet'] + read_data
                            bInTweet=False #only count a line once

with open(options.outputcsv,'w') as f:
    header="When\tTotal"
    if len(args)>0:
        for txtval in args: header = header+"\t"+txtval
    header=header+"\n"
    f.write(header)
    for i in DateArr: 
        sline = i + "\t" + str(DateArr[i]['Total'])
        if len(args)>0:
            for txtval in args:sline=sline+"\t"+str(DateArr[i][txtval])
        sline=sline+"\n"
        f.write(sline)

s=""
for i in DateArr:
    s=s+DateArr[i]['Tweet']

with open(options.outputtxt,'w') as f: f.write(s)

    
