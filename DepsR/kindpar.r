project.name <- "egit-github"
project.roots <- paste(project.name, "roots2.csv", sep = "/")
roots <- read.csv(project.roots, sep = ',', header = TRUE, row.names = NULL)

kind_name <- c("e", "r", "ee", "rr", "er", "re", "o")
#kind_par <- c(sum(roots$e), sum(roots$r), sum(roots$ee), sum(roots$rr), sum(roots$er), sum(roots$re), sum(roots$o))

kind_par <- list(roots$e, roots$r, roots$ee, roots$rr, roots$er, roots$re, roots$o)
kind_par <- sapply(kind_par, mean)

##kind_par <- kind_par / nrow(roots)

barplot(kind_par, names.arg = kind_name, ylim = c(0.0, 0.8))