# Part4
https://hbnb.alwaysdata.net/

python3 -m http.server 5500

## Login.html
email: user@hbnb.com   --> identification backend (developpment.db)

password: user1234


email: admin@hbnb.io   --> identification backend (developpment.db)

password: admin1234


email: admin@hbnb.com   --> identification frontend

password: admin1234

![alt text](frontend/images/image-11.png)

![alt text](frontend/images/image-4.png)

### new page login
![alt text](frontend/images/image-12.png)

#### register a new user (in progress to resolve bug)
![alt text](frontend/images/image-13.png)
![alt text](frontend/images/image-14.png)
![alt text](frontend/images/image-15.png)

### success login
![alt text](frontend/images/image-7.png)
![alt text](frontend/images/image-16.png)
![alt text](frontend/images/image-17.png)

### invalid login
![alt text](frontend/images/image-8.png)

## index.html
![alt text](frontend/images/image-3.png)

### filtre max-price
![alt text](frontend/images/image-9.png)


## place.html
![alt text](frontend/images/image-5.png)
![alt text](frontend/images/image-6.png)


## add-review
![alt text](frontend/images/image-2.png)
![alt text](frontend/images/image.png)
![alt text](frontend/images/image-1.png)


![alt text](frontend/images/image-10.png)


curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/users/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "first_name": "Stéphane",
  "last_name": "Dinahet",
  "email": "st.di@hbnb.io",
  "password": "user1234",
  "is_admin": false
}'
