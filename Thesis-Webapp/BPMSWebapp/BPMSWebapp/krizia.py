from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pyrebase

from firebase import firebase
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from djexmo import send_message
from django.views.decorators.cache import cache_control
from django.core.cache import cache

now = " "
ses = " "
name = " "
## ernie
# email1 = " "          #unused
uid = " "
tok = " "
PassedPatientId = " "   #datt
PatientId = " "         #datt1
## ernie
# datt = " "
# datt1 = " "

### notes
# renamed "fav_color" to SessionStart
# renamed "did" to SortedAccountInformationList
# renamed "li" to AccountInformationList
# renamed "det" to UserInfoDictionary
### end notes

config = {          ## initial configurations
    'apiKey': "AIzaSyCwy2DSVWgniTi2PRbHlDKvF58dzE5LhmY",
    'authDomain': "thesisbpms-af272.firebaseapp.com",
    'databaseURL': "https://thesisbpms-af272.firebaseio.com",
    'projectId': "thesisbpms-af272",
    'storageBucket': "thesisbpms-af272.appspot.com",
    'messagingSenderId': "789763107091"
 }


firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()
sto = firebase.storage()

#this function is used for calling the landing page
def home(request):
    return render(request, 'index.html')

# this is a dummy landing page
## needed ni para maka log in ##
def home_log(request):
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
    return render(request, 'home_log.html', {'n':name} )

# this function calls for login page
def LoginForm(request): ## SignInForm
    return render(request,'form_login.html')

# this function calls sign in functionalities 
def Login(request):    ## SignIn
    email=request.POST.get('email')     ## fetch email address data
    passw = request.POST.get("pass")    ## fetch password
    try:
        user = authe.sign_in_with_email_and_password(email,passw)   ## authenticate email add and password
    except:
        message = "Invalid Credentials"    ## error message if invalid
        return render(request,"form_login.html",{"m":message})  ## error message if invalid
    uid = user['localId']       ## if accepted, assign localid to uid
    # ------------------------------------
    #assigning users's ID token to 'tok'
    tok = user['idToken']
    # ------------------------------------
    request.session['SessionStart'] = str(uid)
    #global ses
    ses = request.session['SessionStart']
    # ------------------------------------
    # Assigning account information to lol
    AccountInformation = authe.get_account_info(tok)
## ernie
#    lol = authe.get_account_info(tok)
    # ------------------------------------
    print("this is for Account Information")
    print(AccountInformation)

    AccountInformationList = []     ## new empty list
    for key,value in AccountInformation.items():    ## for i in old_list
        AccountInformationList.append(tuple((key,value)))   ## store key and value in list
    AccountInformationList.sort(reverse = True)     ## reverse list to show first data first?
    print ("The following is the AccountInformationList")
    print (AccountInformationList)
    print ("End of AccountInformationList")
    ## new_list = [expression(i) for i in old_list]
    f = [y[1] for y in AccountInformationList]  ## array for account info list
    # y[1] means start at users information 
    print("this is f")
    print(f)
    sort = sorted(str(f))  ## sort data stored in f
    print("this is sorted f")
    print(sort)
    g = [g[0] for g in f]   ## no idea
    print("this is g")
    print(g)
    sortg = sorted(str(g))  ## sort again but idk what for
    print("this is sorted g")
    print(sortg)
## ernie
    # print("this is f")
    # print(f)
    # sorted(str(f))  ## sort data stored in f
    # g = [g[0] for g in f]   ## no idea
    # print("this is g")
    # print(g)
    # sorted(str(g))  ## sort again but idk what for

## ernie
    # did = list(g)[0]
    SortedAccountInformationList = list(g)[0]
## ernie
    #li1 = []
    AccountInformationList1 = []
    for key,value in SortedAccountInformationList.items():
        AccountInformationList1.append(tuple((key,value)))
        AccountInformationList1.sort(reverse = True)
    print("This is AccountInformationList1")
    print (AccountInformationList1)
## ernie
    #ew = 'emailVerified'
    print("This is AccountInformationList1 [6]")
    print (AccountInformationList1[6])  ## email verified, true
    AccountInformationList2 = []
    AccountInformationList2 = AccountInformationList1[6]
    EmailAddress = list(AccountInformationList2)[1]
    print (str(EmailAddress))
    EmailVerified = str(EmailAddress)
    if EmailVerified == 'False':
        EmailVerifyMsg = "You need to verify your email first. Redirecting you to Homepage"
        return render(request,'index.html', {'m':EmailVerifyMsg})
    SuccessMsg = "Login Successful!"
    HttpResponse(SuccessMsg)
    UserInfoDictionary = db.child("users").child("doctor").child(ses).get().val() # det is user information dictionary
    print("This is UserInfoDictionary")
    print (UserInfoDictionary)
    UserInfoList = []        ## empty list
    for key,value in UserInfoDictionary.items():
        UserInfoList.append(tuple((key, value)))     ## add key and value data in lis array
    UserInfoList.sort(reverse=True)  ## sort lis contents in descending order
    print("This is lis")
    print(UserInfoList)                  
    g = [x[1] for x in UserInfoList]
    print("This is G")
    print (g)
    dab = g
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
    print (name)
    pic = db.child("users").child("profilepic").child(ses).child("link").get().val()
    if pic is None:
        checklicnum = db.child("users").child("doctor").shallow().get().val()
        print (checklicnum)
        return render(request, "dash.html", {'dab':dab, 'n':name})
    else:
        picc = []
        for ka,va in pic.items():
            picc.append(tuple((ka, va)))
        print (picc)
        l = [x[1] for x in picc]
        print (l)
        pic = l
        checklicnum = db.child("users").child("doctor").shallow().get().val()
        print (checklicnum)
        return render(request, "dash.html", {'dab':dab,'p':pic, 'n':name})

def RegistrationForm(request):    ## signupForm
    return render(request,'register.html')

def Register(request):    ## signuppost
    famName = request.POST.get('famName')
    firstName = request.POST.get('firstName')
    gender = request.POST.get("gender")
    birthdate = request.POST.get("birthdate")
    email = request.POST.get('email')
    passw = request.POST.get('password')
    conf_pass = request.POST.get('conf_password')
    address = request.POST.get("address")
    num = '+63' + str(request.POST.get("mobileNum"))
    MS=request.POST.getlist('MS')
    lNum = request.POST.get("lNum")
    fullname = {
        'lastName': famName,
        'firstname': firstName
    }
###Firebase init
### somewhat needed kay mu email address already registered siya if wala
    config = {
        'apiKey': "AIzaSyCwy2DSVWgniTi2PRbHlDKvF58dzE5LhmY",
        'authDomain': "thesisbpms-af272.firebaseapp.com",
        'databaseURL': "https://thesisbpms-af272.firebaseio.com",
        'projectId': "thesisbpms-af272",
        'storageBucket': "thesisbpms-af272.appspot.com",
        'messagingSenderId': "789763107091"
      }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
### validation of password
    if(passw != conf_pass):
        ErrorMsg = "Passwords do not match"
        return render(request, "register.html",{'m':ErrorMsg})
### verification of licenseNum
    checklicnum = db.child("users").child("doctor").shallow().get().val()
    if checklicnum is None:
        try:
            user = auth.create_user_with_email_and_password(email,passw)
        except:
            ErrorMsg = "Email Address Already Registered"
            return render(request, "register.html", {'m':ErrorMsg})
        print (user)
        uid = user['localId']
        tok = user['idToken']
        users_ref = db.child("users").child("doctor").child(uid)
        sendemail = auth.send_email_verification(tok)
        users_ref.set({
        'email': email,
        'fullname': fullname,
        'address': address,
        'gender' : gender,
        'contactNo' : num,
        'birthDate' : birthdate,
        'medicalSpecialization' : MS,
        'LicenseNum': lNum,
        'status': "1",
        })

        SuccessMsg  = "Account Created Successfully"
        HttpResponse(SuccessMsg)
        return render(request, "verify.html",{"e":email,'m':SuccessMsg})
    else:
        lis=[]
        for x in checklicnum:
            j = db.child("users").child("doctor").child(x).child("LicenseNum").get().val()
            if j == lNum:
                ErrorMsg = "Duplicate License Number!"
                return render(request, "register.html", {'m':ErrorMsg})
        try:
            user = auth.create_user_with_email_and_password(email,passw)
        except:
            ErrorMsg = "Email Address Already Registered"
            return render(request, "register.html", {'m':ErrorMsg})
        print (user)
        uid = user['localId']
        tok = user['idToken']
        users_ref = db.child("users").child("doctor").child(uid)
        sendemail = auth.send_email_verification(tok)
        users_ref.set({
        'email': email,
        'fullname': fullname,
        'address': address,
        'gender' : gender,
        'contactNo' : num,
        'birthDate' : birthdate,
        'medicalSpecialization' : MS,
        'LicenseNum': lNum,
        'status': "1",
        })

        SuccessMsg  = "Account Created Successfully"
        HttpResponse(SuccessMsg)
        return render(request, "verify.html",{"e":email,'m':SuccessMsg})
        

def DoctorDashboard(request): ## dashboard                    return render(request, "patientdash.html",{'da':da,'s':ses, 'd':PassedPatientId, 'n':name, 'q':qo})
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
    else:
        print ("No Session")
        return redirect('/SignIn')

    try:
        UserInfoDictionary = db.child("users").child("doctor").child(ses).get().val()
    except:
        return render(request,"index.html")
    print (UserInfoDictionary)
    lis = []
    for key,value in UserInfoDictionary.items():
        lis.append(tuple((key, value)))
    lis.sort(reverse=True)
    DoctorInformation = [x[1] for x in lis]
    print (DoctorInformation)
    dab = DoctorInformation
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
    pic = db.child("users").child("profilepic").child(ses).child("link").get().val()
    if pic is None:
        return render(request, "dash.html", {'dab':dab, 'n':name})
    else:
        picc = []
        for ka,va in pic.items():
            picc.append(tuple((ka, va)))
        l = [x[1] for x in picc]
        print (l)
        pic = l


        if 'patientdash_session' in request.session:
            del request.session['patientdash_session']
            request.session.modified = True
        return render(request, "dash.html", {'dab':dab,'p':pic, 'n':name})

def notif(request):
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()

        if 'patientdash_session' in request.session:
            del request.session['patientdash_session']
            request.session.modified = True

        return render(request, "notif.html", {'n':name})
    else:
        print ("No Session")
        return redirect('/SignIn')


def AddPatientForm(request):    ## createform
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')

    if 'SessionStart' not in request.session:
        return redirect('/SignIn')
    else:
        return render(request, "add.html", {'n':name})

def AddPatient(request): ## createpat
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')

    import time
    import pytz
    from datetime import datetime, timezone
    tz = pytz.timezone('Asia/Manila')
    utc_dt = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(utc_dt.timetuple()))


    famName = request.POST.get('famName')
    firstName=request.POST.get('firstName')
    email = request.POST.get('email')
    address = request.POST.get("address")
    num = '+63' + str(request.POST.get("mobileNum"))
    gender = request.POST.get("gender")
    birthdate = request.POST.get("birthDate")
    btype = request.POST.get('btype')
    fullname = {
        'lastName': famName,
        'firstname': firstName
    }

    users_ref = db.child("users").child("patient").child(ses).child(millis)
    users_ref.set({
            'fullname':fullname,
            'email':email,
            'address':address,
            'contactNo': num,
            'bloodType': btype,
            'gender':gender,
            'birthDate':birthdate,
            })
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
    SuccessMsg = "Patient Created Successfully. Redirecting you to Pairing of BP Device"
    return render(request, "qrgen.html", {'n':name, 'q':millis, 'm':SuccessMsg, 'f':fullname})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def PatientDashboard(request):   ## patientdash

        print ("PATIENT ID")
        if 'SessionStart' in request.session:
            ses = request.session['SessionStart']
            print (ses)
        else:
            print ("No Session")
            return redirect('/SignIn')

        if 'patientdash_session' not in request.session:
            return redirect('/vform')
        else:
            tell = request.GET.get('z')
            PatientId = tell.split('-')[0]
            print ("patient ID")
            print (PatientId)
            request.session['my_pat'] = PatientId
            le = db.child("users").child("patient").child(ses).child(PatientId).get().val()

            print ("this is le")
            print (le)
            leb = []
            for key,value in le.items():
                leb.append(tuple((key, value)))
            leb.sort(reverse=True)
            print ("this is leb")
            print (leb)
            b = len(leb)
            print ("this is b")
            print (b)

            g = [x[1] for x in leb]
            print ("this is g")
            print (g)
            da = g
            pic = db.child("users").child(ses).child("link").child("patient").child(PatientId).get().val()
            print ("this is pic")
            print (pic)
            ler = db.child("users").child("data").child(ses).child(PatientId).child("BPdata").shallow().get().val()

            print ("this is ler")
            print (ler)
            DoctorName = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
            print ("this is DoctorName")
            print (DoctorName)

            if ler is None:
                if pic is None:
                    if 'patientdash_session' not in request.session:
                        return redirect('/SignIn')
                    else:
                        return render(request, "patientdash.html", {'da':da,'s':ses, 'd':PatientId, 'n':DoctorName})

                else:
                    picc = []
                    for ka,va in pic.items():
                        picc.append(tuple((ka, va)))
                    l = [x[1] for x in picc]
                    print ("this is l in else")
                    print (l)
                    pic = l

                    if 'patientdash_session' not in request.session:
                        return redirect('/SignIn')
                    else:
                        return render(request, "patientdash.html",{'n':DoctorName, 'da':da,'s':ses, 'd':PatientId})

            op = []
            for i in ler:
                op.append(str(i))
                op.sort()
            print ("this is op")
            print (op)
            qo = []
            for a in op:
                jj = db.child("users").child("data").child(ses).child(PatientId).child("BPdata").child(a).child("syst").get().val()
                jk = db.child("users").child("data").child(ses).child(PatientId).child("BPdata").child(a).child("dias").get().val()
                jd = str(jj)+ " " + str(jk)
                qo.append(str(jd))
                print ("this is qo")
                print (str(qo))
            if pic is None:
                return render(request, "patientdash.html", {'da':da,'s':ses, 'd':PatientId, 'n':DoctorName, 'q':qo})

            else:
                picc = []
                for ka,va in pic.items():
                    picc.append(tuple((ka, va)))
                l = [x[1] for x in picc]
                print ("this is l in 2nd else")
                print (l)
                pic = l

                if 'SessionStart' not in request.session:
                    return redirect('/SignIn')
                else:
                    return render(request, "patientdash.html",{'da':da,'s':ses, 'd':PatientId, 'n':DoctorName, 'q':qo})


def UpdateDoctorProfile(request): ## updoc
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')

    try:
        UserInfoDictionary = db.child("users").child("doctor").child(ses).get().val()
    except:
        return render(request,"index.html")
    print (UserInfoDictionary)
    lis = []
    for key,value in UserInfoDictionary.items():
        lis.append(tuple((key, value)))
    lis.sort(reverse=True)
    g = [x[1] for x in lis]
    print (g)
    dab = g
    dabb = dab[5]
    dabb1 = dab[6]
    daabb = str(dabb[4:])
    dabb2 = dab[7]
    gl = db.child("users").child("doctor").child(ses).child("email").shallow().get().val()
    if 'SessionStart' not in request.session:
        return redirect('/SignIn')
    else:
        name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
        return render(request, "upd.html",{'n':name,'dab':dab, 'e':gl, 'd':dabb1,'d1':daabb,'d2':dabb2})

def UpdatedDoctorProfile(request):   ## updatedprof
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')
    email = request.POST.get('email')
    famName = request.POST.get('famName')
    firstName = request.POST.get('firstName')
    gender = request.POST.get("gender")
    birthdate = request.POST.get("birthdate")
    address = request.POST.get("address")
    num = '+63' + str(request.POST.get("mobileNum"))
    MS = request.POST.getlist('MS')
    lNum = request.POST.get('lNum')
    profpic = request.FILES.get('myfile',False)
    a = len(famName)
    if a is 0:
        lett = db.child("users").child("doctor").child(ses).child("fullname").child("lastName").shallow().get().val()
        famName = lett
    print (famName)
    a = len(firstName)
    if a is 0:
        lett1 = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
        firstName = lett1
    a = len(address)
    if a is 0:
        lett2 = db.child("users").child("doctor").child(ses).child("address").shallow().get().val()
        address = lett2
    a = len(num)
    if a is 3:
        lett4 = db.child("users").child("doctor").child(ses).child("contactNo").shallow().get().val()
        num = lett4
    a = len(MS)
    if a is 0:
        lett6 = db.child("users").child("doctor").child(ses).child("medicalSpecialization").shallow().get().val()
        MS = lett6
    a = len(lNum)
    if a is 0:
        lett7 = db.child("users").child("doctor").child(ses).child("LicenseNum").shallow().get().val()
        lNum = str(lett7)
    fullname = {
        'lastName': famName,
        'firstname': firstName
        }
    up = db.child("users").child("doctor").child(ses)
    up.update({
            'email':email,
            'fullname':fullname,
            'address':address,
            'gender':gender,
            'birthDate':birthdate,
            'contactNo' : num,
            'medicalSpecialization' : MS,
            'LicenseNum': lNum
            })
    if profpic is False:
        UserInfoDictionary = db.child("users").child("doctor").child(ses).get().val()
        print (UserInfoDictionary)
        lis = []
        for key,value in UserInfoDictionary.items():
            lis.append(tuple((key, value)))
        lis.sort(reverse=True)
        g = [x[1] for x in lis]
        print (g)
        dab = g
        pic = db.child("users").child("profilepic").child(ses).child("link").get().val()
        if pic is None:
            return render(request, "dash.html", {'e':email,'dab':dab, 'n':name})
        else:
            picc = []
            for ka,va in pic.items():
                picc.append(tuple((ka, va)))
            l = [x[1] for x in picc]
            print (l)
            pic = l
            return render(request, "dash.html", {'dab':dab,'p':pic, 'n':name})
    else:
        print (up)
        j = sto.child("images").child("doctor").child(ses).child("profpicture").put(profpic)
        j_url = sto.child("images").child("doctor").child(ses).child("profpicture").get_url(j['downloadTokens'])
        print (j_url)
        im = db.child("users").child("profilepic").child(ses).child("link")
        im.update({'url':j_url})
        SuccessMsg = "Updated Successfully"
        UserInfoDictionary = db.child("users").child("doctor").child(ses).get().val()
        print (UserInfoDictionary)
        lis = []
        for key,value in UserInfoDictionary.items():
            lis.append(tuple((key, value)))
        lis.sort(reverse=True)
        g = [x[1] for x in lis]
        print (g)
        dab = g
        pic = db.child("users").child("profilepic").child(ses).child("link").get().val()
        if pic is None:
            return render(request, "dash.html", {'dab':dab, 'n':name})
        else:
            picc = []
            for ka,va in pic.items():
                picc.append(tuple((ka, va)))
            l = [x[1] for x in picc]
            print (l)
            pic = l
        if 'SessionStart' not in request.session:
            return redirect('/SignIn')
        else:
            return render(request, "dash.html", {'dab':dab,'p':pic, 'm':SuccessMsg, 'n':name})

def Logout(request):    ## logout
    print (auth)
    # auth.logout(request)
    request.session.flush();
    return render(request,"logout.html")


def UpdatePatientProfile(request): ## uppat
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')
    if 'my_pat' in request.session:
        PatientId = request.session['my_pat']
    print (PatientId)
    le = db.child("users").child("patient").child(ses).child(PatientId).get().val()
    leb = []
    for key,value in le.items():
        leb.append(tuple((key, value)))
    leb.sort(reverse=True)
    print (leb)
    b = len(leb)
    print (b)
    #lis.pop()
    g = [x[1] for x in leb]
    print (g)
    da = g
    dabb = da[3]
    daabb = str(dabb[4:])
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()

    if 'SessionStart' not in request.session:
        return redirect('/SignIn')
    else:
        return render(request,"upp.html", {'n':name,'d':da, 'd1':daabb})

def UpdatedPatientProfile(request):    ## updatedpatprof
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')
    email = request.POST.get('email')
    famName = request.POST.get('famName')
    firstName = request.POST.get('firstName')
    gender = request.POST.get("gender")
    birthdate = request.POST.get("birthDate")
    address = request.POST.get("address")
    btype = request.POST.get("btype")
    num = '+63' + str(request.POST.get("mobileNum"))
    PatientId = request.session['my_pat']
    a = len(email)
    if a is 0:
        lett = db.child("users").child("patient").child(ses).child(PatientId).child("email").shallow().get().val()
        email = lett
    a = len(famName)
    if a is 0:
        lett1 = db.child("users").child("patient").child(ses).child(PatientId).child("fullname").child("lastName").shallow().get().val()
        famName = lett1
    print (famName)
    a = len(firstName)
    if a is 0:
        lett2 = db.child("users").child("patient").child(ses).child(PatientId).child("fullname").child("firstname").shallow().get().val()
        firstName = lett2
    a = len(address)
    if a is 0:
        lett3 = db.child("users").child("patient").child(ses).child(PatientId).child("address").shallow().get().val()
        address = lett3
    a = len(num)
    if a is 3:
        lett4 = db.child("users").child("patient").child(ses).child(PatientId).child("contactNo").shallow().get().val()
        num = lett4
    fullname = {
        'lastName': famName,
        'firstname': firstName
        }
    up = db.child("users").child("patient").child(ses).child(PatientId)
    up.update({
            'email':email,
            'fullname':fullname,
            'address':address,
            'contactNo':num,
            'gender':gender,
            'birthDate':birthdate,
            'bloodType':btype,
            })
    print (up)
    SuccessMsg = "Updated Successfully"

    print (PatientId)
    le = db.child("users").child("patient").child(ses).child(PatientId).get().val()
    print (le)
    leb = []
    for key,value in le.items():
        leb.append(tuple((key, value)))
    leb.sort(reverse=True)
    print (leb)
    b = len(leb)
    print (b)
    #lis.pop()
    g = [x[1] for x in leb]
    print (g)
    da = g
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
    pic = db.child("users").child(ses).child("link").child("patient").child(PatientId).get().val()
    ler = db.child("users").child("data").child(ses).child(PatientId).child("BPdata").shallow().get().val()
    if ler is None:
        if pic is None:
            SuccessMsg = "Updated Successfully"
            return render(request, "patientdash.html", {'da':da,'s':ses, 'd':PatientId, 'n':name})
        else:
            picc = []
            for ka,va in pic.items():
                picc.append(tuple((ka, va)))
            l = [x[1] for x in picc]
            print (l)
            pic = l
            SuccessMsg = "Updated Successfully"
        return render(request, "patientdash.html",{'n':name, 'da':da,'s':ses, 'd':PatientId})
    op = []
    for i in ler:
        op.append(str(i))
        op.sort()
    print (op)
    qo = []
    for a in op:
        jj = db.child("users").child("data").child(ses).child(PatientId).child("BPdata").child(a).child("syst").get().val()
        jk = db.child("users").child("data").child(ses).child(PatientId).child("BPdata").child(a).child("dias").get().val()
        jd = str(jj)+ " " + str(jk)
        qo.append(str(jd))
    print (str(qo))
    if pic is None:
        SuccessMsg = "Updated Successfully"
        return render(request, "patientdash.html", {'da':da,'s':ses, 'd':PatientId, 'n':name, 'q':qo})
    else:
        picc = []
        for ka,va in pic.items():
            picc.append(tuple((ka, va)))
        l = [x[1] for x in picc]
        print (l)
        pic = l

    if 'SessionStart' not in request.session:
        return redirect('/SignIn')
    else:
        SuccessMsg = "Updated Successfully"
        return render(request, "patientdash.html",{'da':da,'s':ses, 'd':PatientId, 'n':name, 'q':qo})

def Chart(request): ## chart
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')
    if 'my_pat' in request.session:
        PatientId = request.session['my_pat']
    print (PatientId)
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
#        datt1 = cache.get('my_pat2')
    return render(request, "chart.html",{'s':ses,'d':PatientId, 'n':name})
    #========== ends here
    #return render(request,'form.html')
    
def ContactPatientForm(request):   ## contactForm
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
    return render(request, 'contact.html', {'n':name})

def ContactPatient(request):   ## contactFormSucc
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')

    if 'my_pat' in request.session:
        PatientId = request.session['my_pat']
    print("this is datt1")
    print (PatientId)

    conto = db.child("users").child("patient").child(ses).child(PatientId).child("contactNo").shallow().get().val()
    smss = request.POST.get('noww')
    print('this is smss')
    print(smss)
    send_message(to=conto,text=smss)
    print (smss)
    le = db.child("users").child("patient").child(ses).child(PatientId).get().val()
    print (le)

    leb = []
    for key,value in le.items():
        leb.append(tuple((key, value)))
    leb.sort(reverse=True)
    print (leb)

    b = len(leb)
    print (b)

    g = [x[1] for x in leb]
    print (g)
    da = g
    # this is for pop up message
    name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
    pic = db.child("users").child("patientprof").child(ses).child("link").get().val()
    if pic is None:
        message = "Message Sent! Redirecting to Patient Profile"
        return render(request, "patientdash.html", {'da':da, 'n':name, 'm':message})
    else:
        picc = []
        for ka,va in pic.items():
            picc.append(tuple((ka, va)))
        l = [x[1] for x in picc]
        print (l)
        pic = l
        message = "Message Sent! Redirecting to Patient Profile"
        return render(request, "patientdash.html", {'da':da,'p':pic, 'n':name, 'm':message})

def ViewPatientVerifyCredentialsForm(request):  ## inputCredentialsForm
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')
    UserInfoDictionary = db.child("users").child("doctor").child(ses).child("email").shallow().get().val()
    if 'SessionStart' not in request.session:
        return redirect('/SignIn')
    else:
        return render(request, 'credentials.html', {'e':UserInfoDictionary})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def PatientListVerifyCredentials(request):  ## inputCredentials
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')
    email = db.child("users").child("doctor").child(ses).child("email").shallow().get().val()
    passw = request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "Invalid Crediantials!"
        return render(request,"credentials.html",{"m":message, 'e':email})

    print (user)
    uid = user['localId']
    print (user)
    request.session['SessionStart'] = str(uid)
    request.session['patientdash_session'] = str(uid)
    ses = request.session['SessionStart']

    if 'patientdash_session' not in request.session:
        return redirect('/vform')
    else:
        all_user_ids = db.child("users").child("patient").child(ses).get().val()
        name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
        if all_user_ids is None:
            return render(request, "nopat.html", {'n':name})
        else:
            print (all_user_ids)
            lis = []
            for item in all_user_ids:
                fename = db.child("users").child("patient").child(ses).child(item).child("fullname").child("firstname").shallow().get().val()
                lename = db.child("users").child("patient").child(ses).child(item).child("fullname").child("lastName").shallow().get().val()
                full = str(item)+ "-" +str(lename) +", "+str(fename)
                lis.append(str(full))
            lis.sort(reverse = True)
            print (lis)
            lise = lis

        if 'patientdash_session' not in request.session:
            return redirect('/login')
        else:
            return render(request, "patientlist.html",{'lise':lise, 'n':name})


def impForm(request):
    
    if 'SessionStart' in request.session:
        ses = request.session['SessionStart']
        print (ses)
    else:
        print ("No Session")
        return redirect('/SignIn')

    UserInfoDictionary = db.child("users").child("doctor").child(ses).child("email").shallow().get().val()
    return render(request, 'credentials1.html', {'e':UserInfoDictionary})

def impCredentials(request):
        if 'SessionStart' in request.session:
            ses = request.session['SessionStart']
            print (ses)
        else:
            print ("No Session")
            return redirect('/SignIn')
        UserInfoDictionary = db.child("users").child("doctor").child(ses).child("email").shallow().get().val()
        email = UserInfoDictionary
        passw = request.POST.get('pass')
        name = db.child("users").child("doctor").child(ses).child("fullname").child("firstname").shallow().get().val()
        try:
            user = authe.sign_in_with_email_and_password(email,passw)
        except:
            message = "Invalid Crediantials!"
            return render(request,"credentials1.html",{"m":message, 'e':UserInfoDictionary, 'n':name})
        print (user)
        uid = user['localId']
        print (user)
        request.session['SessionStart'] = str(uid)

        if 'SessionStart' not in request.session:
            return redirect('/SignIn')
        else:
            return render(request, "add.html",{'n':name})
