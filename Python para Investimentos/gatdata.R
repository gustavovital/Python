# Get data from yahoo fiance

# install.packages("tidyquant")
library(tidyquant)

options("getSymbols.warning4.0"=FALSE)
options("getSymbols.yahoo.warning"=FALSE)

BVSP <- getSymbols("^BVSP", warnings = FALSE, auto.assign = FALSE)

class(BVSP)
# plot(BVSP$BVSP.Close)
# chart_Series(BVSP['2007-12/2021-05'])
