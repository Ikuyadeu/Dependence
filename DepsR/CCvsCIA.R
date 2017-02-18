# Change Coupling‚ÆChange Impact Analysis‚Ì‡ˆÊ‘ŠŠÖ‚Ì”äŠr
library(dplyr)

project.name <- "vert.x"
#project.roots <- paste(project.name, "roots.csv", sep = "/")
#project.deps <- paste(project.name, "deps.csv", sep = "/")
#project.cc <- paste(project.name, "cc.csv", sep = "/")
project.cia <- paste(project.name, "cia4.csv", sep = "/")

#roots <- read.csv(project.roots, sep = ',', header = TRUE, row.names = NULL)
#deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
#cc <- read.csv(project.cc, sep = ',', header = TRUE, row.names = NULL)
cia <- read.csv(project.cia, sep = ',', header = TRUE, row.names = NULL)
#cc$coupled.count <- as.numeric(cc$coupled.count)
#cc$countpar <- cc$coupled.count / cc$entity.count

#kindset <- c("r", "e", "rr", "er", "re", "ee", "o")

#deps$kind <- factor(deps$kind, levels = kindset)
ranks <- c()
commitNum <- max(cia$commitNo)
cranks <- c()

#cia <- head(cia, nrow(cia) %/% 2)

for (no in 0:commitNum) {
    change.files <- subset(cia, cia$commitNo == no)
    if (nrow(change.files) > 2) {
        change.files$crank <- rank(change.files$SubDate)
        #change.files$erank <- rank(change.files$eSubDate)
        #cranks <- append(cranks, change.files$crank)
        ranks <- append(ranks, cor.test(change.files$crank, change.files$eranking, method = "k", exact = FALSE)["estimate"]$estimate)

        #current <- subset(deps, deps$commitNo == no, c(file_location, SubNo, SubDate))
        
        ##couples <- data.frame()
        ##for (fileno in 1:length(change.files)) {
             ##couples <- rbind(couples, subset(cc, cc$entity == change.file, c(coupled, coupled.count, countpar)))
        ##}
        ##couples.count <- count(couples, coupled, wt = countpar)
        ##cc2 <- merge(current, couples.count, by.x = "file_location", by.y = "coupled")
        ##if (nrow(cc2) > 2) {
            ##cc2$cc.rank <- rank(cc2$n)
            ##cc2$cur.rank <- rank(cc2$SubNo)

            ###print(cor.test(cc2$cur.rank, cc2$cc.rank, method = "s", exact = FALSE)["estimate"]$estimate)
            ###break
            ##ranks <- append(ranks, cor.test(cc2$cur.rank, cc2$cc.rank, method = "s", exact = FALSE)["estimate"]$estimate)
        ##}
    }

}
ranks <- na.omit(ranks)
#print(head(ranks))
#cia$ranking <- cranks
#write.csv(cia, paste(project.name, "cia3.csv", sep = "/"), quote = TRUE, row.names = FALSE)
#boxplot(ranks, ylim = c(-1.0, 1.0))
plot(ranks, ylim = c(1.0, -1.0))
plot.zoo(apply.quarterly(xts(cia$SubDate, cia$date), median))