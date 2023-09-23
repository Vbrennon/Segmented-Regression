#
# Brennon Villacarlos
# Start: 1/4/2023
# Current: 9/18/2023
# Statistical Analysis for Homo Sapien Brain Size
#

# import relevant packages
import os
import threading as th
from time import sleep
import matplotlib.pyplot as plt  # plots graphs
import pandas as pd
import pingouin as pin  # tests for normality
import statsmodels.api as sm  # fits regression model
from statsmodels.stats.diagnostic import het_white  # tests for homoscedasticity


def main():
    while True:
        try:
            # Asks user for file name, then runs for loop to find filename in C: (or whatever you named it)
            file = input('Please enter a file name (including file extension): ')
            print('This may take a few seconds...')
            for root, dirs, files in os.walk('/'):
                for i in files:
                    if i == file:
                        file_name = os.path.join(root, i)

            # extracts dataframe from excel file
            xl = pd.ExcelFile(file_name)
            df = xl.parse(xl.sheet_names[0])
            df = df.dropna()
            strip = pd.DataFrame().assign(x=df['Age'], y=df['CC'])
            break
        except UnboundLocalError:
            print('\nFile not found. Make sure file exists and check for typos.')
            print()
    print()
    # asks user if they would like to consolidate data
    consolidate = input('Would you like to consolidate data? y/n ')
    if consolidate == 'y':
        ungroup_x = strip.iloc[:, 0]

        # Then, averages y value for every unique x value and creates new dataframe
        anth = strip.groupby(ungroup_x).agg('mean', numeric_only=True).reset_index(drop=True)
        print()
        print('Data has been consolidated.')
        y_values = anth['y']
        x_values = anth['x']
    else:
        anth = pd.DataFrame().assign(x=df['Age'], y=df['CC'])
        y_values = anth['y']
        x_values = anth['x']
    print()

    # Main menu loop
    while True:
        select = input('Enter 1 to test for Normality\n'
                       'Enter 2 to test for Homoscedasticity\n'
                       'Enter 3 to display scatter plot\n'
                       'Or enter any other key to finish ')
        if select == '1':
            print()
            condition1 = test_norm(anth)
        elif select == '2':
            print()
            condition2 = test_white(x=x_values, y=y_values)
        elif select == '3':
            print()
            scatter_plot(x=x_values, y=y_values)
        else:
            # Write anth to file and check conditions
            anth.to_excel('Pywrit.xlsx')
            # adds loading effect with for loop, by concatenating a period to end of the previous string
            print('\n\ncopying data to Pywrit.xlsx', end='')
            for i in range(3):
                print('.', end='')
                sleep(1)
            try:
                # if conditions are met program is ready for segmeneted regression
                # The user is still able to perform this operation, for testing purposes.
                if condition1 is True and condition2 is True:
                    print('\n\nYour data is suitable for Segmented Regression!!\n')
                else:
                    print('\n\nData is not suitable for Segmented Regression. :(\n')
            except UnboundLocalError:
                print('\n\nYou have not performed any tests')
            answer = input('\nWould you like to open file and Segreg? y/n ')
            while answer != 'y' and answer != 'n':
                print("\nWrong input, make sure you type either 'y' or 'n'")
                answer = input('\nWould you like to open file and Segreg? y/n ')
            # if user answer yes the program uses os to create a pywrit file.
            # is used threading to start seg reg at the same time otherwise, it won't open until you close pywrite
            if answer == 'y':
                # allows SegReg to be opened at the same time as Pywrit
                print('\nThis may take a few seconds...')
                s = th.Thread(target=segreg)
                s.start()
                # opens Pywrit
                os.startfile('Pywrit.xlsx')
                break
            else:
                print("\nF-Fine then. It's not like I wanted you to do that or anything b-baka!")

                break


# this function uses a for loop to search the drive for SegReg and then opens it
def segreg():
    for root, dirs, files in os.walk('/'):
        for file in files:
            if file == 'SegReg.exe':
                filename = os.path.join(root, file)
                os.startfile(filename)


def test_norm(anth):
    # Henze-Zirkler Multivariate Normality Test
    # H0 (null): The variables follow a multivariate normal distribution.
    # Ha (alternative): The variables do not follow a multivariate normal distribution.
    # If statistic above alpha then fail to reject Null.
    mn_results = pin.multivariate_normality(anth, alpha=.05)
    result = getattr(mn_results, 'normal')
    value = getattr(mn_results, 'pval')

    if result:
        print(f'p-value = {value:.4f}')
        print('Fail to reject the null hypothesis.\n'
              'There is no evidence the data does not follow a normal distribution\n')
        return True

    else:
        print(f'p-value = {value:.4f}')
        print('Reject the null hypothesis.\n'
              'There is no evidence the data follows a normal distribution\n')
        return False


def test_white(x, y):
    # add constant to predictor variable and fit regression model
    cons = sm.add_constant(x)
    model = sm.OLS(y, cons).fit()

    # Perform White's test, define labels, and return results
    # Null (H0): Homoscedasticity is present (residuals are equally scattered)
    # Alternative (HA): Heteroscedasticity is present (residuals are not equally scattered)
    # If statistic above significance level then fail to reject Null.
    white_test = het_white(model.resid, model.model.exog)
    result = white_test[1]

    if result > .05:
        print(f'p-value = {result:.4f}')
        print('Fail to reject the Null Hypothesis.\n'
              'There is no evidence Homoscedasticity is not present (residuals are equally scattered)\n')
        return True
    else:
        print(f'p-value = {result:.4f}')
        print(' Reject the Null Hypothesis.\n'
              'There is evidence Heteroscedasticity is present (residuals are not equally scattered)\n')
        return False
    # corresponding labels = ['Test Statistic', 'Test Statistic p-value', 'F-Statistic', 'F-Test p-value']


# creates scatterplot out of data
def scatter_plot(x, y):
    # Adds title and label to graph
    chart_title = 'Brain Size Trends'
    x_axis_label = 'Age'
    y_axis_label = 'CC'

    # Creates figure 1 and places scatter plot
    plt.figure(1)
    plt.scatter(x, y)

    # Add title and labels for the axes and then displays graph
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(chart_title)
    plt.show()
    print()


main()
