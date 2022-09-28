#!/usr/bin/env python
# coding: utf-8

# To get started with this project, I will import the csv library to work within insurance.csv. 

# In[1]:


# import csv library.
import csv


# In review of insurance.csv, I came across the follow columns:
# 
#     -Patient Age
#     -Patient Sex
#     -Patient BMI
#     -Patient Number of Children
#     -Patient Smoking Status
#     -Patient U.S. Geographical Region
#     -Patient Yearly Medical Insurance Cost
# 
# There were no signs of missing data, and from this information, I decided to make seven empty lists that will hold each individual column from insurance.csv. 

# In[2]:


# I'm creating seven empty lists for each column uncovered in review of insurance.csv.
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


# The below function is created to load the data from insurance.csv into the empty lists created above. This provides effeciency and simplicity in extracting the data from insurance.csv so I do not have to open insurance.csv and run the 'for' loop seven times. 

# In[3]:


# function created to load csv data
def load_ins_data(column, csv_file, column_name):
    with open(csv_file) as csv_data:
        csv_dict = csv.DictReader(csv_data)
        for row in csv_dict:
            column.append(row[column_name])
        return column


# Below, I call the function to load each list individually with the data associated with it. 

# In[4]:


# load the lists with the insurance data using the created function. 
load_ins_data(ages, 'insurance.csv', 'age')
load_ins_data(sexes, 'insurance.csv', 'sex')
load_ins_data(bmis, 'insurance.csv', 'bmi')
load_ins_data(num_children, 'insurance.csv', 'children')
load_ins_data(smoker_statuses, 'insurance.csv', 'smoker')
load_ins_data(regions, 'insurance.csv', 'region')
load_ins_data(insurance_charges, 'insurance.csv', 'charges')


# The data has now been extracted from insurance.csv, and has been organized by each column in their corresponding lists. I am now ready to begin analyzing the data. The following aspects of the data are what I am going to analyze:
# 
#     1. Average age of the patients.
#     2. Number of males and females counted within the dataset. 
#     3. Geographical location of the patients. 
#     4. Create a dictionary that contains all patient information.
#     5. Average BMI of male vs. female patients.
#     6. Average annual medical charges for smokers vs. non-smokers.
# 
# To perform these inspections, a class called PatientsInfo is built which contains six methods:
# 
#     -average_age()
#     -num_sexes()
#     -patient_regions()
#     -create_dictionary()
#     -average_bmis()
#     -average_charges()
#     
# Please see class built out below.

# In[5]:


# the class PatientsInfo is created and initialized below.
class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    # method that calculates the average age of the patients in insurance.csv    
    def average_age(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
            avg_age = round(total_age / len(self.patients_ages), 2)
        print("Average Patient Age: " + str(avg_age) + " years.")
        
    # method to calculates the number of males and females in insurance.csv
    def num_sexes(self):
        males = 0
        females = 0
        for sex in self.patients_sexes:
            if sex == 'male':
                males += 1
            if sex == 'female':
                females += 1
        print("Total number of males: " + str(males))
        print("Total number of females: " + str(females))
        
    # method to find the unigue regions of patients in insurance.csv
    def patient_regions(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions:
                unique_regions.append(region)
        return unique_regions
        
    # create a dictionary of all data in insurance.csv
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary
    
    # method created to get average BMI for males and females in insurance.csv
    def average_bmis(self): 
        sexes_bmis = list(zip(sexes, bmis))
        male_bmis = []
        female_bmis=[]
        for x in sexes_bmis:
            for i in x:
                if i == 'male':
                    male_bmis.append([i, x[1]])
                elif i =='female':
                    female_bmis.append([i, x[1]])
        total_male_bmi = 0
        total_female_bmi = 0
        for x in male_bmis:
            total_male_bmi += float(x[1])
        for x in female_bmis:
            total_female_bmi += float(x[1])
        male_avg_bmi = round(total_male_bmi / len(male_bmis), 2)
        female_avg_bmi = round(total_female_bmi / len(female_bmis), 2)
        print("Average Male BMI: " + str(male_avg_bmi) + "\n" + "Average Female BMI: " + str(female_avg_bmi))
        
    # method created to calculate average insurance charges for smokers vs. nonsmokers in insurance.csv
    def average_charges(self):
        smoker_status_charges = list(zip(smoker_statuses, insurance_charges))
        smoker_charges = []
        nonsmoker_charges = []
        for x in smoker_status_charges:
            for i in x:
                if i == 'yes':
                    smoker_charges.append([i, x[1]])
                elif i =='no':
                    nonsmoker_charges.append([i, x[1]])
        total_smoker_charges = 0
        total_nonsmoker_charges = 0
        for x in smoker_charges:
            total_smoker_charges += float(x[1])
        for x in nonsmoker_charges:
            total_nonsmoker_charges += float(x[1])
        avg_smoker_charges = round(total_smoker_charges / len(smoker_charges), 2)
        avg_nonsmoker_charges = round(total_nonsmoker_charges / len(nonsmoker_charges), 2)
        print("Average Smoker Charges: " + str(avg_smoker_charges) + "\n" + "Average Non-smoker Charges: " + str(avg_nonsmoker_charges))


# The next step is to create an instance of the class called patient_info. With this instance, each method can be used to see the results of the analysis.

# In[6]:


patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)


# In[7]:


patient_info.average_age()


# The average age of patients in insurance.csv is about 39 years old. It is beneficial to check this to ensure the data in insurance.csv is representative for the broader population. 

# In[8]:


patient_info.num_sexes()


# Next we calculate the number of males (676) and females (662) in insurance.csv to ensure the data has a balance of the sexes and is not skewed toward one sex more than the other. As you can see, the data shows a very close balance of sexes for the patients. 

# In[9]:


patient_info.patient_regions()


# Patients in insurance.csv are located in four unique regions, all within the United States. 

# In[10]:


patient_info.create_dictionary()


# All patient data is neatly organized in a dictionary, which allows for easy access and further analysis to be conducted in the future.

# In[11]:


patient_info.average_bmis()


# From the data in insurance.csv, both male and female BMI's average out very closely, with males having a slightly higher average BMI. 

# In[12]:


patient_info.average_charges()


# The average insurance charge for a patient in insurance.csv who smokes is nearly four times higher than the average insurance charge is for non-smoking patients. This puts it into perspective how much more a patient is charged for insurance for simply being a smoker. 

# In[ ]:




