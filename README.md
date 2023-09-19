<h1>Statistical Analysis of Homo Sapien Brain Size</h1>

## Description
The program is designed to take an Excel file containing the age and brain size of hundreds of Homo sapiens specimens and perform various statistical analyses on the dataset. This program was specifically to test Villamoare and Grabowski (2022), who were, in turn, testing DeSilva et al. (2021). As such, this program is not meant to be downloaded and used. It's simply to showcase my abilities in Data Analysis using Python. However, I have decided to leave the Python file and a sample Excel file for anyone interested  in testing the program's capabilities for themselves. It should be noted that you need to download the SegReg (linked below) application for you to use all of this program's available features.

## Languages and Utilities Used

- <b>Python</b> 
- <b>Pycharm 2023.2.1 Community</b>
- [SegReg](https://www.waterlog.info/segreg.htm)

## Modules/Packages used

- os
- threading
- matplotlib.pyplot
- pandas
- pingouin
- statsmodels.api
- statsmodels.stats.diagnostic
- time


<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

## Program walk-through:
<b>Launch Program:</b> 
First, you need to download the Python, Excel, and SegReg files. Make sure all are in the same drive. The program can be launched by running it through your cmd (assuming path variables are set correctly, and you are in the correct directory) or any IDE. 

<b>Step 1:</b>  
The program will ask you to input the file and then ask if you want to consolidate the data. You might want to do this if the data you have is heteroscedastic (it disperses more as X increases.) Homoscedasticity is one of the requirements outlined by Villamoare & Grabowski (2022) in order for Segmented Regression to work.

<img src="https://i.imgur.com/kjuFHHq.png" height="80%" width="80%" />

<b>Step 2:</b> 
This will lead you to the main menu loop. Here, you have 4 options. The first tests for normality, the second tests for homoscedasticity, the third creates a scatter plot of the data, and the fourth finishes up the program by writing the dataframe to a new file and then asking one final question. You can technically skip all the tests or do any combination of them, but this isn't recommended. 

<img src="https://i.imgur.com/bY69aKJ.png" height="80%" width="80%" />

<b>Option 1:</b>
This option tests to see if the data follows a normal distribution using the Henze-Zirkler Test. As you can see, we failed to reject the null, and therefore, the data most likely follows a multivariate normal distribution.

<img src="https://i.imgur.com/9jFubZr.png" height="80%" width="80%" />

<img src="https://i.imgur.com/JwwPQoZ.png" height="80%" width="80%" />

<b>Option 2:</b>
This option tests for Homoscedasticity using White's Test. As in option 1, we failed to reject the null, indicating the data is homoscedastic.

<img src="https://i.imgur.com/VYY0rJ3.png" height="80%" width="80%" />

<img src="https://i.imgur.com/BW7pwIh.png" height="80%" width="80%" />

<b>Option 3:</b> 
This option simply displays the data as a scatter plot. The program won't continue until you close the graph (click the picture to increase size).

<img src="https://i.imgur.com/KxQbntZ.png" height="80%" width="80%" />

<img src="https://i.imgur.com/GgVKV2L.png" height="80%" width="80%" />

<b>Step 3:</b>
Finally, this option will end the program. The program will copy your data into a new file called "Pywrit." If normality and homoscedasticity are detected, the program will tell you that your program is ready for Segreg. Even if it doesn't, you are still given the option to open SegReg. Once SegReg and Pywrit are opened, you can copy the columns in the Excel file into SegReg to perform Segmented regression. Check the documentation on how SegReg exactly works.

<img src="https://i.imgur.com/RBPKiuC.png" height="80%" width="80%" />

<img src="https://i.imgur.com/AWbiUHs.png" height="80%" width="80%" />

## Documentation

[Villamoare and Grabowski (2022)](https://www.frontiersin.org/articles/10.3389/fevo.2022.963568/full)

[os package](https://docs.python.org/3/library/os.html)

[pandas packages](https://pandas.pydata.org/pandas-docs/stable/)

[matplotlib package](https://matplotlib.org/stable/users/index)

[pingouin package](https://pingouin-stats.org/build/html/index.html)

[statsmodels package](https://www.statsmodels.org/stable/user-guide.html)

[time package](https://docs.python.org/3/library/time.html)

[threading package](https://docs.python.org/3/library/threading.html)

[SegReg](https://www.waterlog.info/segreg.htm)
