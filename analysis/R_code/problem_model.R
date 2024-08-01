# Load necessary libraries and data
library(data.table)
library(lme4)
library(multcomp)
library(psych)
dt <- fread("/Users/nrcase/research/cc-repo/cc/df/best/problem_df.csv")

factor_columns <- c("person", "problem", "size", "depth", "gpt", "modality", "Pttn", "Trust", "Exp", "order")
dt[, (factor_columns) := lapply(.SD, as.factor), .SDcols = factor_columns]
str(dt)

non = dt[(Trust == -1)]

dt = dt[(Trust == 1 | Trust == 2)]


model <- glmer(accuracy ~ order + problem + (1 | person), data = dt, family = binomial, 
               control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 1e5)))

print(describe(dt))
print(describe(non))

#K <- matrix( c(-1,0,0,0,0,0,0,0,-1,1,-1,-1,1,1), 1) small v large
#K <- matrix( c(-1,0,0,0,0,0,0,0,-1,-1,1,1,1,1), 1) shallow v deep
#K <-  matrix( c(-1,0,0,0,0,0,0,0,1,-1,-1,-1,-1,-1), 1) B vs the world
#t <- glht(model, linfct = K)
#print(summary(t))

