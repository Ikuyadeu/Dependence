project.name <- "netty"
project.original <- paste("../", project.name, ".csv", sep = "")
project.roots <- paste(project.name, "roots.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")

data_set <- read.csv(project.original, sep = ',', header = TRUE, row.names = NULL)

data_set$file_location <- as.character(data_set$file_location)
data_set$author <- as.character(data_set$author)
data_set$date <- as.Date(data_set$date)

roots <- subset(data_set, data_set$kind == "root")
deps <- subset(data_set, data_set$kind != "root", c(file_location ,author, date))

deps$SubDate <- NA



getSubdate <- function(x) {
    return()
}

cc$entity.count <- apply(cc, 1, entity)


for (fl in levels(deps$file_location)) {
    froots <- subset(roots, roots$filelocation == fl)
    for (froot in froots[order(froots$commitNo), ]) {
        for (fdep in deps[supply(deps$file_location == fl & deps$commitNo >= froot$commitNo), ]) {
            fdep$Subdate <- froot$date - fdep$date
        }
    }
}



for (dep in 1:nrow(roots)) {
    d <- deps[dep,]
    nc <- max(subset(roots, roots$commitNo <= d$commitNo & roots$file_location == d$file_location)$commitNo)

    if (dep%1000 == 0) {
        print(dep)
    }
    if (nrow(nc) > 0) {
        # ソートを行って一番上
        n <- subset(nc, nc$commitNo == max(nc$commitNo))[1,]
        deps$SubDate[dep] <- n$date - d$date
        deps$SubNo[dep] <- d$commitNo - n$commitNo
        deps$same_author[dep] <- (n$author == d$author)
    }
}
deps <- na.omit(deps)

write.csv(deps, project.deps, quote = TRUE, row.names = FALSE)
write.csv(roots, project.roots, quote = TRUE, row.names = FALSE)