project.name <- "egit-github"
project.original <- paste("../", project.name, ".csv", sep = "")
project.roots <- paste(project.name, "roots.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")

#data_set <- read.csv(project.original, sep = ',', header = TRUE, row.names = NULL)
##data_set <- head(data_set, 200)
#data_set$file_location <- as.character(data_set$file_location)
#data_set$author <- as.character(data_set$author)
#data_set$date <- as.Date(data_set$date)

#roots <- subset(data_set, data_set$kind == "root")
#deps <- subset(data_set, data_set$kind != "root")

roots <- read.csv(project.roots, sep = ',', header = TRUE, row.names = NULL)
deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
deps$file_location <- as.character(deps$file_location)
deps$date <- as.Date(deps$date)
deps$commitNo <- as.integer(deps$commitNo)

roots$file_location <- as.character(roots$file_location)
roots$date <- as.Date(roots$date)
roots$commitNo <- as.integer(roots$commitNo)

depslen <- nrow(deps)
rootslen <- nrow(roots)
kindname <- levels(deps$kind)
kindnum <- length(kindname)
for (j in 1:kindnum) {
    k <- kindname[j]
    roots[k] <- NA
}

for (i in 1:rootslen) {
    root <- roots[i,]
    beforeNo <- min(roots[roots$commitNo > root$commitNo & roots$file_location == root$file_location,]$commitNo)
    if (!is.infinite(beforeNo)) {
        for (j in 1:kindnum) {
            k <- kindname[j]
            roots[i,][k] <- sum(deps$kind == k & 
                               deps$file_location == root$file_location & 
                               deps$commitNo > root$commitNo & 
                               deps$commitNo < beforeNo)
        }

    }
}


#getkind <- function(x) {
    #root <- as.data.frame(x)
    ##print(root)
    ##print(mode(x))
    ##print("a")
    #beforeNo <- min(roots[roots$commitNo > root$commitNo & roots$file_location == root$file_location,]$commitNo)
    #if (!is.infinite(beforeNo)) {
        #for (j in 1:kindnum) {
            #k <- kindname[j]
            #x[k] <- any(deps$kind == k &
                               #deps$file_location == root$file_location & 
                               #deps$commitNo > root$commitNo & 
                               #deps$commitNo < beforeNo)
        #}

    #}
    #return(x)
#}



#roots < apply(roots, 1, getkind)

roots <- na.omit(roots)

write.csv(roots, paste(project.name, "roots2.csv", sep = "/"), quote = TRUE, row.names = FALSE)


for (j in 1:kindnum) {
    k <- kindname[j]
    roots[k] <- NA
}

kind_par <- c(sum(roots$e), sum(roots$r), sum(roots$ee), sum(roots$rr), sum(roots$er), sum(roots$re), sum(roots$o))
kind_par <- kind_par / nrow(roots)