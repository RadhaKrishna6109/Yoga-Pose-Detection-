from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from users.forms import UserRegistrationForm
from users.models import UserRegistrationModel

def UserLogin(request):
    return render(request, 'UserLogin.html', {})

def userHome(request):
    return render(request, 'users/UserHomePage.html', {})



def UserRegisterAction(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            # return HttpResponseRedirect('./CustLogin')
            form = UserRegistrationForm()
            return render(request, 'Register.html', {'form': form})
        else:
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'Register.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHomePage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})

def training_view(request):
    return render(request, "Yoga_training/index.html")

def UserTraining(request):
    from .utility import yoga_pose_classification
    rf_acc,rf_precision,rf_recall,rf_f1 = yoga_pose_classification.RandomForest()
    lr_acc,lr_precision,lr_recall,lr_f1 = yoga_pose_classification.LogisticRegression()
    svm_acc,svm_precision,svm_recall,svm_f1 = yoga_pose_classification.SVM()
    knn_acc,knn_precision,knn_recall,knn_f1 = yoga_pose_classification.KNN()
    results = {
        'rf_acc':rf_acc,'rf_precision':rf_precision,'rf_recall':rf_recall,'rf_f1':rf_f1,
        'lr_acc':lr_acc,'lr_precision':lr_precision,'lr_recall':lr_recall,'lr_f1':lr_f1,
        'svm_acc':svm_acc,'svm_precision':svm_precision,'svm_recall':svm_precision,'svm_f1':svm_f1,
        'knn_acc':knn_acc,'knn_precision':knn_precision,'knn_recall':knn_precision,'knn_f1':knn_f1
        
    }
    return render(request,'Yoga_training/yoga_training.html',results)

def prediction_view(request):
    return render(request, "Yoga_prediction/index.html")

