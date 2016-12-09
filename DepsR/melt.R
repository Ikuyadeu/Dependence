library(reshape2)
library(plyr)

project.name <- "vert.x"
project.cia <- paste(project.name, "cia5.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")

deps <- read.csv(project.cia, sep = ',', header = TRUE, row.names = NULL)
deps <- subset(deps, TRUE, c("commitNo", "file_location", "date", "author", "SubNo", "SubDate", "same_author", "e", "ee", "r", "rr", "o", "er", "re"))
deps <- melt(data = deps, id.vars = c("commitNo", "file_location", "date", "author", "SubNo", "SubDate", "same_author"),
            variable.name="kind",na.rm = TRUE)

write.csv(deps, project.deps, quote = TRUE, row.names = FALSE)