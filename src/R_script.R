# R script comes here

install.packages("tidyverse")

library("tidyverse")

mes_df <- read.csv("/home/mate/code/nucleome/mES.tsv", sep = "\t")
ter_df <- read.csv("/home/mate/code/nucleome/Ter119.tsv", sep = "\t")

50000^2