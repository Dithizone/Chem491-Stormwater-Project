# This will just be a quick TheFData2 = TheFData.replace('wrong things', 'right things')
# so I don't have to copy-paste a million times.
# And it worked, yay!

TheFData = open('TheFData.csv', 'r').read()
TheFData2ArrowheadFix = TheFData.replace('Arrowhead,(old) ', 'Arrowhead (old),')
TheFData2ubingFix = TheFData2ArrowheadFix.replace('ubing,Blank (distille ', 'Tubing Blank (distilled),')
TheFData2RinseFix = TheFData2ubingFix.replace('Rinse,2L (plastic) ', 'Rinse 2L (plastic),')
TheFData2yFix = TheFData2RinseFix.replace('y,Blank (HNO3||me ', 'Carboy Blank (HNO3||methanol),')
TheFData2CarboyBlankFix = TheFData2yFix.replace('Carboy Blank,(HNO3||methanol) ', 'Carboy Blank (HNO3||methanol),').replace('Carboy Blank,(HNO3||methanol)', 'Carboy Blank (HNO3||methanol),')
TheFData2RCFix = TheFData2CarboyBlankFix.replace('RC,pipe at MPK - ', 'Edison RC Pipe at MPK,').replace('RC,Pipe at MPK - ', 'Edison RC Pipe at MPK,').replace('Edison RC pipe at MP, ', 'Edison RC Pipe at MPK,')
TheFData2UltrapureWaterFix = TheFData2RCFix.replace('Blankwater-ultrapure', 'Ultrapure Water')  # This is called Ultrapure Water except in 2016/17

# with open('data/TheFDataComplete.csv', 'w') as file:
#     file.write(TheFData2UltrapureWaterFix)
