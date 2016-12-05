library(reshape2)
library(plyr)

project.name <- "vert.x"
project.original <- paste("../", project.name, ".csv", sep = "")
project.roots <- paste(project.name, "roots.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")

data_set <- read.csv(project.original, sep = ',', header = TRUE, row.names = NULL)

data_set <- head(data_set, 500)
data_set$file_location <- as.character(data_set$file_location)
data_set$author <- as.character(data_set$author)
data_set$date <- as.Date(data_set$date)

roots <- subset(data_set, data_set$kind == "root")
write.csv(roots, project.roots, quote = TRUE, row.names = FALSE)

deps <- subset(data_set, data_set$kind != "root")
#deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location, deps$kind)),]

deps$SubNo <- NA
deps$SubDate <- NA
deps$same_author <- TRUE

deps <- dcast(data = deps, formula = commitNo + file_location + date + author ~ kind,
              fun.aggregate = length, value.var = "same_author", fill = 0)

write.csv(deps, project.deps, quote = TRUE, row.names = FALSE)