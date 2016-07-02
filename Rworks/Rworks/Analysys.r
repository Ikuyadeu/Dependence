deps <- read.csv("./dep_3.csv", sep = ',', header = TRUE, row.names = NULL)

deps$file_location <- as.character(deps$file_location)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)
deps$SubNo <- as.numeric(deps$SubNo)

judgeset <- c(TRUE, FALSE)
judge_name <- "author"

for (judge in judgeset){
    #deps2 <- subset(deps, deps$is_merge == judge)
    deps2 <- subset(deps, deps$same_author == judge)
    #print(by(deps, deps$kind, summary))

    dates <- list()
    nos <- list()

    kindset <- c("dependee", "depender", "dependee2", "depender2", "other")

    for (ki in kindset) {
        dep2 <- subset(deps2, deps2$kind == ki)
        dates <- append(dates, list(dep2$SubDate))
        nos <- append(nos, list(dep2$SubNo))
    }

    dates <- append(dates, list(deps2$SubDate))
    nos <- append(nos, list(deps2$SubNo))
    kindset <- append(kindset, c("all"))

    pdf(paste(judge_name, "/date_", judge, ".pdf", sep = ""))
    boxplot(dates, names = kindset, ylim = c(0, 200))

    pdf(paste(judge_name, "/CommitNo_", judge, ".pdf", sep = ""))
    boxplot(nos, names = kindset, ylim = c(0, 300))
}