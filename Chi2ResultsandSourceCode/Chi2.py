import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axis import XTick
np.set_printoptions(formatter={'float_kind':'{:f}'.format})   

# Read in data frame
trainingDf = pd.read_csv("cleaning_output.csv")

# Separate data into categories, starting with crime divided into 6 distinct categories, violent crime, non violent, theivery/robbery, traffic crimes, sexual crimes, and child crimes.
# The demographics into gender, age group, and race are also separated.
codeDf = trainingDf['Crime Code Description']

# Child Crime Category
childCrimeDf = codeDf[trainingDf['Crime Code Description'].isin(['KIDNAPPING - GRAND ATTEMPT','KIDNAPPING','CHILD STEALING','CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT','CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT','CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)0060','CHILD ABANDONMENT','DRUGS, TO A MINOR','CONTRIBUTING','CHILD NEGLECT (SEE 300 W.I.C.)','DISRUPT SCHOOL', 'CHILD ANNOYING (17YRS & UNDER)'])]

# Violent Crime Category
violentCrimeDf = codeDf[trainingDf['Crime Code Description'].isin(['CRIMINAL HOMICIDE',
'RAPE, FORCIBLE',
'RAPE, ATTEMPTED',
'LYNCHING',
'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER',
'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT',
'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
'SHOTS FIRED AT INHABITED DWELLING',
'BATTERY WITH SEXUAL CONTACT',
'INTIMATE PARTNER - AGGRAVATED ASSAULT',
'LYNCHING - ATTEMPTED',
'BATTERY POLICE (SIMPLE)',
'BATTERY ON A FIREFIGHTER',
'INTIMATE PARTNER - SIMPLE ASSAULT',
'BATTERY - SIMPLE ASSAULT',
'OTHER ASSAULT',
'ARSON',
'DISCHARGE FIREARMS/SHOTS FIRED',
'BRANDISH WEAPON',
'BOMB SCARE',
'WEAPONS POSSESSION/BOMBING',
'INCITING A RIOT',
'EXTORTION',
'CRIMINAL THREATS - NO WEAPON DISPLAYED',
'CRUELTY TO ANIMALS',
'THREATENING PHONE CALLS/LETTERS',
'RESISTING ARREST'])]

# NonViolent Crime
nonViolentCrimeDf = codeDf[trainingDf['Crime Code Description'].isin(['BIGAMY',
'BRIBERY',
'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)0132',
'ABORTION/ILLEGAL',
'CONSPIRACY',
'FALSE IMPRISONMENT',
'FALSE POLICE REPORT',
'ILLEGAL DUMPING',
'TELEPHONE PROPERTY - DAMAGE',
'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS) 0114',
'VANDALISM - MISDEAMEANOR ($399 OR UNDER)',
'VIOLATION OF COURT ORDER',
'VIOLATION OF RESTRAINING ORDER',
'VIOLATION OF TEMPORARY RESTRAINING ORDER',
'PROWLER',
'STALKING',
'UNAUTHORIZED COMPUTER ACCESS',
'TRESPASSING',
'CONTEMPT OF COURT',
'FAILURE TO DISPERSE',
'PANDERING',
'DRUNK ROLL',
'DISTURBING THE PEACE',
'OTHER MISCELLANEOUS CRIME'])]

# Sexual crimes
sexualCrimeDf = codeDf[trainingDf['Crime Code Description'].isin(['PIMPING',
'INCEST (SEXUAL ACTS BETWEN BLOOD RELATIVES)',
'SEX, UNLAWFUL',
'SEXUAL PENTRATION WITH A FOREIGN OBJECT',
'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH 0007=02',
'ORAL COPULATION',
'BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT WITH ANIM0065',
'INDECENT EXPOSURE',
'PEEPING TOM',
'LEWD CONDUCT',
'LETTERS, LEWD'])]

# Theft
theftCrimeDf = codeDf[trainingDf['Crime Code Description'].isin(['ROBBERY',
'ATTEMPTED ROBBERY',
'THEFT, PERSON',
'THEFT FROM PERSON - ATTEMPT',
'THEFT OF IDENTITY',
'BURGLARY',
'BURGLARY, ATTEMPTED',
'VEHICLE - STOLEN',
'BOAT - STOLEN',
'VEHICLE - ATTEMPT STOLEN',
'BURGLARY FROM VEHICLE',
'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)',
'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD0036',
'CREDIT CARDS, FRAUD USE ($950.01 & OVER)',
'GRAND THEFT / AUTO REPAIR',
'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)',
'GRAND THEFT / INSURANCE FRAUD',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $400',
'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)',
'DISHONEST EMPLOYEE - GRAND THEFT',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $400 & UNDER',
'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)',
'BUNCO, GRAND THEFT',
'TILL TAP - GRAND THEFT',
'DOCUMENT FORGERY / STOLEN FELONY',
'COUNTERFEIT',
'CREDIT CARDS, FRAUD USE ($950 & UNDER)',
'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
'TILL TAP - ATTEMPT',
'TILL TAP - PETTY ($950 & UNDER)',
'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
'THEFT, COIN MACINE - ATTEMPT',
'BUNCO, PETTY THEFT',
'DOCUMENT WORTHLESS ($200.01 & OVER)',
'PETTY THEFT - AUTO REPAIR',
'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)',
'BURGLARY FROM VEHICLE, ATTEMPTED',
'THEFT FROM MOTOR VEHICLE - ATTEMPT',
'THEFT PLAIN - PETTY ($950 & UNDER)',
'THEFT PLAIN - ATTEMPT',
'DOCUMENT WORTHLESS ($200 & UNDER)',
'DISHONEST EMPLOYEE - PETTY THEFT',
'DISHONEST EMPLOYEE ATTEMPTED THEFT',
'SHOPLIFTING - PETTY THEFT ($950 & UNDER)',
'SHOPLIFTING - ATTEMPT',
'BUNCO, ATTEMPT',
'DRIVING WITHOUT OWNER CONSENT (DWOC)',
'BIKE - STOLEN',
'BIKE - ATTEMPTED STOLEN',
'PURSE SNATCHING',
'PICKPOCKET',
'PURSE SNATCHING - ATTEMPT',
'PICKPOCKET, ATTEMPT'])]

# Traffic crimes
trafficCrimeDf = codeDf[trainingDf['Crime Code Description'].isin(['RECKLESS DRIVING',
'THROWING OBJECT AT MOVING VEHICLE',
'FAILURE TO YIELD'])]

# Gender Demographic
sexDfbefore = trainingDf['Victim Sex']
sexDf = sexDfbefore[trainingDf['Victim Sex'].isin(['M','F'])]
# Race Demographic
raceDf = trainingDf['Victim Descent']
descentDf = raceDf[trainingDf['Victim Descent'].isin(['B','H','W','A'])]
# Age group demographic
ageDfSingle = trainingDf['Age Class Code']
ageDf = ageDfSingle[trainingDf['Age Class Code'].isin(['1','2','3','4','5','6','7','8'])]

############################## Compute cross tab of categories ##############################
# Crosstab of child crimes tested against sex, race, and age
crosstabSexChild = pd.crosstab(childCrimeDf,sexDf)
crosstabRaceChild = pd.crosstab(childCrimeDf,descentDf)
crosstabAgeChild = pd.crosstab(childCrimeDf,ageDf)

# Crosstab of Violent crimes tested against sex, race, and age
crosstabAgeViolent = pd.crosstab(violentCrimeDf,ageDf)
crosstabRaceViolent = pd.crosstab(violentCrimeDf,descentDf)
crosstabSexViolent = pd.crosstab(violentCrimeDf,sexDf)

# Crosstab of sexual crimes tested against sex, race, and age
crosstabAgeSexual = pd.crosstab(sexualCrimeDf,ageDf)
crosstabRaceSexual = pd.crosstab(sexualCrimeDf,descentDf)
crosstabSexSexual = pd.crosstab(sexualCrimeDf,sexDf)

# Crosstab of traffic crimes tested against sex, race, and age
crosstabAgeTraffic = pd.crosstab(trafficCrimeDf,ageDf)
crosstabRaceTraffic = pd.crosstab(trafficCrimeDf,descentDf)
crosstabSexTraffic = pd.crosstab(trafficCrimeDf,sexDf)

# Crosstab of Non Violent crimes tested against sex, race, and age
crosstabAgeNonViolent = pd.crosstab(nonViolentCrimeDf,ageDf)
crosstabRaceNonViolent = pd.crosstab(nonViolentCrimeDf,descentDf)
crosstabSexNonViolent = pd.crosstab(nonViolentCrimeDf,sexDf)

# Crosstab of Theft crimes tested against sex, race, and age
crosstabAgeTheft = pd.crosstab(theftCrimeDf,ageDf)
crosstabRaceTheft = pd.crosstab( theftCrimeDf,descentDf)
crosstabSexTheft = pd.crosstab(theftCrimeDf,sexDf)

############################## Compute chi2 values ##############################
# Chi2 of child crimes tested against sex, race, and age group
chiXSexChild = stats.chi2_contingency(crosstabSexChild)
chiXRaceChild = stats.chi2_contingency(crosstabRaceChild)
chiXAgeChild = stats.chi2_contingency(crosstabAgeChild)

# Chi2 of theft crimes tested against sex, race, and age group
chiXSexTheft = stats.chi2_contingency(crosstabSexTheft)
chiXRaceTheft = stats.chi2_contingency(crosstabRaceTheft)
chiXAgeTheft = stats.chi2_contingency(crosstabAgeTheft)

# Chi2 of violent crimes tested against sex, race, and age group
chiXSexViolent = stats.chi2_contingency(crosstabSexViolent)
chiXRaceViolent = stats.chi2_contingency(crosstabRaceViolent)
chiXAgeViolent = stats.chi2_contingency(crosstabAgeViolent)

# Chi2 of non violent crimes tested against sex, race, and age group
chiXSexNonViolent = stats.chi2_contingency(crosstabSexNonViolent)
chiXRaceNonViolent = stats.chi2_contingency(crosstabRaceNonViolent)
chiXAgeNonViolent = stats.chi2_contingency(crosstabAgeNonViolent)

# Chi2 of traffic crimes tested against sex, race, and age group
chiXSexTraffic = stats.chi2_contingency(crosstabSexTraffic)
chiXRaceTraffic = stats.chi2_contingency(crosstabRaceTraffic)
chiXAgeTraffic = stats.chi2_contingency(crosstabAgeTraffic)

# Chi2 of sexual crimes tested against sex, race, and age group
chiXSexSexual = stats.chi2_contingency(crosstabSexSexual)
chiXRaceSexual = stats.chi2_contingency(crosstabRaceSexual)
chiXAgeSexual = stats.chi2_contingency(crosstabAgeSexual)

########################################################################################################################
# This function takes in the observed values area, the expected values array and generates a new final array of (Observed - expected) ^2
# Need to pass in row and col for this because I had to hardcode this to resemble the original crosstab
def observedExpected(obsArray, row, col, expArray):
    newArray = []
    for i in range(row):
        newArray.append([])
        for j in range(col):
            newArray[i].append(obsArray[i][j])
    finalArray = []
    for i in range(row):
        finalArray.append([])
        for j in range(col):
            finalArray[i].append((newArray[i][j]-expArray[i][j])**2)
            
    return finalArray
    
#################################################    
# FROM HERE ON OUT IS A LARGE DATA DUMP, PRINTING CROSSTABS,
# CHI SQUARED VALUES, OBSERVED VALUES, EXPECTED, (Observed - expected)^2, and show heatmaps!
       
# Sex against Child Crimes
print("Sex tested against Child Crimes")
print(crosstabSexChild)
print(chiXSexChild)
obsArraySexChild = crosstabSexChild.get_values()
print("Observed Values: " + "\n")
print(obsArraySexChild)
expArraySexCrime =  chiXSexChild[3]
print("Expected Values: " + "\n")
print(expArraySexCrime)
finalArray = observedExpected(obsArraySexChild,10,2,expArraySexCrime)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
plt.xticks(np.arange(0,2,step = 1),("F","M"))
list1 = ['KIDNAPPING - GRAND ATTEMPT','KIDNAPPING','CHILD STEALING','CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT','CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT','CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)0060','CHILD ABANDONMENT','CONTRIBUTING','CHILD NEGLECT (SEE 300 W.I.C.)', 'CHILD ANNOYING (17YRS & UNDER)']
list1.sort()
plt.yticks(np.arange(0,10,step=1),(list1))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Sex tested against Child Crimes')
plt.show()

# Race Against Child Crimes
print("Race tested against Child Crimes")
print(crosstabRaceChild)
print(chiXRaceChild)
obsArrayRaceChild = crosstabRaceChild.get_values()
print("Observed Values: " + "\n")
print(obsArrayRaceChild)
expArrayRaceCrime =  chiXRaceChild[3]
print("Expected Values: " + "\n")
print(expArrayRaceCrime)
finalArray = observedExpected(obsArrayRaceChild,10,4,expArrayRaceCrime)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list2 = ['KIDNAPPING - GRAND ATTEMPT','KIDNAPPING','CHILD STEALING','CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT','CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT','CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)0060','CHILD ABANDONMENT','CONTRIBUTING','CHILD NEGLECT (SEE 300 W.I.C.)', 'CHILD ANNOYING (17YRS & UNDER)']
list2.sort()
plt.xticks(np.arange(0,4,step = 1),("A", "B","H","W"))
plt.yticks(np.arange(0,10,step=1),(list2))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Race tested against Child Crimes')
plt.show()

# Age Against Child Crimes
print("Age tested against Child Crimes")
print(crosstabAgeChild)
print(chiXAgeChild)
obsArrayAgeChild = crosstabAgeChild.get_values()
print("Observed Values: " + "\n")
print(obsArrayAgeChild)
expArrayAgeCrime =  chiXAgeChild[3]
print("Expected Values: " + "\n")
print(expArrayAgeCrime)
finalArray = observedExpected(obsArrayAgeChild,10,5,expArrayAgeCrime)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list3 = ['KIDNAPPING - GRAND ATTEMPT','KIDNAPPING','CHILD STEALING','CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT','CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT','CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)0060','CHILD ABANDONMENT','CONTRIBUTING','CHILD NEGLECT (SEE 300 W.I.C.)', 'CHILD ANNOYING (17YRS & UNDER)']
list3.sort()
plt.xticks(np.arange(0,5,step = 1),("1.0","2.0","3.0","4.0","5.0"))
plt.yticks(np.arange(0,10,step=1),(list3))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Age tested against Child Crimes')
plt.show()

# Sex against Violent Crimes
print("Sex tested against Violent Crimes")
print(crosstabSexViolent)
print(chiXSexViolent)
obsArraySexViolent = crosstabSexViolent.get_values()
print("Observed Values: " + "\n")
print(obsArraySexViolent)
expArraySexViolent =  chiXSexViolent[3]
print("Expected Values: " + "\n")
print(expArraySexViolent)
finalArray = observedExpected(obsArraySexViolent,25,2,expArraySexViolent)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list4 = ['CRIMINAL HOMICIDE',
'RAPE, FORCIBLE',
'RAPE, ATTEMPTED',
'LYNCHING',
'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER',
'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT',
'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
'SHOTS FIRED AT INHABITED DWELLING',
'BATTERY WITH SEXUAL CONTACT',
'INTIMATE PARTNER - AGGRAVATED ASSAULT',
'BATTERY POLICE (SIMPLE)',
'BATTERY ON A FIREFIGHTER',
'INTIMATE PARTNER - SIMPLE ASSAULT',
'BATTERY - SIMPLE ASSAULT',
'OTHER ASSAULT',
'ARSON',
'DISCHARGE FIREARMS/SHOTS FIRED',
'BRANDISH WEAPON',
'BOMB SCARE',
'WEAPONS POSSESSION/BOMBING',
'EXTORTION',
'CRIMINAL THREATS - NO WEAPON DISPLAYED',
'CRUELTY TO ANIMALS',
'THREATENING PHONE CALLS/LETTERS',
'RESISTING ARREST']
list4.sort()
plt.xticks(np.arange(0,2,step = 1),("F","M"))
plt.yticks(np.arange(0,25,step=1),(list4))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Sex tested against Violent Crimes')
plt.show()

# Race Against Violent Crimes
print("Race tested against Violent Crimes")
print(crosstabRaceViolent)
print(chiXRaceViolent)
obsArrayRaceViolent = crosstabRaceViolent.get_values()
print("Observed Values: " + "\n")
print(obsArrayRaceViolent)
expArrayRaceViolent =  chiXRaceViolent[3]
print("Expected Values: " + "\n")
print(expArrayRaceViolent)
finalArray = observedExpected(obsArrayRaceViolent,24,4,expArrayRaceViolent)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list5 = ['CRIMINAL HOMICIDE',
'RAPE, FORCIBLE',
'RAPE, ATTEMPTED',
'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER',
'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT',
'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
'SHOTS FIRED AT INHABITED DWELLING',
'BATTERY WITH SEXUAL CONTACT',
'INTIMATE PARTNER - AGGRAVATED ASSAULT',
'BATTERY POLICE (SIMPLE)',
'BATTERY ON A FIREFIGHTER',
'INTIMATE PARTNER - SIMPLE ASSAULT',
'BATTERY - SIMPLE ASSAULT',
'OTHER ASSAULT',
'ARSON',
'DISCHARGE FIREARMS/SHOTS FIRED',
'BRANDISH WEAPON',
'BOMB SCARE',
'WEAPONS POSSESSION/BOMBING',
'EXTORTION',
'CRIMINAL THREATS - NO WEAPON DISPLAYED',
'CRUELTY TO ANIMALS',
'THREATENING PHONE CALLS/LETTERS',
'RESISTING ARREST']
list5.sort()
plt.xticks(np.arange(0,4,step = 1),("A", "B","H","W"))
plt.yticks(np.arange(0,24,step=1),(list5))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Race tested against Violent Crimes')
plt.show()

# Age Against Violent Crimes
print("Age tested against Violent Crimes")
print(crosstabAgeViolent)
print(chiXAgeViolent)
obsArrayAgeViolent = crosstabAgeViolent.get_values()
print("Observed Values: " + "\n")
print(obsArrayAgeViolent)
expArrayAgeViolent =  chiXAgeViolent[3]
print("Expected Values: " + "\n")
print(expArrayAgeViolent)
finalArray = observedExpected(obsArrayAgeViolent,24,7,expArrayAgeViolent)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list6 = ['CRIMINAL HOMICIDE',
'RAPE, FORCIBLE',
'RAPE, ATTEMPTED',
'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER',
'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT',
'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT',
'SHOTS FIRED AT INHABITED DWELLING',
'BATTERY WITH SEXUAL CONTACT',
'INTIMATE PARTNER - AGGRAVATED ASSAULT',
'BATTERY POLICE (SIMPLE)',
'BATTERY ON A FIREFIGHTER',
'INTIMATE PARTNER - SIMPLE ASSAULT',
'BATTERY - SIMPLE ASSAULT',
'OTHER ASSAULT',
'ARSON',
'DISCHARGE FIREARMS/SHOTS FIRED',
'BRANDISH WEAPON',
'BOMB SCARE',
'WEAPONS POSSESSION/BOMBING',
'EXTORTION',
'CRIMINAL THREATS - NO WEAPON DISPLAYED',
'CRUELTY TO ANIMALS',
'THREATENING PHONE CALLS/LETTERS',
'RESISTING ARREST']
list6.sort()
plt.xticks(np.arange(0,7,step = 1),("1","2","3","4","5","6","7"))
plt.yticks(np.arange(0,24,step=1),(list6))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Age tested against Violent Crimes')
plt.show()

# Sex against non-Violent Crimes
print("Sex tested against NonViolent Crimes")
print(crosstabSexNonViolent)
print(chiXSexNonViolent)
obsArraySexNonViolent = crosstabSexNonViolent.get_values()
print("Observed Values: " + "\n")
print(obsArraySexNonViolent)
expArraySexNonViolent =  chiXSexNonViolent[3]
print("Expected Values: " + "\n")
print(expArraySexNonViolent)
finalArray = observedExpected(obsArraySexNonViolent,21,2,expArraySexNonViolent)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list7 = [
'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)0132',
'ABORTION/ILLEGAL',
'CONSPIRACY',
'FALSE IMPRISONMENT',
'FALSE POLICE REPORT',
'ILLEGAL DUMPING',
'TELEPHONE PROPERTY - DAMAGE',
'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS) 0114',
'VANDALISM - MISDEAMEANOR ($399 OR UNDER)',
'VIOLATION OF COURT ORDER',
'VIOLATION OF RESTRAINING ORDER',
'VIOLATION OF TEMPORARY RESTRAINING ORDER',
'PROWLER',
'STALKING',
'UNAUTHORIZED COMPUTER ACCESS',
'TRESPASSING',
'CONTEMPT OF COURT',
'FAILURE TO DISPERSE',
'PANDERING',
'DISTURBING THE PEACE',
'OTHER MISCELLANEOUS CRIME']
list7.sort()
plt.xticks(np.arange(0,2,step = 1),("F","M"))
plt.yticks(np.arange(0,21,step=1),(list7))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Sex tested against Non-Violent Crimes')
plt.show()

# Race Against NonViolent Crimes
print("Race tested against NonViolent Crimes")
print(crosstabRaceNonViolent)
print(chiXRaceNonViolent)
obsArrayRaceNonViolent = crosstabRaceNonViolent.get_values()
print("Observed Values: " + "\n")
print(obsArrayRaceNonViolent)
expArrayRaceNonViolent =  chiXRaceNonViolent[3]
print("Expected Values: " + "\n")
print(expArrayRaceNonViolent)
finalArray = observedExpected(obsArrayRaceNonViolent,19,4,expArrayRaceNonViolent)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list8 = [
'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)0132',
'CONSPIRACY',
'FALSE IMPRISONMENT',
'FALSE POLICE REPORT',
'ILLEGAL DUMPING',
'TELEPHONE PROPERTY - DAMAGE',
'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS) 0114',
'VANDALISM - MISDEAMEANOR ($399 OR UNDER)',
'VIOLATION OF COURT ORDER',
'VIOLATION OF RESTRAINING ORDER',
'VIOLATION OF TEMPORARY RESTRAINING ORDER',
'PROWLER',
'STALKING',
'UNAUTHORIZED COMPUTER ACCESS',
'TRESPASSING',
'CONTEMPT OF COURT',
'PANDERING',
'DISTURBING THE PEACE',
'OTHER MISCELLANEOUS CRIME']
list8.sort()
plt.xticks(np.arange(0,4,step = 1),("A", "B","H","W"))
plt.yticks(np.arange(0,19,step=1),(list8))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Race tested against Non-Violent Crimes')
plt.show()

# Age Against NonViolent Crimes
print("Age tested against NonViolent Crimes")
print(crosstabAgeNonViolent)
print(chiXAgeNonViolent)
obsArrayAgeNonViolent = crosstabAgeNonViolent.get_values()
print("Observed Values: " + "\n")
print(obsArrayAgeNonViolent)
expArrayAgeNonViolent =  chiXAgeNonViolent[3]
print("Expected Values: " + "\n")
print(expArrayAgeNonViolent)
finalArray = observedExpected(obsArrayAgeNonViolent,21,7,expArrayAgeNonViolent)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list9 = [
'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)0132',
'BRIBERY',
'CONSPIRACY',
'FALSE IMPRISONMENT',
'FALSE POLICE REPORT',
'ILLEGAL DUMPING',
'TELEPHONE PROPERTY - DAMAGE',
'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS) 0114',
'VANDALISM - MISDEAMEANOR ($399 OR UNDER)',
'VIOLATION OF COURT ORDER',
'VIOLATION OF RESTRAINING ORDER',
'VIOLATION OF TEMPORARY RESTRAINING ORDER',
'PROWLER',
'STALKING',
'UNAUTHORIZED COMPUTER ACCESS',
'TRESPASSING',
'CONTEMPT OF COURT',
'FAILURE TO DISPERSE',
'PANDERING',
'DISTURBING THE PEACE',
'OTHER MISCELLANEOUS CRIME']
list9.sort()
plt.xticks(np.arange(0,7,step = 1),("1","2","3","4","5","6","7"))
plt.yticks(np.arange(0,21,step=1),(list9))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Age tested against Non-Violent Crimes')
plt.show()

# Sex against traffic Crimes
print("Sex tested against Traffic Crimes")
print(crosstabSexTraffic)
print(chiXSexTraffic)
obsArraySexTraffic = crosstabSexTraffic.get_values()
print("Observed Values: " + "\n")
print(obsArraySexTraffic)
expArraySexTraffic =  chiXSexTraffic[3]
print("Expected Values: " + "\n")
print(expArraySexTraffic)
finalArray = observedExpected(obsArraySexTraffic,3,2,expArraySexTraffic)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list10 = [
'RECKLESS DRIVING',
'THROWING OBJECT AT MOVING VEHICLE',
'FAILURE TO YIELD']
list10.sort()
plt.xticks(np.arange(0,2,step = 1),("F","M"))
plt.yticks(np.arange(0,3,step=1),(list10))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Sex tested against Traffic Crimes')
plt.show()

# Race Against Traffic Crimes
print("Race tested against Traffic Crimes")
print(crosstabRaceTraffic)
print(chiXRaceTraffic)
obsArrayRaceTraffic = crosstabRaceTraffic.get_values()
print("Observed Values: " + "\n")
print(obsArrayRaceTraffic)
expArrayRaceTraffic =  chiXRaceTraffic[3]
print("Expected Values: " + "\n")
print(expArrayRaceTraffic)
finalArray = observedExpected(obsArrayRaceTraffic,3,4,expArrayRaceTraffic)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list11 = [
'RECKLESS DRIVING',
'THROWING OBJECT AT MOVING VEHICLE',
'FAILURE TO YIELD']
list11.sort()
plt.xticks(np.arange(0,4,step = 1),("A", "B","H","W"))
plt.yticks(np.arange(0,3,step=1),(list11))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Race tested against Traffic Crimes')
plt.show()

# Age Against Traffic Crimes
print("Age tested against Traffic Crimes")
print(crosstabAgeTraffic)
print(chiXAgeTraffic)
obsArrayAgeTraffic = crosstabAgeTraffic.get_values()
print("Observed Values: " + "\n")
print(obsArrayAgeTraffic)
expArrayAgeTraffic =  chiXAgeTraffic[3]
print("Expected Values: " + "\n")
#print(expArrayAgeTraffic)
finalArray = observedExpected(obsArrayAgeTraffic,3,4,expArrayAgeTraffic)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list12 = [
'RECKLESS DRIVING',
'THROWING OBJECT AT MOVING VEHICLE',
'FAILURE TO YIELD']
list12.sort()
plt.xticks(np.arange(0,4,step = 1),("2","3","4","5"))
plt.yticks(np.arange(0,3,step=1),(list12))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Age tested against Traffic Crimes')
plt.show()

# Sex against sexual Crimes
print("Sex tested against Sexual Crimes")
print(crosstabSexSexual)
print(chiXSexSexual)
obsArraySexSexual = crosstabSexSexual.get_values()
print("Observed Values: " + "\n")
print(obsArraySexSexual)
expArraySexSexual =  chiXSexSexual[3]
print("Expected Values: " + "\n")
print(expArraySexSexual)
finalArray = observedExpected(obsArraySexSexual,10,2,expArraySexSexual)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list13 = [
'PIMPING',
'SEX, UNLAWFUL',
'SEXUAL PENTRATION WITH A FOREIGN OBJECT',
'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH 0007=02',
'ORAL COPULATION',
'BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT WITH ANIM0065',
'INDECENT EXPOSURE',
'PEEPING TOM',
'LEWD CONDUCT',
'LETTERS, LEWD']
list13.sort()
plt.xticks(np.arange(0,2,step = 1),("F","M"))
plt.yticks(np.arange(0,10,step=1),(list13))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Sex tested against Sexual Crimes')
plt.show()

# Race Against Sexual Crimes
print("Race tested against Sexual Crimes")
print(crosstabRaceSexual)
print(chiXRaceSexual)
obsArrayRaceSexual = crosstabRaceSexual.get_values()
print("Observed Values: " + "\n")
print(obsArrayRaceSexual)
expArrayRaceSexual =  chiXRaceSexual[3]
print("Expected Values: " + "\n")
print(expArrayRaceSexual)
finalArray = observedExpected(obsArrayRaceSexual,9,4,expArrayRaceSexual)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list14 = [
'PIMPING',
'SEX, UNLAWFUL',
'SEXUAL PENTRATION WITH A FOREIGN OBJECT',
'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH 0007=02',
'ORAL COPULATION',
'INDECENT EXPOSURE',
'PEEPING TOM',
'LEWD CONDUCT',
'LETTERS, LEWD']
list14.sort()
plt.xticks(np.arange(0,4,step = 1),("A", "B","H","W"))
plt.yticks(np.arange(0,9,step=1),(list14))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Race tested against Sexual Crimes')
plt.show()

# Age Against Sexual Crimes
print("Age tested against Sexual Crimes")
print(crosstabAgeSexual)
print(chiXAgeSexual)
obsArrayAgeSexual = crosstabAgeSexual.get_values()
print("Observed Values: " + "\n")
print(obsArrayAgeSexual)
expArrayAgeSexual =  chiXAgeSexual[3]
print("Expected Values: " + "\n")
print(expArrayAgeSexual)
finalArray = observedExpected(obsArrayAgeSexual,9,7,expArrayAgeSexual)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list15 = [
'PIMPING',
'SEX, UNLAWFUL',
'SEXUAL PENTRATION WITH A FOREIGN OBJECT',
'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH 0007=02',
'ORAL COPULATION',
'INDECENT EXPOSURE',
'PEEPING TOM',
'LEWD CONDUCT',
'LETTERS, LEWD']
list15.sort()
plt.xticks(np.arange(0,7,step = 1),("1","2","3","4","5","6","7"))
plt.yticks(np.arange(0,9,step=1),(list15))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Age tested against Sexual Crimes')
plt.show()

# Sex against Theft Crimes
print("Sex tested against Theft Crimes")
print(crosstabSexTheft)
print(chiXSexTheft)
obsArraySexTheft = crosstabSexTheft.get_values()
print("Observed Values: " + "\n")
print(obsArraySexTheft)
expArraySexTheft =  chiXSexTheft[3]
print("Expected Values: " + "\n")
print(expArraySexTheft)
finalArray = observedExpected(obsArraySexTheft,44,2,expArraySexTheft)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list16 = [
'ROBBERY',
'ATTEMPTED ROBBERY',
'THEFT, PERSON',
'THEFT FROM PERSON - ATTEMPT',
'THEFT OF IDENTITY',
'BURGLARY',
'BURGLARY, ATTEMPTED',
'VEHICLE - STOLEN',
'VEHICLE - ATTEMPT STOLEN',
'BURGLARY FROM VEHICLE',
'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)',
'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD0036',
'CREDIT CARDS, FRAUD USE ($950.01 & OVER)',
'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)',
'GRAND THEFT / INSURANCE FRAUD',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $400',
'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)',
'DISHONEST EMPLOYEE - GRAND THEFT',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $400 & UNDER',
'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)',
'BUNCO, GRAND THEFT',
'DOCUMENT FORGERY / STOLEN FELONY',
'COUNTERFEIT',
'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
'TILL TAP - PETTY ($950 & UNDER)',
'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
'BUNCO, PETTY THEFT',
'DOCUMENT WORTHLESS ($200.01 & OVER)',
'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)',
'BURGLARY FROM VEHICLE, ATTEMPTED',
'THEFT FROM MOTOR VEHICLE - ATTEMPT',
'THEFT PLAIN - PETTY ($950 & UNDER)',
'THEFT PLAIN - ATTEMPT',
'DISHONEST EMPLOYEE - PETTY THEFT',
'SHOPLIFTING - PETTY THEFT ($950 & UNDER)',
'SHOPLIFTING - ATTEMPT',
'BUNCO, ATTEMPT',
'DRIVING WITHOUT OWNER CONSENT (DWOC)',
'BIKE - STOLEN',
'BIKE - ATTEMPTED STOLEN',
'PURSE SNATCHING',
'PICKPOCKET',
'PURSE SNATCHING - ATTEMPT',
'PICKPOCKET, ATTEMPT']
list16.sort()
plt.xticks(np.arange(0,2,step = 1),("F","M"))
plt.yticks(np.arange(0,44,step=1),(list16))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Sex tested against Robberies and Thefts')
plt.show()

# Race Against Theft Crimes
print("Race tested against Theft Crimes")
print(crosstabRaceTheft)
print(chiXRaceTheft)
obsArrayRaceTheft = crosstabRaceTheft.get_values()
print("Observed Values: " + "\n")
print(obsArrayRaceTheft)
expArrayRaceTheft =  chiXRaceTheft[3]
print("Expected Values: " + "\n")
print(expArrayRaceTheft)
finalArray = observedExpected(obsArrayRaceTheft,43,4,expArrayRaceTheft)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list17 = [
'ROBBERY',
'ATTEMPTED ROBBERY',
'THEFT, PERSON',
'THEFT FROM PERSON - ATTEMPT',
'THEFT OF IDENTITY',
'BURGLARY',
'BURGLARY, ATTEMPTED',
'VEHICLE - STOLEN',
'VEHICLE - ATTEMPT STOLEN',
'BURGLARY FROM VEHICLE',
'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)',
'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD0036',
'CREDIT CARDS, FRAUD USE ($950.01 & OVER)',
'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)',
'GRAND THEFT / INSURANCE FRAUD',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $400',
'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)',
'DISHONEST EMPLOYEE - GRAND THEFT',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $400 & UNDER',
'BUNCO, GRAND THEFT',
'DOCUMENT FORGERY / STOLEN FELONY',
'COUNTERFEIT',
'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
'TILL TAP - PETTY ($950 & UNDER)',
'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
'BUNCO, PETTY THEFT',
'DOCUMENT WORTHLESS ($200.01 & OVER)',
'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)',
'BURGLARY FROM VEHICLE, ATTEMPTED',
'THEFT FROM MOTOR VEHICLE - ATTEMPT',
'THEFT PLAIN - PETTY ($950 & UNDER)',
'THEFT PLAIN - ATTEMPT',
'DISHONEST EMPLOYEE - PETTY THEFT',
'SHOPLIFTING - PETTY THEFT ($950 & UNDER)',
'SHOPLIFTING - ATTEMPT',
'BUNCO, ATTEMPT',
'DRIVING WITHOUT OWNER CONSENT (DWOC)',
'BIKE - STOLEN',
'BIKE - ATTEMPTED STOLEN',
'PURSE SNATCHING',
'PICKPOCKET',
'PURSE SNATCHING - ATTEMPT',
'PICKPOCKET, ATTEMPT']
list17.sort()
plt.xticks(np.arange(0,4,step = 1),("A", "B","H","W"))
plt.yticks(np.arange(0,43,step=1),(list17))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Race tested against Robberies and Thefts')
plt.show()

# Age Against Theft Crimes
print("Age tested against Theft Crimes")
print(crosstabAgeTheft)
print(chiXAgeTheft)
obsArrayAgeTheft = crosstabAgeTheft.get_values()
print("Observed Values: " + "\n")
print(obsArrayAgeTheft)
expArrayAgeTheft =  chiXAgeTheft[3]
print("Expected Values: " + "\n")
print(expArrayAgeTheft)
finalArray = observedExpected(obsArrayAgeTheft,43,7,expArrayAgeTheft)
print("Observed - expected sqaured values: " + "\n")
# Heatmap
heat = plt.imshow(np.matrix(finalArray),cmap ='hot',interpolation='nearest')
list18 = [
'ROBBERY',
'ATTEMPTED ROBBERY',
'THEFT, PERSON',
'THEFT FROM PERSON - ATTEMPT',
'THEFT OF IDENTITY',
'BURGLARY',
'BURGLARY, ATTEMPTED',
'VEHICLE - STOLEN',
'VEHICLE - ATTEMPT STOLEN',
'BURGLARY FROM VEHICLE',
'THEFT FROM MOTOR VEHICLE - GRAND ($400 AND OVER)',
'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD0036',
'CREDIT CARDS, FRAUD USE ($950.01 & OVER)',
'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)',
'GRAND THEFT / INSURANCE FRAUD',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $400',
'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)',
'DISHONEST EMPLOYEE - GRAND THEFT',
'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $400 & UNDER',
'BUNCO, GRAND THEFT',
'DOCUMENT FORGERY / STOLEN FELONY',
'COUNTERFEIT',
'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)',
'TILL TAP - PETTY ($950 & UNDER)',
'THEFT, COIN MACHINE - PETTY ($950 & UNDER)',
'BUNCO, PETTY THEFT',
'DOCUMENT WORTHLESS ($200.01 & OVER)',
'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)',
'BURGLARY FROM VEHICLE, ATTEMPTED',
'THEFT FROM MOTOR VEHICLE - ATTEMPT',
'THEFT PLAIN - PETTY ($950 & UNDER)',
'THEFT PLAIN - ATTEMPT',
'DISHONEST EMPLOYEE - PETTY THEFT',
'SHOPLIFTING - PETTY THEFT ($950 & UNDER)',
'SHOPLIFTING - ATTEMPT',
'BUNCO, ATTEMPT',
'DRIVING WITHOUT OWNER CONSENT (DWOC)',
'BIKE - STOLEN',
'BIKE - ATTEMPTED STOLEN',
'PURSE SNATCHING',
'PICKPOCKET',
'PURSE SNATCHING - ATTEMPT',
'PICKPOCKET, ATTEMPT']
list18.sort()
plt.xticks(np.arange(0,7,step = 1),("1","2","3","4","5","6","7"))
plt.yticks(np.arange(0,43,step=1),(list18))
plt.colorbar(heat)
print(np.matrix(finalArray))
plt.title('Age tested against Robberies and Thefts')
plt.show()



        




