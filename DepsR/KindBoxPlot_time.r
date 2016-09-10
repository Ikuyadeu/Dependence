deps <- read.csv("netty/deps.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("r", "rr", "e", "ee", "o")
kindnum <- c()

deps$kind <- factor(deps$kind, levels = kindset)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)
print(summary(deps$date))

sdate <- summary(deps$date)
date4 <- c(sdate[['1st Qu.']], sdate[['Median']], sdate[['3rd Qu.']], sdate[['Max.']])

cols <- c("#FF8888", "#88FF88", "#8888FF", "#FFFF88")
i <- 0
plot.new()
legend_name <- date4
tmp <- sdate[['Min.']]
for (d in date4) {
    i <- i + 1
    deps2 <- subset(deps, deps$date < d & deps$date > tmp)
    par(cex.axis = 2.0)
    if (i == 1) {
        par(cex.axis = 2)
        boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.1, at = 1:7, col = cols[i], ylim = c(0, 100))
    } else {
        boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.1, at = 1:7 + 0.2 * (i-1), col = cols[i], ylim = c(0, 100), add = TRUE, xaxt = "n", yaxt = "n")
    }

    tmp <- d
}

par(family = "Japan1GothicBBB")
legend("topleft", legend = legend_name, fill = cols, cex = 1.5)