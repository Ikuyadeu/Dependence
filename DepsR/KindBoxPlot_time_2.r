deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("depender", "depender2", "depender3", "depender4", "dependee", "dependee2", "other")
cols <- c("#FF8888", "#88FF88", "#8888FF", "#FFFF88", "#FF88FF", "#88FFFF", "#000000")

deps$kind <- factor(deps$kind, levels = kindset)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)

library(xts)
i = 1
plot.new()
#for (ki in kindset) {
    #dep2 <- subset(deps, deps$kind == ki)
    #ts <- xts(dep2$SubDate, dep2$date)
    #plot(apply.daily(ts, median), ylim = c(0, 200))
    #par(new = T)
    #i = i + 1
#}
ts <- xts(deps$SubDate, deps$date)
plot(apply.daily(ts, median), ylim = c(0, 200))
