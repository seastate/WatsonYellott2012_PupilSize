from wy_getPupilSize import getPupilSize
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

#close all;

## Full Pupil diameter calculation and demonstration scrip
# variables entered here feed through the first function
ageYrs = 30
fieldDiameterDeg = 60
eyeNumber = 2
x = np.logspace(-4,4,base=10,num=100)# 10.^(-4:0.01:4)
## first plot
# run the function generated in 'pupilequation2'
pupilDiameterMm1 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Unified')
pupilDiameterMm2 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Holladay')
pupilDiameterMm3 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Crawford')
pupilDiameterMm4 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'MoonSpencer')
pupilDiameterMm5 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'DeGrootGebhard')
pupilDiameterMm6 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'StanleyDavies')
pupilDiameterMm7 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Barten')
pupilDiameterMm8 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'BlackieHowland')
pupilDiameterMm9 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Winn')


fig, axs = plt.subplots(1,2)
#fig0 = figs[0]
ax0 = axs[0]

ax0.semilogx(x, pupilDiameterMm1, 'k--', linewidth=2.5)
ax0.semilogx(x, pupilDiameterMm2, color=[202/255, 202/255, 202/255], linewidth=1.5) 
ax0.semilogx(x, pupilDiameterMm3, 'b', linewidth=1.5) 
ax0.semilogx(x, pupilDiameterMm4, 'm', linewidth=1.5) 
ax0.semilogx(x, pupilDiameterMm5, 'r', linewidth=1.5) 
ax0.semilogx(x, pupilDiameterMm6, '--', color=[179/255, 138/255, 99/255], linewidth=1.5) 
ax0.semilogx(x, pupilDiameterMm7, '--', color=[163/255, 70/255, 161/255], linewidth=1.5) 
ax0.semilogx(x, pupilDiameterMm8, color=[254/255, 188/255, 120/255], linewidth=1.5) 
ax0.semilogx(x, pupilDiameterMm9, '--', color=[126/255, 162/255, 134/255], linewidth=1.5) 
ax0.set(xlabel='Luminance (cd{\cdot}m^{-2})', ylabel='Diameter (mm)')
ax0.grid()

ax0.legend(['Unified', 'Holladay', 'Crawford', 'MoonSpencer', 'DeGrootGebhard', 'StanleyDavies', 'Barten', 'BlackieHowland', 'Winn'])
ax0.set_ylim([2, 8.15])
ax0.set(title='Observer age: '+str(ageYrs)+' yrs\nField diameter: '+str(fieldDiameterDeg)+' deg')

## second plot
ageYrs = 30
fieldDiameterDeg = 10
eyeNumber = 1

x = np.logspace(-4,4,base=10,num=100)# 10.^(-4:0.01:4)
## first plot
# run the function generated in 'pupilequation2'
pupilDiameterMm1 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Unified')
pupilDiameterMm2 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Holladay')
pupilDiameterMm3 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Crawford')
pupilDiameterMm4 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'MoonSpencer')
pupilDiameterMm5 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'DeGrootGebhard')
pupilDiameterMm6 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'StanleyDavies')
pupilDiameterMm7 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Barten')
pupilDiameterMm8 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'BlackieHowland')
pupilDiameterMm9 = getPupilSize(ageYrs, x, fieldDiameterDeg, eyeNumber, 'Winn')


#fig1 = figs[1]
ax1 = axs[1]


ax1.semilogx(x, pupilDiameterMm1, 'k--', linewidth=2.5)
ax1.semilogx(x, pupilDiameterMm2, color=[202/255, 202/255, 202/255], linewidth=1.5) 
ax1.semilogx(x, pupilDiameterMm3, 'b', linewidth=1.5) 
ax1.semilogx(x, pupilDiameterMm4, 'm', linewidth=1.5) 
ax1.semilogx(x, pupilDiameterMm5, 'r', linewidth=1.5) 
ax1.semilogx(x, pupilDiameterMm6, '--', color=[179/255, 138/255, 99/255], linewidth=1.5) 
ax1.semilogx(x, pupilDiameterMm7, '--', color=[163/255, 70/255, 161/255], linewidth=1.5) 
ax1.semilogx(x, pupilDiameterMm8, color=[254/255, 188/255, 120/255], linewidth=1.5) 
ax1.semilogx(x, pupilDiameterMm9, '--', color=[126/255, 162/255, 134/255], linewidth=1.5) 
ax1.set(xlabel='Luminance (cd{\cdot}m^{-2})', ylabel='Diameter (mm)')
ax1.grid()

ax1.legend(['Unified', 'Holladay', 'Crawford', 'MoonSpencer', 'DeGrootGebhard', 'StanleyDavies', 'Barten', 'BlackieHowland', 'Winn'])
ax1.set_ylim([2, 8.15])
ax1.set(title='Observer age: '+str(ageYrs)+' yrs\nField diameter: '+str(fieldDiameterDeg)+' deg')

# Save plots
plt.savefig('py_allModels.png',bbox_inches='tight',dpi=600)
plt.savefig('py_allModels.pdf',bbox_inches='tight',dpi=600)
