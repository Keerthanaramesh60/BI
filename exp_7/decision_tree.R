library(rpart)
library(rpart.plot)
library(tidyverse)

dataset <- read.csv("C:/Users/AI_LAB/Desktop/iris.csv")
dataset$variety <- as.factor(dataset$variety)

set.seed(123)
trainIndex <- sample(1:nrow(dataset), 0.8 * nrow(dataset))
trainData <- dataset[trainIndex, ]
testData <- dataset[-trainIndex, ]

dt_model <- rpart(variety ~ ., data = trainData, method = "class")
rpart.plot(dt_model)
predictions <- predict(dt_model, testData, type = "class")
confMatrix <- confusionMatrix(predictions, testData$Species)
print(confMatrix)