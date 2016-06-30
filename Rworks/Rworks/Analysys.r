deps <- read.csv("./dep_2.csv", sep = ',', header = TRUE, row.names = NULL)

#deps <- subset(deps, deps$is_merge == "False")

deps$file_location <- as.character(deps$file_location)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)
deps$SubNo <- as.numeric(deps$SubNo)

print(by(deps, deps$kind, summary))

dates <- list()
nos <- list()

kindset <- c("dependee", "depender", "dependee2", "depender2", "other")

for (ki in kindset) {
    dep2 <- subset(deps, deps$kind == ki)
    dates <- append(dates, list(dep2$SubDate))
    nos <- append(nos, list(dep2$SubNo))
}

pdf("date.pdf")
#pdf("merge/date_F.pdf")
boxplot(dates, names = kindset, ylim = c(0, 200))

pdf("no.pdf")
#pdf("merge/no_F.pdf")
boxplot(nos, names = kindset, ylim = c(0, 300))