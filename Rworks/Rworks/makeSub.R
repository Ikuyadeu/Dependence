data_set <- read.csv("../../dep.csv", sep = ',', header = TRUE, row.names = NULL)

roots <- subset(data_set, data_set$kind == "root")
deps <- subset(data_set, data_set$kind != "root")

roots$file_location <- as.character(roots$file_location)
deps$file_location <- as.character(deps$file_location)

roots$date <- as.Date(roots$date)
deps$date <- as.Date(deps$date)

deps$SubNo <- NA
deps$SubDate <- NA

for (dep in 1:nrow(deps)) {
    fc <- deps$commitNo[dep]
    fl <- deps$file_location[dep]
    fd <- deps$date[dep]

    nextchange <- subset(roots, roots$commitNo <= fc)
    nc <- subset(nextchange, nextchange$file_location == fl)
    if (nrow(nc) > 0) {
        deps$SubDate[dep] <- min(nc$date) - fd
        deps$SubNo[dep] <- fc - max(nc$commitNo)
    }
}
deps <- na.omit(deps)

write.csv(deps, "dep_2.csv", quote=FALSE, row.names = FALSE)
write.csv(roots, "root_2.csv", quote = FALSE, row.names = FALSE)


print(by(deps, deps$kind, summary))
