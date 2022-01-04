import math
import pandas as pd
import openpyxl, xlrd
from matplotlib import pyplot

StatData = pd.read_excel ('Substats.xlsx', engine='openpyxl')
StatData = StatData.loc[:,~StatData.columns.str.match("Unnamed")]
#print(StatData.columns)

class data():
	def __init__(self, CRIT, DET, DH, TEN):
		self.CRIT = CRIT
		self.DET = DET
		self.DH = DH
		self.TEN = TEN 
		dummy, self.CRITrate, self.CRITmult = CRITmod(CRIT)
		dummy, self.DHrate, self.DHmult = DHmod(DH)
		self.f_DET = DETmod(DET)
		self.f_TEN = TENmod(TEN)

		#Separate pure Crit and DH from combined
		self.CRIT_DHmult = (1 + self.CRITmult) * (1 + self.DHmult) - 1
		self.CRIT_DHrate = self.CRITrate * self.DHrate
		pureCRITrate = self.CRITrate - self.CRIT_DHrate
		pureDHrate = self.DHrate - self.CRIT_DHrate 

		#Calculate adjusted multipliers
		self.f_CRIT = 1 + pureCRITrate * self.CRITmult
		self.f_DH = 1 + pureDHrate * self.DHmult
		self.f_CRIT_DH = 1 + self.CRIT_DHrate * self.CRIT_DHmult

		self.f_tot = self.f_CRIT * self.f_DH * self.f_CRIT_DH * self.f_DET * self.f_TEN

	def show(self):
		spacer = 20
		num2show = 5
		print('Stat results')
		print(' ')
		print(f"{'CRIT':<7}{'DET':<7}{'DH':<7}{'TEN':<7}")
		print(f"{self.CRIT:<7}{self.DET:<7}{self.DH:<7}{self.TEN:<7}")
		print(' ')
		print(f"{' ':<20}  {'Average multiplier':<20}  {'Hitrate (%)':<20}  {'Hit multiplier (%)':<20}")
		print(f"{'CRIT (pure):':>20}  {round(self.f_CRIT, num2show):<20}  {round(self.CRITrate*100, num2show):<20}  +{round(self.CRITmult*100, num2show):<20}")
		print(f"{'DET:':>20}  {round(self.f_DET, num2show):<20}  {' ':<20}  {' ':<20}")
		print(f"{'DH (pure):':>20}  {round(self.f_DH, num2show):<20}  {round(self.DHrate*100, num2show):<20}  +{round(self.DHmult*100, num2show):<20}")
		print(f"{'TEN:':>20}  {round(self.f_TEN, num2show):<20}  {' ':<20}  {' ':<20}")
		print(f"{'CRIT DH:':>20}  {round(self.f_CRIT_DH, num2show):<20}  {round(self.CRIT_DHrate*100, num2show):<20}  +{round(self.CRIT_DHmult*100, num2show):<20}")
		print("-"*83)
		print(f"{'Total avg mult:':>20}  {round(self.f_tot, 5):<20}")
		print(' ')

#Functions to read the data in the spreadsheet
def DHmod(DH):
	f_DH = StatData.loc[StatData["DH stat"] <= DH, "f(DH) avg"].max()
	hitrate = StatData.loc[StatData["DH stat"] <= DH, "DH rate"].max()
	multiplier = 0.25
	return f_DH, hitrate, multiplier
	
def CRITmod(CRIT):
	f_CRIT = StatData.loc[StatData["CRIT stat"] <= CRIT, "f(CRIT) avg"].max()
	hitrate = StatData.loc[StatData["CRIT stat"] <= CRIT, "CRIT rate"].max()
	multiplier = StatData.loc[StatData["CRIT stat"] <= CRIT, "CRIT dmg"].max()
	return f_CRIT, hitrate, multiplier

def DETmod(DET):
	f_DET = StatData.loc[StatData["DET stat"] <= DET, "f(DET)"].max()
	return f_DET

def TENmod(TEN):
	if TEN < 400:
		f_TEN = 1.0
	else: 
		f_TEN = StatData.loc[StatData["TEN stat"] <= TEN, "f(TEN)"].max()
	return f_TEN



DETBUILD = [2097, 1443, 436, 759]
CRITBUILD = [2097, 1119, 760, 759]
TESTBUILD = [2000, 1200, 2500,0] 

test = data(*TESTBUILD)
test.show()
