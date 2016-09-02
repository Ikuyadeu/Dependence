data_set <- read.csv("../nettydep.csv", sep = ',', header = TRUE, row.names = NULL)
data_set$file_location <- as.character(data_set$file_location)
data_set$author <- as.character(data_set$author)
data_set$date <- as.Date(data_set$date)

roots <- subset(data_set, data_set$kind == "root")
deps <- subset(data_set, data_set$kind != "root")

deps$SubNo <- NA
deps$SubDate <- NA
deps$same_author <- NA

for (dep in 1:nrow(deps)) {
    d <- deps[dep,]
    nc <- subset(roots, roots$commitNo <= d$commitNo & roots$file_location == d$file_location)
    #nc <- subset(nc, nc$file_location == d$file_location)


    if (nrow(nc) > 0) {
        maxcommit <- max(nc$commitNo)
        nc2 <- subset(nc, nc$commitNo == maxcommit)
        n <- nc2[1,]
        #deps$SubDate[dep] <- min(nc2$date) - fd
        #deps$SubNo[dep] <- fc - max(nc2$commitNo)
        deps$SubDate[dep] <- n$date - d$date
        deps$SubNo[dep] <- d$commitNo - maxcommit
        deps$same_author[dep] <- (n$author == d$author)
    }
}
deps <- na.omit(deps)

write.csv(deps, "nettydep_2.csv", quote=TRUE, row.names = FALSE)
write.csv(roots, "nettyroot_2.csv", quote = TRUE, row.names = FALSE)

#print(by(deps, deps$kind, summary))