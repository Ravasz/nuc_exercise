# R script comes here

### Environment ####

# install.packages("tidyverse")
# install.packages("moments")

library("tidyverse")
library("moments")

setwd("/home/mate/git/nuc_exercise/src/")

### distances histogram ####

# load in results from python script exercise_1.py
mes_dist_df <- read.csv("mES_distances.tsv", sep = "\t") %>% 
  as_tibble() %>%
  mutate(chr = as_factor(chr)) %>%
  rename("distance" = dist)

# basic stats
dist_mean = mean(mes_dist_df[["distance"]])
sd_dist = sd(mes_dist_df[["distance"]])
skew_dist = skewness(mes_dist_df[["distance"]])
kurt_dist = kurtosis(mes_dist_df[["distance"]])
quant_dist = quantile(mes_dist_df[["distance"]])

# plot histogram
p <- ggplot(mes_dist_df, aes(x = distance)) +
  geom_histogram(
    binwidth = 200000,
    aes(y = ..density..),
    fill = "lightgreen",
    colour = "black",
    alpha = 0.8
  ) +
  ggtitle("Distribution of minimum distances from nearest sequence") +
  geom_vline(aes(xintercept = 0), colour = "#000000", size = 0.5) +
  geom_density(colour = "#888888", fill = "lightblue", alpha = 0.5) +
  xlim(-5500000,5500000) +
  stat_function(
    fun = dnorm, 
    args = list(mean = dist_mean, sd = sd_dist), 
    linetype = "dashed"
  )

ggsave("hist_dist.png", p)

