library(psych)
library(data.table)
dt <- fread("/Users/nrcase/research/cc-repo/cc/filtered_dataframe.csv")

# Convert specified columns to factors (categorical variables)
factor_columns <- c("person", "problem", "size", "depth", "gpt", "modality", "Pttn", "Trust", "Exp")
dt[, (factor_columns) := lapply(.SD, as.factor), .SDcols = factor_columns]
#str(dt)

