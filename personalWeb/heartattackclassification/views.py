from django.shortcuts import render
from .models import HAC
import pandas as pd
import sklearn
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from django.shortcuts import redirect

df = pd.read_csv("heartattackclassification\static\heartattackclassification\heart.csv")

# Use the SimpleImputer to replace missing values
imp = SimpleImputer(strategy='mean')
df = imp.fit_transform(df)

# Convert the imputed data back to a DataFrame
df = pd.DataFrame(df, columns=['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall', 'output'])

X = df.drop(['output'], axis = 1)
Y = df['output']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25)
optiparams = {'criterion': 'entropy', 'max_depth': 4, 'max_features': 'auto', 'min_samples_leaf': 1, 'min_samples_split': 5, 'splitter': 'random'}
Tree = DecisionTreeClassifier(criterion = optiparams['criterion'], max_depth = optiparams['max_depth'], max_features = optiparams['max_features'], min_samples_leaf = optiparams['min_samples_leaf'], min_samples_split = optiparams['min_samples_split'], splitter = optiparams['splitter'])
Tree.fit(X_train, Y_train)


# Create your views here.
def heartattackclassification(request):
    hac_submits = HAC.objects.all().order_by('-id')
    context = {'hac_submits': hac_submits}
    return render(request, 'heartattackclassification/home.html', context)

def info(request):
    return render(request, 'heartattackclassification/info.html')

def hac_submit(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        cp = request.POST.get('cp')
        trtbps = request.POST.get('trtbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        thalachh = request.POST.get('thalachh')
        exng = request.POST.get('exng')
        oldpeak = request.POST.get('oldpeak')
        slp = request.POST.get('slp')
        caa = request.POST.get('caa')
        thall = request.POST.get('thall')
        
        inputs = {'age': [age], 'sex': [sex], 'cp': [cp], 'trtbps': [trtbps], 'chol': [chol],
              'fbs': [fbs], 'restecg': [restecg], 'thalachh': [thalachh], 'exng': [exng],
              'oldpeak': [oldpeak], 'slp': [slp], 'caa': [caa], 'thall': [thall]}
        df_inputs = pd.DataFrame(inputs)

        # Use the classifier to make a prediction
        prediction = Tree.predict(df_inputs)
        output = prediction[0]

        hac_object = HAC(
            age=age, 
            sex=sex, 
            cp=cp, 
            trtbps=trtbps, 
            chol=chol, 
            fbs=fbs, 
            restecg=restecg, 
            thalachh=thalachh, 
            exng=exng, 
            oldpeak=oldpeak, 
            slp=slp, 
            caa=caa, 
            thall=thall,
            output=output)
        hac_object.save()

    # If the request is not a POST, return the form template
    return redirect('heartattackclassification:heartattackclassification')