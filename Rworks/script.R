roots <- data.frame()
deps <- data.frame()

roots <- read.csv("../root.csv", sep = ',', header = TRUE, row.names = NULL)
deps <- read.csv("../dep.csv", sep = ',', header = TRUE, row.names = NULL)

from <- subset(deps, deps$kind == "from")

for (dep in 1:nrow(from)) {
    print(from$file_location[dep])
    #for (root in 1:nrow(roots)) {
        
    #}
}