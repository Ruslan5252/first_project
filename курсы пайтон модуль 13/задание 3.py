cart = {
 "orderID": 12345,
 "shopperName": "Ilyas Zhuanyshov",
 "shopperEmail": "ilyas@gmail.com",
 "products": [
   {
     "productID": 34,
     "productName": "apple",
     "price": 100,
     "quantity": 2
   },
   {
     "productID": 56,
     "productName": "banana",
     "price": 300,
     "quantity": 3
   },
  {
   "productID": 56,
   "productName": "ice-cream",
   "price": 1000,
   "quantity": 2
  },
  {
   "productID": 56,
   "productName": "cake",
   "price": 4000,
   "quantity": 1
  }
 ]
}
sum=0
for i in cart['products']:
    sum+=i['price']*i['quantity']
print(sum)