# Data Extraction Scripts

These scripts extract texts from images using the Google Vision API and place the extracted text into the correct columns in the database
using a Regex Rule-based text classification method. The goal of these scripts is to fasten the data entry step and improve the accuracy of 
the texts filled in the database.

### Set-up
* Create an [account](https://console.cloud.google.com/freetrial/signup/tos?_ga=2.160765819.771726954.1587596482-2000106597.1582312663&_gac=1.45933584.1586882930.EAIaIQobChMIxOLRxK_o6AIVTr7ACh1hwAwjEAAYASAAEgIVtPD_BwE&pli=1) Google Cloud to access Google Vision
* Create a folder called "Credentials"
* Add your Google Vision Account Credentials here.

### Development
* The main entry point to the project is [controller.py](https://github.com/FourFront-Senior-Design/Autofill-pythonenv/blob/master/FourFrontScripts/controller.py). 
* Contributors and future developers are requested to [fork](https://guides.github.com/activities/forking/) from this project.
