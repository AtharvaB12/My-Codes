import webbrowser

wb=input("Google search :")

w=webbrowser.open("https://www.google.com/search?q="+wb)

A=[]
for i in w(wb,stop=10):
         print(i)
         A.append(i)
print(A)
