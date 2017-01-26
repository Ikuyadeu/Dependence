#projects <- c("egit", "egit-github", "vert.x")
#projects <- c("guava", "retrofit", "okhttp")
projects <- c("guava", "retrofit", "okhttp","egit", "egit-github", "vert.x")

## 7 colors
kindset <- c("e", "ee", "r", "rr", "o")

kindname <- c("depender", "depender2", "dependee", "dependee2", "other")
#cols <- c("#FF8888","#FF8800","#888888","#888888" ,"#FFFFFF")
## 7 colors
#kindset <- c("e", "ee", "o")
#cols <- c("#FF8888", "#FF8800", "#FFFFFF")
# 5 colors
#kindset <- c("depender", "depender2", "dependee", "dependee2", "other")
#kindname <- kindset
cols <- c("#FF8888", "#CC99FF", "#00CC88", "#0088FF", "#CCCCCC")
cols <- c("#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF")
### 2 colors
##kindset <- c("o", "e")

### 2 colors
##kindset <- c("r", "o")

### 2 colors
##kindset <- c("r", "e")

## 2 colors
##kindset <- c("e", "ee")

for (i in 1:length(projects)) {
    project.name <- projects[i]
    #project.name <- ""
    print(project.name)
    project.deps <- paste(project.name, "deps.csv", sep = "/")

    #deps <- read.csv("newdep_2.csv", sep = ',', header = TRUE, row.names = NULL) # for fose
    deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)

    ## 3 colors
    ##kindset <- c("r", "e", "o")

    #toother <- function(x) {
    #x <- ifelse(x %in% kindset, x, "other")
    #return(x)
    #}

    #deps$kind <- apply(deps$kind, 2,toother)
    
    kind.num <- length(kindset)
    #deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location), fromLast = TRUE),]

    #print(by(deps, deps$kind, summary))

    deps$kind <- factor(deps$kind, levels = kindset)
    deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location, deps$kind), fromLast = FALSE),]

    deps$commitNo <- as.numeric(deps$commitNo)

    deps$date <- as.Date(deps$date)
    deps$SubDate <- as.numeric(deps$SubDate)

    #deps$file_location <- as.character(deps$file_location)
    pdf(paste("C:/Users/YukiUeda/Documents/reserch/mypaper/graduate/fig", paste(project.name, "dupbox.pdf", sep = "/"), sep = "/"),
        width=16,height=8)
    #width=1627, height=857
    par(cex.axis = 2.5)
    par(tck = 1)
    par(mar = c(3, 4, 2, 1) + 0.1)
    par(xpd = F)
    boxplot(deps$SubDate ~ kind, data = deps,
    ylim = c(0, 150),
    xaxt = "n",
    lwd = 2.5,
    yaxp = c(0, 200, 4),
    yaxs = "i",
    col = cols,
    main = project.name
    )
    par(tck = NA)
    #axis(side = 2,
    #tck = 1,
    #lty = 2,
    #labels = F,
    #lwd.ticks = 1,
    #yaxp = c(0, 150, 20)
    #)
    axis(side = 1,
    at = 1:kind.num,
    labels = kindname)
    par(xpd = T)
    dev.off()
    #legend(x = par()$usr[2] * 0.7, y = par()$usr[4], 
    #legend = c("r   :depender", "rr  :depender2", "e  :dependee", "ee:dependee2", "o  :other"),
    #cex = 2.5,
    #bty = "n",
    #xjust = 0,
    #inset = c(0, 0)
    #)

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
}