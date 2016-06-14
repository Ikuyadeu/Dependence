roots <- read.csv("../root.csv", sep = ',', header = TRUE, row.names = NULL)
deps <- read.csv("../dep.csv", sep = ',', header = TRUE, row.names = NULL)

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
        deps$SubNo[dep] <- (fc - min(nc$commitNo))
    }
}
deps <- na.omit(deps)


kindset <- c("from", "to", "from_from", "from_to", "to_from", "to_to")

dates <- list()
nos <- list()
for (ki in kindset) {
    dep2 <- subset(deps, deps$kind == ki)
    dates <- append(dates, list(dep2$SubDate))
    nos <- append(nos, list(dep2$SubNo))
}

#pdf("data.pdf")
#boxplot(dates, names = kindset)
#pdf("no.pdf")
boxplot(nos, names = kindset)
