##
# What's the difference in pop change between 2010 and 2100? 
# Which continent is going to grow the most in 90 years? 
##

import collections
population_dict = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += float((line[6] - line[5])/line[5])

with open('national_population_deltas.csv', 'w') as outputFile:
    outputFile.write('continent,population_deltas\n')

    for k, v in population_dict.items():
        outputFile.write(str(k) + ',' + str(v) + ('\n'))