from mrjob.job import MRJob

class Sequence_finder(MRJob):

    def mapper(self,line_no,line):
        sequences = list()
        counter=0
        for i in line.split(" "):
            sequences.append(i)
            if(len(sequences)==4):
                yield sequences,1
            elif(len(sequences)>4):
                counter+=1
                yield sequences[counter:counter+4], 1
                


    def reducer(self,word,occurrences):
        str1 = " "
        yield str1.join(word), sum(occurrences)

Sequence_finder.run()
