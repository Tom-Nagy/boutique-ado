# Family Friendly Deployment process

**[:leftwards_arrow_with_hook: *README.md*](README.md)**

Visit the live Website : **[What You Need :arrow_right:](https://WEBSITE-NAME.herokuapp.com/)**.

## Table of Content

* [Get Started](#Get-Started)
  * [Cloning](#Cloning)
  * [Forking](#Forking)
  * [Installations and dependencies](#Installations-and-dependencies)
* [Live Deployment](#Live-Deployment)
  * [Create the Heroku app](#Create-the-Heroku-app)
  * [Heroku Git method](#Heroku-Git-method)
  * [GitHub method](#GitHub-method)
* [App Configurations](#App-Configurations)
* [Implementing API](#Implementing-API)
  * [Emailjs](#Emailjs)

This project was developed on [GitPod Workspaces IDE](https://www.gitpod.io/) (Integrated Development Environment) committed and pushed to GitHub, to [my Repository](https://github.com/Tom-Nagy/family-friendly) using GitPod Command Line Interface (CLI) with [Git version control](https://git-scm.com/).

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

17. Remove the Heroku database config and uncomment the original so your database url doesn't end up in version control.
    * The Database settings should be reverted to the way it was:
    * ![Revert Database](revert-database.png)

<!-- 
5. Navigate to the Deploy tab and notice that three options are given to you on how to deploy your app.


We are going to cover the Heroku Git method using Heroku CLI and the GitHub method connecting to GitHub.

### Heroku Git method

Here we are using Heroku command-line-interface (CLI) also known as **Heroku toolbelt**.

1. Navigate to your app dashboard.

2. Click on the Deploy tab.

3. Scroll down and click on ``Heroku Git`` method.

4. Scroll down to *Install the Heroku CLI*:
    * There are different option available to deploy the project.

5. Go to your Integrated Development Environment (IDE) and open your project.

6. Open the **terminal** and follow the next steps.

7. Install Heroku by typing:
    * `` npm install -g heroku`` in the CLI.
    * **npm** stand for Node Package Manager.
    * **-g** means that we install the Heroku **globally** or system-wide.
    * It is important to note that if **-g** is not included, Heroku will only be installed within a directory called “node-modules” and it will not work as we want it to.

8. Login to Heroku in the terminal:
    * Type ``heroku login -i``.
    * Follow the steps by entering the account details used for this project on Heroku.

9. On the Heroku platform and on your app dashboard, look for **Open app** on the top right by scrolling up:
    * ![open-app](app/static/images/README-images/DEPLOYMENT-images/open-app.png)

10. Now your Heroku app is running:
    * Note that this is the default Heroku app and that you still need to **push** your project to it.
    * Your app's URL corresponds to https://**your-app-name**.herokuapp.com

#### Push your code to the Git URL that Heroku provides

1. Go to settings on your Heroku dashboard and copy your Heroku Git URL.
2. ![Heroku settings](app/static/images/README-images/DEPLOYMENT-images/heroku-settings)
3. ![Heroku Git URL](app/static/images/README-images/DEPLOYMENT-images/heroku-git-url)
4. Create another git remote (that will be different from “origin”)
    * Type in the terminal ``git remote add *name-of-your-remote*`` + paste the Git URL and press enter.
    * ![Git remote command](app/static/images/README-images/DEPLOYMENT-images/git-remote-command.png)
5. Push to Heroku:
    * Type in the terminal ``git push -u *name-of-your-remote* master``
    * ![Push to Heroku](app/static/images/README-images/DEPLOYMENT-images/push-to-heroku.png)
6. You will get an error message because the requirements file is missing. We will add it in the next step.
7. We need to create a requirements.txt file that will list all the Python dependencies the project needs to install in order to run successfully:
    * This will provide Heroku a mean to know what language we are using.
    * Type in the terminal ``pip3 freeze --local > requirements.txt``. This will redirect the output of the freeze command (that list the dependencies) into a file called **requirements.txt**.
    * **Add**, **Commit** and **Push** to Heroku remote master as in step **5.**:
    * ![Requirements file](app/static/images/README-images/DEPLOYMENT-images/create-requirements-file.png)
8. Create a Procfile:
    * Type in the terminal ``echo web: python run.py > Procfile``.
    * It is important to note that *run.py* is the name of our python file and *Procfile* is with a capital **P**.
9. **Add**, **Commit** and **Push**
10. By reloading a refreshing your app on Heroku or by clicking on ``Open app``, your app should display now.

### GitHub method

This method use Automatic Deployment from GitHub, by linking a GitHub repository to Heroku and deploy it automatically.

1. From the Deploy section of your app, click on the GitHub Deployment method:
2. ![Deploy with GitHub](app/static/images/README-images/DEPLOYMENT-images/deploy-github.png)
3. Click on connect to GitHub and Authorize Heroku to connect.
    * ![Connect GitHub](app/static/images/README-images/DEPLOYMENT-images/connect-github.png)
    * ![Authorize Heroku](app/static/images/README-images/DEPLOYMENT-images/auth-heroku.png)
4. Fill up the input for the name of your repository and click search.
5. Click connect.
    * ![Connect the app](app/static/images/README-images/DEPLOYMENT-images/connect-app.png)
6. You need to make sure your project is not connected to Heroku but only to GitHub:
    * in the terminal, type `git remote -v` and if it returns more the *heroku* remote, than remove it with the command ``git remote rm *name-of-your-remote*``
7. **Add** and **Push** your project to GitHub typing in the terminal:
    * ``git add .``
    * ``git commit -m "Push to GitHub."``
    * ``git push origin master``
    * Note that here the “main” branch is called “master”. You can check your main branch name in the settings of your repository on GitHub.
8. Click on ``Deploy Automatically`` and ``Deploy Branch``.
    * ![Deployment](app/static/images/README-images/DEPLOYMENT-images/final-deploy.png)
9. When Deployment successful, you can view the website clicking on ``view`` or ``Òpen app``
    * ![Open app GitHub](app/static/images/README-images/DEPLOYMENT-images/view-app-github.png)

### App Configurations

Because in this project we use a secret-key and other variables, we need, for the application to fully function, to add any hidden environment variables, or Config Vars, within our App Settings.

* Go to the app settings.
* Click on ``Reveal Config Vars``.
* ![Reveal Config Vars](app/static/images/README-images/DEPLOYMENT-images/reveal-config-vars.png)
* Add the variables as shown:
* ![Config Vars](app/static/images/README-images/DEPLOYMENT-images/config-vars.png)
* Most of those variables come from the env.py file. File that is never push to GitHub for security reason.

:warning: Never share sensible and private information as they are confidential and could put the security of your database and website at risk.

#### Key steps to Deploy on Heroku

This will give a quick and short reminder on the important steps to deploy the on Heroku.

1. Create a Heroku app
2. Connect Git remote to Heroku or Set automatic Deployment from GitHub.
3. Create a requirements.txt file
4. Create a Heroku Procfile: Tells Heroku how to run the project.

You can find the Heroku CLI command on [Code-Institute-Solutions/ FlaskFramework](https://github.com/Code-Institute-Solutions/FlaskFramework/blob/master/05-DeployingOurProjectToHeroku/04-pushing_to_heroku/Heroku_CLI_commands.md) -->

[**:back:** *Table of Content*](#Table-of-Content)
