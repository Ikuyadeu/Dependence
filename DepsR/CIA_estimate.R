library(reshape2)
library(plyr)

project.name <- "vert.x"
project.deps <- paste(project.name, "cia3.csv", sep = "/")

print(project.name)
deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)


##data_set <- read.csv(project.original, sep = ',', header = TRUE, row.names = NULL)
###data_set <- head(data_set, 200)
##data_set$file_location <- as.character(data_set$file_location)
##data_set$author <- as.character(data_set$author)
##data_set$date <- as.Date(data_set$date)

##roots <- subset(data_set, data_set$kind == "root")
##deps <- subset(data_set, data_set$kind != "root")

##deps <- deps[duplicated(data.frame(deps$commitNo, deps$file_location, deps$kind)),]
#print(head(deps))
##deps <- subset(deps, !duplicated(data.frame(commitNo, file_location, kind)))
#deps$same_author <- TRUE
#deps <- dcast(data = deps, formula = commitNo + file_location + date + author ~ kind, fun.aggregate = length)
#deps[is.na(deps)] <- 0
#print(head(deps))
#print("casted")
deps2 <- tail(deps, nrow(deps) %/% 2)
m <- glm(same_author ~ e + ee + r + rr + re + er + o, data = deps2, family = binomial)
deps$issame <- predict(m, type="response", newdata = deps)
#deps$eranking <- predict(m, newdata = deps)
write.csv(deps, paste(project.name, "cia5.csv", sep = "/"), quote = TRUE, row.names = FALSE)

print(head(subset(deps, re >= 2)))
# SIGSS 3/9 ~ 3/10 