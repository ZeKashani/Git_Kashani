

s = {1,2,3,4,6,7,7}
print(s)
print(len(s))

s = s.add(10)
print(s)

print("=" * 30)

str = "دوستان امیدوارم حالتون خوب باشه. دوستان این جلسه پایتون رو شروع میکنیم که امیدوارم براتون مفید باشه"
str2 = str.replace(".", "")
word = set()
for i in str2.split():
    word.add(i)
    print(word)
    print(len(word))

print("=" * 30)

str = "دوستان امیدوارم حالتون خوب باشه. دوستان این جلسه پایتون رو شروع میکنیم که امیدوارم براتون مفید باشه"
str2 = str.replace(".", "")
word = set()
for i in str2.split():
    word.add(i)
print(word)
print(len(word))


print("=" * 30)

#  شمارش تعداد کل کلمات

# t=input("   Paragheraf    ").strip()
t = "I am Zeinab. my Lastname is kashani. age is 39."
c=0
space=False
for i in t:
  if i==" ":
     if space==False:
       c=c+1
       space=True
  else:
      space=False

print(f"Word {c+1}")