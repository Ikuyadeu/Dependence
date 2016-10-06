roots <- read.csv("vert/roots.csv", sep = ',', header = TRUE, row.names = NULL)
library(dplyr)

flist <- levels(roots$file_location)
flist <- flist[grep(".java$", flist)]

cc <- expand.grid(entity = flist, coupled = flist)
cc <- subset(cc, unclass(entity) < unclass(coupled))

entity_num <- function(x) {
    return(sum(roots$file_location == x))
}

num <- lapply(flist, entity_num)
f <- data.frame(list = flist, num = sapply(num, "[", 1))


entity <- function(x) {
    return(f[f$list == x[1], 2])
}

couple <- function(x) {
    return(as.numeric(sum(cc2$entity == x[1] & cc2$coupled == x[2])[1]))
}

cc2 <- data.frame()

commitNum <- max(roots$commitNo)
for (no in 0:commitNum) {
    flist2 <- subset(roots, roots$commitNo == no)$file_location
    flist2 <- flist2[grep(".java$", flist2)]
    couples <- expand.grid(entity = flist2, coupled = flist2)
    cc2 <- rbind(cc2, subset(couples, unclass(entity) < unclass(coupled)))
    if (no %% 1000 == 0) {
        print(commitNum - no)
    }
}

print(nrow(cc2))

cc$entity.count <- apply(cc, 1, entity)
print("GET ENTITY")

cc$coupled.count <- apply(cc, 1, couple)
cc[is.na(cc)] <- 0

print(head(cc))
write.csv(cc, "vert/cc.csv", quote = TRUE, row.names = FALSE)
