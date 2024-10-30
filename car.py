#Step 1
%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt


#Read in data frame - Note the new style "bmh"
plt.style.use("ggplot")
df_cars = pd.read_csv("mtcars.csv")


#Get automatic (am=0) versus manual (am=1) cars.  We will see a faster way to do this using SQL.
df_cars_auto = df_cars[df_cars.am==0]
df_cars_manual = df_cars[df_cars.am==1]

plt.figure(figsize=(15,5))
plt.subplot(1,3,1) # 1 row, 2 columns. select first subplot
plt.scatter(df_cars_auto['hp'] , df_cars_auto['mpg'], label= "Auto") #plot in red dashed lines
plt.scatter(df_cars_manual['hp'] , df_cars_manual['mpg'],c='blue', label="manual") #plot in red dashed lines
plt.xlabel("horspower")
plt.ylabel("miles per gallon")
plt.title("hp vs. mpg")
plt.legend(loc='upper left')


plt.subplot(1,3,2) # 1 row, 2 columns. select second subplot
plt.scatter(df_cars_auto['hp'] , df_cars_auto['disp'], label= "Auto") #plot in red dashed lines
plt.scatter(df_cars_manual['hp'] , df_cars_manual['disp'],c='blue', label="manual") #plot in red dashed lines
plt.xlabel("horspower")
plt.ylabel("disp")
plt.title("hp vs. disp")
plt.legend(loc='upper left')

plt.subplot(1,3,3) # 1 row, 2 columns. select third subplot
plt.scatter(df_cars_auto['hp'] , df_cars_auto['qsec'], label= "Auto") #plot in red dashed lines
plt.scatter(df_cars_manual['hp'] , df_cars_manual['qsec'],c='blue', label="manual") #plot in red dashed lines
plt.xlabel("horspower")
plt.ylabel("qsec")
plt.title("hp vs. qsec")
plt.legend(loc='upper left')
