library(reshape)

project.name <- "vert2"
project.deps <- paste(project.name, "deps.csv", sep = "/")

deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)

deps <- tail(deps, nrow(deps) %/% 2)
deps$same_author <- TRUE

deps <- cast(deps, commitNo + file_location + date + author + SubNo + SubDate ~ kind, value = 'same_author')
deps[is.na(deps)] <- FALSE

print(summary(lm(SubDate ~ e + ee + er + r + rr + re + o, data = deps)))