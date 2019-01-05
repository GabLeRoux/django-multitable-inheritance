# Django Model Inheritance - Multi-Table Inheritance Example

[![Build Status](https://travis-ci.com/gableroux/django-multitable-inheritance.svg?branch=master)](https://travis-ci.com/GabLeRoux/django-multitable-inheritance)
[![Requirements Status](https://requires.io/github/GabLeRoux/django-multitable-inheritance/requirements.svg?branch=master)](https://requires.io/github/GabLeRoux/django-multitable-inheritance/requirements/?branch=master)

As described in [the following post](https://godjango.com/blog/django-abstract-base-class-multi-table-inheritance/) Here's what happens when you use Multi Table Inheritance :rocket:

See [multitable/models.py](multitable/models.py) for code snippet.

## Model graph

Generated using the awesome [django-extensions](https://github.com/django-extensions/django-extensions), you should really use this :v:

```bash
pip install -r requirements
python manage.py migrate
python manage.py graph_models -a -g -I "*Ticket*" -o result/graph.png
python manage.py graph_models -a -g -I "*Ticket*" -o result/graph.svg
```

![model graph](result/graph.png)

## What you get in admin panel

```bash
python manage.py createsuperuser
python manage.py runserver
```
### admin panel

![admin](result/admin.png)

### `CustomerTicket`

![CustomerTicket](result/CustomerTicket.png)

### `InternalTicket`

![InternalTicket](result/InternalTicket.png)

### `Ticket`

![Ticket](result/Ticket.png)

# License

MIT © [Gabriel Le Breton](https://gableroux.com)
