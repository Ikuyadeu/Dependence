data_set <- read.csv("../../dep.csv", sep = ',', header = TRUE, row.names = NULL)
data_set$file_location <- as.character(data_set$file_location)
data_set$date <- as.Date(data_set$date)

roots <- subset(data_set, data_set$kind == "root")
deps <- subset(data_set, data_set$kind != "root")

deps$SubNo <- NA
deps$SubDate <- NA
deps$same_author <- NA

for (dep in 1:nrow(deps)) {
    fc <- deps$commitNo[dep]
    fl <- deps$file_location[dep]
    fd <- deps$date[dep]

    nc <- subset(roots, roots$commitNo <= fc)
    nc <- subset(nc, nc$file_location == fl)
    maxcommit <- max(nc$commitNo)
    nc <- subset(nc, nc$commitNo == maxcommit)

    if (nrow(nc) > 0) {
        #deps$SubDate[dep] <- min(nc$date) - fd
        #deps$SubNo[dep] <- fc - max(nc$commitNo)
        deps$SubDate[dep] <- nc$date[1] - fd
        deps$SubNo[dep] <- fc - nc$commitNo[1]
        deps$same_author <- (nc$author[1] == deps$author)
    }
}
deps <- na.omit(deps)

write.csv(deps, "dep_3.csv", quote=TRUE, row.names = FALSE)
write.csv(roots, "root_3.csv", quote = TRUE, row.names = FALSE)

print(by(deps, deps$kind, summary))