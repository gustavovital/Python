# Get data from yahoo finance

# Set wd
setwd("E:\\Python\\Python para Investimentos")

# install.packages("tidyquant")
library(tidyquant)

options("getSymbols.warning4.0"=FALSE)
options("getSymbols.yahoo.warning"=FALSE)

BVSP <- getSymbols("^BVSP", warnings = FALSE, auto.assign = FALSE)
BVSP <- data.frame(as.Date(index(BVSP)), BVSP)

colnames(BVSP) <- c("Date", "Open", "High", "Low", "Close", "Volume", "Adjusted")
# class(BVSP)
# plot(BVSP$BVSP.Close)
# chart_Series(BVSP['2007-12/2021-05'])

write.csv(BVSP, "BVSP.csv")
# saveRDS(BVSP, "BVSP.rds")
