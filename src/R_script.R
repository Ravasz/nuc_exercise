# R script comes here

### Environment ####

# install.packages("tidyverse")

library("tidyverse")

setwd("/home/mate/git/nuc_exercise/src/")

### distances histogram ####

mes_dist_df <- read.csv("mES_distances.tsv", sep = "\t") %>% 
  as_tibble() %>%
  mutate(chr = as_factor(chr)) %>%
  rename("distance" = dist)

dist_mean = mean(mes_dist_df[["distance"]])
sd_dist = sd(mes_dist_df[["distance"]])




p <- ggplot(mes_dist_df[1:100,], aes(x = distance)) +
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
  xlim(-3000000,3000000) +
  stat_function(
    fun = dnorm, 
    args = list(mean = dist_mean, sd = sd_dist), 
    linetype = "dashed"
  )

ggsave("test.png", p)