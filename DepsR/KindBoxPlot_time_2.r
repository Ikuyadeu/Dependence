deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("depender", "depender2", "depender3", "depender4", "dependee", "dependee2", "other")
kindnum <- c()

deps$kind <- factor(deps$kind, levels = kindset)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)

library(xts)
library(zoo)
ts <- xts(deps$Subdate, deps$date)
print(head(deps))
#plot(apply.monthly(ts, mean), ylim = c(0, 200))
