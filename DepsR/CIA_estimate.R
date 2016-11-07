library(reshape2)
library(plyr)

projects <- c("vert.x")

project.name <- projects
print(project.name)
project.deps <- paste(project.name, "deps.csv", sep = "/")
deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)

#deps <- deps[duplicated(data.frame(deps$commitNo, deps$file_location, deps$kind)),]
print(head(deps))
#deps <- subset(deps, !duplicated(data.frame(commitNo, file_location, kind)))
deps$same_author <- TRUE
deps <- dcast(data = deps, formula = commitNo + file_location + date + author + SubNo + SubDate ~ kind, fun.aggregate = length)
deps[is.na(deps)] <- 0
print(head(deps))
print("casted")
deps2 <- tail(deps, nrow(deps) %/% 2)
m <- lm(SubDate ~ e + ee + er + r + rr + re + o, data = deps2)

deps$eSubDate <- predict(m, newdata = deps)
write.csv(deps, paste(project.name, "cia.csv", sep = "/"), quote = TRUE, row.names = FALSE)
print(tail(subset(deps, re >= 2)))
# SIGSS 3/9 ~ 3/10 