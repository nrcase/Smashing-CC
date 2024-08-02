# Load necessary libraries and data
library(data.table)
library(lme4)
library(multcomp)
library(psych)
dt <- fread("/Users/nrcase/research/cc-repo/cc/df/best/people_df.csv")
dt$GPT = as.factor(dt$GPT)
dt$Modality = as.factor(dt$Modality)
dt$Pttn = as.factor(dt$Pttn)
dt$GPT = relevel(dt$GPT, ref = "none")
str(dt)

model <- lm(AvgAcc ~ Modality, data = dt)
print(summary(model))

#K <- matrix(c(0, 1,0,0,-1),1)
#t <- glht(model, linfct = K)
#print(summary(t))


