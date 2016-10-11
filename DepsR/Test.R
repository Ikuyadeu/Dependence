project.name <- "vert"
project.deps <- paste(project.name, "deps.csv", sep = "/")

deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)
deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location)),]
## 7 colors
#kindset <- c("e", "ee", "r", "rr", "o")
# 5 colors
kindset <- c("depender", "depender2", "dependee", "dependee2", "other")

for (ki in kindset) {
    d1 <- subset(deps, deps$kind == ki)$SubDate
    for (ki2 in kindset) {
        d2 <- subset(deps, deps$kind == ki2)$SubDate
        if (ki != ki2) {
            print(c(ki2, ki))
            print(wilcox.test(d1, d2))
        }
    }
}