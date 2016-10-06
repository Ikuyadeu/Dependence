roots <- read.csv("vert/roots.csv", sep = ',', header = TRUE, row.names = NULL)

flist <- levels(roots$file_location)
flist <- flist[grep(".java$", flist)]

cc <- expand.grid(entity = flist, coupled = flist)
cc <- subset(cc, unclass(entity) < unclass(coupled))


entity_num <- function(x) {
    return(nrow(subset(roots, x == roots$file_location)))
}

f <- data.frame(list = flist, num = lapply(flist, entity_num))


entity <- function(x) {
    return(subset(f, f$list == x[1])$num)
}

couple <- function(x) {
    return(nrow(subset(cc2, x[1] == cc2$entity & x[2] == cc2$coupled)))
}

#count <- function(x) {
    #return(list(
    #subset(f, f$list == x[1])$num,
    #nrow(subset(cc2, x[1] == cc2$entity & x[2] == cc2$coupled))
    #)
    #)
#}

cc2 <- data.frame()

commitNum <- max(roots$commitNo)
for (no in 0:commitNum) {
    flist2 <- subset(roots, roots$commitNo == no)$file_location
    flist2 <- flist[grep(".java$", flist2)]
    couples <- expand.grid(entity = flist2, coupled = flist2)
    cc2 <- rbind(cc2, subset(couples, unclass(entity) < unclass(coupled)))
    if (no %% 1000 == 0) {
        print(commitNum - no)
    }
}

print(nrow(cc))

#cccount <- apply(cc, 1, count)
#cc$entity.count <- cccount[1]
#cc$coupled.count <- cccount[2]

cc$entity.count <- apply(cc, 1, entity)
print("GET ENTITY")

cc$coupled.count <- apply(cc, 1, couple)

print(head(cc))
write.csv(cc, "vert/cc.csv", quote = TRUE, row.names = FALSE)
