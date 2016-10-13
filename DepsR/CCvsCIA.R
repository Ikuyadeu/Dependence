project.name <- "egit"
project.roots <- paste(project.name, "roots.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")
project.cc <- paste(project.name, "cc4.csv", sep = "/")

roots <- read.csv(project.roots, sep = ',', header = TRUE, row.names = NULL)
deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
cc <- read.csv(project.cc, sep = ',', header = TRUE, row.names = NULL)

kindset <- c("r", "e", "rr", "er", "re", "ee", "o")

deps$kind <- factor(deps$kind, levels = kindset)

library(dplyr)

#print(head(deps))


commitNum <- max(roots$commitNo)
for (no in 0:commitNum) {
    change.file <- subset(roots, roots$commitNo == no)$file_location

    current <- subset(deps, deps$commitNo == no)
    current.date <- rank(current[order(current$SubNo),]$SubNo)
    
    couples <- subset(cc, cc$entity %in% change.file)
    couples <- couples[order(couples$coupled.count),]$file_location



    cia <- subset(deps, deps$commitNo == no)
    #print(head(cia))
    #cia <- cia[order(cia$kind),]$file_location
    cia.date <- rank(cia[order(cia$kind),]$SubNo)

    #print(wilcox.test(current, cia))
    #wilcox.test(current, couples)

    if (no == 81) {
        kindlength = nrow(subset(cia, cia$kind == "r"))
        print(kindlength)
        print(head(current.date, n = kindlength))
        print(head(cia.date, n = kindlength))

        print(commitNum - no)
        #print(wilcox.test(current.date, cia.date))
        print(wilcox.test(head(cia.date, n = kindlength), head(current.date, n = kindlength)))
        break
    }

}