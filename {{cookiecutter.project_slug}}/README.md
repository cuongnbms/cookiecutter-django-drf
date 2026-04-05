# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Step 1: Install coreui theme

`make install-coreui`

## Step 2: Install requirements

```
make install
```

## Step 3: Run

- with docker: `docker-compose up -d`

- without docker: `make run`

## Create new app
```
./startapp.sh <app_name>
```

## Utils commands

```
# remove all migration files
make remove-all-migrations

# remove all tables in database
python3 manage.py reset_db

# show all urls
python3 manage.py show_urls
```

# Custom admin page

```
# models.py
class QuickAction(models.Model):
    class Meta:
        verbose_name_plural = 'Quick actions'
        app_label = 'admin_extension'
```


## Custom list admin page
```
from base.admin import CustomListPageAdmin

@admin.register(models.QuickAction)
class QuickActionAdmin(CustomListPageAdmin):
    model = models.QuickAction

    def custom_view(self, request, *args, **kwargs):
        context = {
            **admin.site.each_context(request),
        }
        # your logic here
        return render(request, 'admin/quick_action.html', context)
```

## Custom form admin page
```
#forms.py
class InitDataForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea)
```


```
from base.admin import CustomFormPageAdmin

@admin.register(models.InitData)
class InitDirectProxyAdmin(CustomFormPageAdmin):
    title = 'Init Data'
    model = models.InitData
    form_class = InitDataForm

    def process_form(self, request, form, *args, **kwargs):
        # your logic here
        messages.success(request, f"Form processed")
```
