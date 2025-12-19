import pandas as pd

#dataframe
#series

# Manually creating the data:
# datas={
#     "order_id":[1,2,3,4],
#     "product":["mobile","laptop","tv","fridge"],
#     "price":[10000,50000,30000,40000]
# }
# df=pd.DataFrame(datas)
# print(df)


#load data fromexcel
#df=pd.read_excel('data.xlxs)
#from a dictionary:
#df=pd.DataFrame(data_dict)

#load and read the dataframe from csv
df = pd.read_csv("orders.csv")
print(df)

#better to use jupiter btw
#for this, you need to use Ctrl+Shift+p and write new jypiter notebook, or manually create a file with the extension .ipynb.
#you can also use google colab for jupyter notebooks
#you need to install jupyter notebook using pip install jupyterlab or pip install notebook
#you need to have python extension installed in vs code to use jypiter notebooks in vs code.
#if you don't, you can go to extensions and search for python and install python extension.

with open("C:/Users/user/Documents/Python for Data Science/text.txt", "r")as file1:
    file_stuff=file1.read()
    print(file_stuff)
    
    
lines=["This is the line A\n", "This is the line B\n", "This is the line C\n", "This is the line D\n", "This is the line E\n"]
with open("C:/Users/user/Documents/Python for Data Science/text2.txt", "w+") as file2: #creating new file and w+ meand write and read
    file2.write("This is the line A\n") #if you use print, the cursor will be in the end, so print won't print anything.
    file2.write("This is the line B\n")
    for line in lines:
        file2.write(line)
    file2.seek(0)              # ⬅️ rewind to beginning
    print(file2.read())
    
with open("C:/Users/user/Documents/Python for Data Science/text.txt", "a+")as file1: #ammend and read
    for line in lines:
        file1.write(line)
    file1.seek(0)
    print(file1.read())
    
#copy one file to another
with open("C:/Users/user/Documents/Python for Data Science/text.txt", "r") as file1:
    with open("C:/Users/user/Documents/Python for Data Science/text2.txt", "w+") as file2:
        for line in file1:
            file2.write(line)
        file2.seek(0)
        print("final print is", file2.read())