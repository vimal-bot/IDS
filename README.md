##CYBER-SPHERE

An Intrusion Detection System based on Random Forest Classifier
OVERVIEW
A Website based Intrusion Destection System(IDS) aimed towards reducing cost of IDS for small to mid-sized businesses. An easily accessible and reliable tool which provides solutions to all the security needs. It works on the ML trained model and classifies data uploaded by the client into different categories, such as 'normal data', 'attack scenario'. It further gives subclassifications to attacks and provides relevant information and recommendations to deal with the problem.

TECHNOLOGIES USED
Language : Python
Back-end : Django
Front-end : HTML/CSS/Java Script , Bootstrap
ARCHITECTURE
The Use-Cases of my Project are:

LOGIN

Two Pages in this use case -> 'Login' and 'Signup'
User Database of Django used to register and authenticate user.
Admin can be created on the server-side ; Admin can view/modify database(s).
I have created a seperate app(use case as said in Django) under 'APPS' folder for its coding and implementation.
Upload File

File is the 'Traffic Capture File' of one's Network. The format should be in .csv , can be achieved using Wireshark features.
File should contain required column/fields required for the algorithm functioning.
The Webpage assosciated to this is the 'detect.html' and the coded function in the server is 'detect'.
It contains a form to be filled with description, name, etc.
Option for file to be uploaded from anywhere in the device
Confirm button to upload it to the server.
After this the user is directed to 'Result'.
Result

The Algorithm written in the jupyter notebook named 'Model' is used.
It is the Random Forest Algorithm trained on KDD'99 Cup Data saved under 'KDD'.
Using 'Joblib' , the learner and scaler are saved named as 'learner' and 'scaler' in 'Model'. These are further loaded inside the Server function named as 'detect'.
The Algorithm gives classification of attacks( if one is present ) and the possible solutions are searched in the databse named as 'Results.
The database gives results on the basis of key tags; all databases are in 'Model.py' file in Dashb App.
Recommendation

These are saved in 'Recommendations' Database. Can be called after results if the client wants recommended solutions.
Different possible solutions are given to the clients from our Database.
At last the client can choose to 'Save' their detection and results.
History

If 'Save Changes' is opted history gets saved in 'History' Database.
When client want to see his/her history the history corresponding to thier username is displayed.
This is achieved using username as Foriegn Key between 'User' and 'History' Database.
ARCHIECTURE DIAGRAM


PROTOTYPE






REPORT
The Complete report is uploaded and can be viwed from above.
