library(xts)
#projects <- c("egit", "egit-github", "vert.x")
projects <- c("guava", "retrofit", "okhttp")
projects <- c("guava", "retrofit", "okhttp", "egit", "egit-github", "vert.x")
## 7 colors
#kindset <- c("r", "rr", "e", "ee", "er", "re", "o")
#cols <- c("#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#000000", "#FFFFFF")

## 5 colors
#kindset <- c("r", "rr", "e", "ee", "o")
#cols <- c("#FF0000", "#00FF00", "#0000FF", "#00FFFF", "#FF00FF")

# 3 colors
kindset <- c("r", "e", "o")
kindname <- c("dependee", "depender", "other")
cols <- c("#FF0000", "#00FF00", "#0000FF")

## 3 colors
#kindset <- c("e", "ee", "o")
#kindname <- c("dependee", "dependee2", "other")
#cols <- c("#FF0000", "#00FF00", "#0000FF")

## 2 colors
#kindset <- c("o", "e")
#cols <- c("#FF0000", "#00FF00")

## 2 colors
#kindset <- c("r", "o")
#cols <- c("#FF0000", "#0000FF")

## 2 colors
#kindset <- c("r", "e")
#cols <- c("#FF0000", "#00FF00")

# 2 colors
#kindset <- c("e", "ee")
#cols <- c("#FF0000", "#00FF00")

for (i in 1:length(projects)) {
    project.name <- projects[i]
    print(project.name)
    project.deps <- paste(project.name, "deps.csv", sep = "/")

    deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)

    # times
    # 2016-6-24 3.3.0
    # 2015-12-15 3.2.0
    # 2015-10-7 3.1.0
    # 2015-6-24 3.0.0
    # 2014-12-18 3.0.0 dev
    # 2014-5-27 2.1
    # 2013-7-25 2.0.0
    # 2013-5-14 2.0.0 dev
    # 2012-5-9 1.0.0

    deps$kind <- factor(deps$kind, levels = kindset)

    deps$date <- as.Date(deps$date)
    deps$SubDate <- as.numeric(deps$SubDate)

    deps$file_location <- as.character(deps$file_location)
    deps <- deps[!duplicated(data.frame(deps$commitNo, deps$file_location), fromLast = TRUE),]

    i = 1

    plot.new()
    pdf(paste("C:/Users/YukiUeda/Documents/reserch/mypaper/graduate/fig", paste(project.name, "time.pdf", sep = "/"), sep = "/"),
        width = 16, height = 8)
    for (ki in kindset) {
        dep2 <- subset(deps, deps$kind == ki)
        ts <- apply.yearly(xts(dep2$SubDate, dep2$date), median)
        if (i == 1) {
            last_ts <- ts
            i = 0
        } else {
            last_ts <- na.locf(merge(last_ts, ts))
        }
    }

    plot.zoo(last_ts, ylim = c(0, 600), col = cols, plot.type = "single", ylab = "next changed date", xlab = "date")
    legend("topleft", legend = kindname, fill = cols, cex = 1.0)
    dev.off()
}