deps <- read.csv("./dep_3.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("depender", "depender2", "dependee", "dependee2", "other")

deps$kind <- factor(deps$kind, levels = kindset)

dups <- deps[duplicated(data.frame(deps$commitNo, deps$file_location)),]
deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location)),]

for (dupNo in 1:length(dups)) {
    deps <- subset(deps, deps$commitNo != dups[dupNo]$commitNo | deps$file_location != dups[dupNo]$file_location)
}

#deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)
#deps$SubNo <- as.numeric(deps$SubNo)

#judge_name <- "author"
#judge_name <- "."

cols <- c("#FF8888", "#8888FF")
#plot(0, 0, type = "n",
     #xlim = range(1:(ncol(y) * 3)), # x 軸を広めにとる
     #ylim = range(y), xlab = "Type", ylab = "Weight",
     #axes = FALSE)
i = 0
plot.new()
#pdf("author_test.pdf")

boxplot(deps$SubDate ~ kind, data = deps, ylim = c(0, 200))

#for (judge in c(TRUE, FALSE)) {
    #i = i + 1
    ##deps2 <- deps
    ##deps2 <- subset(deps, deps$same_author == judge)
    #deps2 <- subset(deps, deps$is_merge == judge)
    ##deps2 <- deps
    ##print(by(deps, deps$kind, summary))

    ##dates <- list()
    ##nos <- list()
    ##judgepar <- c()

    ##for (ki in kindset) {
        ##dep2 <- subset(deps2, deps2$kind == ki)
        ##dates <- append(dates, list(dep2$SubDate))
        ##nos <- append(nos, list(dep2$SubNo))
        ##judgepar <- append(judgepar, c(nrow(dep2) / nrow(subset(deps, deps$kind == ki))))
    ##}

    ##dates <- append(dates, list(deps2$SubDate))
    ##nos <- append(nos, list(deps2$SubNo))
    ##judgepar <- append(judgepar, c(nrow(deps2) / nrow(deps)))

    ##kindset <- append(kindset, c("all"))

    ##pdf(paste(judge_name, "/date_", judge, ".pdf", sep = ""))
    ##par(cex.axis = 2.0)
    ##boxplot(dates, names = kindset, ylim = c(0, 200))
    #if (judge == TRUE) {
        #par(cex.axis = 2)
        #boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.25, at = 1:5 - 0.2, col = cols[i], ylim = c(0, 200))
    #} else {
        #boxplot(deps2$SubDate ~ kind, data = deps2, boxwex = 0.25, at = 1:5 + 0.2, col = cols[i], ylim = c(0, 200), add = TRUE, xaxt = "n", yaxt = "n")
    #}
    ##print(t.test(dates[[1]], dates[[3]]))
    ##print(t.test(dates[[3]], dates[[2]]))
    ##print(t.test(dates[[2]], dates[[4]]))
    ##print(t.test(dates[[4]], dates[[5]]))

    ##pdf(paste(judge_name, "/CommitNo_", judge, ".pdf", sep = ""))
    ##boxplot(nos, names = kindset, ylim = c(0, 300))

    ##pdf(paste(judge_name, "/par_", judge, ".pdf", sep = ""))
    ##barplot(judgepar, names = kindset, ylim = c(0, 1))
#}

#par(family = "Japan1GothicBBB")
#legend("topleft", legend = c("マージとなるコミット　　　　　　　", 
                             #"マージではないコミット　　　　　　"),fill = cols, cex = 1.5)
##legend("topleft", legend = c("同じ開発者によるコミット　　　　　　",
                             ##"異なる開発者によるコミット　　　　　"), fill = cols, cex = 1.5)
