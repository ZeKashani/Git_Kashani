
str = "دوستان امیدوارم حالتون خوب باشه. دوستان این جلسه پایتون رو شروع میکنیم که امیدوارم براتون مفید باشه"
str2 = str.replace(".", "")
word = set()
for i in str2.split():
    word.add(i)
print
print(len(word))