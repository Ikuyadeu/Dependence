project.name <- "vert.x"
project.deps <- paste(project.name, "deps.csv", sep = "/")
project.messages <- paste(project.name, "message.csv", sep = "/")

deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)

deps$futureNo <- deps$commitNo - deps$SubNo

messages <- read.csv(project.messages, sep = ',', header = TRUE, row.names = NULL)
messages$message <-as.character(messages$message)
kinds <- levels(deps$kind)
for (kind2 in 1:length(kinds)) {
    future <- subset(deps, deps$kind == kinds[kind2])$futureNo
    messages$iskind <- messages$commitNo %in% future
    write.csv(messages, paste(project.name, paste(kinds[kind2], "message.csv", sep = ""), sep = "/"), quote = TRUE, row.names = FALSE)
}