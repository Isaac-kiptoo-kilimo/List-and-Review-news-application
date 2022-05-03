

class Article:

    articles_list=[]

    def __init__(self,source,author,title,image_url,description_,url_,published_at,content):
        self.source=source
        self.author = author
        self.title = title
        self.image_url=image_url
        self.description_= description_
        self.url_ =url_
        self.published_at = published_at
        self.content = content
    
    @classmethod
    def save_article(self):
        Article.articles_list.append(self)
    
    @classmethod
    def clear_articles(cls):
        Article.articles_list.clear()

    @classmethod
    def get_articles(cls):
        return cls.articles_list


        
class Source:

    sources_list=[]

    def __init__(self,id,name,description,url,category,language,country):
        self.id =id
        self.name = name
        self.description= description
        self.url =url 
        self.category = category
        self.language = language
        self.country = country

    @classmethod
    def save_source(self):
        Source.sources_list.append(self)
    
    @classmethod
    def clear_sources(cls):
        Source.sources_list.clear()

    @classmethod
    def get_sources(cls):
        return cls.sources_list

# class Category:
#     categories_list=[]
    
#     def __init__(self,general,business,sports,entertainment,technology):
#         self.general =general
#         self.business = business
#         self.sports= sports
#         self.entertainment =entertainment 
#         self.technology = technology

#     @classmethod
#     def save_category(self):
#         Category.categories_list.append(self)
    
#     @classmethod
#     def clear_categories(cls):
#         Category.categories_list.clear()

#     @classmethod
#     def get_categoriess(cls):
#         return cls.categories_list