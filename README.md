<a name="readme-top"></a>

<br />
<div align="center">
  <a">
    <img src="src/assets/padlock.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Authserver🔒</h3>

  <p align="center">
    Never write authentication for your projects again!
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

I got tired writing authentication workflows for my apps and third party solutions didn't work out for me. So i made
an authserver for all my apps. Super safe😅.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
### Prerequisites
For this repo you need python 3.10 or higher.

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo

   ```sh
   git clone git@github.com:Brian-Kariu/authserver.git
   ```

2. Make a virtual env and install directly from the requirements file. However for the project you can use pip-tools
to maintain the library dependecies as such i use this commands to generate the requirements file as needed.Install NPM packages

    ```sh
    python3 -m venv
    pip install pip-tools
    pip-compile -o requirements/requirements.txt
    pip-sync requirements/requirements.txt
    ```

3. Create a .env file with these options and activate it. Remember to create you own postgres db

    ```
    export DB_DEPLOY=dev
    export DB_HOST=example_host
    export DB_NAME=example_db
    export DB_PASSWORD=example_password
    export DB_PORT=5432
    export DB_USER=example_user
    export DEBUG=TRUE
    export SECRET_KEY=""
    ```

4. Make migrations then run the server and voila💃

    ```sh
    python manage.py makemigrations
    python mange.py migrate
    python manage.py runserver
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
Ideally you should be able to create a super user account, login then start creating user groups for your app. Other
features would be create,edit and delete permissions for user, social authentication and even admin dashboards.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Features
- [x] Create a working jwt auth flow
- [ ] Detailed user profile
- [ ] Create user groups models for the different apps
- [ ] Create permissions for each of the groups
- [ ] Admin dashboards
- [ ] Social Authentication


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
