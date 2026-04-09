library(rpart)
library(rpart.plot)
library(caret)

dataset <- read.csv("C:/Users/AI_LAB/Desktop/iris.csv")
dataset$Species <- as.factor(dataset$variety)

set.seed(123)
trainIndex <- createDataPartition(dataset$Species, p = 0.8, list = FALSE)
trainData <- dataset[trainIndex, ]
testData <- dataset[-trainIndex, ]

dt_model <- rpart(Species ~ ., data = trainData, method = "class")
rpart.plot(dt_model)

predictions <- predict(dt_model, testData, type = "class")
confMatrix <- confusionMatrix(predictions, testData$Species)
print(confMatrix)