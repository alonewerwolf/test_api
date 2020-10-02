
from sqlalchemy import create_engine


class DbUtils():
    db_string = "postgresql+psycopg2://postgres:a1e2bdrn@localhost:5432/postgres"
    db = create_engine(db_string)

    def add_new_review(self, product_id, asin, title, review):
        self.db.execute("INSERT INTO review(product_id, asin, title, review) VALUES (%s, %s, %s, %s)", product_id, asin, title, review)

    def get_products(self):
        return self.db.execute(f"""SELECT products.title, products.asin, reviews.review
        FROM products, reviews 
        WHERE products.id = reviews.product_id""")


    def get_product_data_by_id(self, product_id):
        return self.db.execute(f"""SELECT products.asin, products.title
                FROM products
                WHERE  products.id={product_id}""")

    def get_reviews_data_by_id(self, product_id):
        return self.db.execute(f"""SELECT reviews.review
                FROM reviews
                WHERE  reviews.product_id={product_id}""")
