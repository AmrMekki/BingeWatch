import pandas as pd 

# importing pandas module 
import pandas as pd 
    
# making data frame from csv file 
data = pd.read_csv("Dataset/MovieGenre.csv") 
    
# making new data frame with dropped NA values 
new_data = data.dropna(axis = 0, how ='any') 
    
new_data

print("Old data frame length:", len(data))
print("New data frame length:", len(new_data)) 
print("Number of rows with at least 1 NA value: ",
      (len(data)-len(new_data)))