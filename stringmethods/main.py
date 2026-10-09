str1 = "green donut1"
str2 = "g"
st3 = "i love eating donut donuts DONut donut"
print(str1.find("donut"))
print(str2.find("donut"))
print(st3.find("donut"))

str3 = "i love playing games"
st4 = "jerry went to the library"
str5 = "cats. cats cats cat"
# print(str3.index("I LOVE"))
print(st4.index("jerry"))
print(str5.index("cats"))

str4 = "today i went to the beach"
st5 = "emma did this, emma did that"
str6 = "dinosaurs lived a long time ago"
print(str4.replace("today","yesterday"))
print(st5.replace("emma","alex"))
print(str6.replace("birds","reptiles"))


str7 = ".  ..hi "
print(str7.strip())
print(str7.strip("."))
print(str7.strip("j"))

str8 = "jjjjjjhello"
print(str8.lstrip())
print(str8.lstrip("j"))

str9 = "tea.   .."
str10 = "tea.      "
print(str10.rstrip())
print(str9.rstrip("."))
print(str9.rstrip("hello"))

str11 = "cat,cat,dog,cat"
print(str11.count('cat'))
print(str11.count('dog'))
print(str11.count('fish'))

str12 = "apple;banana;pear;orange;peach"
print(str12.split(';'))
print(str12.split('a'))

str13 = str12.split(';')

str14 = "123abc"
print(str14.isalnum())
print(str14.islower())

str15 = "abedeF"
print(str15.isalpha())
print(str15.islower())
print(str15.isalnum())

str16 = "192384      "
print(str16.isdigit())
print(str16.islower())
print(str16.isspace())

str17 = "       "
print(str17.isspace())
print(str17.isdigit())
print(str17.islower())
print(str17.isalnum())

str18 = "92"
print(str18.isdigit())
print(str18.isalnum())
print(str18.isalpha())

str19 = "Cats Are Green"
print(str19.istitle())
print(str19.startswith('CATS'))
print(str19.endswith('een'))
print(str19.isupper())

str20 = "GREEN"
print(str20.isupper())
print(str20.istitle())
print(str20.startswith('g'))
print(str20.startswith("G"))

str21 = "         N"
print(str21.isupper())
print(str21.endswith('N'))
print(str21.startswith(' '))

if "hi" not in "hello!":
  print('hi is not in hello')

if "math" in "mathletics":
  print('mathletics has math in it')








