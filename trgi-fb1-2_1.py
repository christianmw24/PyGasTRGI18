from tkinter import *
import locale

locale.setlocale(locale.LC_ALL, 'de_DE')

# Tabellenwerte nach TRGI2018
# Druckverlust Gasstörmungswächter
gs0 = 0
gs25 = {10: 10, 12: 15, 14: 20, 15: 25, 17: 30, 18: 35, 19: 40, 20: 45, 21: 50}
gs4 = {17: 10, 20: 15, 23: 20, 25: 25, 27: 30, 29: 35, 31: 40, 33: 45, 34: 50}
gs6 = {25: 10, 30: 15, 34: 20, 38: 25, 41: 30, 44: 35, 47: 40, 50: 45, 51: 50}
gs10 = {43: 10, 50: 15, 57: 20, 63: 25, 69: 30, 74: 35, 79: 40, 83: 45, 86: 50}
gs16 = {68: 10, 81: 15, 92: 20, 102: 25, 110: 30, 119: 35, 126: 40, 134: 45, 138: 50}
# Druckverlust Gaszähler
gbz2 = {5: 30, 10: 35, 13: 40, 15: 45, 17: 50, 19: 55, 21: 60, 22: 65, 24: 70, 25: 75, 26: 80, 28: 85, 29: 90, 30: 95,
        31: 100, 32: 105, 33: 110, 34: 115}
gbz4 = {8: 30, 14: 35, 18: 40, 21: 45, 24: 50, 27: 55, 29: 60, 31: 65, 33: 70, 35: 75, 37: 80, 39: 85, 40: 90, 42: 95,
        43: 100, 45: 105, 46: 110, 48: 115, 49: 120, 50: 125, 51: 130}
gbz6 = {10: 30, 18: 35, 23: 40, 28: 45, 32: 50, 35: 55, 38: 60, 41: 65, 44: 70, 46: 75, 49: 80, 51: 85, 53: 90, 55: 95,
        57: 100, 59: 105, 61: 110, 63: 115, 65: 120, 67: 125, 68: 130}
gbz10 = {17: 30, 30: 35, 39: 40, 47: 45, 53: 50, 59: 55, 64: 60, 69: 65, 73: 70, 77: 75, 81: 80, 85: 85, 89: 90, 92: 95,
         96: 100, 99: 105, 102: 110, 105: 115, 108: 120, 111: 125, 114: 130}
gbz16 = {25: 30, 44: 35, 57: 40, 68: 45, 77: 50, 85: 55, 92: 60, 99: 65, 106: 70, 112: 75, 118: 80, 123: 85, 128: 90,
         134: 95, 138: 100, 143: 105, 148: 110, 152: 115, 156: 120, 161: 125, 165: 130}
gbz25 = {39: 30, 69: 35, 89: 40, 106: 45, 120: 50, 133: 55, 145: 60, 156: 65, 166: 70, 175: 75, 184: 80, 193: 85,
         201: 90, 209: 95, 217: 100}
gbz40 = {63: 30, 111: 35, 143: 40, 170: 45, 193: 50, 213: 55, 232: 60, 249: 65, 265: 70, 281: 75, 295: 80, 309: 85,
         322: 90, 335: 95, 347: 100}
gbz65 = {103: 30, 180: 35, 233: 40, 276: 45, 314: 50, 347: 55, 377: 60, 405: 65, 431: 70, 456: 75, 480: 80, 502: 85,
         523: 90, 544: 95, 564: 100}
# Druckverlust Anschlussarmaturen
gsdx = {3: 5, 4: 10, 5: 15, 6: 25, 7: 35, 8: 45, 9: 55, 10: 70, 11: 80, 12: 100, 13: 110}
eck15x = {7: 5, 9: 10, 11: 15, 12: 20, 14: 25, 15: 30, 16: 35, 17: 40, 18: 45, 19: 50, 20: 55, 21: 60, 22: 65, 23: 75,
          24: 80, 26: 90, 27: 100, 28: 110}
eck20x = {12: 5, 15: 10, 18: 15, 21: 20, 23: 25, 25: 30, 27: 35, 29: 40, 31: 45, 32: 50, 34: 55, 35: 60, 37: 65, 38: 70,
          39: 75, 41: 80, 44: 90, 46: 100, 48: 110}
eck25x = {20: 5, 26: 10, 31: 15, 36: 20, 40: 25, 43: 30, 46: 35, 49: 40, 52: 45, 55: 50, 57: 55, 60: 60, 62: 65, 64: 70,
          67: 75, 69: 80, 74: 90, 78: 100, 81: 110}
eck32x = {37: 5, 48: 10, 57: 15, 64: 20, 71: 25, 77: 30, 83: 35, 89: 40, 94: 45, 98: 50, 103: 55, 107: 60, 112: 65,
          116: 70, 120: 75, 124: 80, 133: 90, 139: 100, 146: 110}
eck40x = {58: 5, 75: 10, 89: 15, 100: 20, 111: 25, 121: 30, 130: 35, 138: 40, 146: 45, 154: 50, 161: 55, 168: 60,
          184: 65, 181: 70, 187: 75, 193: 80, 207: 90, 218: 100, 228: 110}
eck50x = {75: 5, 96: 10, 114: 15, 130: 20, 143: 25, 156: 30, 167: 35, 178: 40, 188: 45, 198: 50, 207: 55, 216: 60,
          225: 65, 233: 70, 241: 75, 248: 80, 267: 90, 280: 100, 293: 110}
durchg15x = {10: 5, 13: 10, 16: 15, 18: 20, 20: 25, 21: 30, 23: 35, 25: 40, 26: 45, 27: 50, 29: 55, 30: 60, 31: 65,
             32: 70, 33: 75, 34: 80, 35: 85, 36: 90}
durchg20x = {21: 5, 27: 10, 32: 15, 36: 20, 40: 25, 44: 30, 47: 35, 50: 40, 53: 45, 55: 50, 58: 55, 60: 60, 63: 65,
             65: 70, 67: 75, 69: 80, 71: 85, 73: 90}
durchg25x = {33: 5, 43: 10, 51: 15, 58: 20, 64: 25, 69: 30, 74: 35, 79: 40, 84: 45, 88: 50, 92: 55, 96: 60, 100: 65,
             103: 70, 107: 75, 110: 80, 114: 85, 117: 90}
durchg32x = {56: 5, 73: 10, 86: 15, 97: 20, 108: 25, 117: 30, 126: 35, 134: 40, 141: 45, 149: 50, 156: 55, 162: 60,
             169: 65, 175: 70, 181: 75, 186: 80, 192: 85, 197: 90}
durchg40x = {83: 5, 108: 10, 127: 15, 144: 20, 160: 25, 173: 30, 186: 35, 198: 40, 210: 45, 220: 50, 231: 55, 240: 60,
             250: 65, 259: 70, 268: 75, 276: 80, 285: 85, 293: 90}
durchg50x = {135: 5, 175: 10, 207: 15, 235: 20, 259: 25, 282: 30, 303: 35, 322: 40, 341: 45, 358: 50, 375: 55, 391: 60,
             406: 65, 421: 70, 435: 75, 449: 80, 463: 85, 476: 90}
# Druckverlust Kupferrohr
cu15 = {3: 1.6, 4: 2.0, 5: 2.5, 6: 3.5, 7: 5, 8: 6, 9: 7, 10: 9, 11: 10, 12: 12, 13: 14, 14: 16, 15: 18, 16: 20}
cu18 = {3: 0.8, 4: 1, 5: 1.2, 6: 1.4, 7: 1.8, 8: 2.5, 9: 3, 10: 3.5, 11: 4, 13: 5, 14: 6, 16: 7, 17: 8, 18: 9, 20: 10,
        22: 12, 24: 14, 26: 16, 28: 18, 29: 20}
cu22 = {4: 0.4, 6: 0.6, 8: 0.8, 9: 1, 10: 1.2, 11: 1.6, 12: 1.8, 13: 2, 15: 2.5, 17: 3, 18: 3.5, 20: 4, 23: 5, 26: 6,
        28: 7, 30: 8, 32: 9, 35: 10, 39: 12, 42: 14, 46: 16, 49: 18, 52: 20}
cu28 = {11: 0.4, 14: 0.6, 16: 0.8, 19: 1, 21: 1.2, 23: 1.4, 24: 1.6, 26: 1.8, 29: 2, 33: 2.5, 36: 3, 39: 3.5, 43: 4,
        49: 5, 54: 6, 59: 7, 64: 8, 68: 9, 74: 10, 81: 12, 88: 14, 95: 16, 101: 18, 107: 20}
cu35 = {20: 0.4, 26: 0.6, 31: 0.8, 35: 1, 39: 1.2, 42: 1.4, 46: 1.6, 49: 1.8, 53: 2, 61: 2.5, 67: 3, 73: 3.5, 80: 4,
        91: 5, 100: 6, 109: 7, 117: 8, 125: 9, 136: 10, 150: 12, 163: 14, 175: 16, 186: 18, 197: 20}
cu42 = {36: 0.4, 45: 0.6, 54: 0.8, 61: 1, 68: 1.2, 74: 1.4, 79: 1.6, 85: 1.8, 92: 2, 105: 2.5, 116: 3, 126: 3.5, 138: 4,
        157: 5, 173: 6, 188: 7, 200: 8, 215: 9, 230: 10, 255: 12, 275: 14, 300: 16, 315: 18, 335: 20}
cu54 = {75: 0.4, 96: 0.6, 113: 0.8, 129: 1, 142: 1.2, 154: 1.4, 166: 1.6, 177: 1.8, 193: 2, 215: 2.5, 240: 3, 260: 3.5,
        285: 4, 325: 5, 355: 6, 385: 7, 415: 8, 445: 9, 480: 10, 530: 12, 575: 14, 615: 16, 655: 18, 695: 20}
cu64 = {118: 0.4, 150: 0.6, 177: 0.8, 200: 1, 220: 1.2, 240: 1.4, 255: 1.6, 275: 1.8, 300: 2, 340: 2.5, 375: 3,
        405: 3.5, 445: 4, 505: 5, 555: 6, 600: 7, 645: 8, 690: 9, 750: 10, 820: 12, 890: 14, 955: 16, 1020: 18,
        1080: 20}
cu76 = {196: 0.4, 245: 0.6, 290: 0.8, 330: 1, 365: 1.2, 395: 1.4, 425: 1.6, 455: 1.8, 495: 2, 560: 2.5, 615: 3,
        670: 3.5, 730: 4, 830: 5, 915: 6, 990: 7, 1060: 8, 1130: 9, 1230: 10, 1350: 12, 1460: 14, 1570: 16, 1670: 18,
        1760: 20}
cu88 = {305: 0.4, 385: 0.6, 455: 0.8, 515: 1, 570: 1.2, 615: 1.4, 665: 1.6, 705: 1.8, 770: 2, 870: 2.5, 960: 3,
        1040: 3.5, 1140: 4, 1290: 5, 1420: 6, 1540: 7, 1650: 8, 1750: 9, 1900: 10, 2090: 12, 2270: 14, 2430: 16,
        2590: 18, 2740: 20}
# Druckverlust Stahlrohr
stm15 = {}
stm20 = {}
stm25 = {}
stm32 = {}
stm40 = {}
stm50 = {}
stm65 = {}
stm80 = {}
# Gerätetyp
gbf = 'Gasbrennwert'
kwh = 'Kombiwasserheizer'
uwh = 'Umlaufwasserheizer'
gh = 'Gasherd'
gr = 'Gasraumheizer'
# Gasarmatur
gsd = 'Gassteckdose'
eck15 = 'Eckform DN 15'
eck20 = 'Eckform DN 20'
eck25 = 'Eckform DN 25'
eck32 = 'Eckform DN 32'
eck40 = 'Eckform DN 40'
eck50 = 'Eckform DN 50'
durchg15 = 'Durchgang DN15'
durchg20 = 'Durchgang DN20'
durchg25 = 'Durchgang DN25'
durchg32 = 'Durchgang DN32'
durchg40 = 'Durchgang DN40'
durchg50 = 'Durchgang DN50'
# Gaszähler
g2 = 'G2,5'
g4 = 'G4'
g6 = 'G6'
g10 = 'G10'
g16 = 'G16'
g25 = 'G25'
g40 = 'G40'
g65 = 'G65'
# Funktionen
# vorauswahl cu vorauswahl dimension für berechnungslänge
# gesamtlcu berechnungslänge bei cu rohr nach vorauswahl
# hoehdp druckänderung durch höhe
# getdparm druckverlust armatur
# checkqnb prüfung nennwärmebelastung
testfuck = '.'


def vorauswahlcu(qnb):
    qnb = int(qnb)
    if qnb < 12:
        rohrtab = cu15
    elif 11 < qnb < 21:
        rohrtab = cu18
    elif 20 < qnb < 36:
        rohrtab = cu22
    elif 35 < qnb < 75:
        rohrtab = cu28
    elif 74 < qnb < 137:
        rohrtab = cu35
    elif 136 < qnb < 231:
        rohrtab = cu42
    elif 135 < qnb < 481:
        rohrtab = cu54
    elif 480 < qnb < 751:
        rohrtab = cu64
    elif 750 < qnb < 1231:
        rohrtab = cu76
    else:
        rohrtab = cu88
    return rohrtab


def gesamtlcu(rohrlaenge, boegen, rohrvorauswahl):
    laengelocal = locale.atof(rohrlaenge)
    laenge = float(laengelocal)
    boegen = int(boegen)
    rohrdn = rohrvorauswahl
    if rohrdn == cu15 or rohrdn == cu18 or rohrdn == cu22 or rohrdn == cu28:
        formteilzuschlagw = 0.3
        formteilzuschlagt = 0.7
    elif rohrdn == cu35:
        formteilzuschlagw = 0.5
        formteilzuschlagt = 1.0
    elif rohrdn == cu42:
        formteilzuschlagw = 0.7
        formteilzuschlagt = 1.5
    elif rohrdn == cu54:
        formteilzuschlagw = 1
        formteilzuschlagt = 2.0
    elif rohrdn == cu64:
        formteilzuschlagw = 1.2
        formteilzuschlagt = 2.5
    else:
        formteilzuschlagw = 1.5
        formteilzuschlagt = 3.0
    gesamtlaenge1 = laenge + boegen * formteilzuschlagw + formteilzuschlagt
    gesamtlaengef = float(gesamtlaenge1)
    gesamtlaenge = round(gesamtlaengef)
    textlaenge = 'Berechnungslänge (ink. T-St.): ' + str(gesamtlaenge) + ' m'
    return gesamtlaenge, textlaenge


def hoehedp(hoehe):
    try:
        type(int(hoehe))
        checkhoehe = hoehe
    except:
        hoehelocal = locale.atof(hoehe)
        hoehegerundet = round(hoehelocal)
        hoehechecked = int(hoehegerundet)
        checkhoehe = hoehechecked
    hoehe = int(checkhoehe)
    hoehedp = int(hoehe) * -4
    hoehetext = 'Druckdifferenz durch Höhenunterschied: ' + str(hoehedp) + ' Pa'
    return hoehedp, hoehetext


def getdparm(selectqnb, typearm):
    selectqnb = int(selectqnb)
    armdimension = True
    if typearm == gsd and selectqnb < 14:
        armtab = gsdx
    elif typearm == eck15 and selectqnb < 29:
        armtab = eck15x
    elif typearm == eck20 and selectqnb < 49:
        armtab = eck20x
    elif typearm == eck25 and selectqnb < 82:
        armtab = eck25x
    elif typearm == eck32 and selectqnb < 147:
        armtab = eck32x
    elif typearm == eck40 and selectqnb < 229:
        armtab = eck40x
    elif typearm == eck50 and selectqnb < 294:
        armtab = eck50x
    elif typearm == durchg15 and selectqnb < 37:
        armtab = durchg15x
    elif typearm == durchg20 and selectqnb < 74:
        armtab = durchg20x
    elif typearm == durchg25 and selectqnb < 118:
        armtab = durchg25x
    elif typearm == durchg32 and selectqnb < 197:
        armtab = durchg32x
    elif typearm == durchg40 and selectqnb < 294:
        armtab = durchg40x
    elif typearm == durchg50 and selectqnb < 477:
        armtab = durchg50x
    else:
        armdimension = False
        armtab = 0
    if armdimension:
        if selectqnb in armtab:
            armdp = armtab[selectqnb]
        else:
            while selectqnb not in armtab:
                selectqnb = selectqnb + 1
            armdp = armtab[selectqnb]
        armtext = 'Druckverlust Armatur: ' + str(armdp) + ' Pa'
        return armdp, armdimension, armtext
    else:
        armdp = 0
        armdimension = False
        armtext = 'Anschlussarmatur zu klein! '
        return armdp, armdimension, armtext


def checkqnb(qnb):
    try:
        type(int(qnb))
        qnbtext = 'Belastung: ' + qnb + ' kW'
        qnb = int(qnb)
    except:
        qnblocal = locale.atof(qnb)
        qnbgerundet = round(qnblocal)
        qnbchecked = int(qnbgerundet)
        qnbtext = 'Belastung: ' + str(qnbchecked) + ' kW (autom. gerundet)'
        qnb = qnbchecked
    if int(qnb) < 1:
        qnbtext = 'Fehler: Eingabe "Nennwärmebelastung" muss größer als 1 sein '
        qnb = 0
        qnbcheck = False
        return qnb, qnbtext, qnbcheck
    else:
        qnbcheck = True
        return qnb, qnbtext, qnbcheck


# check-button
def button_check():
    gtype1 = selectgeraet1.get()
    gtype2 = selectgeraet2.get()
    summaryL1 = Label(fenster, text='Gerät 1 ' + str(gtype1))
    summaryR1 = Label(fenster, text='Gerät 2 ' + str(gtype2))
    summaryL1.grid(row=30, column=0)
    summaryR1.grid(row=30, column=2)
    qnb1, qnbtext1, qnbcheck1 = checkqnb(usergeraet1qnb.get())
    qnb2, qnbtext2, qnbcheck2 = checkqnb(usergeraet2qnb.get())
    summaryL2 = Label(fenster, text=qnbtext1)
    summaryR2 = Label(fenster, text=qnbtext2)
    summaryL2.grid(row=31, column=0)
    summaryR2.grid(row=31, column=2)
    armatur1dp, armcheck1, armtext1 = getdparm(qnb1, selectgeraet1arm.get())
    armatur2dp, armcheck2, armtext2 = getdparm(qnb2, selectgeraet2arm.get())
    summaryL3 = Label(fenster, text=armtext1)
    summaryR3 = Label(fenster, text=armtext2)
    summaryL3.grid(row=32, column=0)
    summaryR3.grid(row=32, column=2)
    hoehedp1, hoehetext1 = hoehedp(usergeraet1h.get())
    hoehedp2, hoehetext2 = hoehedp(usergeraet2h.get())
    summaryL4 = Label(fenster, text=hoehetext1)
    summaryR4 = Label(fenster, text=hoehetext2)
    summaryL4.grid(row=33, column=0)
    summaryR4.grid(row=33, column=2)
    rohrvorauswahl1typ = selectgeraet1rt.get()
    rohrvorauswahl2typ = selectgeraet2rt.get()
    rohrvorauswahl1 = vorauswahlcu(qnb1)
    rohrvorauswahl2 = vorauswahlcu(qnb2)
    rohrlaenge1, rohrtext1 = gesamtlcu(usergeraet1rl.get(), usergeraet1bo.get(), rohrvorauswahl1)
    rohrlaenge2, rohrtext2 = gesamtlcu(usergeraet2rl.get(), usergeraet2bo.get(), rohrvorauswahl2)
    summaryL5 = Label(fenster, text=rohrtext1)
    summaryR5 = Label(fenster, text=rohrtext2)
    summaryL5.grid(row=34, column=0)
    summaryR5.grid(row=34, column=2)
    # weiter mit rohrtyp cu/stahl unterscheidung
#usergeraet1rtcu = Radiobutton(fenster, text='Kupferrohr', variable=selectgeraet1rt, value=1)
#usergeraet1rtsr = Radiobutton(fenster, text='Stahlrohr', variable=selectgeraet1rt, value=2)

# Fenster
# Fenstertitel
fenster = Tk()
fenster.title('TRGI-Dimensionierung')
trgi_name = Label(fenster, text='TRGI 2018 Formblatt 1.2 - zwei Gasgeräte')
trgi_name.grid(row=0, column=0)
# Gerätetyp
selectgeraet1 = StringVar(fenster)
selectgeraet1.set(gbf)
gasgeraet1type = Label(fenster, text='Gasgerät 1 - Typ: ')
gasgeraet1type.grid(row=2, column=0)
usergasgeraete1type = OptionMenu(fenster, selectgeraet1, gbf, kwh, uwh, gh, gr)
usergasgeraete1type.configure(width=20)
usergasgeraete1type.grid(row=2, column=1)
selectgeraet2 = StringVar(fenster)
selectgeraet2.set(gbf)
gasgeraet2type = Label(fenster, text='Gasgerät 2 - Typ: ')
gasgeraet2type.configure(width=20)
gasgeraet2type.grid(row=2, column=2)
usergasgeraete2type = OptionMenu(fenster, selectgeraet2, gbf, kwh, uwh, gh, gr)
usergasgeraete2type.grid(row=2, column=3)
# Nennwärmebelastung
lgeraet1qnb = Label(fenster, text='Nennwärmebelastung in kW: ')
lgeraet1qnb.grid(row=3, column=0)
usergeraet1qnb = Entry(fenster, bd=5, width=10)
usergeraet1qnb.insert(0, 1)
usergeraet1qnb.grid(row=3, column=1)
lgeraet2qnb = Label(fenster, text='Nennwärmebelastung in kW: ')
lgeraet2qnb.grid(row=3, column=2)
usergeraet2qnb = Entry(fenster, bd=5, width=10)
usergeraet2qnb.insert(0, 1)
usergeraet2qnb.grid(row=3, column=3)
# Anschlussarmatur
selectgeraet1arm = StringVar(fenster)
selectgeraet1arm.set(eck20)
lgeraet1arm = Label(fenster, text='Anschlussarmatur')
lgeraet1arm.grid(row=4, column=0)
usergeraet1arm = OptionMenu(fenster, selectgeraet1arm, gsd, eck15, durchg15, eck20, durchg20, eck25, durchg25, eck32,
                            durchg32, eck40, durchg40, eck50, durchg50)
usergeraet1arm.grid(row=4, column=1)
selectgeraet2arm = StringVar(fenster)
selectgeraet2arm.set(eck20)
lgeraet2arm = Label(fenster, text='Anschlussarmatur')
lgeraet2arm.grid(row=4, column=2)
usergeraet2arm = OptionMenu(fenster, selectgeraet2arm, gsd, eck15, durchg15, eck20, durchg20, eck25, durchg25, eck32,
                            durchg32, eck40, durchg40, eck50, durchg50)
usergeraet2arm.grid(row=4, column=3)
# Höhendifferenz
infohoehe = Label(fenster, text='Unterschied Druckregler zu Gasgerät, gerundet in m: ')
infohoehe.grid(row=5, column=0, columnspan=2)
infohoehe2 = Label(fenster, text='Wenn Gerät tiefer als DR ist die Höhendifferenz negativ "-" einzutragen. ')
infohoehe2.grid(row=5, column=2, columnspan=2)
lgerate1h = Label(fenster, text='Höhenunterschied in m ')
lgerate1h.grid(row=7, column=0)
usergeraet1h = Entry(fenster, bd=5, width=10)
usergeraet1h.insert(0, 0)
usergeraet1h.grid(row=7, column=1)
lgerate2h = Label(fenster, text='Höhenunterschied in m ')
lgerate2h.grid(row=7, column=2)
usergeraet2h = Entry(fenster, bd=5, width=10)
usergeraet2h.insert(0, 0)
usergeraet2h.grid(row=7, column=3)
# Rohrleitung Einzelanschlussleitung
lgeraetrt1 = Label(fenster, text='Rohrtyp ')
lgeraetrt1.grid(row=8, column=0)
lgeraetrt2 = Label(fenster, text='Rohrtyp ')
lgeraetrt2.grid(row=8, column=2)
selectgeraet1rt = IntVar()
selectgeraet1rt.set(1)
selectgeraet2rt = IntVar()
selectgeraet2rt.set(1)
usergeraet1rtcu = Radiobutton(fenster, text='Kupferrohr', variable=selectgeraet1rt, value=1)
usergeraet1rtsr = Radiobutton(fenster, text='Stahlrohr', variable=selectgeraet1rt, value=2)
usergeraet1rtcu.grid(row=8, column=1)
usergeraet1rtsr.grid(row=9, column=1)
usergeraet2rtcu = Radiobutton(fenster, text='Kupferrohr', variable=selectgeraet2rt, value=1)
usergeraet2rtsr = Radiobutton(fenster, text='Stahlrohr', variable=selectgeraet2rt, value=2)
usergeraet2rtcu.grid(row=8, column=3)
usergeraet2rtsr.grid(row=9, column=3)
lgeraet1rl = Label(fenster, text='Rohrlänge in m ab T-Stück: ')
lgeraet1rl.grid(row=10, column=0)
lgeraet2rl = Label(fenster, text='Rohrlänge in m ab T-Stück: ')
lgeraet2rl.grid(row=10, column=2)
usergeraet1rl = Entry(fenster, bd=5, width=10)
usergeraet1rl.grid(row=10, column=1)
usergeraet2rl = Entry(fenster, bd=5, width=10)
usergeraet2rl.grid(row=10, column=3)
lgeraet1bo = Label(fenster, text='Anzahl Winkel')
lgeraet1bo.grid(row=11, column=0)
lgeraet2bo = Label(fenster, text='Anzahl Winkel')
lgeraet2bo.grid(row=11, column=2)
usergeraet1bo = Entry(fenster, bd=5, width=10)
usergeraet1bo.grid(row=11, column=1)
usergeraet2bo = Entry(fenster, bd=5, width=10)
usergeraet2bo.grid(row=11, column=3)
# Trennlinie
lblank = Label(fenster,
               text='------------------------------------------------------------------------------------------------')
lblank.grid(row=14, column=0, columnspan=2)
lblank2 = Label(fenster,
                text='------------------------------------------------------------------------------------------------')
lblank2.grid(row=14, column=2, columnspan=2)
# Rohrleitung Verteilungsleitung
lvorgzrt = Label(fenster, text='Rohrtyp vor Gaszähler ')
lvorgzrt.grid(row=16, column=0)
lnachgzrt = Label(fenster, text='Rohrtyp nach Gaszähler bis T-St.: ')
lnachgzrt.grid(row=16, column=2)
selectvorgzrt = IntVar()
selectvorgzrt.set(2)
selectnachgzrt = IntVar()
selectnachgzrt.set(1)
uservorgzrtcu = Radiobutton(fenster, text='Kupferrohr', variable=selectvorgzrt, value=1)
uservorgzrtsr = Radiobutton(fenster, text='Stahlrohr', variable=selectvorgzrt, value=2)
uservorgzrtcu.grid(row=16, column=1)
uservorgzrtsr.grid(row=17, column=1)
usernachgzrtcu = Radiobutton(fenster, text='Kupferrohr', variable=selectnachgzrt, value=1)
usernachgzrtsr = Radiobutton(fenster, text='Stahlrohr', variable=selectnachgzrt, value=2)
usernachgzrtcu.grid(row=16, column=3)
usernachgzrtsr.grid(row=17, column=3)
lvorgzrl = Label(fenster, text='Rohrlänge vor Gaszähler: ')
lvorgzrl.grid(row=19, column=0)
lnachgzrl = Label(fenster, text='Rohrlänge nach Gaszähler bis T-St.: ')
lnachgzrl.grid(row=19, column=2)
uservorgzrl = Entry(fenster, bd=5, width=10)
uservorgzrl.grid(row=19, column=1)
usernachgzrl = Entry(fenster, bd=5, width=10)
usernachgzrl.grid(row=19, column=3)
lvorgzbo = Label(fenster, text='Anzahl Winkel vor Gaszähler: ')
lvorgzbo.grid(row=20, column=0)
lnachgzbo = Label(fenster, text='Anzahl Winkel nach Gaszähler bis T-St.: ')
lnachgzbo.grid(row=20, column=2)
uservorgzbo = Entry(fenster, bd=5, width=10)
uservorgzbo.grid(row=20, column=1)
usernachgzbo = Entry(fenster, bd=5, width=10)
usernachgzbo.grid(row=20, column=3)
# Typ Gaszähler
lgaszaehler = Label(fenster, text='Typ Gaszähler: ')
lgaszaehler.grid(row=22, column=0)
selectgz = StringVar(fenster)
selectgz.set(g6)
usergz = OptionMenu(fenster, selectgz, g2, g4, g6, g10, g16, g25, g40, g65)
usergz.configure(width=20)
usergz.grid(row=22, column=1)
# Position GS1
selectposgs = IntVar()
selectposgs.set(2)
lpositiongs = Label(fenster, text='Einbauort Gasströmungswachter: ')
lpositiongs.grid(row=22, column=2)
lpositiongsinfo = Label(fenster, text='(Vor DR: dP GS = 0 Pa) ')
lpositiongsinfo.grid(row=23, column=2)
userposgsvor = Radiobutton(fenster, text='Vor Druckregler', variable=selectposgs, value=1)
userposgsnach = Radiobutton(fenster, text='Nach Druckregler', variable=selectposgs, value=2)
userposgsnach.grid(row=22, column=3)
userposgsvor.grid(row=23, column=3)
# Trennlinie 2
lblank3 = Label(fenster,
                text='------------------------------------------------------------------------------------------------')
lblank3.grid(row=28, column=0, columnspan=2)
lblank4 = Label(fenster,
                text='------------------------------------------------------------------------------------------------')
lblank4.grid(row=28, column=2, columnspan=2)
# Checkbutton, Zusammenfassung
check_button = Button(fenster, text='Eingaben prüfen', command=button_check)
check_button.grid(row=29, column=1)

# Mainloop
mainloop()
