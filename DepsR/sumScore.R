library(dplyr)

project.name <- "eclipse"
project.deps <- paste(project.name, "one_double_message.csv", sep = "/")

deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
deps <- count(deps, before_word, after_word, wt = score)
deps <- deps[order(deps$n, decreasing = TRUE),]

#write.csv(deps, paste(project.name, "one_double_message2.csv", sep = "/"), quote = TRUE, row.names = FALSE)