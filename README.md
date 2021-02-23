# CYBER-SPHERE

### An Intrusion Detection System based on Random Forest Classifier
## OVERVIEW
A Website based Intrusion Destection System(IDS) aimed towards reducing cost of IDS for small to mid-sized businesses. An easily accessible and reliable tool which provides solutions to all the security needs. It works on the ML trained model and classifies data uploaded by the client into different categories, such as 'normal data', 'attack scenario'. It further gives subclassifications to attacks and provides relevant information and recommendations to deal with the problem.

## TECHNOLOGIES USED
    Language : Python
    Back-end : Django
    Front-end : HTML/CSS/Java Script , Bootstrap
## ARCHITECTURE
The Use-Cases of my Project are:

### 1.LOGIN

    i.Two Pages in this use case -> 'Login' and 'Signup'
    ii.User Database of Django used to register and authenticate user.
    iii.Admin can be created on the server-side ; Admin can view/modify database(s).
    iv.I have created a seperate app(use case as said in Django) under 'APPS' folder for its coding and implementation.
### 2.Upload File

    i.File is the 'Traffic Capture File' of one's Network. The format should be in .csv , can be achieved using Wireshark features.
    ii.File should contain required column/fields required for the algorithm functioning.
    iii.The Webpage assosciated to this is the 'detect.html' and the coded function in the server is 'detect'.
       a.It contains a form to be filled with description, name, etc.
       b.Option for file to be uploaded from anywhere in the device
       c.Confirm button to upload it to the server.
    iv.After this the user is directed to 'Result'.
### 3.Result

    i.The Algorithm written in the jupyter notebook named 'Model' is used.
    ii.It is the Random Forest Algorithm trained on KDD'99 Cup Data saved under 'KDD'.
    iii.Using 'Joblib' , the learner and scaler are saved named as 'learner' and 'scaler' in 'Model'. These are further loaded inside the Server function named as 'detect'.
    iv.The Algorithm gives classification of attacks( if one is present ) and the possible solutions are searched in the databse named as 'Results.
    v.The database gives results on the basis of key tags; all databases are in 'Model.py' file in Dashb App.
### 4.Recommendation

    i.These are saved in 'Recommendations' Database. Can be called after results if the client wants recommended solutions.
    ii.Different possible solutions are given to the clients from our Database.
    iii.At last the client can choose to 'Save' their detection and results.
### 5.History

    i.If 'Save Changes' is opted history gets saved in 'History' Database.
    ii.When client want to see his/her history the history corresponding to thier username is displayed.
    iii.This is achieved using username as Foriegn Key between 'User' and 'History' Database.
## ARCHIECTURE DIAGRAM
![Architecture](https://user-images.githubusercontent.com/69494580/108812803-c2b41e00-75d5-11eb-9c46-228306675190.PNG)


## PROTOTYPE
![index](https://user-images.githubusercontent.com/69494580/108813531-34d93280-75d7-11eb-9da0-06aa7d48ab65.PNG)
![report1](https://user-images.githubusercontent.com/69494580/108813540-399de680-75d7-11eb-81a5-43590850656e.PNG)
![report2](https://user-images.githubusercontent.com/69494580/108813542-3a367d00-75d7-11eb-98c1-a96513f37cea.PNG)






# REPORT
The Complete report is uploaded and can be viwed from above.
