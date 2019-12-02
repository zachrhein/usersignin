from flask import Flask, request, render_template
import jinja2
import html

app = Flask(__name__)
app.config['DEBUG'] = True


        


@app.route('/')
def display_signin_form():
    return render_template("signin.html")


@app.route('/usersignin', methods=['POST'])
def usersignin():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']
    verifypassworderror = ''
    passworderror = ''
    usernameerror= ''
    emailerror = ''
    if verifypassword != password:
        verifypassworderror = "Passwords do not match"

    if not 3 < len(password) < 20 or " " in password:
        passworderror = "Please enter a valid password"

            
    if not 3 < len(username) < 20 or " " in username:
        username = ''
        usernameerror = "Please enter a valid username"

    if (not 3 < len(email) < 20 or email.count('@') != 1 or email.count('.') != 1) and email != '':
        email = ''
        emailerror = "Please enter a valid email"

    if not usernameerror and not verifypassworderror and not passworderror and not emailerror:
        return "Hello, {}!".format(username)
    else: 
        return render_template("signin.html",username = username, email = email, usernameerror=usernameerror, verifypassworderror = verifypassworderror, passworderror = passworderror, emailerror = emailerror)

    


if __name__ == "__main__":
    app.run() 


        


