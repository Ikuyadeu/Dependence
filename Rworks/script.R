roots <- data.frame()
deps <- data.frame()

roots <- read.csv("../root.csv", sep = ',', header = TRUE, row.names = NULL)
deps <- read.csv("../dep.csv", sep = ',', header = TRUE, row.names = NULL)

from <- subset(deps, deps$kind == "from")
print(min(from$commitNo))

for (dep in 1:nrow(from)) {
    fc = from$commitno[dep]
    fl = from$file_location[dep]
    nextchange <- subset(roots, 
                        (roots$commitno > fc) &&
                         roots$file_location == fl, c(date, commitNo))
    print(roots$commitNo)

    #for (root in 1:nrow(roots)) {
        
    #}
}