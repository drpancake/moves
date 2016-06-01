# coding: utf-8


import pytest
import responses

import moves


class TestMovesClient(object):
    def test_raises_if_no_acess_token_is_provided(self):
        client = moves.MovesClient()
        with pytest.raises(moves.MovesAPIError) as err:
            client.api('/user')

        assert 'provide a valid access token' in str(err.value)

    @responses.activate
    def test_performs_call_to_api_if_access_token_is_provided(self):
        responses.add(responses.GET,
                      url='https://api.moves-app.com/api/1.1/user/profile',
                      status=200, body='{"success": true, "id": 1}',
                      content_type='application/json')

        client = moves.MovesClient(access_token='secret')

        resp = client.user_profile()

        assert resp == dict(success=True, id=1)
        assert (responses.calls[0].request.headers.get('authorization')
                == 'Bearer secret')

    @responses.activate
    def test_performs_call_to_api_with_overriden_token(self):
        responses.add(responses.GET,
                      url='https://api.moves-app.com/api/1.1/user/profile',
                      status=200, body='{"success": true}',
                      content_type='application/json')

        client = moves.MovesClient(access_token='secret')

        client.user_profile(access_token='new-secret')

        assert (responses.calls[0].request.headers.get('authorization')
                == 'Bearer new-secret')
