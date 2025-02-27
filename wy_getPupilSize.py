# Import required modules
from math import *
import numpy as np
#set up a function to incorporate the entire equation
def getPupilSize(ageYrs, luminanceCdM2, fieldDiameterDeg, eyeNumber, whichModel):
    ## W&Y's (2012) unified formula
    fieldSizeDeg = ((fieldDiameterDeg/2)**2)*pi
    # switch will allow to chose which model we want to look at
    if whichModel == 'Unified':
        # refAge taken from W&Y(2012) paper, based on the mean age from S&D(1995)
        # sample. fieldSizeDeg calculates the field area (as required from the formula) from
        # the input of field diameter
        refAge = 28.58
        ## calculate pupil diameter
        # monocular/binocular effect factored into Stanley and Davies (1995) model.
        # *Luminance in the formula by 0.1 for one eye and 1 for two eyes
        if eyeNumber ==1:
            formulaDSD = 7.75-5.75*(((fieldSizeDeg*luminanceCdM2*0.1/846)**0.41)/((fieldSizeDeg*luminanceCdM2*0.1/846)**0.41 +2))
        else:
            formulaDSD = 7.75-5.75*(((fieldSizeDeg*luminanceCdM2/846)**0.41)/((fieldSizeDeg*luminanceCdM2/846)**0.41 +2))
        #this is the formula for the 'age slope' as mentioned in W&Y(2012)
        formulaS = 0.021323-0.0095623*formulaDSD
        #this is the formula for the 'age effect' as mentioned in W&Y(2012), it
        #includes the 'age slope' as part of the formula
        formulaA = (ageYrs-refAge)*formulaS
        #then calculate the unified formula. This involves the Stanley and Davies
        #formula with the mono/bino adjustment  added to the 'age effect'
        formulaU = formulaDSD + formulaA
        pupilDiameterMm = formulaU
        
        
    ## Other models quoted in W&Y (2012)
    # presented in order they are discussed in the paper.
    # D = pupil diameter, the following letter is the author's initals to help
    # differentiate between formulas.
    #
    # MoonSpencer, DeGrootGebhard and Crawford appear to underestimate
    # pupil size relative to the firgure in Watson & Yellot. We'll
    # ignore this for now.
    elif whichModel == 'Holladay':
        pupilDiameterMm = 7*np.exp(-0.1007*np.power(luminanceCdM2,0.4))
    elif whichModel == 'Crawford':
        pupilDiameterMm = 5 -2.2*np.tanh(0.61151+0.447*np.log10(luminanceCdM2))
    elif whichModel == 'MoonSpencer':
        pupilDiameterMm = 4.9 - 3*np.tanh(0.4*np.log10(luminanceCdM2))
    elif whichModel == 'DeGrootGebhard':
        pupilDiameterMm = 7.175*np.exp(-0.00092*np.power((7.597+np.log10(luminanceCdM2)),3))
    elif whichModel == 'StanleyDavies':
        pupilDiameterMm = 7.75-5.75*((np.power((fieldSizeDeg*luminanceCdM2/846),0.41))/(np.power((fieldSizeDeg*luminanceCdM2/846),0.41) +2))
    elif whichModel == 'Barten':
        pupilDiameterMm = 5 - 3*np.tanh(0.4*np.log10((luminanceCdM2*fieldSizeDeg)/(40**2)))
    elif whichModel == 'BlackieHowland':
        pupilDiameterMm = 5.697 - 0.658*np.log10(luminanceCdM2) - 0.07*np.power(np.log10(luminanceCdM2),2)
    elif whichModel == 'Winn':
        lCdM2 = np.copy(luminanceCdM2) # make a copy so limits don't change original range
        lCdM2[lCdM2 < 9] = 9
        lCdM2[lCdM2 > 4400] = 4400
        #calculate individual parts of the main formula, both of which are
        #summations
        S = [-0.024501, -0.0368073, 0.0210892, -0.00281557]
        #S = S.reverse() #(end:-1:1)
        B = [6.9039, 2.7765, -1.909, 0.25599]
        #B = B.reverse() #(end:-1:1)
        pupilDiameterMm = 0
        for k in range(4):
            pupilDiameterMm += ageYrs*S[k]*np.power(np.log10(lCdM2),k) +  B[k]*np.power(np.log10(lCdM2),k)
        #pupilDiameterMm = ageYrs*polyvalm(S, log10(lCdM2)) +  polyvalm(B, log10(lCdM2))
        #if something other than these model names is entered then it will
        # return an error
    else:
        error('unknown model')
        pupilDiameterMm
    return pupilDiameterMm

