deps <- read.csv("netty/deps.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("r", "rr", "e", "ee", "o")
kindnum <- c()

deps$kind <- factor(deps$kind, levels = kindset)
deps$SubDate <- as.numeric(deps$SubDate)
deps$is_merge <- as.logical(deps$is_merge)

fauthor <- names(rev(sort(table(deps$author))))

deps2 <- deps
for (i in 1:5) {
    deps2 <- subset(deps2, deps2$author != fauthor[i])
}


print(nrow(deps2))
print(nrow(deps))
legend_name <- c("無制限", "上位５人（全体の９０％）のコミット削除")

cols <- c("#FF8888", "#8888FF")
i <- 0
plot.new()
for (judge in c(TRUE, FALSE)) {
    i <- i + 1
    par(cex.axis = 2.0)
    if (judge == TRUE) {
        par(cex.axis = 2)
        boxplot(deps$SubDate ~ kind, data = deps, boxwex = 0.25, at = 1:7, col = cols[i], ylim = c(0, 100))
    } else {
        #plot(judgepar, ylim = c(0, 100), add = TRUE, xaxt = "n", yaxt = "n")
        boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.25, at = 1:7 + 0.4, col = cols[i], ylim = c(0, 100), add = TRUE, xaxt = "n", yaxt = "n")
    }
}

par(family = "Japan1GothicBBB")
legend("topleft", legend = legend_name, fill = cols, cex = 1.5)