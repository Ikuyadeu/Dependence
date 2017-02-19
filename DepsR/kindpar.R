#projects <- c("vert.x", "egit", "egit-github")
projects <- c("guava", "retrofit", "okhttp")


getpar <- function(x) {
    #return(sum(x) / length(x))
    return(sum(x))
}

for (i in 1:length(projects)) {
    project.name <- projects[i]
    print(project.name)
    #project.roots <- paste(project.name, "roots2.csv", sep = "/")
    #roots <- read.csv(project.roots, sep = ',', header = TRUE, row.names = NULL)


    project.deps <- paste(project.name, "deps.csv", sep = "/")
    deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)
    deps$dup <- duplicated(data.frame(deps$commitNo, deps$file_location), fromLast = TRUE)
    #deps$same_author <- as.logical(deps$same_author)
    #kind_name <- c("e", "r", "ee", "rr", "er", "re", "o")
    #kind_par <- c(sum(roots$e), sum(roots$r), sum(roots$ee), sum(roots$rr), sum(roots$er), sum(roots$re), sum(roots$o))

    #kind_par <- list(roots$e, roots$r, roots$ee, roots$rr, roots$er, roots$re, roots$o)
    #kind_par <- sapply(kind_par, mean)

    ##kind_par <- kind_par / nrow(roots)

    kind_par <- tapply(deps$same_author, deps$kind, getpar)
    #print(levels(deps$kind))
    kind_par <- append(kind_par, sum(kind_par))
    print(kind_par)

    #prop.table

    #deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location), fromLast = TRUE),]
    #kind_par2 <- tapply(deps$same_author, deps$kind, getpar)

    ##kind_par2 <- 1 - kind_par

    #kind_par <- rbind(kind_par, kind_par2)
    #barplot(kind_par, beside = T, ylim = c(0.0, 1.0))
}