SECRET_KEY = 'django-insecure-uh*#d@d4jg(=*=%-!1c_!38=kz)ibk_jv*ghehkzw-9)qdm)q!'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library',
        'USER': 'root',
        'PASSWORD': 'toor',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}