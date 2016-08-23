deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)

# 7 colors
#kindset <- c("depender", "depender2", "depender3", "depender4", "dependee", "dependee2", "other")
#cols <- c("#FF8888", "#88FF88", "#8888FF", "#FFFF88", "#FF88FF", "#88FFFF", "#000000", "#888888")

# 5 colors
#kindset <- c("depender", "depender2", "dependee", "dependee2", "other")
#cols <- c("#FF0000", "#00FF00", "#0000FF", "#00FFFF", "#FF00FF")

# 3 colors
kindset <- c("depender", "dependee", "other")
cols <- c("#FF0000", "#00FF00", "#0000FF")


deps$kind <- factor(deps$kind, levels = kindset)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)

library(xts)
i = 1
plot.new()
for (ki in kindset) {
    dep2 <- subset(deps, deps$kind == ki)
    ts <- apply.monthly(xts(dep2$SubDate, dep2$date), median)
    if (ki == "depender") {
        last_ts <- ts
    } else {
        last_ts <- na.locf(merge(last_ts, ts))
    }
}

plot.zoo(last_ts, ylim = c(0, 100), col = cols, plot.type = "single")
legend("topleft", legend = kindset, fill = cols, cex = 1.0)