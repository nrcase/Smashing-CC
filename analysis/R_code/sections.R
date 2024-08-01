library(data.table)
library(psych)

section1 <- fread("/Users/nrcase/research/cc-repo/cc/df/best/section1.csv")
section2 <- fread("/Users/nrcase/research/cc-repo/cc/df/best/section2.csv")

s1_acc = section1[["AvgAcc"]]
s2_acc = section2[["AvgAcc"]]

done = wilcox.test(s1_acc, s2_acc)
print(done)