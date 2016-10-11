project.name <- "egit"
project.roots <- paste(project.name, "roots.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")
project.cc <- paste(project.name, "cc4.csv", sep = "/")

roots <- read.csv(project.roots, sep = ',', header = TRUE, row.names = NULL)
deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
cc <- read.csv(project.cc, sep = ',', header = TRUE, row.names = NULL)

kindset <- c("r", "rr", "e", "ee", "er", "re", "o")

library(dplyr)

print(head(deps))


#commitNum <- max(roots$commitNo)
#for (no in 0:commitNum) {
    #change.file <- subset(roots, roots$commitNo == no)$file_location

    #current <- subset(deps, deps$commitNo == no)
    #current <- current[order(current$SubDate),]$SubDate
    
    #couples <- subset(cc, cc$entity %in% change.file)
    #couples <- couples[order(couples$coupled.count),]$file_location

    #cia <- subset(deps, deps$commitNo == no)
    #print(head(cia))
    ##cia <- cia[order(cia$kind),]$file_location
    #cia <- cia[order(cia$kind),]$SubDate

    ##print(wilcox.test(current, cia))
    ##wilcox.test(current, couples)

    #if (no %% 100 == 0) {
        #print(head(cia))
        #print(head(current))


        #break
        #print(commitNum - no)
        #print(wilcox.test(current, cia))
        #break
    #}

#}