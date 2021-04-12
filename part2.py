from mrjob.job import MRJob
import re

class EveryWord(MRJob):

    def mapper(self, line_no, line):
        for i in line.split(","):
            yield i, line


    def reducer(self, word, word_sum):

        yield word, list(word_sum)
        



EveryWord.run()
        
