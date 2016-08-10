deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("depender", "depender2", "depender3", "depender4", "dependee", "dependee2", "other")
kindnum <- c()

deps$kind <- factor(deps$kind, levels = kindset)
deps$SubDate <- as.numeric(deps$SubDate)
deps$is_merge <- as.logical(deps$is_merge)

judge_name <- "author"
judge_name <- "merge"

cols <- c("#FF8888", "#8888FF")
i <- 0
plot.new()
for (judge in c(TRUE, FALSE)) {
    i <- i + 1
    if (judge_name == "author") {
        deps2 <- subset(deps, deps$same_author == judge)
        legend_name <- c("同じ開発者によるコミット　　　　　　",
                         "異なる開発者によるコミット　　　　　")
    } else {
        deps2 <- subset(deps, deps$is_merge == judge)
        legend_name <- c("マージとなるコミット　　　　　　　","マージではないコミット　　　　　　")
    }

    par(cex.axis = 2.0)
    if (judge == TRUE) {
        # ジャッジに当てはまる割合
        judgepar <- c()
        for (ki in kindset) {
            judgepar <- append(judgepar, c(nrow(subset(deps2, deps2$kind == ki)) / nrow(subset(deps, deps$kind == ki))))
        }
        par(cex.axis = 2)
        boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.25, at = 1:7, col = cols[i], ylim = c(0, 200))
    } else {
        #plot(judgepar, ylim = c(0, 100), add = TRUE, xaxt = "n", yaxt = "n")
        boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.25, at = 1:7 + 0.4, col = cols[i], ylim = c(0, 200), add = TRUE, xaxt = "n", yaxt = "n")
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
}

par(family = "Japan1GothicBBB")
legend("topleft", legend = legend_name, fill = cols, cex = 1.5)