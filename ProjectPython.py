import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
import sys
import os


if __name__ == "__main__":
    args = sys.argv[1:]

    if args:

        name = args[0]
        if os.path.exists(name):
            content = open(name, "r")
            data = pd.read_csv(content)
            print(data)

    # Reading a CSV column in Pandas
            mean = data['age'].mean()
            median = data['age'].median()
            stdeviation = data['age'].std()
            min = data['age'].min()
            max = data['age'].max()
            Q1 = data['age'].quantile(0.25)
            Q2 = data['age'].quantile(0.5)
            Q3 = data['age'].quantile(0.75)
            covariance = data.age.cov(data.IQ)
            corr_coeff = data.age.corr(data.IQ, method='pearson')


            print('Mean age : ' + str(mean))
            print('Median age : ' + str(median))
            print('Standart deviation age : ' + str(stdeviation))
            print('Min age : ' + str(min))
            print('Max age : ' + str(max))
            print('Quartile Q1 of age: ' + str(Q1))
            print('Quartile Q2 of age: ' + str(Q2))
            print('Quartile Q3 of age: ' + str(Q3))
            print('Covariance between age and IQ : ' + str(covariance))
            print('Correlation coefficient between age and IQ:' + str(corr_coeff))

        else:
            print("%s does not exist" % name)
