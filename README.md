# djreact_csv
Upload and save csv files with django and react

##Frontend
Select and upload csv file through the frontend. It should contain two fields - name, price

##Backend
Products model has two fields - name, price

Once the file is received through a post request,it is parsed inside the ProductCreateView. The new Product objects are created and then stored in the database


