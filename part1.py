from mrjob.job import MRJob
import csv

class TopNumber(MRJob):

    def mapper(self, key , numbers):


        for number in numbers.split(","):
            yield "define_same_key_for_all",float(number)

    def reducer(self, key, maximum):

        
        yield "Given this CSV file, the maximum is",max(maximum)
    







    

"""        yield "Max", int(max(numbers))
        
        

    def reducer(self, key, maximum):

        yield "Given this CSV file, the maximum is", int(max(maximum))
"""        

TopNumber.run()
