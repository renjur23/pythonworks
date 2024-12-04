from json import load

f=open("D:\\Pythonworks\\datasets\\books.json")

data=load(f)

book=[book.get("price")for book in data]

costly_book=max(book)

print(costly_book)


max_pages=max(data,key=lambda d:d.get("pages"))

print(max_pages)

autors=[book.get("author")for book in data]

print(autors)

author_count={auth:autors.count(auth) for auth in autors}


print([k for k,v in author_count.items() if v>1])