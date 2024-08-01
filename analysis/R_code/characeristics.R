library(data.table)
library(psych)
dt <- fread("/Users/nrcase/research/cc-repo/cc/df/best/characteristics.csv")
factor_columns <- c("person",  "GPT", "Modality", "Pttn")
dt[, (factor_columns) := lapply(.SD, as.factor), .SDcols = factor_columns]
str(dt)

wrong = dt[AvgAcc <= 0.5, AvgAcc]

print(length(wrong))

