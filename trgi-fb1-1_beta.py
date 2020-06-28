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
          67: 75, 69: 80, 74:90, 78:100, 81: 110}
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
cu64 = {118: 0.4, 150: 0.6, 177: 0.8, 200: 1, 220: 1.2, 240: 1.4, 255: 1.6, 275: 1.8, 300: 2, 340: 2.5, 375: 3, 405: 3.5, 445: 4, 505: 5, 555: 6, 600: 7, 645: 8, 690: 9, 750: 10, 820: 12, 890: 14, 955: 16, 1020: 18, 1080: 20}
cu76 = {196: 0.4, 245: 0.6, 290: 0.8, 330: 1, 365: 1.2, 395: 1.4, 425: 1.6, 455: 1.8, 495: 2, 560: 2.5, 615: 3, 670: 3.5, 730: 4, 830: 5, 915: 6, 990: 7, 1060: 8, 1130: 9, 1230: 10, 1350: 12, 1460: 14, 1570: 16, 1670: 18, 1760: 20}
cu88 = {305: 0.4, 385: 0.6, 455: 0.8, 515: 1, 570: 1.2, 615: 1.4, 665: 1.6, 705: 1.8, 770: 2, 870: 2.5, 960: 3, 1040: 3.5, 1140: 4, 1290: 5, 1420: 6, 1540: 7, 1650: 8, 1750: 9, 1900: 10, 2090: 12, 2270: 14, 2430: 16, 2590: 18, 2740: 20}
# Druckverlust Stahlrohr
stm15 = {}
stm20 = {}
stm25 = {}
stm32 = {}
stm40 = {}
stm50 = {}
stm65 = {}
stm80 = {}
# def Funktionen, Reihenfolge:
# vorauswahl(DN nach Qnb),
# vorauswahlinfo(DN als str()),
# gesamtl (rohrlänge + formteilzuschläge in abhängigkeit über 28)
# rohrdpcalc (druckverlust der gasamtl),
# getgs (auswahl GS-Typ),
# getgsdp (Druckverlust GS nach Tabelle)
# checkposgs (textausgabe gs pos vor oder nach dr),
# checkqnb (Benutzereingabe wird ggf gerundet und als int gecasted)
# gsdpbefor (dP GS positionsabhängig, vor dr=0, nach dr= nach getgsdp)
# getdpgbz (dP Gaszähler nach Vorauswahl GBZ und qnb)
# getdparm (dP Anschlussarmatur nach User-Auswahl und gültigkeitscheck)
# checkhoeheuser (Höhenunterschied, ggf gerundet und als int gecasted)
# hoehedp (dP Höhe auf Grundlage checkhoeheuser)
# dpuserinput (bisher vom gewählte sachen, dp GS,GZ,Armatur,Höhe werden bis dahin berechnet)
# calcsmaller (versucht bei dp<300 Pa ob eine dim. kleiner möglich ist)
# calcbigger (wenn mit 10Pa/Vorauswahl dp>300 Pa, versuch eine dim. größer)
# button_check (nutzereingaben werden geprüft, vorauswahl GS, GZ, Armatur, dP bis dahin ausgegeben)
# button_calc (ckeck wird nochmal ausgeführt, anhand Rohrlänge und Bögen wird gesamt-dP ermittelt)


def vorauswahl(qnb):
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


def vorauswahlinfo(rohrdn):
    if rohrdn == cu15:
        dimensioninfo = 'Cu 15'
    elif rohrdn == cu18:
        dimensioninfo = 'Cu 18'
    elif rohrdn == cu22:
        dimensioninfo = 'Cu 22'
    elif rohrdn == cu28:
        dimensioninfo = 'Cu 28'
    elif rohrdn == cu35:
        dimensioninfo = 'Cu 35'
    elif rohrdn == cu42:
        dimensioninfo = 'Cu 42'
    elif rohrdn == cu54:
        dimensioninfo = 'Cu 54'
    elif rohrdn == cu64:
        dimensioninfo = 'Cu 64'
    elif rohrdn == cu76:
        dimensioninfo = 'Cu 76'
    elif rohrdn == cu88:
        dimensioninfo = 'Cu 88'
    else:
        dimensioninfo = 'Programmfehler in Funktion "vorauswahlinfo". '
    return dimensioninfo


def gesamtl(rohrlaenge, boegen, rohrvorauswahl):
    laengelocal = locale.atof(rohrlaenge)
    laenge = float(laengelocal)
    boegen = int(boegen)
    rohrdn = rohrvorauswahl
    if rohrdn == cu15 or rohrdn == cu18 or rohrdn == cu22 or rohrdn == cu28:
        formteilzuschlag = 0.3
    elif rohrdn == cu35:
        formteilzuschlag = 0.5
    elif rohrdn == cu42:
        formteilzuschlag = 0.7
    elif rohrdn == cu54:
        formteilzuschlag = 1
    elif rohrdn == cu64:
        formteilzuschlag = 1.2
    else:
        formteilzuschlag = 1.5
    gesamtlaenge1 = laenge + boegen * formteilzuschlag
    gesamtlaengef = float(gesamtlaenge1)
    gesamtlaenge = round(gesamtlaengef)
    return gesamtlaenge


def rohrdpcalc(dimension, gesamtlaenge, qnb):
    dimtab = dimension
    laengeges = float(gesamtlaenge)
    qnb = int(qnb)
    if qnb in dimtab:
        rohrpm = dimtab[qnb]
    else:
        while qnb not in dimtab:
            qnb = qnb + 1
        rohrpm = dimtab[qnb]
    rohrdp = laengeges * rohrpm
    return rohrdp


def getgs(qnb):
    selectqnb = int(qnb)
    if selectqnb <= 17:
        typgs = 'GS 2,5 K'
    elif 17 < selectqnb < 28:
        typgs = 'GS 4 K'
    elif 27 < selectqnb < 42:
        typgs = 'GS 6 K'
    elif 41 < selectqnb < 69:
        typgs = 'GS 10 K'
    elif 68 < selectqnb < 111:
        typgs = 'GS 16 K'
    else:
        typgs = 'Qnb > 110kW, kein GS erforderlich (Einzelgerät)'
    return typgs


def getgsdp(selectqnb):
    selectqnb = int(selectqnb)
    if selectqnb <= 17:
        gstab = gs25
    elif 17 < selectqnb < 28:
        gstab = gs4
    elif 27 < selectqnb < 42:
        gstab = gs6
    elif 41 < selectqnb < 69:
        gstab = gs10
    elif 68 < selectqnb < 111:
        gstab = gs16
    else:
        gstab = gs0
    if gstab == 0:
        gsdp = 0
    else:
        if selectqnb in gstab:
            gsdp = gstab[selectqnb]
        else:
            while selectqnb not in gstab:
                selectqnb = selectqnb + 1
            gsdp = gstab[selectqnb]
    return gsdp


def checkposgs(posgs):
    if posgs == 1:
        posgstxt = 'Einbau GS vor Druckregler, dP GS = 0'
    elif posgs == 2:
        posgstxt = 'Einbau GS nach Druckregler'
    else:
        posgstxt = 'Einbauort Druckregler nicht gewählt'
    return posgstxt


def checkqnb(qnb):
    try:
        type(int(qnb))
        qnbtext = 'Belastung: ' + qnb + ' kW'
        summaryqnb_label.config(text=qnbtext)
        qnbtrue = qnb
    except:
        qnblocal = locale.atof(qnb)
        qnbgerundet = round(qnblocal)
        qnbchecked = int(qnbgerundet)
        qnbtext = 'Belastung: ' + str(qnbchecked) + ' kW (autom. gerundet)'
        summaryqnb_label.config(text=qnbtext)
        qnbtrue = qnbchecked
    if int(qnbtrue) < 1:
        qnbtext = 'Fehler: Eingabe muss größer als 1 sein '
        summaryqnb_label.config(text=qnbtext)
        qnbtrue = 0
        return qnbtrue
    else:
        return qnbtrue


def gsdpbefor(posgs, deltags):
    posgs = int(posgs)
    deltags = int(deltags)
    if posgs == 1:
        deltags2 = 0
    else:
        deltags2 = deltags
    return deltags2


def getdpgbz(gbz, selectqnb):
    selectqnb = int(selectqnb)
    gbzdimension = True
    if gbz == 'G2,5' and selectqnb < 35:
        gbztab = gbz2
    elif gbz == 'G4' and selectqnb < 52:
        gbztab = gbz4
    elif gbz == 'G6' and selectqnb < 69:
        gbztab = gbz6
    elif gbz == 'G10' and selectqnb < 115:
        gbztab = gbz10
    elif gbz == 'G16' and selectqnb < 166:
        gbztab = gbz16
    elif gbz == 'G25' and selectqnb < 259:
        gbztab = gbz25
    elif gbz == 'G40' and selectqnb < 413:
        gbztab = gbz40
    elif gbz == 'G65' and selectqnb < 671:
        gbztab = gbz65
    else:
        gbzdimension = False
        gbztab = 0
    if gbzdimension:
        if selectqnb in gbztab:
            gbzdp = gbztab[selectqnb]
        else:
            while selectqnb not in gbztab:
                selectqnb = selectqnb + 1
            gbzdp = gbztab[selectqnb]
        return gbzdp
    else:
        gbzfalse = True
        return gbzfalse


def getdparm(typearm, selectqnb):
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
        return armdp
    else:
        armfalse = True
        return armfalse


def checkhoeheuser(hoehe):
    try:
        type(int(hoehe))
        checkhoehe = hoehe
    except:
        hoehelocal = locale.atof(hoehe)
        hoehegerundet = round(hoehelocal)
        hoehechecked = int(hoehegerundet)
        checkhoehe = hoehechecked
    return checkhoehe


def hoehedp(hoehe):
    try:
        type(int(hoehe))
        checkhoehe = True
    except:
        checkhoehe = False
    if checkhoehe:
        hoehe = int(hoehe) * -4
    else:
        hoehe = 0
    return hoehe


def dpuserinput(dpgs, dpgz, dparm, dph):
    dpgs = int(dpgs)
    dpgz = int(dpgz)
    dparm = int(dparm)
    dph = int(dph)
    summeuser = dpgs + dpgz + dparm + dph
    return summeuser


def calcsmaller(inputergebnis, qnb, rohrlaenge, boegen, rohrvorauswahl):
    dimsmnp = True
    if rohrvorauswahl == cu18 and qnb < 17:
        rohrvorauswahlsm = cu15
        dimsm = 'Cu 15'
    elif rohrvorauswahl == cu22 and qnb < 30:
        rohrvorauswahlsm = cu18
        dimsm = 'Cu 18'
    elif rohrvorauswahl == cu28 and qnb < 53:
        rohrvorauswahlsm = cu22
        dimsm = 'Cu 22'
    elif rohrvorauswahl == cu35 and qnb < 108:
        rohrvorauswahlsm = cu28
        dimsm = 'Cu 28'
    elif rohrvorauswahl == cu42 and qnb < 198:
        rohrvorauswahlsm = cu35
        dimsm = 'Cu 35'
    elif rohrvorauswahl == cu54 and qnb < 336:
        rohrvorauswahlsm = cu42
        dimsm = 'Cu 42'
    elif rohrvorauswahl == cu64 and qnb < 696:
        rohrvorauswahlsm = cu54
        dimsm = 'Cu 54'
    elif rohrvorauswahl == cu76 and qnb < 1081:
        rohrvorauswahlsm = cu64
        dimsm = 'Cu 64'
    elif rohrvorauswahl == cu88 and qnb < 1761:
        rohrvorauswahlsm = cu76
        dimsm = 'Cu 76'
    else:
        dimsmnp = False
    if not dimsmnp:
        dimsmout = 'Rohr mit geringerer DN nicht möglich'
        calcdpsmout = 0
    else:
        gesamtlaenge = gesamtl(rohrlaenge, boegen, rohrvorauswahlsm)
        rohrdpsm = rohrdpcalc(rohrvorauswahlsm, gesamtlaenge, qnb)
        rohrdpsmfl = float(rohrdpsm)
        calcdplongsm = float(inputergebnis) + float(rohrdpsmfl)
        calcdpsmout = round(calcdplongsm)
        dimsmout = dimsm
    return calcdpsmout, dimsmout


def calcbigger(inputergebnis, qnb, rohrlaenge, boegen, rohrvorauswahl):
    if rohrvorauswahl == cu15 and qnb < 30:
        rohrvorauswahlsm = cu18
        dimbg = 'Cu 18'
    elif rohrvorauswahl == cu18 and qnb < 53:
        rohrvorauswahlsm = cu22
        dimbg = 'Cu 22'
    elif rohrvorauswahl == cu22 and qnb < 108:
        rohrvorauswahlsm = cu28
        dimbg = 'Cu 28'
    elif rohrvorauswahl == cu28 and qnb < 198:
        rohrvorauswahl = cu35
        dimbg = 'Cu 35'
    elif rohrvorauswahl == cu35 and qnb < 336:
        rohrvorauswahl = cu42
        dimbg = 'Cu 42'
    elif rohrvorauswahl == cu42 and qnb < 696:
        rohrvorauswahl = cu54
        dimbg = 'Cu 54'
    elif rohrvorauswahl == cu54 and qnb < 1081:
        rohrvorauswahl = cu64
        dimbg = 'Cu 64'
    elif rohrvorauswahl == cu64 and qnb < 1761:
        rohrvorauswahl = cu76
        dimbg = 'Cu 76'
    elif rohrvorauswahl == cu76 and qnb < 2741:
        rohrvorauswahl = cu88
        dimbg = 'Cu 88'
    else:
        fuck = 300
        dimbg = 'nichtmöglich'
    gesamtlaenge = gesamtl(rohrlaenge, boegen, rohrvorauswahl)
    rohrdpbg = rohrdpcalc(rohrvorauswahl, gesamtlaenge, qnb)
    fuck = float(rohrdpbg)
    calcdplongbg = float(inputergebnis) + float(fuck)
    fuckout = round(calcdplongbg)
    dimbgout = dimbg
    return fuckout, dimbgout


def button_check():
    qnbunchecked = userqnb.get()
    qnbtrue = checkqnb(qnbunchecked)
    qnb = int(qnbtrue)
    if qnb > 1:
        posgstrue = selectposgs.get()
        posgs = checkposgs(posgstrue)
        summaryposgs_label.config(text=posgs)
        typegs = getgs(qnb)
        summarytypgs_label.config(text='Typ Gasströmungswächter: ' + typegs)
        dpgs = getgsdp(qnb)
        dpgscalc = gsdpbefor(posgstrue, dpgs)
        summarydpgs_label.config(text='Druckverlust GS: ' + str(dpgscalc) + ' Pa')
        typegbz = selectgbz.get()
        summarygbz_label.config(text='Gaszähler: ' + typegbz)
        dpgbzcalc = getdpgbz(typegbz, qnb)
        summarydpgbz_label.config(text='Druckverlust GZ: ' + str(dpgbzcalc) + ' Pa')
        typearmatur = selectarmatur.get()
        summaryarmatur_label.config(text='Anschlussarmatur: ' + str(typearmatur))
        dparmatur = getdparm(typearmatur, qnb)
        summaryarmaturdp_label.config(text='Druckverlust Armatur: ' + str(dparmatur) + ' Pa')
        hoeheuser = userhoehe.get()
        hoehechecked = checkhoeheuser(hoeheuser)
        hoehe = int(hoehechecked)
        summaryhoehe_label.config(text='Höhenunterschied in m: ' + str(hoehe))
        dphoehe = hoehedp(hoehe)
        summaryhoehedp_label.config(text='Delta P durch Höhe: ' + str(dphoehe) + ' Pa')
        dpuserinputsum = dpuserinput(dpgscalc, dpgbzcalc, dparmatur, dphoehe)
        summarydpinput_label.config(text='Druckverlust durch GS, GZ, Armatur, Höhe: ' + str(dpuserinputsum) + ' Pa')
        if dpgbzcalc == True:
            gzerror = 'Fehler: Gaszähler zu klein '
        else:
            gzerror = ''
        if dparmatur == True:
            armerror = ' Fehler: Anschlussarmatur zu klein'
        else:
            armerror = ''
        userinputerror_label.config(text=gzerror + armerror)
    else:
        dpuserinputsum = 0
        qnb = 0
    return dpuserinputsum, qnb


def button_calc():
    inputergebnis, qnb = button_check()
    rohrlaenge = userlaenge.get()
    boegen = userboegen.get()
    rohrvorauswahl = vorauswahl(qnb)
    rohrvorinfo = vorauswahlinfo(rohrvorauswahl)
    gesamtlaenge = gesamtl(rohrlaenge, boegen, rohrvorauswahl)
    rohrdp = rohrdpcalc(rohrvorauswahl, gesamtlaenge, qnb)
    calcdplong = float(rohrdp) + float(inputergebnis)
    calcdp = round(calcdplong)
    rechenlaenge_label.config(text='Gesamtlänge: ' + str(gesamtlaenge) + ' m')
    rohrinfo_label.config(text='Dimension nach 10Pa/m Vorauswahl: ' + str(rohrvorinfo))
    gesamtdp_label.config(text='Gesamtdruckverlust: ' + str(calcdp) + ' Pa')
    if calcdp < 300:
        ergebnisdp1_label.config(text='Druckverlust kleiner 300 Pa, Berechnung OK')
        dpgessmall, dimsmout = calcsmaller(inputergebnis, qnb, rohrlaenge, boegen, rohrvorauswahl)
        dimensiondiff1_label.config(text='Nächstkleineres Rohr: ' + str(dimsmout))
        dimensiondiff2_label.config(text='Druckverlust: ' + str(dpgessmall))
        if 1 < int(dpgessmall) < 300:
            textdiff3 = 'Geänderte Dimensionierung möglich'
        else:
            textdiff3 = 'kleinere Dimensionierung nicht möglich'
        dimensiondiff3_label.config(text=textdiff3)
    else:
        ergebnisdp1_label.config(text='Druckverlust größer 300 Pa, Dimensionierung nicht OK')
        dpgesbig, dimsmoutbg = calcbigger(inputergebnis, qnb, rohrlaenge, boegen, rohrvorauswahl)
        dimensiondiff1_label.config(text='Nächstgrößeres Rohr: ' + str(dimsmoutbg))
        dimensiondiff2_label.config(text='Druckverlust: ' + str(dpgesbig))
        textdiff3 = 'Dimensionierung möglich'
        dimensiondiff3_label.config(text=textdiff3)


fenster = Tk()  # Fenstertitel
fenster.title('TRGI')
trgi_name = Label(fenster, text='TRGI 2018 Formblatt 1.1 - Einzelgerät')

trgi_qnb = Label(fenster, text='Nennwärmebelastung gerundet in kW:')  # Nennwärmebelastung
userqnb = Entry(fenster, bd=5, width=10)

selectposgs = IntVar()  # Einbau GS
trgi_posgs = Label(fenster, text='Einbauort Gasströmungswächter:')
userposgs1 = Radiobutton(fenster, text='Vor Druckregler', variable=selectposgs, value=1)
userposgs2 = Radiobutton(fenster, text='Nach Druckregler', variable=selectposgs, value=2)

g2 = 'G2,5'  # Gaszähler
g4 = 'G4'
g6 = 'G6'
g10 = 'G10'
g16 = 'G16'
g25 = 'G25'
g40 = 'G40'
g65 = 'G65'
selectgbz = StringVar(fenster)
selectgbz.set(g4)
trgi_gbz = Label(fenster, text='Vorauswahl Gaszähler')
usergbz = OptionMenu(fenster, selectgbz, g2, g4, g6, g10, g16, g25, g40, g65)
usergbz.configure(width=20)

gsd = 'Gassteckdose'  # Gasarmatur
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
selectarmatur = StringVar(fenster)
selectarmatur.set(eck20)
trgi_armatur = Label(fenster, text='Vorauswahl Geräteanschlussarmatur (mit TAE) ')
userarmatur = OptionMenu(fenster, selectarmatur, gsd, eck15, durchg15, eck20, durchg20, eck25, durchg25, eck32,
                         durchg32, eck40, durchg40, eck50, durchg50)
userarmatur.configure(width=20)

trgi_hoehe = Label(fenster, text='Höhenunterschied Druckregler zu Gasgerät, gerundet in m:')  # Höhenunterschied
userhoehe = Entry(fenster, bd=5, width=10)
userhoehe.insert(END, 0)
trgi_hoehe2 = Label(fenster, text='(Wenn Gerät tiefer als DR ist die Höhendifferenz negativ "-" einzutragen)')

# Zusammenfassung Input
summaryqnb_label = Label(fenster)
summaryposgs_label = Label(fenster)
summarytypgs_label = Label(fenster)
summarydpgs_label = Label(fenster)
summarygbz_label = Label(fenster)
summarydpgbz_label = Label(fenster)
summaryarmatur_label = Label(fenster)
summaryarmaturdp_label = Label(fenster)
summaryhoehe_label = Label(fenster)
hoheinputerror_label = Label(fenster)
summaryhoehedp_label = Label(fenster)
summarydpinput_label = Label(fenster)
userinputerror_label = Label(fenster)

check_button = Button(fenster, text="Eingaben prüfen", command=button_check)  # Button check

trgi_rohrlaenge = Label(fenster, text='Rohrlänge in m: ')  # Länge und Bögen
userlaenge = Entry(fenster, bd=5, width=10)
trgi_boegen = Label(fenster, text='Anzahl Bögen :')
userboegen = Entry(fenster, bd=5, width=10)

calc_button = Button(fenster, text='Berechnung starten', command=button_calc)  # Button Berechnung

rechenlaenge_label = Label(fenster)  # Ergebnis Berechnung
rohrinfo_label = Label(fenster)
gesamtdp_label = Label(fenster)
ergebnisdp1_label = Label(fenster)
dimensiondiff1_label = Label(fenster)
dimensiondiff2_label = Label(fenster)
dimensiondiff3_label = Label(fenster)

exit_button = Button(fenster, text="Beenden", command=fenster.quit)  # Ende

trgi_name.grid(row=0, column=0)  # Fensteranordnung
trgi_qnb.grid(row=1, column=0)
userqnb.grid(row=1, column=1)
trgi_posgs.grid(row=2, column=0)
userposgs1.grid(row=2, column=1)
userposgs2.grid(row=3, column=1)
trgi_gbz.grid(row=4, column=0)
usergbz.grid(row=4, column=1)
trgi_armatur.grid(row=5, column=0)
userarmatur.grid(row=5, column=1)
trgi_hoehe.grid(row=6, column=0)
userhoehe.grid(row=6, column=1)
trgi_hoehe2.grid(row=7, column=0)

summaryqnb_label.grid(row=11, column=0)
summaryposgs_label.grid(row=12, column=0)
summarytypgs_label.grid(row=13, column=0)
summarydpgs_label.grid(row=13, column=1)
summarygbz_label.grid(row=14, column=0)
summarydpgbz_label.grid(row=14, column=1)
summaryarmatur_label.grid(row=15, column=0)
summaryarmaturdp_label.grid(row=15, column=1)
summaryhoehe_label.grid(row=16, column=0)
summaryhoehedp_label.grid(row=16, column=1)
summarydpinput_label.grid(row=17, column=0)
userinputerror_label.grid(row=18, column=0)
check_button.grid(row=20, column=0)

trgi_rohrlaenge.grid(row=22, column=0)
userlaenge.grid(row=22, column=1)
trgi_boegen.grid(row=23, column=0)
userboegen.grid(row=23, column=1)

calc_button.grid(row=24, column=0)

rechenlaenge_label.grid(row=25, column=0)
rohrinfo_label.grid(row=26, column=0)
gesamtdp_label.grid(row=27, column=0)
ergebnisdp1_label.grid(row=28, column=0)
dimensiondiff1_label.grid(row=30, column=0)
dimensiondiff2_label.grid(row=31, column=0)
dimensiondiff3_label.grid(row=32, column=0)
exit_button.grid(row=40, column=1)

mainloop()
