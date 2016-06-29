deps <- read.csv("dep_2.csv", sep = ',', header = TRUE, row.names = NULL)
#roots <- read.csv("root_2.csv", sep = ',', header = TRUE, row.names = NULL)

deps$file_location <- as.character(deps$file_location)
deps$date <- as.Date(deps$date)

#print(by(deps, deps$kind, summary))

dates <- list()
nos <- list()

kindset <- c("dependee", "depender", "dependee2", "depender2", "other")

for (ki in kindset) {
    dep2 <- subset(deps, deps$kind == ki)
    dates <- append(dates, list(dep2$SubDate))
    nos <- append(nos, list(dep2$SubNo))
}

pdf("date3.pdf")
boxplot(dates, names = kindset)
pdf("no3.pdf")
boxplot(nos, names = kindset)