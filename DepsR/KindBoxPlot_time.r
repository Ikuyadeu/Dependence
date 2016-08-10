deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("depender", "depender2", "depender3", "depender4", "dependee", "dependee2", "other")
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
#meandate = mean(deps$date)
#legend_name <- c("開始～初期", "初期から中期", "中期から後期", "後期から最新")
legend_name <- date4
#print(date4)
tmp <- sdate[['Min.']]
for (d in date4) {
    i <- i + 1
    deps2 <- subset(deps, deps$date < d & deps$date > tmp)
    par(cex.axis = 2.0)
    #print(summary(deps2))
    if (i == 1) {
        par(cex.axis = 2)
        boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.1, at = 1:7, col = cols[i], ylim = c(0, 100))
    } else {
        #plot(judgepar, ylim = c(0, 100), add = TRUE, xaxt = "n", yaxt = "n")
        boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.1, at = 1:7 + 0.2 * (i-1), col = cols[i], ylim = c(0, 100), add = TRUE, xaxt = "n", yaxt = "n")
    }

    #2標本検定
    #print(t.test(dates[[1]], dates[[3]]))
    #print(t.test(dates[[3]], dates[[2]]))
    #print(t.test(dates[[2]], dates[[4]]))
    #print(t.test(dates[[4]], dates[[5]]))

    #pdf(paste(judge_name, "/CommitNo_", judge, ".pdf", sep = ""))
    #boxplot(nos, names = kindset, ylim = c(0, 300))

    #pdf(paste(judge_name, "/par_", judge, ".pdf", sep = ""))
    #barplot(judgepar, names = kindset, ylim = c(0, 1))
    tmp <- d
}

par(family = "Japan1GothicBBB")
legend("topleft", legend = legend_name, fill = cols, cex = 1.5)