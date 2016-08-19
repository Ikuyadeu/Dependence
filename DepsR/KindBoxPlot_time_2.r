deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("depender", "depender2", "depender3", "depender4", "dependee", "dependee2", "other")
kindnum <- c()

deps$kind <- factor(deps$kind, levels = kindset)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)

library(xts)
library(zoo)
ts <- zoo(deps$Subdate, deps$date)

plot(sqrt(251) * apply.monthly(as.xts(diff(log(ts))), sd), ylim = c(0, 1.0))
