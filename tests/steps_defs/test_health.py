from pytest_bdd import scenario, given, when, then


@scenario("../features/health.feature", "I want to check the service is alive")
def test_health_check():
    pass


@given("health endpoint")
def endpoint():
    return "/health"


@when("I send the Get request")
def invoke_get_request(context, client, endpoint):
    response = client.get(endpoint)
    context.response = response


@then("I should get a '200' response")
def status_code_is_200(context):
    assert context.response.status_code == 200
