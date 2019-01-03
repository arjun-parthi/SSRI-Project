import pandas as pd
import numpy as np
from scipy import interp
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler

file1 = '../../data/FINAL_FEATURE_VECTOR_improved.csv'
features_all = pd.read_csv(file1)

disch = features_all.drop('DELTA_PAIN_3WEEKS', axis=1)
disch = disch.drop('DELTA_PAIN_8WEEKS', axis=1)
disch = disch.drop('CHANGE_DISCHARGE', axis=1)
disch = disch.drop('CHANGE_FOLLOWUP_3', axis=1)
disch = disch.drop('CHANGE_FOLLOWUP_8', axis=1)
disch = disch.drop('DAY_OF_DISCHARGE1', axis=1)
disch = disch.drop('FOLLOW_UP_3WEEKS1', axis=1)
disch = disch.drop('FOLLOW_UP_8WEEKS1', axis=1)
gender = {'Male': 0,'Female': 1}
race = {'White': 1,'Black': 2,'Hispanic': 3,'Asian': 4,'Other': 5}
marital = {'Married': 0,'Single': 1}
surgery = {'ORTHOPEDICS': 1,'BREAST': 2,'GENERAL': 3,'BREAST RECONSTRUCTION': 4,'THORACOTOMY': 5,'VASCULAR': 6}
insurance = {'Private': 1,'Medicare': 2,'Medicaid': 2,'Other': 2}
opioid = {'NO': 0,'YES': 1}
output = {'DECREASE': 0,'INCREASE': 1}

disch.GENDER = [gender[item] for item in disch.GENDER]
disch.RACE = [race[item] for item in disch.RACE]
disch.MARITAL_STATUS = [marital[item] for item in disch.MARITAL_STATUS]
disch.SURGERY_TYPE = [surgery[item] for item in disch.SURGERY_TYPE]
disch.INSURANCE_TYPE = [insurance[item] for item in disch.INSURANCE_TYPE]
disch.OPIOID_TOLERANT = [opioid[item] for item in disch.OPIOID_TOLERANT]
disch.DELTA_PAIN_DISCHARGE = [output[item] for item in disch.DELTA_PAIN_DISCHARGE]

disch1 = disch.dropna(subset=['DELTA_PAIN_DISCHARGE', 'PREOP_PAIN'])

fpr_load = []
tpr_load = []
thresholds = []
for i in range(10):
    train, test = train_test_split(disch1, test_size=0.2)

    scaler = MinMaxScaler()
    scaler.fit(train)
    train = scaler.transform(train)
    test = scaler.transform(test)
    regr = SVC(C=1.0, kernel='rbf', probability=True, tol=0.001, max_iter=3, class_weight = 'balanced')
    X = train[:,1:65]

    y = train[:,65]
    print(y.shape)
    regr.fit(X, y)
    X1 = test[:,1:65]
    y1 = test[:,65]
    predict_y1 = regr.predict_proba(X1)[:,1]
    false_positive_rate, true_positive_rate, thresholds = roc_curve(y1, predict_y1)
    fpr_load.append(false_positive_rate)
    tpr_load.append(true_positive_rate)

n_folds = len(fpr_load)
tprs = []
aucs = []
mean_fpr = np.linspace(0, 1, 100)
plt.figure(figsize=(10,8))
for i in range(n_folds):
    tprs.append(interp(mean_fpr, fpr_load[i], tpr_load[i]))
    tprs[-1][0] = 0.0
    roc_auc = auc(fpr_load[i], tpr_load[i])
    aucs.append(roc_auc)
    plt.plot(fpr_load[i], tpr_load[i], lw=1, alpha=0.3,
             label='ROC fold %d (AUC = %0.2f)' % (i, roc_auc))

plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
         label='Random prediction', alpha=.8)

mean_tpr = np.mean(tprs, axis=0)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
std_auc = np.std(aucs)
plt.plot(mean_fpr, mean_tpr, color='b',
         label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
         lw=2, alpha=.8)

std_tpr = np.std(tprs, axis=0)
tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
                 label=r'$\pm$ 1 std. dev.')

plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")
plt.show()

