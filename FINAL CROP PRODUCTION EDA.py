#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# So here I had imported all the libraries which is needed for doing EDA and after importing the libraries now i am going to import the dataset which is in .csv file so here i will use .read_csv()

# ## Importing Data Set 

# In[55]:


Data = pd.read_csv("crop_production.csv")


# After importing the dataset now I am ready to see the insights of the dataset how the dataset looks like by .head() function

# In[56]:


Data.head()


# Now here only first 5 rows are displayed. I want to see for the last 5 rows so for that I will use tail() function

# In[57]:


Data.tail()


# So this is the tail part of Dataset Now I will be looking for the overall discription of the dataset where i will be getting mean,max,count values for this dataset by using .describe()

# ## Statistical Measurements And Details Of The DataSet

# In[58]:


Data.describe()


# So here I am having the mean,count,max,min value of this dataset where in further process it will help me to subsitute these values for cleaning partof my dataset.

# Now I will be checking for the Shape of the dataset where it will show me how many rows and columns are present in the Dataset

# In[59]:


Data.shape


# So here I am having in this dataset 7 columns and 246091 rows. Now i will be checking for the data type of dataset by using .info() function

# In[60]:


Data.info()


# So in this dataset I am having mostly object,float and int datatype. 

# ## Data Cleaning

# So, here Now I will be checking for Null values in this dataset by using isnull() function which usually show true and false values but here I will be using .sum() which will show me total number of null values present in that particular column

# In[61]:


Data.isnull().sum()


# So here this dataset is almost clean but just the Production column is showing few null values which is almost 1% where I can drop it and use this data for future eda process.

# In[62]:


Data.dropna(inplace=True)


# Here I had drop particular null values. Now if I again check the data it should show me 0 null values for Production dataset.

# In[63]:


Data.isnull().sum()


# So I had successfully drop all the null values and now the dataset is clean and ready for further Data mining process.

# Again once I will check the description of the dataset 

# In[64]:


Data.describe()


# ## Exploratory Data Analysis & Data Mining 

# So I will be looking for each and every column of this dataset I will be checking for State-Wise, District-Wise,Crop-Year Wise,Season-Wise,Crop-Wise Value Counts which will be giving me unique values in particular column

# #### State-Wise Counts

# In[65]:


Data.State_Name.value_counts()


# #### District-Wise Counts

# In[66]:


Data.District_Name.value_counts()


# #### Crop-Year-Wise Counts

# In[67]:


Data.Crop_Year.value_counts()


# #### Season-Wise Counts

# In[68]:


Data.Season.value_counts()


# #### Crop-Wise Counts

# In[69]:


Data.Crop.value_counts()


# Now I will be checking for the correlation between the variables for Crop_Year, Area & Production.Its necessary to see if any outlier is there or not so that i would not affect the EDA process. 

# In[70]:


plt.tick_params(labelsize=10)
sns.heatmap(Data.corr(),annot=True)


# So from this we can conclude if we for particular area the value starts from 0 and its till 1 so there is clearly seen that no variable is showing High correlation and other variables in this dataset. So now i am ready to go for my Data Visualization Part.

# ## Data Visualization 

# So now here I am going to plot Histogram where I will checking for the Season wise Crop Production 

# In[71]:


plt.figure(figsize=(10,8))
plt.hist(Data['Season'])


# So here from this figure I can conclude that variety of Crops production in a particular season. Here variety of Crops in Kharif season are very much high as compare to others And variety of crops in Summer, Winter and autumn are very much low. Here Rabi and Whole Year produces average number of various Crops. From which I can say that season Kharif is suitable for most of the Crops Summer, Winter and Autumn are suitable for some selective Crops.

# Now here I will be plotting Count Plot to check the Variety of Crop Production in particular Year.

# In[72]:


plt.figure(figsize=(18,8))
sns.countplot(x=Data['Crop_Year'])
plt.xticks(rotation=90)


# So here from this figure I can conclude that variety of Crops production in a particular Year. The dataset is from the year 1997 to 2015. Here I have noticed that Variety of Crops have increased during 1997 to 2003 and have decreased afterwards. In the year 2015 there is a certain downfall in the number of various Crops. From which I can conclude that maybe in that year some unexpected incidents or policies were taken.

# Now here I want to check for the overall Production by state which will be giving me basically state wise Production.

# First for this I have to import one visualization library ie. plotly.express where I will be getting morefeatures of visualization in this library

# In[73]:


import plotly.express as px


# In[74]:


Stpro = Data.groupby(by='State_Name')['Production'].sum().reset_index().sort_values(by='Production')
px.bar(Stpro, 'State_Name', 'Production')


# So here from this bar plot I can say that Kerala is the highest crops producing state overall. It had produced more than 500% crop and I can say second highest is state Andhra Pradesh.

# Now here I will be checking for the District Wise Crop Production basically it will give us the highest district of crop production 

# In[75]:


crp = Data.groupby(by='District_Name')['Production'].sum().reset_index().sort_values(by='Production')


# In[76]:


crp


# In[77]:


crp1 = crp.tail()
pro1 = px.bar(crp1, x= 'District_Name', y='Production', title = 'Highest crop production District')


# In[78]:


pro1.show()


# So here from the above bar plot its clearly visible that Kozhikode is having the highest production whereas the second highest is malappuram .

# Similarly I will also check for the lowest crop production district as above .

# In[79]:


crp2 = crp.head()
pro2 = px.bar(crp2, x= 'District_Name', y='Production', title = 'Lowest crop production District')


# In[80]:


pro2.show()


# So here it is showing me the lowest crop production district wise and i can say that Mumbai is having null production and second lowest is Namsai.

# Now I will be checking for the production rate of Crops for different years. I will be doing here bivariate analysis for this.

# In[81]:


sns.lineplot(Data["Crop_Year"],Data["Production"])


# In[82]:


plt.figure(figsize=(25,15))
sns.barplot(Data["Crop_Year"],Data["Production"])
plt.xticks(rotation=90)


# So here in this above line and bar plot it describe about Production rate of Crops of different years. Production rate was very low during the year 1997 but afterward it increased to a certain production level and continued. In the year 2011 there was increase in the Crop Production and it continued till 2014. After that in the year 2015 there was a huge amount of downfall in the Crop Production. Previously we have observed downfall on variety of Crops in the same year. This concludes that maybe because of some unexpected incidents or policies, many types of Crops were not Produced which caused a drastic downfall in the Production rate.

# Now I will check for the Yearly Production of crops

# In[83]:


cp= Data.groupby("Crop_Year")["Production"].agg("sum")
fig = px.line(cp, y = 'Production', markers = True)


# In[84]:


fig.show()


# So here from above line plot I can say that Production of crop since 1997 was in increasing state it continued till 2006 & In 2011 and 2013 it was having disaster increase But in 2015 it suddenly fall down and I can conclude that 2011 year was the highest year for the production of crop.

# Now I will be checking for the Production Rate with respect to Season. 

# In[85]:


plt.figure(figsize=(25,10))
sns.barplot(Data["Season"],Data["Production"])


# So here from above bar plot I can say that the Production rate with respect to Season. Production rate of Whole Year Crops are drastically higher than others. Previously also I had observed that the number of Kharif Crops were very high but here this Bar Plot describes that the Production rate of Kharif is average. From this understanding I can conclude that though the Variety of Kharif Crops are much higher but its Production rate very low, same for Rabi Crops also. Variety of Rabi Crops were high but its Production rate is not upto the mark. In case of Winter Crops, there was less variety but its Production rate is quite well.

# Now I am going to check State Wise Area of Agriculture land

# In[86]:


plt.figure(figsize=(25,15))
sns.barplot(Data["State_Name"],Data["Area"])
plt.xticks(rotation=90)


# So here from the above visualization I can observe the state wise area of agriculture land. I can infer that Punjab has the largest area for agriculture and maharashtra has the second largest and west bengal has the third largest area for agriculture.I can also infer that chandigarh has the smallest area for agriculture.

# Now I will be finding for TOP crops Produced in India which basically will be telling us the Crop types cultivated in India

# So here I will be doing with For loop where if my generated variable is a Crop then it should return me the values like Cereal,Pulses,Fruits,Beans,Vegetables,Spices,Fibres,Nuts,Oilseeds & Commercial.

# In[87]:


def crp(crop):
    for i in ['Rice','Maize','Wheat','Barley','Varagu','Other Cereals & Millets','Ragi','Small millets','Bajra','Jowar', 'Paddy','Total foodgrain','Jobster']:
        if crop==i:
            return 'Cereal'
    for i in ['Moong','Urad','Arhar/Tur','Peas & beans','Masoor',
              'Other Kharif pulses','other misc. pulses','Ricebean (nagadal)',
              'Rajmash Kholar','Lentil','Samai','Blackgram','Korra','Cowpea(Lobia)',
              'Other  Rabi pulses','Other Kharif pulses','Peas & beans (Pulses)','Pulses total','Gram']:
        if crop==i:
            return 'Pulses'
    for i in ['Peach','Apple','Litchi','Pear','Plums','Ber','Sapota','Lemon','Pome Granet',
               'Other Citrus Fruit','Water Melon','Jack Fruit','Grapes','Pineapple','Orange',
               'Pome Fruit','Citrus Fruit','Other Fresh Fruits','Mango','Papaya','Coconut','Banana']:
        if crop==i:
            return 'Fruits'
    for i in ['Bean','Lab-Lab','Moth','Guar seed','Soyabean','Horse-gram']:
        if crop==i:
            return 'Beans'
    for i in ['Turnip','Peas','Beet Root','Carrot','Yam','Ribed Guard','Ash Gourd ','Pump Kin','Redish','Snak Guard','Bottle Gourd',
              'Bitter Gourd','Cucumber','Drum Stick','Cauliflower','Beans & Mutter(Vegetable)','Cabbage',
              'Bhindi','Tomato','Brinjal','Khesari','Sweet potato','Potato','Onion','Tapioca','Colocosia']:
              if crop==i:
                return 'Vegetables'
    for i in ['Perilla','Ginger','Cardamom','Black pepper','Dry ginger','Garlic','Coriander','Turmeric','Dry chillies','Cond-spcs other']:
        if crop==i:
            return 'spices'
    for i in ['other fibres','Kapas','Jute & mesta','Jute','Mesta','Cotton(lint)','Sannhamp']:
        if crop==i:
            return 'fibres'
    for i in ['Arcanut (Processed)','Atcanut (Raw)','Cashewnut Processed','Cashewnut Raw','Cashewnut','Arecanut','Groundnut']:
        if crop==i:
            return 'Nuts'
    for i in ['other oilseeds','Safflower','Niger seed','Castor seed','Linseed','Sunflower','Rapeseed &Mustard','Sesamum','Oilseeds total']:
        if crop==i:
            return 'oilseeds'
    for i in ['Tobacco','Coffee','Tea','Sugarcane','Rubber']:
        if crop==i:
            return 'Commercial'


# In[88]:


crops = Data['Crop']
Data['crp']=Data['Crop'].apply(crp)


# In[89]:


Data.head()


# In[90]:


data = Data.groupby("crp")["Production"].agg("count")
fig = px.bar(data,y = 'Production',title="Crop wise Production in India ")
fig.show()


# So from the above bar plot I am able to conclude that the top crop categories are Cereal,Pulses,Oilseeds Whereas the Lowest crop category is Fruits.

# Now here I will be checking For some Particular Crops like Rice,Coconut or Sugarcane.

# #### For Rice: 

# In[91]:


rice_df = Data[Data["Crop"]=="Rice"]


# In[92]:


rice_df


# Here I will be checking for Rice Production Season Wise

# In[93]:


plt.figure(figsize=(13,10))
sns.barplot(x = "Season", y = "Production",data=rice_df)


# Now I will be checking for Area-Wise Ricee Production

# In[94]:


sns.jointplot(x = "Area",y = "Production",data=rice_df,kind="reg")
plt.show()


# Now here I will be checking rice production over the year

# In[95]:


plt.figure(figsize=(15,10))
sns.barplot("Crop_Year","Production",data=rice_df)
plt.xticks(rotation=45)
plt.show()


# a :Rice is grown heavily when we look the frequency of crops in India
# 
# b :Rice needs Winter for it mature
#     
# c :Yearwise 2014 is the year when production reached the peak production
# 
# d :Correlation between Area and Production shows high production is directly proportional to Area under cultivation.
# 

# #### For Coconut:

# In[96]:


coc_df = Data[Data["Crop"]=="Coconut "]


# In[97]:


coc_df


# Now here I will be checking for seasonal Coconut Production

# In[98]:


plt.figure(figsize=(8,6))
sns.barplot(x= "Season",y="Production",data=coc_df)


# Now I will be checking for State Wise Coconut Production

# In[99]:


plt.figure(figsize=(13,10))
sns.barplot(x = "State_Name",y = "Production",data=coc_df)
plt.xticks(rotation=90)
plt.show()


# In[100]:


plt.figure(figsize=(15,10))
sns.barplot("Crop_Year","Production",data=coc_df)
plt.xticks(rotation=45)
plt.show()


# In[101]:


sns.jointplot("Area","Production",data=coc_df,kind="reg")


# a :Coconut cultivation is yearlong and doesn't get restricted to any particular seasons
# 
# b :Top states involved in coconut production are: Kerala, Andhra Pradesh and Tamil Nadu
#     
# c :Yearwise coconut cultivation is strong and its increasing healthly
# 
# d :High coconut cultivation is directly proportional to area under cultivation.

# #### For Sugarcane:

# In[102]:


sug_df = Data[Data["Crop"]=="Sugarcane"]


# In[103]:


sug_df


# Now here I will be checking for Season Wise Sugarcane Production 

# In[104]:


sns.barplot(x= "Season",y="Production",data=sug_df)


# Now here I will be checking for State Wise Sugarcane Production

# In[105]:


plt.figure(figsize=(13,8))
sns.barplot(x = "State_Name", y = "Production",data=sug_df)
plt.xticks(rotation=90)
plt.show()


# Now Here I will be checking for area wise Sugarcane Production

# In[106]:


sns.jointplot(x= "Area",y = "Production",data=sug_df,kind="reg")


# a :Sugarecane production is directly proportional to area
# 
# b :The production is high in some state only
# 
# c :Production is Decreasing over the Year.

# # Conclusion

# I started with 246091 samples wih 7 columns. Production Variable had 3730 (1.5% of total sample size) missing values which was dropped and working dataset has 242361 sample size. Also checked for multicollinearity of variables using heatmap.

# Visualization Done On:
# 
# 1: Season Wise Crop Production
# 
# 2: District Wise Crop Production
#     
# 3: State Wise Crop Production
#     
# 4: Top Crops Production In India Where Cereal, Pulses and oilseeds.
#     
# 5: Particular For Rice Season,Area,Year Wise Production and where I conclude 
# 
#          a :Rice is grown heavily when we look the frequency of crops in India
# 
#          b :Rice needs Winter for it mature
# 
#          c :Yearwise 2014 is the year when production reached the peak production
# 
#          d :Correlation between Area and Production shows high production is directly proportional to Area undercultivation.
#             
# 6: Particular For Coconut Season,State,Area,Year-Wise Production and where I conclude 
#     
#          a :Coconut cultivation is yearlong and doesn't get restricted to any particular seasons
# 
#          b :Top states involved in coconut production are: Kerala, Andhra Pradesh and Tamil Nadu
# 
#          c :Yearwise coconut cultivation is strong and its increasing healthly
# 
#          d :High coconut cultivation is directly proportional to area under cultivation
#             
# 7: Particular For Sugarcane Season,State,Area-Wise Production and where I conclude
# 
#          a :Sugarecane production is directly proportional to area
# 
#          b :The production is high in some state only
# 
#          c :Production is Decreasing over the Year.
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




