# Academic-portal
Academic portal made using Python and libraries Tkinter and Pandas

<b>Note:</b> To run the program on Linux, change window.state('zoomed') in Frontend.py to window.attributes('-zoomed', True)

<h3>Project description:</h3>
This project is about creating a functional academic portal, that allows users to:
<ul>
 <li>Sign In to their accounts</li>
 <li>Sign Up and create a new account</li>
 <li>View their user profile with their academic information</li>
 <li>Edit the information in their profile</li>
 <li>Submit a deregistration request to delete their account</li>
</ul>

It is implemented using Python and its libraries, Tkinter for GUI design, Re for regular expression checking and Pandas for database management.

<h3>Design and Implementation:</h3>
All tasks are accomplished by means of a token object, that calls its class methods to store, check and retrieve information from the database. The classes are Person, Teacher, Student, UG Student and PG Student, following the following hierarchy.

![image](https://github.com/DevButani/Academic-portal/assets/130752788/041c9ba1-8b41-4519-86ae-d41b72d95ecd)

The token thus acts as a means of communication between methods in the front-end and the back-end of the portal. 

<h4>Back-end:</h4>
<p>This part of the program contains the class declarations and definitions.
It provides the functional part of the application via class methods as well as interaction with the database, which is stored as a .csv file and accessed via Pandas dataframes.</p>

The following are the classes, their instance attributes and their methods:
<ul>
<li><p><b>Person:</b> This class contains the common attributes for all user types.
     Its instance attributes are: 
     <ol type="1">
      <li>User_ID: The email id of the user. Used for sign in purposes.</li>
      <li>Password: The password of the user.  Used for sign in purposes.</li>
      <li>classno: Denotes the class of the user for program references.</li>
      <li>FirstName: The first name of the user. Displayed in user profile.</li>
      <li>LastName: The last name of the user. Displayed in user profile.</li>
      <li>Department: The department of the user. Displayed in user profile.</li>
      <li>Age: The age of the user. Displayed in user profile.</li>
     </ol></p>
<p>Its methods are:
 <ol>
  <li><i>__init__</i> constructor takes parameters userId and password and assigns them as User_ID and Password attributes of the object, as well as instantiates the other instance attributes and assigns None value.</li>
  <li><i>User_Authentication</i> is the class method that authenticates the information provided by user for Signing In and returns the response based on the validity of this information. It first loads the database onto a Pandas dataframe and checks whether the User_ID of the token object is present in the dataframe and that its classno matches the stored class. Then it checks whether the entered password given to the token object matches the stored password. If it matches, the authentication is complete and the method returns 0 (successful sign in). Otherwise, the user is denied access and the number of remaining attempts is decreased by 1; the method returns 1 (incorrect sign in details). Once the number of remaining attempts (Tries) becomes 0, the account is deactivated and Sign In attempts are immediately denied.</li>
  <li><i>User_Registration</i> is the class method that checks whether the information provided by user matches the criteria and creates a new account. It first checks whether the email matches the general regular expression of email ids, and whether there’s already another user in the database with the same id. Then it checks whether the entered password matches the criteria (length between 8 to 12, at least one uppercase and lowercase alphabet, digit and special character, and no blank spaces). If the provided information matches all criteria, the new user information is loaded into the database via dataframe. Otherwise, the appropriate error code is returned.</li>
  <li><i>User_Deregistration</i> is the class method that deletes user data from the database by loading the dataframe, dropping the row corresponding to the user, and uploading the updated dataframe to the database.</li>
 </ol></p></li>

 <li><p><b>Teacher:</b> This class is a child class of Person and contains attributes specific to teachers.
     Its instance attributes are: 
     <ol type="1">
      <li>Designation: The designation of the user (Professor / Assistant Professor / Associate Professor).</li>
      <li>YearOfJoining: The year of joining the academic institution.</li>
      <li>Office: The office of the user.</li>
     </ol></p>
<p>Its methods are:
 <ol>
  <li><i>__init__</i> constructor takes parameters userId and password and calls the constructor of its parent class (Person), as well as	instantiates the other instance attributes and assigns None value.</li>
  <li><i>Retrieve_Data</i> is the class method that retrieves the information of a	user from the database by loading it onto a dataframe and then	assigning those values, if present, to the token object’s fields.</li>
  <li><i>Save_Data</i> is the class method that updates user information in the	database by loading the dataframe, making the changes, and	uploading the dataframe back to the database.</li>
 </ol></p></li>
 
<li><p><b>Student:</b> This class is a child class of Person and contains attributes specific to students.
     Its instance attributes are: 
     <ol type="1">
      <li>RollNo: The roll number of the user.</li>
      <li>BatchYear: The year of joining the academic institution.</li>
     </ol></p>
<p>Its methods are:
 <ol>
  <li><i>__init__</i> constructor takes parameters userId and password and calls the constructor of its parent class (Person), as well as	instantiates the other instance attributes and assigns None value.</li>
  <li><i>Retrieve_Data</i> is the class method that retrieves the information of a	user from the database by loading it onto a dataframe and then	assigning those values, if present, to the token object’s fields.</li>
  <li><i>Save_Data</i> is the class method that updates user information in the	database by loading the dataframe, making the changes, and	uploading the dataframe back to the database.</li>
 </ol></p></li>

<li><p><b>UG_Student:</b> This class is a child class of Student and contains the instance attribute Degree, denoting the Under Graduate program of the user.</p>
<p>Its <i>__init__</i> constructor takes parameters userId and password and calls the constructor of its parent class (Student), and instantiates Degree attribute and assigns None value.</p></li>

<li><p><b>PG_Student:</b> This class is a child class of Student and contains the instance attribute Degree, denoting the Post Graduate program of the user.</p>
<p>Its <i>__init__</i> constructor takes parameters userId and password and calls the constructor of its parent class (Student), and instantiates Degree attribute and assigns None value.</p></li>
</ul>

<h4>Front-end:</h4>
<p>This part of the program creates the Graphical User Interface and links it to the back-end. It first creates a Tkinter window (which will be set into main-loop) and places a background image on it. Then it packs one of the following Tkinter frames on top of the background image:</p>
<ul>
<li><p><b>Welcome frame</b> is the starting frame. It contains the Sign In and Sign Up Label frames along with the buttons to switch between them. The Label frames contain the widgets for sign in and sign up- labels and entry fields- with their display parameters, and put them in a grid. They also contain a checkbutton clicking which displays the password in the entry field(s) instead of being hidden as *s, by configuring the entry field(s). Lastly, they contain the submit button, clicking which calls the bound submit function:
 <ol type="1">
  <li><i>signin_submit</i> reads data from the entry fields and creates a token object of desired class. It then calls the <i>User_Authentication</i> method and if authentication is successful, calls <i>Retrieve_Data</i> method and switches the frame to the user profile. Otherwise it displays the appropriate error message.</li>
  <li><i>signup_submit</i> reads data from the entry fields, checks whether password and confirm password are same, and creates a token object of desired class. It then calls the <i>User_Registration</i> method and if registration is successful, switches to the user profile and displays confirmation message. Otherwise it displays the appropriate warning message about the criteria not met.</li>
 </ol></p>
<p>The switch_to_signin and switch_to_signup functions work by erasing the entry fields of the previous Label frame, unpacking their contents, and packing the new Label frame and its contents into the Welcome frame.</p>
</li>
<li><p><b>Profile</b> frame is the frame that is used to display and edit user information. It contains a Common_details frame, having widgets for displaying and editing information relating to Person class fields, a Teacher_details frame for Teacher class specific fields, a Student_details frame for Student class specific fields, and similar UG_detail and PG_detail frames. The widgets used include labels, entry fields, spin-box (for numeric assignments) and option-menus (for choosing from a given set of options). Their appearance parameters are configured, they are put in a grid, and editing is initially disabled. It also contains a Profile_Editing frame, which contains the buttons for editing the profile, confirming changes made to the profile, and canceling the changes made via one of the bound functions:
<ol type="1">
 <li><i>edit_profile</i> function unpacks the edit button and packs the Profile_Changes frame containing the cancel and confirm buttons. It also disables the sign-out and deregister buttons. This function enables the widgets to be edited by configuring their states from disabled to normal or read-only.</li>
 <li><i>confirm_changes</i> function unpacks the Profile_changes frame and packs the edit button back, along with restoring the state of sign-out and deregister buttons. It creates a token object and assigns all its attributes by taking information from the edited profile fields. It then calls the <i>Save_Data</i> method and sets the profile to the new values.</li>
 <li><i>cancel_changes</i> function unpacks the Profile_changes frame and packs the edit button back, along with restoring the state of sign-out and deregister buttons. It creates a token object and retrieves original profile data by calling the <i>Retrieve_Data</i> method and sets the profile to the old values.</li>
</ol></p>
<p>The <i>deregister</i> function is called when the deregister button is pressed. It asks the user for confirmation regarding the account deletion and if it’s positive, creates a token and calls <i>User_Deregistration</i> method, switches to Welcome frame and informs the user about completion of the deletion.</p>
</li>
<li><p><b>Frame Switching</b> functions are used to switch between Welcome and Profile frames and to set the Profile frame. These are:
 <ol type="1">
  <li><i>switch_to_welcome</i> function unpacks the Profile frame and its contents and packs the Welcome frame and its contents. It also resets the show-password checkbuttons.</li>
  <li><i>set_profile</i> function takes a token object as its parameter and sets the profile fields to the token’s attributes (if set) by enabling the widgets, modifying the values, and disabling them back.</li>
  <li><i>switch_to_profile</i> function takes a token object and switching mode as its parameters. It unpacks the Welcome frame and the Sign In or Sign Up related contents depending on the switching mode. It then packs the Profile frame and its related contents and calls the <i>set_profile</i> function by passing the token.</li>
 </ol></p>
</li>
</ul>

<h3>GUI Images:</h3>

Sign Up GUI (as UG student) - password hidden
![image](https://github.com/DevButani/Academic-portal/assets/130752788/f3171cc8-7cc3-4a90-9314-a9dab6571f3c)

Sign Up GUI (as Teacher) - show password
![image](https://github.com/DevButani/Academic-portal/assets/130752788/d5c5ab76-9f6e-40dc-ad75-934a4a7bb1e4)

Sign In GUI (as Teacher) - password hidden
![image](https://github.com/DevButani/Academic-portal/assets/130752788/aad9b557-34f5-4d46-b1ba-2d18648ae3b6)

Sign In GUI (as PG student) - show password
![image](https://github.com/DevButani/Academic-portal/assets/130752788/92483cf0-abd9-47c6-8694-5be1db3a78b8)

Profile GUI (after Sign Up as Teacher)
![image](https://github.com/DevButani/Academic-portal/assets/130752788/31264d24-1e73-4321-8648-8bcae66c88af)

Profile GUI (after pressing Edit Profile and editing details)
![image](https://github.com/DevButani/Academic-portal/assets/130752788/714f5b95-5818-4fa2-a891-b8fa291437ce)

Profile GUI (after Sign In as UG student)
![image](https://github.com/DevButani/Academic-portal/assets/130752788/bed694a1-043b-4734-abd0-ca21751b8fe1)

Account Creation Message  
![image](https://github.com/DevButani/Academic-portal/assets/130752788/a826802a-4a44-40c2-a292-c97cf87b88a0)

Sign In completion Message  
![image](https://github.com/DevButani/Academic-portal/assets/130752788/7d104eac-700d-4daf-a0e6-00ab14ca4804)

Account deletion Confirmation  
![image](https://github.com/DevButani/Academic-portal/assets/130752788/14dc4449-f5c0-47fc-8f4e-117b51b23a5f)

Successful Account deletion Message  
![image](https://github.com/DevButani/Academic-portal/assets/130752788/42ddbd9b-8a54-4dc5-bbd6-e1df6885475f)
