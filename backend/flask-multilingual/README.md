# Flask Babel

- [blog-tutorial](https://medium.datadriveninvestor.com/translating-your-web-app-via-flask-babel-a1561376256c)
- [i18n](https://flask-user.readthedocs.io/en/v0.6/internationalization.html)

## Commands

```shell
# to create template - what the message needs to translate
pybabel extract -F babel.cfg -o messages.pot --input-dirs=.

# create a language file
pybabel init -i messages.pot -d translations -l ta

# update translation files from template
pybabel update -i messages.pot -d translations

# compilation
pybabel compile -d translations
```
