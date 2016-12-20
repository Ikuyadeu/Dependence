projects <- c("vert.x","egit","egit-github")
kinds <- c("e", "ee", "r", "rr", "er", "re", "o")
merge_name <- "eclipse"

#for (c_kind in kinds) {
    #kind_message <- data.frame()
    #for (project.name in projects) {
        #project.deps <- paste(project.name, "deps.csv", sep = "/")
        #project.messages <- paste(project.name, "message.csv", sep = "/")

        #deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)

        #deps$futureNo <- deps$commitNo - deps$SubNo

        #messages <- read.csv(project.messages, sep = ',', header = TRUE, row.names = NULL)
        #messages$message <- as.character(messages$message)
        
        #future <- subset(deps, deps$kind == c_kind)$futureNo
        #messages$iskind <- messages$commitNo %in% future
        #kind_message <- rbind(kind_message, messages)
    #}
    #print(c_kind)
    #write.csv(kind_message, paste(merge_name, paste(c_kind, "message.csv", sep = ""), sep = "/"), quote = TRUE, row.names = FALSE)
#}


kind_message <- data.frame()
for (project.name in projects) {
    project.messages <- paste(project.name, "message.csv", sep = "/")
    messages <- read.csv(project.messages, sep = ',', header = TRUE, row.names = NULL)
    messages$message <- as.character(messages$message)

    kind_message <- rbind(kind_message, messages)
}
write.csv(kind_message, paste(merge_name, "message.csv", sep = "/"), quote = TRUE, row.names = FALSE)
