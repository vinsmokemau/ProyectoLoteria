# ProyectoLoteria

## Installation
You need to have python3, pip and virtualenv or virtualenv wrapper

```sh
pip install -r base.txt
```

## Run project

Check for issues:
```sh
python manage.py check
```

If you have to update the db because changes in models.py:
```sh
python manage.py makemigrations
```

Update db with migrations:
```sh
python manage.py migrate
```

Run server:
```sh
python manage.py runserver
```

## Contact

Vinsmoke Mau – [@vinsmokemau](https://twitter.com/vinsmokemau) – mauricio.munguia@makingmex.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/resetSystemss/ferreteriapos](https://github.com/vinsmokemau/ProyectoLoteria)

## Contributing

1. Create your feature branch (`git checkout -b feature/fooBar`)
2. Commit your changes (`git commit -am 'Add some fooBar'`)
3. Push to the branch (`git push origin feature/fooBar`)
4. Create a new Pull Request