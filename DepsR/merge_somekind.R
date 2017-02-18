# •¡”‚ÌˆË‘¶ŠÖŒW‚Ìî•ñ‚ğ‚Â‚È‚°‚é
kinds <- c("e", "ee", "r", "rr")
project.name <- "eclipse"

kind_message <- data.frame()
allorone <- "one_"

getmax <- function(x) {
    kinds.order <- order(c(x["e"], x["ee"], x["r"], x["rr"]))
    return(paste(kinds[kinds.order[1]], kinds[kinds.order[2]], sep = "_"))
}


message.name <- paste(project.name, paste(allorone, "message3.csv", sep = ""), sep = "/")
kind_message <- read.csv(message.name, sep = ',', header = TRUE, row.names = NULL)
kind_message$maxkind <- apply(kind_message, 1, getmax)


write.csv(kind_message, paste(project.name, paste(allorone, "message3.csv", sep = ""), sep = "/")
            , quote = TRUE, row.names = FALSE)
