# Sharing Images with Docker Hub and Other Registers

## Sharing Images with Docker Hub

### Optional: Docker Credential Pass on Linux

By default, Docker may store registry credentials in `~/.docker/config.json`.
To avoid storing them there in an unencrypted form, 
Docker can use an external credential store.

On Linux, one option is `pass`, which stores credentials encrypted with GNU Privacy Guard (GPG).
GPG is a tool for encrypting data and managing cryptographic keys.
It uses a public/private key pair.
`pass` encrypts the credentials using the public GPG key, 
and they can be decrypted using the corresponding private key.
The private key can be protected with a passphrase.

```
docker login
  ↓
docker-credential-pass
  ↓
pass
  ↓
GPG public key
  ↓
encrypt
  ↓
encrypted credentials
```

```
docker push / pull
  ↓
docker-credential-pass
  ↓
pass
  ↓
encrypted credentials
  ↓
GPG private key
  ↓
decrypt
  ↓
credentials
  ↓
Docker authenticates to registry
```

`"credsStore": "pass"` in `~/.docker/config.json` tells Docker to use`docker-credential-pass` 
instead of storing registry credentials directly in `~/.docker/config.json`.

- Install `pass` and GPG
  ```console
  $ sudo apt update
  $ sudo apt install pass gnupg2
  ```

- Check that they are installed
  ```console
  $ which pass
  /usr/bin/pass
  ```

  ```console
  $ gpg --version
  gpg (GnuPG) 2.2.27
  libgcrypt 1.9.4
  Copyright (C) 2021 Free Software Foundation, Inc.
  License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
  ...
  ```

- Generate a GPG key 
  ```console
  $ gpg --full-generate-key
  ...
  sec   ...
        <key-ID>
  uid              ...
  ssb   ...
  ```
  Select:
  ```
  Key type: RSA and RSA
  Key size: 3072 bits
  Expiration: 0 (key does not expire)
  ```
  GPG will also ask for your name, email address, and a passphrase to protect the private key.
  Use the key ID from generated key in the next step.


- Initialize `pass`
  ```console
  $ pass init <key-ID>
  ...
  Password store initialized for <key-ID>
  ```
  This password store will use the selected GPG key to encrypt credentials.


- Install the Docker credential helper
  ```console
  $ sudo apt install golang-docker-credential-helpers
  ```

- Check that the helper is available
  ```console
  $ which docker-credential-pass
  /usr/bin/docker-credential-pass
  ```

- Configure Docker to use `pass` in Nano
  ```console
  $ nano ~/.docker/config.json
  ```

- Change 
  ```
  {
          "auths": {
                  "https://index.docker.io/v1/": {
                          "auth": "..."
                  }
          }
  }
  ```
  to
  ```
  {
      "credsStore": "pass"
  }
  ```
  Save and exit Nano
  `Ctrl + O` → `Enter` → `Ctrl +X`


- Check the configuration
  ```console
  $ cat ~/.docker/config.json
  {
    "credsStore": "pass"
  }
  ```

### Log In to Docker Hub

- Set your Docker ID (your username, not your email address) to the environment variable `dockerId`

  - PowerShell
    ```console
    > $dockerId='<docker-id>'
    ```
    
  - Bash
    ```console
    $ export dockerId='<docker-id>'
    ```
  
- Check the environment variable and log in
    ```console
    $ echo $dockerId
    <docker-id>
    ```

- Log in to Docker Hub
  ```console
  $ docker login --username <doker-id>
  
  i Info → A Personal Access Token (PAT) can be used instead.
           To create a PAT, visit https://app.docker.com/settings
           
           
  Password: 
  Login Succeeded
  ```