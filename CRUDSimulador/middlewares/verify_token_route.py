from fastapi.routing import APIRoute
from fastapi import Request
from utils.jwt import jwt_handler
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN


class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def verify_token_middleware(request: Request):

            if request.headers.getlist("Authorization"):
                token = request.headers["Authorization"].split(" ")[1]
                validation_response = jwt_handler.validate_token(token, output=False)
                if validation_response:
                    return validation_response
                else:
                    return await original_route(request)
            else:
                raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="authorization not found")

        return verify_token_middleware
