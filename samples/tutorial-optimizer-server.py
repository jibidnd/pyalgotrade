import itertools
from pyalgotrade.barfeed import csvfeed
from pyalgotrade.optimizer import server

def parameters_generator():
    entrySMA = range(150, 251)
    exitSMA = range(5, 16)
    rsiPeriod = range(2, 11)
    overBoughtThreshold = range(75, 96)
    overSoldThreshold = range(5, 26)
    return itertools.product(entrySMA, exitSMA, rsiPeriod, overBoughtThreshold, overSoldThreshold)

# Load the feed from the CSV files.
feed = csvfeed.YahooFeed()
feed.addBarsFromCSV("dia", "dia-2009.csv")
feed.addBarsFromCSV("dia", "dia-2010.csv")
feed.addBarsFromCSV("dia", "dia-2011.csv")

# Run the server.
server.serve(feed, parameters_generator(), "192.168.1.112", 5000)
