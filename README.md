ABSTRACT
  # djangoblog  - blog on django with automated bot who make signup users and posts
                  name and password of new users are random

  root user: socialnetwork
  root pass: socialnetworkpassword

  python3 manage.py runserver 0.0.0.0:5000 --noreload
  Bot path: http://127.0.0.1:5000/bot/
  We prefered to call bot from URL rather then from terminal

  token obtain:
  http://127.0.0.1:5000/api/token/

  checking token and api:
  http://127.0.0.1:5000/hello/



TO DO:
  0. add token auth to bot
  1. extending user data on signup
  2. verify mail on thirdpart site
  3. like/unlike post


LITERATURE CITED
  http://127.0.0.1:8000/admin/auth/user/1/change/
  https://pypi.org/project/rest-social-auth/
  https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg
  https://stackoverflow.com/questions/50383432/count-of-likes-not-showing-in-django
  https://saralgyaan.com/posts/how-to-extend-django-user-model-using-abstractuser/
  https://codingwithmitch.com/courses/build-a-rest-api/register-new-user/
  https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
  curl http://127.0.0.1:8000/hello/ -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVzZXJfaWQiOjF9.Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIckTn9Xx7vhikY'
  curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/
