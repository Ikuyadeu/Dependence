project.name <- "vert"
project.roots <- paste(project.name, "roots.csv", sep = "/")
project.deps <- paste(project.name, "deps.csv", sep = "/")

deps <- read.csv("./newdep_2.csv", sep = ',', header = TRUE, row.names = NULL)

## 7 colors
#kindset <- c("e", "ee", "r", "rr", "o")
# 5 colors
kindset <- c("depender", "depender2", "dependee", "dependee2", "other")

## 3 colors
##kindset <- c("r", "e", "o")

### 2 colors
##kindset <- c("o", "e")

### 2 colors
##kindset <- c("r", "o")

### 2 colors
##kindset <- c("r", "e")

## 2 colors
##kindset <- c("e", "ee")

deps$kind <- factor(deps$kind, levels = kindset)
deps$date <- as.Date(deps$date)
deps$SubDate <- as.numeric(deps$SubDate)

deps$file_location <- as.character(deps$file_location)
deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location)),]
plot.new()
par(cex.axis = 2.5)
par(tck = 1)
par(family = "Japan1")
par(mai = c(0.5, 0.75, 0.5, 4))
par(xpd = F)
boxplot(deps$SubDate ~ kind, data = deps, 
    ylim = c(0, 200), 
    names = c("depender", "depender2", "dependee", "dependee2", "other"), 
    xaxt = "n",
    lwd = 2.5,
    yaxp = c(0, 200, 4),
    yaxs = "i"
    )
par(tck = NA)
axis(side = 2,
     tck = 1,
     lty = 2,
     labels = F,
     lwd.ticks = 1,
     yaxp = c(0, 200, 20)
     )
axis(side = 1,
     at = 1:5, 
     labels = c("r", "rr", "e", "ee", "o"))
par(xpd = T)
legend(x = par()$usr[2] * 0.7, y = par()$usr[4], 
     legend = c("r   :depender", "rr  :depender2", "e  :dependee", "ee:dependee2", "o  :other"),
     cex = 2.5,
     bty = "n",
     xjust = 0,
     inset = c(0, 0)
     )

#print(by(deps, deps$kind, summary))
#i = 0
#for (ki in kindset) {
    #d1 <- subset(deps, deps$kind == ki)$SubDate
    #for (ki2 in kindset) {
        #d2 <- subset(deps, deps$kind == ki2)$SubDate
        #print(c(ki2,ki))
        #print(t.test(d1, d2, var.equal = F))
    #}
#}