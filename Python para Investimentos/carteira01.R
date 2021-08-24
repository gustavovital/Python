# Get tickers

library(tidyquant)
library(purrr)
options("getSymbols.warning4.0"=FALSE)
options("getSymbols.yahoo.warning"=FALSE)

# tickers
tickers <- c("^BVSP", "USDBRL=X")
tickers.names <- c("BVSP", "USDBRL=X")

getSymbols(tickers)

carteira01 <- map(tickers.names, function(x) Cl(get(x)))
carteira01 <- reduce(carteira01, merge)

carteira01 <- data.frame(as.Date(index(carteira01)), carteira01)

colnames(carteira01) <- c("Date", tickers.names)
write.csv(carteira01, "carteira01.csv")