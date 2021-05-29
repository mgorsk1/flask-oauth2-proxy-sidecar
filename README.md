# Flask oauth2proxy side-container

This repository contains minimal setup for running your Flask application behind oauth2proxy side container with Keycloak
as oidc provider.

## Installation

1. Deploy Keycloak:

    1.1. Run:
    ```shell script
    docker-compose up -d keycloak
    ```
    1.2. Add new line with `127.0.0.1       keycloak` to your `/etc/hosts` file

2. Setup Keycloak client:

    2.1. Go to [http://localhost:8080/auth/admin/master/console/](http://localhost:8080/auth/admin/master/console/)
    
    2.2. Login using `admin` as both username and password.
    
    2.3. Go to `Clients` view.
    
    2.4. Click on `Create` button.
    
    2.5. Use `flask-oidc` as Client ID and `openid-connect` as Client Protocol. Click `Save`.
    
    2.6. Fill out necessary settings:
        - `Access Type`: `confidential`
        - `Valid Redirect URIs`: `http://localhost:5000/*`
        - `Base URL`: `http://localhost:5000/*`
        - Enable options: `Standard Flow Enabled`, `Implicif Flow Enabled` and `Direct Access Grants Enabled`
    
    2.7. Click `Save`.
    
    2.8. From `Credentials` tab copy value of `Secret` field and replace `todo` with it in `OAUTH2_PROXY_CLIENT_SECRET` setting in `docker-compose.yml` file.

3. Setup Keycloak user:
    
    3.1. Still in Keycloak UI go to `Users` view.
    
    3.2. Click on `Add user`.
    
    3.3. Fill out fields `User`, `Email`, `First Name`, `Last Name`.
    
    3.4. Make sure `Email verified` is turned on - switch with `On` label.
    
    3.5. Click on `Save`.
    
    3.6. In `Credentials` tab set users password (make sure `Temporary` is turned off - switch with `Off` label).

4. Deploy the rest of the stack:

```shell script
docker-compose up -d
```

## Usage

Go to [http://localhost:5000](http://localhost:5000) in browser. After logging in with username and password set in point `3` you should see corresponding name and email values.