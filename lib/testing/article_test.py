
        article_1.magazine = magazine_2
        assert isinstance(article_1.magazine, Magazine)
        assert article_1.magazine.name == "AD"

    def test_get_all_articles(self):
        """Article class has all attribute"""
        Article.all = []
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")
        article_1 = Article(author, magazine_1, "How to wear a tutu with style")
        article_2 = Article(author, magazine_2, "Dating life in NYC")

        assert len(Article.all) == 2
        assert article_1 in Article.all
        assert article_2 in Article.all