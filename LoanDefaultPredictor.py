
# Predict whether a small business borrower will default or repay.

from sklearn.datasets import make_moons
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


# Generating the data
X, y = make_moons(n_samples=1000, noise=0.25, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Using a basic pipeline and a polynomial pipeline

basic_path = make_pipeline(StandardScaler(), LogisticRegression())
poly_path = make_pipeline(PolynomialFeatures(degree=3, include_bias=False), StandardScaler(), LogisticRegression())

basic = basic_path.fit(X_train, y_train)
poly = poly_path.fit(X_train, y_train)

# Getting probable outcomes.

y_prob_base = basic.predict_proba(X_test)[:,1]
y_prob_poly = poly.predict_proba(X_test)[:,1]

# Area under the curve

auc_base = roc_auc_score(y_test, y_prob_base)
auc_poly = roc_auc_score(y_test, y_prob_poly)

print(f"Baseline AUC: {auc_base:.3f}")
print(f"Polynomial AUC: {auc_poly:.3f}")

""" I'll use an ROC curve to see how well the model catches actual defaulters (True positive rate)
as opposed to flagging good borrowers by mistake (false positive rate). 
"""

fpr_base, tpr_base, _ = roc_curve(y_test, y_prob_base)
fpr_poly, tpr_poly, thresholds = roc_curve(y_test, y_prob_poly)

# Plotting the curve

plt.figure(figsize=(8, 6))
plt.plot(fpr_base, tpr_base, linestyle='--', label=f'Baseline Linear(AUC = {auc_base:.2f})')
plt.plot(fpr_poly, tpr_poly, linewidth=2, label=f"Polynomial Degree 3: {auc_poly:.2f}")
plt.plot([0,1], [0,1], 'k', label='Random Guess (AUC = 0.50)')

plt.title('ROC curve: Loan Default Prediction')
plt.xlabel('False Positive Rate (Actual good borrowers flagged as defaulters.)')
plt.ylabel('True Posistive Rate (Actual defaulters caught.)')
plt.legend(loc='lower right')
plt.grid(alpha=0.3)
plt.show()


# Save to Json

