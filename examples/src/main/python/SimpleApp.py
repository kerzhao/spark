"""SimpleApp.py"""
from pyspark import SparkContext

logFile = "kmeans.py"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
#sc.master = 'local'
#sc.appName = 'Simple App'
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

sc.stop()
