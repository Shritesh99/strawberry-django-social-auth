import pytest
from strawberry.types import ExecutionResult

from google.auth.transport.requests import Request
from google.oauth2 import service_account

from gql_social_auth.constants import Messages

scopes = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
credentials = service_account.Credentials.from_service_account_file(
    'key.json', scopes=scopes
)


@pytest.fixture
def login_query():
    def inner() -> str:
        return """
            mutation SocialAuth($provider: String!, $accessToken: String!){
                socialAuth(provider: $provider, accessToken: $accessToken){
                    uid
                    avatar
                    extraData
                    errors
                    success
                    refreshToken {
                        created
                        isExpired
                        expiresAt
                        token
                        revoked
                    }
                    token {
                        token
                        payload {
                            exp
                            origIat
                        }
                    }
                    user {
                        email
                        archived
                        dateJoined
                        firstName
                        isActive
                        id
                        isStaff
                        isSuperuser
                        lastLogin
                        lastName
                        logentrySet {
                            pk
                        }
                        status {
                            archived
                            verified
                        }
                        verified
                    }
                  }
                }
           """

    return inner


@pytest.fixture()
def get_variables():
    if credentials.valid is False:
        credentials.refresh(Request())
    return {
        "provider": "google-oauth2",
        "accessToken": credentials.token
    }


def default_test(res: ExecutionResult):
    assert not res.errors
    res = res.data["socialAuth"]
    assert res["success"]
    assert not res["errors"]
    assert res["refreshToken"]["token"]
    assert res["token"]["token"]


def test_login_success(transactional_db, anonymous_schema, get_variables, login_query):
    res = anonymous_schema.execute(login_query(), arguments=get_variables)
    default_test(res)


def test_invalid_provider(transactional_db, anonymous_schema, get_variables, login_query):
    res = anonymous_schema.execute(login_query(), arguments={"provider": "a", "accessToken": ""})
    assert not res.errors
    res = res.data["socialAuth"]
    assert not res["success"]
    assert res["errors"]["nonFieldErrors"] == Messages.NO_PROVIDER


def test_invalid_access_token(transactional_db, anonymous_schema, get_variables, login_query):
    res = anonymous_schema.execute(login_query(), arguments={"provider": "google-oauth2", "accessToken": ""})
    assert not res.errors
    res = res.data["socialAuth"]
    assert not res["success"]
    assert res["errors"]["nonFieldErrors"]
