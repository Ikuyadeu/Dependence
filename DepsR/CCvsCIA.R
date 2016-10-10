project.name <- "egit"
project.roots <- paste(project.name, "roots.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")
project.cc <- paste(project.name, "cc4.csv", sep = "/")

roots <- read.csv(project.roots, sep = ',', header = TRUE, row.names = NULL)
deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
cc <- read.csv(project.cc, sep = ',', header = TRUE, row.names = NULL)
library(dplyr)

commitNum <- max(roots$commitNo)
for (no in 0:commitNum) {
    change.file <- subset(roots, roots$commitNo == no)$file_location
    couples <- subset(cc, cc$entity == change.file)$coupled


}