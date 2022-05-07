import re, sys, os
import json

def reader2010():
    name_mpg_a = dict();
    name_fg_a = dict();
    name_thfg_a = dict();
    name_twfg_a = dict();
    name_ft_a = dict();
    name_rpg_a = dict();
    name_apg_a = dict();
    name_spg_a = dict();
    name_bpg_a = dict();
    name_tpg_a = dict();
    name_ppg_a = dict();
    with open("2010-2011.txt") as a:
        for line in a:
            regexer2010(line,name_mpg_a,name_fg_a,name_thfg_a,name_twfg_a,name_ft_a,name_rpg_a,name_apg_a,name_spg_a,name_bpg_a,name_tpg_a,name_ppg_a) 
    outputter2010(name_mpg_a,name_fg_a,name_thfg_a,name_twfg_a,name_ft_a,name_rpg_a,name_apg_a,name_spg_a,name_bpg_a,name_tpg_a,name_ppg_a)  

def regexer2010(line,name_mpg_a,name_fg_a,name_thfg_a,name_twfg_a,name_ft_a,name_rpg_a,name_apg_a,name_spg_a,name_bpg_a,name_tpg_a,name_ppg_a):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2010(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_a,name_fg_a,name_thfg_a,name_twfg_a,name_ft_a,name_rpg_a,name_apg_a,name_spg_a,name_bpg_a,name_tpg_a,name_ppg_a)

def writer2010(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_a,name_fg_a,name_thfg_a,name_twfg_a,name_ft_a,name_rpg_a,name_apg_a,name_spg_a,name_bpg_a,name_tpg_a,name_ppg_a):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_a[name] = mpg
        name_fg_a[name] = fg
        name_thfg_a[name] = thfg
        name_twfg_a[name] = twfg
        name_ft_a[name] = ft
        name_rpg_a[name] = rpg
        name_apg_a[name] = apg
        name_spg_a[name] = spg
        name_bpg_a[name] = bpg
        name_tpg_a[name] = tpg
        name_ppg_a[name] = ppg

def outputter2010(name_mpg_a,name_fg_a,name_thfg_a,name_twfg_a,name_ft_a,name_rpg_a,name_apg_a,name_spg_a,name_bpg_a,name_tpg_a,name_ppg_a):        
    with open("2010-2011_mpg.json", "w") as outfile:
        json.dump(name_mpg_a, outfile)
    with open("2010-2011_fg.json", "w") as outfile:    
        json.dump(name_fg_a, outfile)
    with open("2010-2011_thfg.json", "w") as outfile:
        json.dump(name_thfg_a, outfile)
    with open("2010-2011_twfg.json", "w") as outfile:
        json.dump(name_twfg_a, outfile)
    with open("2010-2011_ft.json", "w") as outfile:
        json.dump(name_ft_a, outfile)
    with open("2010-2011_rpg.json", "w") as outfile:
        json.dump(name_rpg_a, outfile)
    with open("2010-2011_apg.json", "w") as outfile:
        json.dump(name_apg_a, outfile)
    with open("2010-2011_spg.json", "w") as outfile:
        json.dump(name_spg_a, outfile)
    with open("2010-2011_bpg.json", "w") as outfile:
        json.dump(name_bpg_a, outfile)
    with open("2010-2011_tpg.json", "w") as outfile:
        json.dump(name_tpg_a, outfile)
    with open("2010-2011_ppg.json", "w") as outfile:
        json.dump(name_ppg_a, outfile)


############################################################################################### ^2010-2011



def reader2011():
    name_mpg_b = dict();
    name_fg_b = dict();
    name_thfg_b = dict();
    name_twfg_b = dict();
    name_ft_b = dict();
    name_rpg_b = dict();
    name_apg_b = dict();
    name_spg_b = dict();
    name_bpg_b = dict();
    name_tpg_b = dict();
    name_ppg_b = dict();
    with open("2011-2012.txt") as b:
        for line in b:
            regexer2011(line,name_mpg_b,name_fg_b,name_thfg_b,name_twfg_b,name_ft_b,name_rpg_b,name_apg_b,name_spg_b,name_bpg_b,name_tpg_b,name_ppg_b) 
    outputter2011(name_mpg_b,name_fg_b,name_thfg_b,name_twfg_b,name_ft_b,name_rpg_b,name_apg_b,name_spg_b,name_bpg_b,name_tpg_b,name_ppg_b)  

def regexer2011(line,name_mpg_b,name_fg_b,name_thfg_b,name_twfg_b,name_ft_b,name_rpg_b,name_apg_b,name_spg_b,name_bpg_b,name_tpg_b,name_ppg_b):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2011(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_b,name_fg_b,name_thfg_b,name_twfg_b,name_ft_b,name_rpg_b,name_apg_b,name_spg_b,name_bpg_b,name_tpg_b,name_ppg_b)

def writer2011(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_b,name_fg_b,name_thfg_b,name_twfg_b,name_ft_b,name_rpg_b,name_apg_b,name_spg_b,name_bpg_b,name_tpg_b,name_ppg_b):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_b[name] = mpg
        name_fg_b[name] = fg
        name_thfg_b[name] = thfg
        name_twfg_b[name] = twfg
        name_ft_b[name] = ft
        name_rpg_b[name] = rpg
        name_apg_b[name] = apg
        name_spg_b[name] = spg
        name_bpg_b[name] = bpg
        name_tpg_b[name] = tpg
        name_ppg_b[name] = ppg

def outputter2011(name_mpg_b,name_fg_b,name_thfg_b,name_twfg_b,name_ft_b,name_rpg_b,name_apg_b,name_spg_b,name_bpg_b,name_tpg_b,name_ppg_b):        
    with open("2011-2012_mpg.json", "w") as outfile:
        json.dump(name_mpg_b, outfile)
    with open("2011-2012_fg.json", "w") as outfile:    
        json.dump(name_fg_b, outfile)
    with open("2011-2012_thfg.json", "w") as outfile:
        json.dump(name_thfg_b, outfile)
    with open("2011-2012_twfg.json", "w") as outfile:
        json.dump(name_twfg_b, outfile)
    with open("2011-2012_ft.json", "w") as outfile:
        json.dump(name_ft_b, outfile)
    with open("2011-2012_rpg.json", "w") as outfile:
        json.dump(name_rpg_b, outfile)
    with open("2011-2012_apg.json", "w") as outfile:
        json.dump(name_apg_b, outfile)
    with open("2011-2012_spg.json", "w") as outfile:
        json.dump(name_spg_b, outfile)
    with open("2011-2012_bpg.json", "w") as outfile:
        json.dump(name_bpg_b, outfile)
    with open("2011-2012_tpg.json", "w") as outfile:
        json.dump(name_tpg_b, outfile)
    with open("2011-2012_ppg.json", "w") as outfile:
        json.dump(name_ppg_b, outfile)



############################################################################################### ^2011-2012



def reader2012():
    name_mpg_c = dict();
    name_fg_c = dict();
    name_thfg_c = dict();
    name_twfg_c = dict();
    name_ft_c = dict();
    name_rpg_c = dict();
    name_apg_c = dict();
    name_spg_c = dict();
    name_bpg_c = dict();
    name_tpg_c = dict();
    name_ppg_c = dict();
    with open("2012-2013.txt") as c:
        for line in c:
            regexer2012(line,name_mpg_c,name_fg_c,name_thfg_c,name_twfg_c,name_ft_c,name_rpg_c,name_apg_c,name_spg_c,name_bpg_c,name_tpg_c,name_ppg_c) 
    outputter2012(name_mpg_c,name_fg_c,name_thfg_c,name_twfg_c,name_ft_c,name_rpg_c,name_apg_c,name_spg_c,name_bpg_c,name_tpg_c,name_ppg_c)  

def regexer2012(line,name_mpg_c,name_fg_c,name_thfg_c,name_twfg_c,name_ft_c,name_rpg_c,name_apg_c,name_spg_c,name_bpg_c,name_tpg_c,name_ppg_c):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2012(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_c,name_fg_c,name_thfg_c,name_twfg_c,name_ft_c,name_rpg_c,name_apg_c,name_spg_c,name_bpg_c,name_tpg_c,name_ppg_c)

def writer2012(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_c,name_fg_c,name_thfg_c,name_twfg_c,name_ft_c,name_rpg_c,name_apg_c,name_spg_c,name_bpg_c,name_tpg_c,name_ppg_c):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_c[name] = mpg
        name_fg_c[name] = fg
        name_thfg_c[name] = thfg
        name_twfg_c[name] = twfg
        name_ft_c[name] = ft
        name_rpg_c[name] = rpg
        name_apg_c[name] = apg
        name_spg_c[name] = spg
        name_bpg_c[name] = bpg
        name_tpg_c[name] = tpg
        name_ppg_c[name] = ppg

def outputter2012(name_mpg_c,name_fg_c,name_thfg_c,name_twfg_c,name_ft_c,name_rpg_c,name_apg_c,name_spg_c,name_bpg_c,name_tpg_c,name_ppg_c):        
    with open("2012-2013_mpg.json", "w") as outfile:
        json.dump(name_mpg_c, outfile)
    with open("2012-2013_fg.json", "w") as outfile:    
        json.dump(name_fg_c, outfile)
    with open("2012-2013_thfg.json", "w") as outfile:
        json.dump(name_thfg_c, outfile)
    with open("2012-2013_twfg.json", "w") as outfile:
        json.dump(name_twfg_c, outfile)
    with open("2012-2013_ft.json", "w") as outfile:
        json.dump(name_ft_c, outfile)
    with open("2012-2013_rpg.json", "w") as outfile:
        json.dump(name_rpg_c, outfile)
    with open("2012-2013_apg.json", "w") as outfile:
        json.dump(name_apg_c, outfile)
    with open("2012-2013_spg.json", "w") as outfile:
        json.dump(name_spg_c, outfile)
    with open("2012-2013_bpg.json", "w") as outfile:
        json.dump(name_bpg_c, outfile)
    with open("2012-2013_tpg.json", "w") as outfile:
        json.dump(name_tpg_c, outfile)
    with open("2012-2013_ppg.json", "w") as outfile:
        json.dump(name_ppg_c, outfile)



############################################################################################### ^2012-2013



def reader2013():
    name_mpg_d = dict();
    name_fg_d = dict();
    name_thfg_d = dict();
    name_twfg_d = dict();
    name_ft_d = dict();
    name_rpg_d = dict();
    name_apg_d = dict();
    name_spg_d = dict();
    name_bpg_d = dict();
    name_tpg_d = dict();
    name_ppg_d = dict();
    with open("2013-2014.txt") as d:
        for line in d:
            regexer2013(line,name_mpg_d,name_fg_d,name_thfg_d,name_twfg_d,name_ft_d,name_rpg_d,name_apg_d,name_spg_d,name_bpg_d,name_tpg_d,name_ppg_d) 
    outputter2013(name_mpg_d,name_fg_d,name_thfg_d,name_twfg_d,name_ft_d,name_rpg_d,name_apg_d,name_spg_d,name_bpg_d,name_tpg_d,name_ppg_d)  

def regexer2013(line,name_mpg_d,name_fg_d,name_thfg_d,name_twfg_d,name_ft_d,name_rpg_d,name_apg_d,name_spg_d,name_bpg_d,name_tpg_d,name_ppg_d):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2013(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_d,name_fg_d,name_thfg_d,name_twfg_d,name_ft_d,name_rpg_d,name_apg_d,name_spg_d,name_bpg_d,name_tpg_d,name_ppg_d)

def writer2013(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_d,name_fg_d,name_thfg_d,name_twfg_d,name_ft_d,name_rpg_d,name_apg_d,name_spg_d,name_bpg_d,name_tpg_d,name_ppg_d):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_d[name] = mpg
        name_fg_d[name] = fg
        name_thfg_d[name] = thfg
        name_twfg_d[name] = twfg
        name_ft_d[name] = ft
        name_rpg_d[name] = rpg
        name_apg_d[name] = apg
        name_spg_d[name] = spg
        name_bpg_d[name] = bpg
        name_tpg_d[name] = tpg
        name_ppg_d[name] = ppg

def outputter2013(name_mpg_d,name_fg_d,name_thfg_d,name_twfg_d,name_ft_d,name_rpg_d,name_apg_d,name_spg_d,name_bpg_d,name_tpg_d,name_ppg_d):        
    with open("2013-2014_mpg.json", "w") as outfile:
        json.dump(name_mpg_d, outfile)
    with open("2013-2014_fg.json", "w") as outfile:    
        json.dump(name_fg_d, outfile)
    with open("2013-2014_thfg.json", "w") as outfile:
        json.dump(name_thfg_d, outfile)
    with open("2013-2014_twfg.json", "w") as outfile:
        json.dump(name_twfg_d, outfile)
    with open("2013-2014_ft.json", "w") as outfile:
        json.dump(name_ft_d, outfile)
    with open("2013-2014_rpg.json", "w") as outfile:
        json.dump(name_rpg_d, outfile)
    with open("2013-2014_apg.json", "w") as outfile:
        json.dump(name_apg_d, outfile)
    with open("2013-2014_spg.json", "w") as outfile:
        json.dump(name_spg_d, outfile)
    with open("2013-2014_bpg.json", "w") as outfile:
        json.dump(name_bpg_d, outfile)
    with open("2013-2014_tpg.json", "w") as outfile:
        json.dump(name_tpg_d, outfile)
    with open("2013-2014_ppg.json", "w") as outfile:
        json.dump(name_ppg_d, outfile)



############################################################################################### ^2013-2014



def reader2014():
    name_mpg_e = dict();
    name_fg_e = dict();
    name_thfg_e = dict();
    name_twfg_e = dict();
    name_ft_e = dict();
    name_rpg_e = dict();
    name_apg_e = dict();
    name_spg_e = dict();
    name_bpg_e = dict();
    name_tpg_e = dict();
    name_ppg_e = dict();
    with open("2014-2015.txt") as d:
        for line in d:
            regexer2014(line,name_mpg_e,name_fg_e,name_thfg_e,name_twfg_e,name_ft_e,name_rpg_e,name_apg_e,name_spg_e,name_bpg_e,name_tpg_e,name_ppg_e) 
    outputter2014(name_mpg_e,name_fg_e,name_thfg_e,name_twfg_e,name_ft_e,name_rpg_e,name_apg_e,name_spg_e,name_bpg_e,name_tpg_e,name_ppg_e)  

def regexer2014(line,name_mpg_e,name_fg_e,name_thfg_e,name_twfg_e,name_ft_e,name_rpg_e,name_apg_e,name_spg_e,name_bpg_e,name_tpg_e,name_ppg_e):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2014(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_e,name_fg_e,name_thfg_e,name_twfg_e,name_ft_e,name_rpg_e,name_apg_e,name_spg_e,name_bpg_e,name_tpg_e,name_ppg_e)

def writer2014(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_e,name_fg_e,name_thfg_e,name_twfg_e,name_ft_e,name_rpg_e,name_apg_e,name_spg_e,name_bpg_e,name_tpg_e,name_ppg_e):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_e[name] = mpg
        name_fg_e[name] = fg
        name_thfg_e[name] = thfg
        name_twfg_e[name] = twfg
        name_ft_e[name] = ft
        name_rpg_e[name] = rpg
        name_apg_e[name] = apg
        name_spg_e[name] = spg
        name_bpg_e[name] = bpg
        name_tpg_e[name] = tpg
        name_ppg_e[name] = ppg

def outputter2014(name_mpg_e,name_fg_e,name_thfg_e,name_twfg_e,name_ft_e,name_rpg_e,name_apg_e,name_spg_e,name_bpg_e,name_tpg_e,name_ppg_e):        
    with open("2014-2015_mpg.json", "w") as outfile:
        json.dump(name_mpg_e, outfile)
    with open("2014-2015_fg.json", "w") as outfile:    
        json.dump(name_fg_e, outfile)
    with open("2014-2015_thfg.json", "w") as outfile:
        json.dump(name_thfg_e, outfile)
    with open("2014-2015_twfg.json", "w") as outfile:
        json.dump(name_twfg_e, outfile)
    with open("2014-2015_ft.json", "w") as outfile:
        json.dump(name_ft_e, outfile)
    with open("2014-2015_rpg.json", "w") as outfile:
        json.dump(name_rpg_e, outfile)
    with open("2014-2015_apg.json", "w") as outfile:
        json.dump(name_apg_e, outfile)
    with open("2014-2015_spg.json", "w") as outfile:
        json.dump(name_spg_e, outfile)
    with open("2014-2015_bpg.json", "w") as outfile:
        json.dump(name_bpg_e, outfile)
    with open("2014-2015_tpg.json", "w") as outfile:
        json.dump(name_tpg_e, outfile)
    with open("2014-2015_ppg.json", "w") as outfile:
        json.dump(name_ppg_e, outfile)



############################################################################################### ^2014-2015



def reader2015():
    name_mpg_f = dict();
    name_fg_f = dict();
    name_thfg_f = dict();
    name_twfg_f = dict();
    name_ft_f = dict();
    name_rpg_f = dict();
    name_apg_f = dict();
    name_spg_f = dict();
    name_bpg_f = dict();
    name_tpg_f = dict();
    name_ppg_f = dict();
    with open("2015-2016.txt") as d:
        for line in d:
            regexer2015(line,name_mpg_f,name_fg_f,name_thfg_f,name_twfg_f,name_ft_f,name_rpg_f,name_apg_f,name_spg_f,name_bpg_f,name_tpg_f,name_ppg_f) 
    outputter2015(name_mpg_f,name_fg_f,name_thfg_f,name_twfg_f,name_ft_f,name_rpg_f,name_apg_f,name_spg_f,name_bpg_f,name_tpg_f,name_ppg_f)  

def regexer2015(line,name_mpg_f,name_fg_f,name_thfg_f,name_twfg_f,name_ft_f,name_rpg_f,name_apg_f,name_spg_f,name_bpg_f,name_tpg_f,name_ppg_f):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2015(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_f,name_fg_f,name_thfg_f,name_twfg_f,name_ft_f,name_rpg_f,name_apg_f,name_spg_f,name_bpg_f,name_tpg_f,name_ppg_f)

def writer2015(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_f,name_fg_f,name_thfg_f,name_twfg_f,name_ft_f,name_rpg_f,name_apg_f,name_spg_f,name_bpg_f,name_tpg_f,name_ppg_f):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_f[name] = mpg
        name_fg_f[name] = fg
        name_thfg_f[name] = thfg
        name_twfg_f[name] = twfg
        name_ft_f[name] = ft
        name_rpg_f[name] = rpg
        name_apg_f[name] = apg
        name_spg_f[name] = spg
        name_bpg_f[name] = bpg
        name_tpg_f[name] = tpg
        name_ppg_f[name] = ppg

def outputter2015(name_mpg_f,name_fg_f,name_thfg_f,name_twfg_f,name_ft_f,name_rpg_f,name_apg_f,name_spg_f,name_bpg_f,name_tpg_f,name_ppg_f):        
    with open("2015-2016_mpg.json", "w") as outfile:
        json.dump(name_mpg_f, outfile)
    with open("2015-2016_fg.json", "w") as outfile:    
        json.dump(name_fg_f, outfile)
    with open("2015-2016_thfg.json", "w") as outfile:
        json.dump(name_thfg_f, outfile)
    with open("2015-2016_twfg.json", "w") as outfile:
        json.dump(name_twfg_f, outfile)
    with open("2015-2016_ft.json", "w") as outfile:
        json.dump(name_ft_f, outfile)
    with open("2015-2016_rpg.json", "w") as outfile:
        json.dump(name_rpg_f, outfile)
    with open("2015-2016_apg.json", "w") as outfile:
        json.dump(name_apg_f, outfile)
    with open("2015-2016_spg.json", "w") as outfile:
        json.dump(name_spg_f, outfile)
    with open("2015-2016_bpg.json", "w") as outfile:
        json.dump(name_bpg_f, outfile)
    with open("2015-2016_tpg.json", "w") as outfile:
        json.dump(name_tpg_f, outfile)
    with open("2015-2016_ppg.json", "w") as outfile:
        json.dump(name_ppg_f, outfile)



############################################################################################### ^2015-2016



def reader2016():
    name_mpg_g = dict();
    name_fg_g = dict();
    name_thfg_g = dict();
    name_twfg_g = dict();
    name_ft_g = dict();
    name_rpg_g = dict();
    name_apg_g = dict();
    name_spg_g = dict();
    name_bpg_g = dict();
    name_tpg_g = dict();
    name_ppg_g = dict();
    with open("2016-2017.txt") as d:
        for line in d:
            regexer2016(line,name_mpg_g,name_fg_g,name_thfg_g,name_twfg_g,name_ft_g,name_rpg_g,name_apg_g,name_spg_g,name_bpg_g,name_tpg_g,name_ppg_g) 
    outputter2016(name_mpg_g,name_fg_g,name_thfg_g,name_twfg_g,name_ft_g,name_rpg_g,name_apg_g,name_spg_g,name_bpg_g,name_tpg_g,name_ppg_g)  

def regexer2016(line,name_mpg_g,name_fg_g,name_thfg_g,name_twfg_g,name_ft_g,name_rpg_g,name_apg_g,name_spg_g,name_bpg_g,name_tpg_g,name_ppg_g):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2016(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_g,name_fg_g,name_thfg_g,name_twfg_g,name_ft_g,name_rpg_g,name_apg_g,name_spg_g,name_bpg_g,name_tpg_g,name_ppg_g)

def writer2016(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_g,name_fg_g,name_thfg_g,name_twfg_g,name_ft_g,name_rpg_g,name_apg_g,name_spg_g,name_bpg_g,name_tpg_g,name_ppg_g):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_g[name] = mpg
        name_fg_g[name] = fg
        name_thfg_g[name] = thfg
        name_twfg_g[name] = twfg
        name_ft_g[name] = ft
        name_rpg_g[name] = rpg
        name_apg_g[name] = apg
        name_spg_g[name] = spg
        name_bpg_g[name] = bpg
        name_tpg_g[name] = tpg
        name_ppg_g[name] = ppg

def outputter2016(name_mpg_g,name_fg_g,name_thfg_g,name_twfg_g,name_ft_g,name_rpg_g,name_apg_g,name_spg_g,name_bpg_g,name_tpg_g,name_ppg_g):        
    with open("2016-2017_mpg.json", "w") as outfile:
        json.dump(name_mpg_g, outfile)
    with open("2016-2017_fg.json", "w") as outfile:    
        json.dump(name_fg_g, outfile)
    with open("2016-2017_thfg.json", "w") as outfile:
        json.dump(name_thfg_g, outfile)
    with open("2016-2017_twfg.json", "w") as outfile:
        json.dump(name_twfg_g, outfile)
    with open("2016-2017_ft.json", "w") as outfile:
        json.dump(name_ft_g, outfile)
    with open("2016-2017_rpg.json", "w") as outfile:
        json.dump(name_rpg_g, outfile)
    with open("2016-2017_apg.json", "w") as outfile:
        json.dump(name_apg_g, outfile)
    with open("2016-2017_spg.json", "w") as outfile:
        json.dump(name_spg_g, outfile)
    with open("2016-2017_bpg.json", "w") as outfile:
        json.dump(name_bpg_g, outfile)
    with open("2016-2017_tpg.json", "w") as outfile:
        json.dump(name_tpg_g, outfile)
    with open("2016-2017_ppg.json", "w") as outfile:
        json.dump(name_ppg_g, outfile)



############################################################################################### ^2016-2017



def reader2017():
    name_mpg_h = dict();
    name_fg_h = dict();
    name_thfg_h = dict();
    name_twfg_h = dict();
    name_ft_h = dict();
    name_rpg_h = dict();
    name_apg_h = dict();
    name_spg_h = dict();
    name_bpg_h = dict();
    name_tpg_h = dict();
    name_ppg_h = dict();
    with open("2017-2018.txt") as d:
        for line in d:
            regexer2017(line,name_mpg_h,name_fg_h,name_thfg_h,name_twfg_h,name_ft_h,name_rpg_h,name_apg_h,name_spg_h,name_bpg_h,name_tpg_h,name_ppg_h) 
    outputter2017(name_mpg_h,name_fg_h,name_thfg_h,name_twfg_h,name_ft_h,name_rpg_h,name_apg_h,name_spg_h,name_bpg_h,name_tpg_h,name_ppg_h)  

def regexer2017(line,name_mpg_h,name_fg_h,name_thfg_h,name_twfg_h,name_ft_h,name_rpg_h,name_apg_h,name_spg_h,name_bpg_h,name_tpg_h,name_ppg_h):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2017(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_h,name_fg_h,name_thfg_h,name_twfg_h,name_ft_h,name_rpg_h,name_apg_h,name_spg_h,name_bpg_h,name_tpg_h,name_ppg_h)

def writer2017(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_h,name_fg_h,name_thfg_h,name_twfg_h,name_ft_h,name_rpg_h,name_apg_h,name_spg_h,name_bpg_h,name_tpg_h,name_ppg_h):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_h[name] = mpg
        name_fg_h[name] = fg
        name_thfg_h[name] = thfg
        name_twfg_h[name] = twfg
        name_ft_h[name] = ft
        name_rpg_h[name] = rpg
        name_apg_h[name] = apg
        name_spg_h[name] = spg
        name_bpg_h[name] = bpg
        name_tpg_h[name] = tpg
        name_ppg_h[name] = ppg

def outputter2017(name_mpg_h,name_fg_h,name_thfg_h,name_twfg_h,name_ft_h,name_rpg_h,name_apg_h,name_spg_h,name_bpg_h,name_tpg_h,name_ppg_h):        
    with open("2017-2018_mpg.json", "w") as outfile:
        json.dump(name_mpg_h, outfile)
    with open("2017-2018_fg.json", "w") as outfile:    
        json.dump(name_fg_h, outfile)
    with open("2017-2018_thfg.json", "w") as outfile:
        json.dump(name_thfg_h, outfile)
    with open("2017-2018_twfg.json", "w") as outfile:
        json.dump(name_twfg_h, outfile)
    with open("2017-2018_ft.json", "w") as outfile:
        json.dump(name_ft_h, outfile)
    with open("2017-2018_rpg.json", "w") as outfile:
        json.dump(name_rpg_h, outfile)
    with open("2017-2018_apg.json", "w") as outfile:
        json.dump(name_apg_h, outfile)
    with open("2017-2018_spg.json", "w") as outfile:
        json.dump(name_spg_h, outfile)
    with open("2017-2018_bpg.json", "w") as outfile:
        json.dump(name_bpg_h, outfile)
    with open("2017-2018_tpg.json", "w") as outfile:
        json.dump(name_tpg_h, outfile)
    with open("2017-2018_ppg.json", "w") as outfile:
        json.dump(name_ppg_h, outfile)



############################################################################################### ^2017-2018



def reader2018():
    name_mpg_i = dict();
    name_fg_i = dict();
    name_thfg_i = dict();
    name_twfg_i = dict();
    name_ft_i = dict();
    name_rpg_i = dict();
    name_apg_i = dict();
    name_spg_i = dict();
    name_bpg_i = dict();
    name_tpg_i = dict();
    name_ppg_i = dict();
    with open("2018-2019.txt") as d:
        for line in d:
            regexer2018(line,name_mpg_i,name_fg_i,name_thfg_i,name_twfg_i,name_ft_i,name_rpg_i,name_apg_i,name_spg_i,name_bpg_i,name_tpg_i,name_ppg_i) 
    outputter2018(name_mpg_i,name_fg_i,name_thfg_i,name_twfg_i,name_ft_i,name_rpg_i,name_apg_i,name_spg_i,name_bpg_i,name_tpg_i,name_ppg_i)  

def regexer2018(line,name_mpg_i,name_fg_i,name_thfg_i,name_twfg_i,name_ft_i,name_rpg_i,name_apg_i,name_spg_i,name_bpg_i,name_tpg_i,name_ppg_i):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2018(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_i,name_fg_i,name_thfg_i,name_twfg_i,name_ft_i,name_rpg_i,name_apg_i,name_spg_i,name_bpg_i,name_tpg_i,name_ppg_i)

def writer2018(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_i,name_fg_i,name_thfg_i,name_twfg_i,name_ft_i,name_rpg_i,name_apg_i,name_spg_i,name_bpg_i,name_tpg_i,name_ppg_i):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_i[name] = mpg
        name_fg_i[name] = fg
        name_thfg_i[name] = thfg
        name_twfg_i[name] = twfg
        name_ft_i[name] = ft
        name_rpg_i[name] = rpg
        name_apg_i[name] = apg
        name_spg_i[name] = spg
        name_bpg_i[name] = bpg
        name_tpg_i[name] = tpg
        name_ppg_i[name] = ppg

def outputter2018(name_mpg_i,name_fg_i,name_thfg_i,name_twfg_i,name_ft_i,name_rpg_i,name_apg_i,name_spg_i,name_bpg_i,name_tpg_i,name_ppg_i):        
    with open("2018-2019_mpg.json", "w") as outfile:
        json.dump(name_mpg_i, outfile)
    with open("2018-2019_fg.json", "w") as outfile:    
        json.dump(name_fg_i, outfile)
    with open("2018-2019_thfg.json", "w") as outfile:
        json.dump(name_thfg_i, outfile)
    with open("2018-2019_twfg.json", "w") as outfile:
        json.dump(name_twfg_i, outfile)
    with open("2018-2019_ft.json", "w") as outfile:
        json.dump(name_ft_i, outfile)
    with open("2018-2019_rpg.json", "w") as outfile:
        json.dump(name_rpg_i, outfile)
    with open("2018-2019_apg.json", "w") as outfile:
        json.dump(name_apg_i, outfile)
    with open("2018-2019_spg.json", "w") as outfile:
        json.dump(name_spg_i, outfile)
    with open("2018-2019_bpg.json", "w") as outfile:
        json.dump(name_bpg_i, outfile)
    with open("2018-2019_tpg.json", "w") as outfile:
        json.dump(name_tpg_i, outfile)
    with open("2018-2019_ppg.json", "w") as outfile:
        json.dump(name_ppg_i, outfile)


############################################################################################### ^2018-2019



def reader2019():
    name_mpg_j = dict();
    name_fg_j = dict();
    name_thfg_j = dict();
    name_twfg_j = dict();
    name_ft_j = dict();
    name_rpg_j = dict();
    name_apg_j = dict();
    name_spg_j = dict();
    name_bpg_j = dict();
    name_tpg_j = dict();
    name_ppg_j = dict();
    with open("2019-2020.txt") as d:
        for line in d:
            regexer2019(line,name_mpg_j,name_fg_j,name_thfg_j,name_twfg_j,name_ft_j,name_rpg_j,name_apg_j,name_spg_j,name_bpg_j,name_tpg_j,name_ppg_j) 
    outputter2019(name_mpg_j,name_fg_j,name_thfg_j,name_twfg_j,name_ft_j,name_rpg_j,name_apg_j,name_spg_j,name_bpg_j,name_tpg_j,name_ppg_j)  

def regexer2019(line,name_mpg_j,name_fg_j,name_thfg_j,name_twfg_j,name_ft_j,name_rpg_j,name_apg_j,name_spg_j,name_bpg_j,name_tpg_j,name_ppg_j):
    reg = re.compile(r"(\d+)(,)(\D+\s\w+)(\D+)(\d+)(,)(\w+)(,)(\d+)(,)(\w+)(,)(\d+)(,)(\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.\d+)(,)(\d+\.+\d+)")
    match = reg.match(line)
    if match is not None:
        name = str(match.group(3))
        mpg = str(match.group(17))
        fg = str(match.group(23))
        thfg = str(match.group(29))
        twfg = str(match.group(35))
        ft = str(match.group(43))
        rpg = str(match.group(49))
        apg = str(match.group(51))
        spg = str(match.group(53))
        bpg = str(match.group(55))
        tpg = str(match.group(57))
        ppg = str(match.group(61))
        writer2019(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_j,name_fg_j,name_thfg_j,name_twfg_j,name_ft_j,name_rpg_j,name_apg_j,name_spg_j,name_bpg_j,name_tpg_j,name_ppg_j)

def writer2019(name,mpg,fg,thfg,twfg,ft,rpg,apg,spg,bpg,tpg,ppg,name_mpg_j,name_fg_j,name_thfg_j,name_twfg_j,name_ft_j,name_rpg_j,name_apg_j,name_spg_j,name_bpg_j,name_tpg_j,name_ppg_j):
        #print(name)
        #print(mpg)
        #print(fg)
        #print(thfg)
        #print(twfg)
        #writer seems to be accepting the regexed stuff
        name_mpg_j[name] = mpg
        name_fg_j[name] = fg
        name_thfg_j[name] = thfg
        name_twfg_j[name] = twfg
        name_ft_j[name] = ft
        name_rpg_j[name] = rpg
        name_apg_j[name] = apg
        name_spg_j[name] = spg
        name_bpg_j[name] = bpg
        name_tpg_j[name] = tpg
        name_ppg_j[name] = ppg

def outputter2019(name_mpg_j,name_fg_j,name_thfg_j,name_twfg_j,name_ft_j,name_rpg_j,name_apg_j,name_spg_j,name_bpg_j,name_tpg_j,name_ppg_j):        
    with open("2019-2020_mpg.json", "w") as outfile:
        json.dump(name_mpg_j, outfile)
    with open("2019-2020_fg.json", "w") as outfile:    
        json.dump(name_fg_j, outfile)
    with open("2019-2020_thfg.json", "w") as outfile:
        json.dump(name_thfg_j, outfile)
    with open("2019-2020_twfg.json", "w") as outfile:
        json.dump(name_twfg_j, outfile)
    with open("2019-2020_ft.json", "w") as outfile:
        json.dump(name_ft_j, outfile)
    with open("2019-2020_rpg.json", "w") as outfile:
        json.dump(name_rpg_j, outfile)
    with open("2019-2020_apg.json", "w") as outfile:
        json.dump(name_apg_j, outfile)
    with open("2019-2020_spg.json", "w") as outfile:
        json.dump(name_spg_j, outfile)
    with open("2019-2020_bpg.json", "w") as outfile:
        json.dump(name_bpg_j, outfile)
    with open("2019-2020_tpg.json", "w") as outfile:
        json.dump(name_tpg_j, outfile)
    with open("2019-2020_ppg.json", "w") as outfile:
        json.dump(name_ppg_j, outfile)


reader2010()
reader2011()
reader2012()
reader2013()
reader2014()
reader2015()
reader2016()
reader2017()
reader2018()
reader2019()
