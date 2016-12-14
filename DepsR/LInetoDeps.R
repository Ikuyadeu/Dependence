project.name <- "vert.x"
project.deps <- paste(project.name, "deps.csv", sep = "/")
project.lines <- paste(project.name, "lines.csv", sep = "/")

deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
deps$futureNo <- deps$commitNo - deps$SubNo
deps$file_location <- as.character(deps$file_location)

lines <- read.csv(project.lines, sep = ',', header = TRUE, row.names = NULL)
lines$file_path <- as.character(lines$file_path)
lines$commit_no <- as.numeric(lines$commit_no)

deps <- merge(deps, lines, by.x = c("futureNo", "file_location"), by.y = c("commit_no", "file_path"))
write.csv(deps, paste(project.name, "linedeps.csv", sep = "/"), quote = TRUE, row.names = FALSE)
