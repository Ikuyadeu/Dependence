kinds <- c("e", "ee", "r", "rr", "er", "re", "o")
project.name <- "eclipse"

kind_message <- data.frame()
allorone <- "one_"

message.name <- paste(project.name, paste(allorone, "message2.csv", sep = ""), sep = "/")
kind_message <- read.csv(message.name, sep = ',', header = TRUE, row.names = NULL)

for (kind in kinds) {
    project.messages <- paste(project.name, paste(allorone, paste(kind, "message.csv", sep = ""), sep = ""), sep = "/")
    messages <- read.csv(project.messages, sep = ',', header = TRUE, row.names = NULL)
    colnames(messages) <- c("word", kind)
    kind_message <- merge(kind_message, messages, by = "word", all = T)
}
kind_message <- kind_message[order(kind_message$score, decreasing = T),]
kind_message[is.na(kind_message)] <- 0
write.csv(kind_message, paste(project.name, paste(allorone, "message2.csv"), sep = "/")
            , quote = TRUE, row.names = FALSE)
