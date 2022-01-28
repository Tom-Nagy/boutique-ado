# What You Need Deployment process

**[:leftwards_arrow_with_hook: *README.md*](README.md)**

Visit the live Website : **[What You Need :arrow_right:](https://WEBSITE-NAME.herokuapp.com/)**.

## Table of Content

* [Get Started](#Get-Started)
  * [Cloning](#Cloning)
  * [Forking](#Forking)
  * [Installations and dependencies](#Installations-and-dependencies)
* [Live Deployment](#Live-Deployment)
  * [Create the Heroku app](#Create-the-Heroku-app)
  * [Set up AWS s3 to host our static files and images](#Set-up-AWS-s3-to-host-our-static-files-and-images)
  * [Connect Django to s3](#Connect-Django-to-s3)
  * [Add Media folder to our bucket](#Add-Media-folder-to-our-bucket)
  * [Final Steps](#Final-Steps)

This project was developed on [GitPod Workspaces IDE](https://www.gitpod.io/) (Integrated Development Environment) committed and pushed to GitHub, to [my Repository](https://github.com/Tom-Nagy/what-you-need) using GitPod Command Line Interface (CLI) with [Git version control](https://git-scm.com/).

:warning: Never share sensible and private information as they are confidential and could put the security of your data, database and website at risk.

## Get Started

1. Log in to your GitHub account.
    * To create an account you need to sign up on [GitHub](https://github.com).
2. Create a repository.
    * See [Create a repo](https://docs.github.com/en/github/getting-started-with-github/create-a-repo).
3. Now several options are available to you:
    * You can copy and paste the code and recreate the same directories structure.
    * You can **clone** my repository.
    * You can **fork** my repository.

### Cloning

When a repository is created on GitHub, it is located on GitHub website (“remotely”). You can create a copy of the repository locally on your machine. This process is called : “**Cloning a repository**”.  
When cloning a repository you are actually copying all the data that the repository contains at that time to your machine.

To clone a repository, take the following steps :

1. Navigate to [What You Need repository](https://github.com/Tom-Nagy/what-you-need).
2. Click on the **Code** dropdown button above the files list.
3. There are three options available to clone the repository :
    * using HTTPS
    * using SSH key
    * using GitHub CLI  
4. Choose HTTPS option and copy the link given.
5. Change the current working directory to the location where you want the cloned directory.
6. Open your IDE and in the CLI type : ```git clone``` and paste the link copied on step 4.
    * ```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY```
7. Press **Enter** and your local clone will be created.

For further information please go to [Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-using-the-command-line).

### Using GitPod

To Clone a repository Using GitPod, take the following steps :

1. Install the GitPod [extension](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki) for Chrome or [Add-on](https://addons.mozilla.org/en-GB/firefox/addon/gitpod/) for Firefox.
2. Navigate to the corresponding repository [What You Need repository](https://github.com/Tom-Nagy/what-you-need).
3. Click on the **GitPod** button on the top right of the files list.
4. This will open a workspace on GitPod where you can work on the repository locally.
    * >The very first time that you do this, you need to connect GitPod and GitHub together. You need to log in with GitHub and launch your workspace (As explain above). And then you need to authorize GitPod to be able to access your GitHub account. You agree to GitPod's terms and conditions, and then create a free account. Then, it will open the workspace for you.
    Quote from : “Creating a GitPod Workspace” on [Code Institute Full Stack Software Development Programme](https://codeinstitute.net/full-stack-software-development-diploma/), by Matt Rudge.

### Using GitHub Desktop

Another option is available : GitHub Desktop. It consists of cloning a repository from GitHub to GitHub Desktop.  
For full information about how to use this option, please visit [GitHub Docs](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-a-repository-from-github-to-github-desktop).

### Forking

Forking a repository will copy it in your own repositories in GitHub.

>A fork is a personal copy of another user's repository that lives on your account. Forks allow you to freely make changes to a project without affecting the original upstream repository. You can also open a pull request in the upstream repository and keep your fork synced with the latest changes since both repositories are still connected.

To Fork a repository take the following steps :

1. Navigate to the corresponding repository [What You Need repository](https://github.com/Tom-Nagy/what-you-need).
2. Identify the ```fork``` button on the top right of the page and click on it.
3. Now you should find a copy of the repository in ```Your repositories```.

### Installations and dependencies

* A requirements.txt file was created in the main project folder. This file tells what applications and dependencies are required to run the application. When you have created/cloned/forked the project, it is import to run this command in the CLI:
  * ``pip3 install -r requirements.txt`` This will make sure to install all the apps requirements for the project.

* Side note: During development whenever a package/dependency is installed with ``pip3 install <name of the package>`` on the project, the following command is ran in the CLI :
  * ``pip3 freeze > requirements.txt`` This is to make sure we update all the apps requirements in requirements.txt for local deployment or for future live deployment.

* You will need to run the migration in order to create the database from the models. Run the following commands in the CLI:
  * ``python3 manage.py makemigrations`` and then,
  * ``python3 manage.py migrate``

* The command to run the project locally (port: 8000):
  * ``python3 manage.py runserver``

* This Project was build with the Django framework, a very powerful and extensive open source project. You can find documentation in the [official django repo](https://github.com/django/django).

The next step is the live deployment of the website :arrow_double_down:

## Live Deployment

* This project was deployed in two steps:
  * First an app to host the website was created on [Heroku](https://heroku.com) where all the code except the static files will live.
  * Then Amazon Web Services (or AWS), and more specifically s3 (simple storage service) will be set up in order to host all static files (css, js, images).

### Create the Heroku app

1. Create an account or Login:
    * [Sing up](https://signup.heroku.com/login)
    * [Login](https://id.heroku.com/login)

2. Click on Create a new app:
    * ![Create a new app](app/static/images/README-images/DEPLOYMENT-images/create-new-app.png)

3. Fill up the form:
    * Make sure to give a unique name to your app.
    * Spaces are not allowed and hyphens should be used instead.
    * Set your region.
    * Click on Create app.

4. You are now directed to your app dashboard.

5. Navigate to the Resources tab.

6. In Add-ons, type Heroku Postgres and select it from the list.
    * ![Select Postgres](select-postgres.png)

7. A pop-up appears to select a plan. Select **Hobby Dev - Free**.
    * ![Free plan Postgres](free-postgres.png)

8. Now you need to save your current database and load it into a db.json file by tyiping in the CLI of your IDE:
    * ``python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json``
    * This will be the data that you will upload to Postgres. Note that you can use a different filename than "db", and it will then be ``<YOUR FILENAME>.json``

9. In order to use Postgres you will need to install **dj_database_url** and **psycopg2**.
    * In the CLI, type:
      * ``pip3 install dj_database_url``
      * ``pip3 install psycopg2-binary``

10. Freeze the requirements. In order to add the new dependencies to *requirements.txt* type in the CLI:
    * ``pip3 freeze > requirements.txt`` This will make sure Heroku install all the apps requirements when we deploy it.

11. Go to what-you-need > settings.py (root folder) and import dj_database_url by typing ``import dj_database_url`` at the top of the file.

12. Then still in settings.py, down in the Database settings, comment out the default database configuration:
    * ![Default config](default-config-commented-out.png)

13. Replace the default database with a call to *dj_database_url.parse* and give it the database URL from Heroku.
    * ![Replace databases](replace-databases.png)
    * You can either get it from your config variables in your Heroku app settings tab, or from the command line by typing Heroku config.
      * ![Database url Heroku](database-url-heroku.png)

14. Run migrations by typing in the CLI:
    * ``Python3 manage.py migrate`` This will apply all the migrations and get the database all set up.

15. Run the following command to load the data previously saved into the json file by typing in the CLI:
    * ``python3 manage.py loaddata db.json``
    * Note that if you used a different file name you need to replace "db" by your file name like so: ``<YOUR FILENAME>.json``

16. Create a superuser to log-in with by typing in the CLI:
    * ``python3 manage.py createsuperuser``
    * Enter a Username, email address and password to complete.

17. In settings.py Remove the Heroku database config and uncomment the original so your database url doesn't end up in version control.
    * The Database settings should be reverted to the way it was:
    * ![Revert Database](revert-database.png)
    * :warning: The Heroku DATABASE_URL should never be public and stay secret. So do not commit your work before you removed the Heroku DATABASE_URL from your file.

18. Now to set up the database depending on the environment (Live on Heroku: -version control/production- or locally on your IDE: -development-); we add an if statement that will set the database to connect to **SQLite** if run locally or set to **Postgres** if run on Heroku.
    * In settings.py your database settings should look like this now:
    * ![Environment database settings](environ-database-settings.png)

19. Now we need to install gunicorn, which will act as our web server. Type in the CLI:
    * ``pip3 install gunicorn``
    * Freeze the package by typing ``pip3 freeze > requirements.txt``

20. Create a Procfile to tell Heroku to create a web dyno and how to run the project.
    * Type in the terminal ``echo web: gunicorn <NAME OF YOUR MAIN FOLDER>.wsgi:application > Procfile``.
    * It is important to note that *the name of your main folder* reflects the name of your project and is where settings.py is located; and *Procfile* is with a capital **P**.
    * Make sure that there is no blank line in your Procfile that should include only one line.

21. Add ``ALLOWED_HOSTS = ['<YOUR APP NAME>.herokuapp.com', 'localhost']`` in settings.py.
    * Add the host name of your Heroku app and localhost, so it still works on your IDE.
    * ![Allowed hosts](allowed-hosts.png)

22. Temporarily disable collectstatic in Heroku.
    * Log-in to Heroku in the CLI by typing:
      * ``heroku login -i``
      * Enter your credentials to complete.

    * Initialize your Heroku git remote by typing in the CLI:
      * ``heroku git:remote -a < HEROKU APP NAME >``, the CLI will prompt ``set git remote heroku to <your heroku git url>``

    * Using Heroku config set, type in the CLI :``heroku config:set DISABLE_COLLECTSTATIC=1``so that Heroku will not try to collect static files when we deploy.
      * This command creates a new var in heroku as shown below:
      * ![Disable collecstatic](disable-collecstatic.png)

    * Add, commit and push your changes to GitHub.

    * Push your work to Heroku by typing: ``git push heroku main``
      * Note that here the “main/master” branch is called “main”. You can check your main branch name in the settings of your repository on GitHub.

23. Create and add a secret key to the config vars of the heroku app in the settings tab. You can generate one by looking up [Django secret key generator online](https://miniwebtool.com/django-secret-key-generator/)
    * ![Secret key](heroku-secret-key.png)

24. In settings.py change configuration for secret key and debug to separate development to production:
    * ``SECRET_KEY = os.environ.get('SECRET_KEY', '')``
    * ``DEBUG = 'DEVELOPMENT' in os.environ``
    * This is so debug is true in development environment, but false in production.
    * You will need to add Variables to your own project either in an env.py file or in your IDE variables like in GitPod:
    * ![GitPod variables](gitpod-variables.png)

25. Add, commit and push your changes to GitHub.

26. Now every time you add, commit and push to GitHub, it will automatically deploy to Heroku.

### Set up AWS s3 to host our static files and images

Now we will set up Amazon Web Services([AWS](https://aws.amazon.com/)) s3(simple storage service) which is a cloud-based storage service that will allow us to store static files and images for the project.

1. Navigate to https://aws.amazon.com/, create an account and sign in.

2. Navigate or look for "s3 Scalable Storage in the Cloud" and create a new bucket used to store our files.
    * To be consistent I recommend naming the bucket the same as your project name on Heroku.
    * Choose the closest region to you.
    * Uncheck "Block all public access" and acknowledge that the bucket will be public.
      * ![AWS public access](aws-public-access.png)
    * Click create bucket and your bucket will be created.

3. Navigate to your bucket and go to the **Properties** tab.
    * Scroll down to "Static website hosting" and click edit.
    * Select enable static website hosting. It will give us a new endpoint we can use to access it from the internet.
    * Enter some default values for the index document (index.html) and for the error document(error.html) as we won't use them for this project.
    * Click save changes.

4. Navigate to the **Permission** tab.

   1. Scroll down to **Cross-origin resource sharing (CORS)** and click edit.
    * Paste the following code to set up the required access between our Heroku app and this s3 bucket and click save changes.

        ```json
        [
            {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
            }
        ]
        ```

   2. Go to the **Bucket Policy** and click edit.
    * Click on "Policy Generator" so we can create a security policy for this bucket.
      * Choose "S3 Bucket Policy" from the policy type list.
      * Allow all principal by entering a star (``*``) in the principal input.
      * Choose "GetObject" from the select Action list.
      * Copy the ARN (Amazon Resource Name) from the "*aws Edit bucket policy*" tab and paste it into the ARN input box. It consists of ``arn:aws:s3:::<your aws bucket name>``
      * Click "Add Statement".
      * The statements should be similar to the following:
        * ![AWS policy](aws-policy.png)
      * Click "Generate Policy".
      * Copy the code snippet provided and paste it in the bucket policy editor replacing the default one.
      * Before to click save we need to modify the resource key because we want to allow access to all resources in this bucket. So we need to add a slash star (``/*``) at the end of the resource key as shown below:
        * ![Resource access](resource-access.png)
      * Click save changes.

    3. Got to **Object Ownership** and click edit.
      * Choose ACLs enabled in order to change ACL list.
      * Acknowledge and click save changes

    4. Got to **Access control list (ACL)** and click edit.
      * At "Everyone (public access)" select List in the Objects column.
      * Tick I understand and save changes.

5. Now the s3 bucket is ready to go, but to access it, we need to create a user. To do This we will use a service called IAM (Identity and Access Management).
    1. Navigate to services or to the search bar, look for and select **IAM**
      * ![AWS IAM](aws-iam.png)
      * first we will create a group for our user to live in.
      * Then we will create an access policy giving the group access to the s3 bucket we created.
      * Finally, we will assign the user to the group, so it can use the policy to access all our files.

    2. Click on "User groups" below Access Management.
      * Click on create a new group and give it a name that is consistent with your project (e.i. ``manage-<your project name>``).
      * Scroll down and click create group.

    3. Click on the "Policies" below Access Management.
      * Click on create policy.
      * Select the JSON tab and click on the import managed policy link. This way we will import one that AWS has pre-built for full access to s3.
      * Search for s3, select "AmazonS3FullAccess" and click import.
      * ![AWS IAM policy](aws-iam-policy.png)
      * We don't actually want to allow full access to everything; we only want to allow full access to our new bucket and everything within it.
      * So get the bucket ARN from your s3 bucket and paste it in resource replacing its ``*`` value.
        * Navigate to services and open s3 from the "recently visited" in a different tab to get your bucket ARN by clicking on your project bucket under the properties tab.
        * We are replacing the current value by a list, so it is important to use the correct syntax as shown bellow.  

        * From this:

          ```json
          "Resource": "*",
          ```

        * To this:

          ```json
          "Resource": [
            "arn:aws:s3:::<your s3 bucket name>",
            "arn:aws:s3:::<your s3 bucket name>/*"
          ]
          ```

        * Click on "next: tags" and leave it as it is.
        * Click on "next: review" and give the policy a name and a description.
        * Click on "create policy".
        * We are now redirected to the policies page, and we can see that the policy was created.
      * Now we will attach the policy to the group we just created.
        * Navigate to user groups and select the group for your project.
        * Click on the Permissons tab.
        * Click on Add Permissions and select Attach Policies.
        * Search for the policy that we just created (It should be on the top of the list, otherwise use the search bar) and select it.
        * Scroll down and click Add Permission.

    4. Now we will create a user to put in the group.
      * Click on Users below Access Management.
      * Click on Add users.
      * Give it a name (e.i. ``<your project name>-staticfiles-user``)
      * Select "Access key - Programmatic access"
      * Click on "Next: Permissions".
      * Select the group we just created that has the policy attached and click next until you create the user as we have nothing else to add.

:warning: Now download the CSV file which will contain the users access key and secret access key which we'll use to authenticate them from our Django app.
**:warning:It is very important you download and save this CSV because once we have gone through this process we CANNOT DOWNLOAD THEM AGAIN. :no_entry:**

### Connect Django to s3

1. Back to your IDE, we will need to install boto3 and django-staorages.
    * Type in the CLI: ``pip3 install boto3``, and ``pip3 install django-storages``.
    * Freeze the packages with ``pip3 freeze > requirements.txt``.
    * We need to add storages to our installed apps.
    * In settings.py and in ``INSTALLED_APPS``, add storages to the list : ``'storages',``.

2. We need to add some settings in settings.py to tell Django to connect to s3 and to which bucket it should be communicating with.

In the "static files" section of settings.py we need to add the following code snippet.

:pushpin: Note that the values will depend on your bucket. You can find the information for the region name in the properties tab of your bucket as well as the name of you bucket which is the end part of the ARN (e.i ``arn:aws:s3:::<your bucket name>``). The access key and secret access key are the one from the .csv file we downloaded earlier.  
As well, we will add cache control in order to tell the browser that it's okay to cache static files for a long time. This will improve performance and user experience.

We use an if statement because we only want to use those on heroku, where we will add the ``USE_AWS`` var next.

```python
# Amazon S3 Bucket
if 'USE_AWS' in os.environ:

  # Cache control
  AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
  }

  # Bucket Config
  AWS_STORAGE_BUCKET_NAME = 'your bucket name'
  AWS_S3_REGION_NAME = 'your region'
  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') 
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' # tell Django where our static files will come from in production.
```

3. Add the AWS variables to the config var in heroku.

Navigate to your Heroku app and to the settings. In Config vars add the following key value pair:

| KEY                   | VALUE      |
| --------------------- |----------- |
| AWS_ACCESS_KEY_ID     | YOUR VALUE |
| AWS_SECRET_ACCESS_KEY | YOUR VALUE |
| USE_AWS               | True       |

Now you can remove/delete the ``DISABLE_COLLECTSTATIC`` variable from the list of variables.

4. Now we need to tell django that in production we want to use s3 to store our static files whenever someone runs collectstatic. And that we want any uploaded product images to go there too.

    * We need to create a file in the root directory called ``custom_storages.py`` and type in the following code snippet.

    ```python
    """
    Configure Amazon s3 for storage in production
    """

    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        """Set static file location"""
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        """Set media files location"""
        location = settings.MEDIAFILES_LOCATION
    ```

    * In settings.py we need to tell Django that for static file storage we want to use our storage class we just created. And git it the location to save the static files (a folder called static).
    * We need to do the same for media files by using the default file storage and media files location settings.
    * As well, we need to override and explicitly set the URLs for static and media files using our custom domain and the new locations.
    * So in settings.py below our bucket settings, add in this code snippet:

    ```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

5. You can now add, commit and push your changes to GitHub. Your static files are now deployed automatically.

### Add Media folder to our bucket

* Navigate to your s3 bucket and to the Objects tab.
* Click on the Create Folder.
* Name your folder media.
* Click Create folder.
* Click on your media folder and inside it,
* Click Upload.
* Click Add Files and select all the product images. If you need to download them all, you can do so from your own GitHub repo.
* In Permissions > Access control list (ACL) > Predefined ACLs select "Grant public-read access" and tick you understand the risks.
* Click on Upload.

### Final Steps

1. Confirm email address for our Superuser in Postgres database.

* Login to Django Admin on the deployed production website of the project by adding ``/admin`` to the website url and press enter.
* You are now directed to the admin login page.
  * Fill in the information with the credentials created when creating the superuser (step 16 of "Create the Heroku app") and login.
* Click on the Email addresses tab under ACCOUNTS.
  * :pushpin: Note that if you do not see your email address, you will need to try and login in first into the website to force allauth to create it.
  * Then repeat the first steps and login to admin, go to email addresses.
* Click on your email address and mark it as **verified** and **primary**.
* Click save.
* You have now successfully register and can logout and login into the website.

2. Set up Stripe with Heroku.

* Login to your Stripe account (or create one if you don't have any).
* Navigate to Developers tab.
* Got to the API keys tab.
  * Retrieve the Publishable key and the Secret key and add them in the config vars settings of your Heroku app.

| KEY                   | VALUE      |
| --------------------- |----------- |
| STRIPE_PUBLIC_KEY     | YOUR VALUE |
| STRIPE_SECRET_KEY     | YOUR VALUE |

* Now we need to create a new webhook endpoint, so it corresponds and connects with the deployed website url.
  * Go to the Webhooks tab in Stripe and click on Add endpoint.
  * Add the url of your Heroku app and add at the end like so: ``<your deployed heroku app url>/checkout/wh/``
  * Click on Select events and choose Select all events.
  * Click on Add events.
  * Scroll down and Click on Add endpoint.
  * Your Webhook is now created, and you can retrieve the Signing secret from it and add it to Heroku.

| KEY                   | VALUE      |
| --------------------- |----------- |
| STRIPE_WH_SECRET      | YOUR VALUE |

:warning: Make sure that the name of your variables in Heroku correspond to the name of the variable used in the stripe set up section of settings.py of your project.

![Stripe variables](stripe-vars.png)

:pushpin: Note that for development, you should have all those variables stored safely somewhere too. For example in the variable settings of your GitPod.  
As well, you should create a Webhook endpoint for development since it will be a different url.

![Gitpod development Variables](gitpod-dev-vars.png)

### Email set up with Django

We are going to use Gmail because it is easy to use, very popular, and it provides a free SMTP server that we can use to send email.

* Login to your Gmail account or create one if needed.
* Go to settings on the upper right, and click view all settings.
* Click on Accounts and Import tab.
* In the "Change account settings:" section, click on "Other Google Account settings" link.
* Go to the Security tab and navigate to "Signing in to Google".
* Select 2-Step Verification. This will allow us to create an app password specific to our Django app that will allow it to authenticate and use our Gmail account to send emails.
* Click on Get Started, enter your credential and click next.
* Select your preferred option and click next.
* Enter the pin to verify and click Turn On.
* Navigate back to "Signing in to Google" and notice the "App passwords" tab below the 2-Step Verification tab.
* Click on App passwords and enter your credentials.
* Select Mail for Select app and Other for Select device and type in Django. You can set whatever you prefer, but it is best practice to stay consistent.
* Click Generate and copy the given password.
* Navigate to the settings tab of your Heroku app and enter the following key/value pair:

| KEY                   | VALUE              |
| --------------------- |------------------- |
| EMAIL_HOST_PASS       | COPY THE PASSWORD  |
| EMAIL_HOST_USER       | YOUR GMAIL ACCOUNT |

* Navigate to settings.py in your project IDE and add the following code snippet to set up email.

```python

# Email settings
if 'DEVELOPMENT' in os.environ:
  EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
  DEFAULT_FROM_EMAIL = '<your default website email>' # This can be configure in the /admin page of the website under sites.
else:
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_USE_TLS = True
  EMAIL_PORT = 587
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
  EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
  DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```

* Add, commit and push your changes.

<!-- What happens now is when our project is deployed to Heroku.
Heroku will run python3 manage.py collectstatic during the build process.
Which will search through all our apps and project folders looking for static files.
And it will use the s3 custom domain setting in conjunction with our custom storage classes that tell it the location at that URL -->

<!-- if we wanted to turn this into a real store at this point
it would involve some additional testing on stripe.
Setting up real confirmation emails.
And switching our stripe settings to use the live keys rather than the test ones we're using now.
we would also likely want to write a plethora of tests for our application.
In particular in the checkout and shopping bag apps.
And make some security adjustments as well as some minor changes to make it easier to work
between our development and production environments seamlessly. -->


<!-- :warning: Never share sensible and private information as they are confidential and could put the security of your data, database and website at risk.

#### Key steps to Deploy on Heroku

This will give a quick and short reminder on the important steps to deploy the on Heroku.

1. Create a Heroku app
2. Connect Git remote to Heroku or Set automatic Deployment from GitHub.
3. Create a requirements.txt file
4. Create a Heroku Procfile: Tells Heroku how to run the project.

You can find the Heroku CLI command on [Code-Institute-Solutions/ FlaskFramework](https://github.com/Code-Institute-Solutions/FlaskFramework/blob/master/05-DeployingOurProjectToHeroku/04-pushing_to_heroku/Heroku_CLI_commands.md) -->

[**:back:** *Table of Content*](#Table-of-Content)
