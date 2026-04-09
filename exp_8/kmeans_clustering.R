library(ggplot2)
library(cluster)

dataset <- read.csv("C:/Users/AI_LAB/Desktop/iris.csv")
df <- dataset[, sapply(dataset, is.numeric)]

set.seed(123)
k <- 3

kmeans_model <- kmeans(df, centers = k, nstart = 25)
dataset$Cluster <- as.factor(kmeans_model$cluster)

ggplot(dataset, aes(x = dataset[,1], y = dataset[,2], color = Cluster)) +
  geom_point(size = 3) +
  labs(title = "K-Means Clustering on Iris Dataset",
       x = colnames(dataset)[1],
       y = colnames(dataset)[2]) +
  theme_minimal()