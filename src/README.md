# Exercise solutions

This is a quick draft report with the required exercise results. Feel free to browse or ask for additional content as you see fit. This project shall be removed once you checked the results as it is public, and as such might accidentally give away the solutions to others.

## First task

1. The coordinates of the overlapping regions are listed in [mES\_overlap.tsv](mES_overlap.tsv) and [ter119\_overlap.tsv](ter119_overlap.tsv). The script for generating the lists is presented in [exercise\_1.py](exercise_1.py). Please note that the coordinates have not been ordered, as this was not requested in the exercise. This can easily be amended if requested. 
2. The unique regions can be found in [mES\_unique.tsv](mES_unique.tsv) and [ter119\_unique.tsv](ter119_unique.tsv), respectively. The same Python script linked above, and found in this repository was used to obtain the results.
3. The distances were recorded in the [mES\_distances.tsv](mES_distances.tsv) file. 
   - the histogram is presented below, and is also available as a full size image in the repository above.
   
   
    <img src="test.png"  width="600" height="600">
    
   
    
   - In terms of statistical distribution, the distribution of closest regions rougly follows
   a normal distribution with an almost perfectly centred mean (-2381.284) but a relatively large spread (sd = 687488). A normal distribution with such parameters is fitted as the dotted line in the histogram above, for reference. The quantiles of the distances is as follows:

|0%         |25%       |50%  |75%      |100%     |
|-----------|----------|-----|---------|---------|
|-5754066.5 |-129321.0 |-9.5 |122438.1 |5726707.5| 
