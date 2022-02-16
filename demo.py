from pyspark import SparkContext

logFile = "file:///Users/sumanb/SB_Code_Dev/SparkDemo/Input/input_big.txt"
sc = SparkContext("local", "first app")  
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print "Lines with a: %i, lines with b: %i" % (numAs, numBs)

# logFile = "file:///Users/sumanb/SB_Code_Dev/SparkDemo/Input/input_big.txt"
# logData = sc.textFile(logFile).cache()
# numAs = logData.filter(lambda s: 'a' in s).count()
# numBs = logData.filter(lambda s: 'b' in s).count()
# print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
