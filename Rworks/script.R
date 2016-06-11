roots <- data.frame()
deps <- data.frame()

roots <- read.csv("root.csv", sep = ',', header = FALSE)
deps <- read.csv("dep.csv", sep = ',', header = FALSE)

for (dep in 1:nrow(deps)) {
    for (root in 1:nrow(roots)) {

    }
}