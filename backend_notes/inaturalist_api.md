# Working with the iNaturalist API

iNaturalist is an oAuth2 Provider, so we'll reference the accounts made in iNaturalist with the accounts that we store in the our database.

There are python wrappers that interact with the iNaturalist api namely 

`pip install pynaturalist` 

however it is still under active development so, we'll see how reliable it is.

https://pypi.org/project/pyinaturalist/

---
## User authentication

*User Required to create an account with iNaturalist*

* With this, we can authenticate users:

```
from pyinaturalist.rest_api import get_access_token
token = get_access_token(username='<your_inaturalist_username>', password='<your_inaturalist_password>',
                         app_id='<your_inaturalist_app_id>',
                         app_secret=<your_inaturalist_app_secret>)
```


## Create a new observation:

```
from pyinaturalist.rest_api import create_observations
params = {'observation':
            {'taxon_id': 54327,  # Vespa Crabro
             'observed_on_string': datetime.datetime.now().isoformat(),
             'time_zone': 'Brussels',
             'description': 'This is a free text comment for the observation',
             'tag_list': 'wasp, Belgium',
             'latitude': 50.647143,
             'longitude': 4.360216,
             'positional_accuracy': 50, # meters,

             # sets vespawatch_id (an observation field whose ID is 9613) to the value '100'.
             'observation_field_values_attributes':
                [{'observation_field_id': 9613,'value': 100}],
             },
}

r = create_observations(params=params, access_token=token)
new_observation_id = r[0]['id']

``` 

We can upload photos of our observation, update existing observation, and even search specific taxonomy

# Using oauth kits from other repositories: 

https://github.com/oauthlib/oauthlib

https://github.com/jazzband/django-oauth-toolkit?ref=drawsql

# some tutorials that I'm checking out right now

https://aaronparecki.com/oauth-2-simplified/

https://www.youtube.com/watch?v=kjp8jYJhujA&ab_channel=MatthewLepore
