# Get tickers

library(tidyquant)
library(purrr)
options("getSymbols.warning4.0"=FALSE)
options("getSymbols.yahoo.warning"=FALSE)

# tickers
tickers <- c("ABEV3.SA", "ITSA4.SA", "WEGE3.SA", "USIM5.SA", "VALE3.SA")
tickers.names <- c("ABEV3.SA", "ITSA4.SA", "WEGE3.SA", "USIM5.SA", "VALE3.SA")

getSymbols(tickers)

carteira02 <- map(tickers.names, function(x) Ad(get(x)))
carteira02 <- reduce(carteira02, merge)

carteira02 <- data.frame(as.Date(index(carteira02)), carteira02)

colnames(carteira02) <- c("Date", tickers.names)
write.csv(carteira02, "carteira02.csv")
