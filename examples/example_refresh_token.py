# -*- coding: utf-8 -*-

from moves import MovesClient

def main():
    # data from https://dev.moves-app.com/apps
    client_id = ''
    client_secret = ''
    refresh_token = ''

    api = MovesClient(
        client_id=client_id,
        client_secret=client_secret
    )

    access_token, refresh_token = api.refresh_oauth_token(refresh_token)

    print(access_token, refresh_token)

if __name__ == '__main__':
    main()
