!pip install google -q

from googlesearch import search
query = "analista de seo"
for result in search(query, num=10, stop=10, lang="pt"):
    print(result)
