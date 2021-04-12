from mrjob.job import MRJob
import functools

class EveryWord(MRJob):

    def mapper(self, line_no, line):
        yield "URL:links:", line.split(",")


    def reducer(self, x,total):
        counter = 0
        s = ""
        t = list(total)
        while(counter<len(t[0])+1):
            for i in t:
                counter+=1
                for j in t:
                    if i[0]==j[1]:
                        res = [int(sub.split('l')[1]) for sub in i+j]
                        res = sorted(res)
                        res = ["url"+str(element) for element in res]
                        yield "URL link:", (res[0]+","+res[1]+","+res[3])

    
   
                    


        



EveryWord.run()
        
