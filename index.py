#!C:\Users\HUN\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type: text/html; charset-utf-8\n")
print()
import cgi
form = cgi.FieldStorage()
pageId = "WEB"
if "id" in form:
    pageId = form["id"].value
print('''<!doctype html>
<html>
<head>
    <title>메인</title>
 <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py?id=WEB">WEB</a></h1>
  <ol>
    <li><a href="index.py?id=HTML">HTML</a></li>
    <li><a href="index.py?id=CSS">CSS</a></li>
    <li><a href="index.py?id=Javascript">Javascript</a></li>
  </ol>
  <h2>{title}</h2>
  <p>The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.
  </p>
</body>
</html>
'''.format(title=pageId))
