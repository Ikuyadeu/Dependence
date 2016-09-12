deps <- read.csv("vert/deps.csv", sep = ',', header = TRUE, row.names = NULL)

kindset <- c("e", "ee", "r","rr","er","re", "o")

deps$kind <- factor(deps$kind, levels = kindset)
deps$file_location <- as.character(deps$file_location)

#dups <- deps[duplicated(data.frame(deps$commitNo, deps$file_location)),]
deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location)),]

#deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)
#deps$SubNo <- as.numeric(deps$SubNo)
print(by(deps$SubDate, deps$kind, summary))
#judge_name <- "author"
#judge_name <- "."

#cols <- c("#FF8888", "#8888FF")
#plot(0, 0, type = "n",
     #xlim = range(1:(ncol(y) * 3)), # x Ž²‚ðL‚ß‚É‚Æ‚é
     #ylim = range(y), xlab = "Type", ylab = "Weight",
     #axes = FALSE)
#i = 0
#plot.new()
#pdf("author_test.pdf")

#boxplot(deps$SubDate ~ kind, data = deps, ylim = c(0, 200))
boxplot(deps$SubDate ~ kind, data = deps, ylim = c(0, 100))