import pytest
from strawberry.types import ExecutionResult

from .conftest import SchemaHelper


@pytest.fixture
def login_query():
    def inner() -> str:
        arguments = (
            f'provider: "",'
            f' accessToken: ""'
        )

        return """
           mutation {
           socialAuth(%s)
                  {
            uid
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
           """ % (
            arguments
        )

    return inner

@pytest.fixture()
def archived_schema(db_archived_user_status, rf) -> SchemaHelper:
    return SchemaHelper.create(rf=rf, us_type=db_archived_user_status)


def default_test(res: ExecutionResult):
    assert not res.errors
    res = res.data["tokenAuth"]
    assert res["success"]
    assert not res["errors"]
    assert res["refreshToken"]["token"]
    assert res["token"]["token"]
    assert res["user"]["lastLogin"]


def test_login_success(verified_schema, unverified_schema, allow_login_not_verified, login_query):
    res = verified_schema.execute(login_query())
    print(res)
    default_test(res)
# def test_archived_user_becomes_active_on_login(
#     db_archived_user_status, login_query, archived_schema
# ):
#     user = db_archived_user_status.user.obj
#     assert user.status.archived
#     res = archived_schema.execute(login_query(db_archived_user_status))
#     user.refresh_from_db()
#     assert not user.status.archived
#     default_test(res)
