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
#you can also use anaconda for jupyter notebooks
#you can also use vs code for jupyter notebooks
#you can also use pycharm for jupyter notebooks
#you need to install jupyter notebook using pip install jupyterlab or pip install notebook
#you need to have python extension installed in vs code to use jypiter notebooks in vs code.
#if you don't, you can go to extensions and search for python and install python extension.
    