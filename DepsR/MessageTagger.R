library(koRpus) 
set.kRp.env(TT.cmd = "C:\\TreeTagger\\cmd", lang = "en")


project.name <- "egit-github"
kinds <- c("e", "ee")

for (kind2 in 1:length(kinds)) {
    print(kinds[kind2])
    tagged.text <- treetag(paste(project.name, paste(kinds[kind2], "message.txt", sep = ""), sep = "/")
                    , treetagger = "manual", lang = "en",
                    TT.options = list(path = "C:\\TreeTagger", preset = "en"))
    print(kinds[kind2])
    print(tagged.text)
    freq.analysis.res <- freq.analysis(tagged.text, corp.freq = NULL)
    print(tanggdText(freq.analysis.res))

    break
    #future <- subset(deps, deps$kind == kinds[kind2])$futureNo
    #mes2 <- subset(messages, messages$commitNo %in% future)$message
    #write(mes2, paste(project.name, paste(kinds[kind2], "message.txt", sep = ""), sep = "/"))
}