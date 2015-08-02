# coding: utf-8


import pytest

import moves


class TestMovesClient(object):
    def test_raises_if_no_acess_token_is_provided(self):
        client = moves.MovesClient()
        with pytest.raises(moves.MovesAPIError) as err:
            client.api('/user')

        assert 'provide a valid access token' in str(err.value)
