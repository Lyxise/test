# keywords/keywords.py

# these are intended to be used on nsfw groups or you may get a few false positives
# note that scores above 100 are most likely not false positives
usernameKeywords = {
    "bull": 80,
    "spade": 80,
    "pic4sale": 200,
    "pics4sale": 200,
    "bbc": 150,
    "bwc": 200,
    "fvta": 170,
    "addfor": 150,
    "ykyk": 170,
    "yk": 10,
    "addforyk": 200,
    "selling": 140,
    "6yo": 180,
    "7yo": 180,
    "8yo": 180,
    "9yo": 180,
    "10yo": 180,
    "11yo": 180,
    "12yo": 180,
    "13yo": 180,
    "14yo": 180,
    "15yo": 180,
    "16yo": 180,
    "17yo": 180,
    "6y": 90, # wish i could put these higher but ppl might have num/y in their name for some reason
    "7y": 90,
    "8y": 90,
    "9y": 90,
    "10y": 90,
    "11y": 120,
    "12y": 140,
    "13y": 140,
    "14y": 140,
    "15y": 140,
    "16y": 140,
    "17y": 140,
    "readbio": 200,
    "fmoboy": 140,
    "fxm": 100,
    "bigblack": 140,
    "big": 10,
    "f16": 140,
    "f17": 140,
    "f13": 140,
    "f14": 140,
    "f15": 140,
    "colonizer": 190,
    "coloniser": 190,
    "buii": 150,
    "buil": 150,
    "buli": 150, # bypassings of 'bull'
    "snowbun": 200,
    "sbmissive": 200,
    "submissive": 200,
    "shxchlong": 200,
    "inch": 100,
    "bigbull": 200,
    "bigbuil": 200,
    "bigbuli": 200,
    "_bbl": 200,
    "_bbc": 200,
    "_bwc": 200,
    "12in": 200,
    "16in": 200,
    "15in": 200,
    "14in": 200,
    "11in": 200,
    "10in": 200,
    "9in": 200,
    "8in": 200,
    "10in": 200,
    "7in": 200,
    "6in": 200,
    "hung": 100,
    "ageplay": 200,
    "young": 40,
    "ykwhat": 140,
    "yk what": 140,
    "snwbun": 200,
    "toy": 15,
    "trading": 120,
    "snwbnny": 200,
    "bnwo": 200,
    "fwta": 200,
}

descriptionKeywords = {
    "studio": {"value": 140, "reason": "DESCRIPTION CONTAINS 'STUDIO'"}, # not many ppl in shady groups are gonna have this in their description
    " studio": {"value": 200, "reason": "DESCRIPTION CONTAINS 'STUDIO'"},
    "bull": 70,
    "railed": 50,
    "pounded": 90,
    "\U0001F4BF": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "looking to get": 90,
    "dc: ": 45,
    " dc ": 55,
    "fmboy": 105,
    "s": 0,
    "fermboy": 170,
    "femmy": 180,
    "femmies": 200,
    "looking for": 50,
    " rp": 100,
    "roleplay": 100,
    " les)": 80,
    " les ": 70,
    "add me": 100,
    "add up": 100,
    "submit": 40,
    "dommed": 160,
    "dominated": 160,
    "owned": 40,
    "creamed": 180,
    "tb ": {"value": 140, "reason": "POTENTIAL DISTRIBUTION OF FILES"},
    "1tb": {"value": 200, "reason": "POTENTIAL DISTRIBUTION OF FILES"},
    "øwner": 200,
    "tops only": 200,
    "selling for robux": {"value": 140, "reason": "SELLING FOR ROBUX"},
    "lati nas": 180,
    "lati na": 180,
    "add~": 200,
    "bottom (sub)": 200,
    "top (dom)": 200,
    "any gender": 140,
    "filled": 95,
    "age:": 150,
    "age: ask": 200,
    "age:ask": 200,
    "abdl": 200, # ew
    "fart": 90,
    "snowbun": 200,
    "sbmissive": 200,
    "submissive": 200,
    "shxchlong": 200,
    " cons ": 200,
    "\u2660\ufe0f": 200, #spade emoji
    "\U0001F407": 100, #on its own does not qualify as enough to warrant a flagging
    "\u2744\ufe0f": 100,
    "\u2744\ufe0f\U0001F407": 200,
    "\u2744\ufe0f \U0001F407": 200,
    "\U0001F4C0": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "snow bunny": 200,
    "snowbunnie": 200,
    "sp4de":200,
    "snowbunny": 200,
    " bbc": 200,
    " bbl": 200,
    " bwc": 200,
    "12in": 200,
    "16in": 200,
    "15in": 200,
    "14in": 200,
    "11in": 200,
    "10in": 200,
    "9in": 200,
    "8in": 200,
    "10in": 200,
    "7in": 200,
    "6in": 200,
    "colonise": 120,
    "colonize": 120,
    "seller": 80,
    "add back": 100,
    "char ": 80,
    "char in studio": 200,
    "chubbies": 200,
    "chubby": 80,
    "\u2660": 200, # spade
    "inches": 80,
    "13 ": 80,
    "12 ": 80,
    "11 ": 80,
    "10 ": 80,
    "9 ": 80,
    "8 ": 80,
    "7 ": 80,
    "14 ": 80,
    "15 ": 80,
    "16 ": 80,
    "17 ": 80,
    "bunny": 90,
    "mxen": 180,
    "little ghirl": 200,
    "ghirl": 95,
    "add  me": 120,
    "daddy": 170,
    "mommy": 170,
    "heat": 100,
    "sub": 40, # may be changed
    "hung": 50,
    "dishcoard": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "dis:": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "on dis": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    " ds ": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "on ds": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "ds:": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "trade on": 200,
    "game only": 200,
    "chat only": 200,
    "\U0001F4BD": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "limitless": 50, # idk why preds put this in their desc
    "young": 30,
    "yk what": 180,
    "follow for": 140,
    "follow to": 80,
    "b0ttom": 200,
    "t0p": 200,
    "obedient": 80,
    "age rp": 200,
    "bara": 120,
    "bara men": 200,
    "fut-nari": 200,
    "(‿ˠ‿)": 200,
    "ageplay": 200,
    "age play": 200,
   # ".-": {"value": 100, "reason": "POSSIBLE MORSE CODE"}, better morse code detection system coming soon hopefully
   # ".-..": {"value": 200, "reason": "MORSE CODE"},
    "literate": 50,
    "mdni": 130,
    "bwreedable": 200,
    "breedable": 200,
    "breed": 150,
    "experienced": 20,
    "some fun": 130,
    "femmie": 200,
    " condo ": 200,
    "blue app": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    " frp": 200,
    "trading": 80,
    "\U0001F47B": {"value": 140, "reason": "DESCRIPTION CONTAINS SNAPCHAT REFERENCE"},
    "snwbnny": 200,
    "hmu": 35,
    "hmu~": 140,
    " cord": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "dscrd": {"value": 140, "reason": "DESCRIPTION CONTAINS DISCORD REFERENCE"},
    "bxll": 140,
    "bnwo": 200,
    " dom ": 120,
    "ykyk": 120,
    "no limits": 140,
    "you know why": 100,
    "chat games": 200,
    "fwta": 200,
}
displayNameKeywords = {
    "4sale": 150, # alright bud
    "bull": 100,
    "bulllover": 200,
    "bwreedable": 200,
    "breedable": 200,
    "breed": 150,
    "bbc": 120,
    "bwc": 140,
    "bbl": 30,
    "_bbl": 200,
    "_bbc": 200,
    "_bwc": 200,
    " bbc": 200,
    " bwc": 200,
    " bbl": 180,
    "addme": 200,
    "add me": 170,
    "addfor": 170,
    "add4": 170,
    "readbio": 100,
    "Bio": 50,
    "readdesc": 70,
    "add for": 170,
    "studio": 200, # basically guaranteed if its a display name
    "toy": 50,
    "colonizer": 190,
    "coloniser": 190,
    "fmboy": 140,
    "snowbun": 200,
    "sbmissive": 200,
    "submissive": 200,
    "shxchlong": 200,
    "inch": 100,
    "bigbull": 200,
    "bigbuil": 200,
    "bigbuli": 200,
    "chatonly": 200,
    "12in": 200,
    "16in": 200,
    "15in": 200,
    "14in": 200,
    "11in": 200,
    "10in": 200,
    "9in": 200,
    "8in": 200,
    "10in": 200,
    "7in": 200,
    "6in": 200,
    "freaky": 40,
    "fart": 140,
    "heat": 100,
    "daddy": 170,
    "mommy": 170,
    "femmy": 200,
    "fun": 30,
    "yk": 40,
    "hung": 100,
    "age play": 200,
    "young": 30,
    "ykwhat": 140,
    "yk what": 140,
    "whit3chocolate": 200,
    "trading": 120,
    "snwbnny": 200,
    "bnwo": 200,
    "ykyk": 200,
    "meru": 130,
    "fwta": 200,
}
