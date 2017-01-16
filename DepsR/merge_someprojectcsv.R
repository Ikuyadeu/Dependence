projects <- c("vert.x","egit","egit-github")
kinds <- c("e", "ee", "r", "rr", "er", "re", "o")
merge_name <- "eclipse"

getmessage <- function(x) {
    return(messages[messages$commitNo == x, 2])
}

getmessage2 <- function(x) {
    return(messages[messages$commitNo == x[2], 2])
}


#for (c_kind in kinds) {
kind_message <- data.frame()
for (project.name in projects) {
    project.deps <- paste(project.name, "deps.csv", sep = "/")
    project.messages <- paste(project.name, "message.csv", sep = "/")

    deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
    
    deps <- data.frame(commitNo = deps$commitNo, futureNo = deps$commitNo - deps$SubNo)
    messages <- read.csv(project.messages, sep = ',', header = TRUE, row.names = NULL)
    messages$message <- as.character(messages$message)
    deps$message <- lapply(deps$commitNo, getmessage)
    #print(head(deps))
    deps$fmessage <- lapply(deps$futureNo, getmessage)
    #deps$fmessage <- apply(deps, 1,getmessage2)
    #future <- subset(deps, deps$kind == c_kind)$commitNo
    #messages$iskind <- messages$commitNo %in% future
    kind_message <- rbind(kind_message, deps)
}
#print(c_kind)
#print(head(kind_message))
write.csv(kind_message, paste(merge_name, "double_message.csv", sep = "/"), quote = TRUE, row.names = FALSE)

#write.csv(kind_message, paste(merge_name, paste(c_kind, "message_b.csv", sep = ""), sep = "/"), quote = TRUE, row.names = FALSE)
#}


#kind_message <- data.frame()
#for (project.name in projects) {
    #project.messages <- paste(project.name, "message.csv", sep = "/")
    #messages <- read.csv(project.messages, sep = ',', header = TRUE, row.names = NULL)
    #messages$message <- as.character(messages$message)

    #kind_message <- rbind(kind_message, messages)
#}
#write.csv(kind_message, paste(merge_name, "message.csv", sep = "/"), quote = TRUE, row.names = FALSE)
