# Load necessary libraries and data
library(data.table)
library(lme4)
library(multcomp)
library(psych)
dt <- fread("/Users/nrcase/research/cc-repo/cc/df/best/people_df.csv")
str(dt)

model <- lm(AvgAcc ~ Years + OO + ProgExp + Compared, data = dt)
print(summary(model))

#anova <- aov(accuracy ~ Years + OO + ProgExp + Compared, data = dt)
#print(summary(anova))

#K <- matrix(c(0, -1, -1, -1, 1), 1)
#t <- glht(model, linfct = K)
#print(summary(t))
