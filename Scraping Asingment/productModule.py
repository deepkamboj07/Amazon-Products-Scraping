from csv import writer
class Product:
    def __init__(self,name,price,rating,review,url):
        self.name=name
        self.price=price
        self.rating=rating
        self.review=review
        self.url=url

    def printProduct(self):
        print("**************************")
        print(self.name)
        print(self.price)
        print(self.review)
        print(self.rating)
        print(self.url)
        print("**************************\n\n")

    def writeIntoCSV(self):
        list=[self.name,self.price,self.review,self.rating,self.url]
        with open('products.csv', 'a+',encoding="utf-8") as f:
            writer_object = writer(f)
            writer_object.writerow(list)
            f.close()


