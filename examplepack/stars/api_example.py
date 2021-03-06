import royalnet.utils as ru
import royalnet.constellation.api as rca
import royalnet.constellation.api.apierrors as rcae

# View autogenerated docs for all ApiStars at the HTTP path `/docs`
# TODO: delete this file!


class EchoStar(rca.ApiStar):
    # What does this ApiStar do?
    summary = "Returns the same string entered as input."

    # Optional: A longer description of what the ApiStar should do.
    description = """
        NOTE: This method can only be used by Royalnet Admins.
    """

    # The HTTP path this ApiStar should bind to.
    path = "/api/example/echo/v1"

    # Does this method require any auth?
    # Only for documentation purposes, it doesn't do any check on it's own.
    auth = {
        "get": True,
        "post": False,
        "put": False,
        "delete": False,
    }
    # To authenticate an user through their token, use the `await data.user()` method.
    # If the user isn't logged in, the method authomatically returns 403 Forbidden, unless `rcae.ForbiddenError`
    # is caught.

    # A dict of paramenters accepted by this method, with a description of their purpose.
    parameters = {
        "get": {
            "echo": "What should the method return? "
                    "(Optional: if nothing is passed, the ApiStar will return the username of the caller.)",
            "error": "Should the method return a sample error?"
        },
        "post": {

        },
        "put": {

        },
        "delete": {

        },
    }
    # You can access parameters by using `data` as a dict with the parameter name as key.
    # If a missing parameter is accessed, a `rcae.MissingParameterError` will be raised, which will lead to a
    # 400 Bad Request error if not caught.

    # The autodoc categories this ApiStar should fall in.
    tags = ["example"]

    # The methods called when the ApiStar received a HTTP request.
    # They must return a JSON-compatible object, such as a str, a int, a float, a list, a dict or None.
    # They also must be wrapped with the @rca.magic decorator.
    # You are free to not add them if you don't want the methods to be available

    # Called on a GET request
    @rca.magic
    async def get(self, data: rca.ApiData) -> ru.JSON:

        # If "true" is passed as the "error" parameter in the query string...
        if data["error"] == "true":
            # ...return an example error
            raise Exception("Example error! Everything works as intended.")
        # If the "error" parameter is missing, the ApiStar will respond with 400 Bad Request

        # Ensure the user is logged in
        user = await data.user()
        # Check if the user has the role "admin"
        if "admin" not in user.roles:
            raise Exception("Only admins can call this method!")

        # Get the value of the "echo" parameter, without raising an exception if it doesn't exist
        echo = data.get("echo")

        if echo is None:
            # Find the username of the logged in user
            # user is a SQLAlchemy ORM object generated from the Users table defined in `royalnet.backpack.tables.users`
            echo = user.username

        # Return a 200 OK successful response containing the value of the echo variable and the HTTP method used
        return {"echo": echo, "method_used": "GET"}

    # Called on a POST request
    @rca.magic
    async def post(self, data: rca.ApiData) -> ru.JSON:
        return "This is a response to a POST."

    # Called on a PUT request
    @rca.magic
    async def put(self, data: rca.ApiData) -> ru.JSON:
        return data

    # Called on a DELETE request
    @rca.magic
    async def post(self, data: rca.ApiData) -> ru.JSON:
        return None
