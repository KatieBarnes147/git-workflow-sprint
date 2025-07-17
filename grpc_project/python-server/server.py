# server.py
from concurrent import futures
import grpc
import time
import sys
import os

# Import the generated classes
sys.path.append(os.path.join(os.path.dirname(__file__), '../proto'))
import user_service_pb2
import user_service_pb2_grpc

# Mock Data
MOCK_USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

MOCK_GRID_DATA = {
    "gridId": "BOX123",
    "gridX": 45,
    "gridY": 62,
    "zone": "NorthEast"
}

MOCK_FORECAST = {
    "forecast": "Sunny with a breeze ☀️",
    "temperature": 72,  # Must be int per proto
    "wind": "NE 10 mph"
}

# Implement the service
class UserService(user_service_pb2_grpc.UserServiceServicer):
    
    def GetUser(self, request, context):
        for user in MOCK_USERS:
            if user["id"] == request.user_id:
                return user_service_pb2.GetUserResponse(
                    user=user_service_pb2.User(
                        id=user["id"],
                        name=user["name"],
                        email=user["email"]
                    ),
                    success=True,
                    message="User found."
                )
        return user_service_pb2.GetUserResponse(
            success=False,
            message="User not found."
        )

    def ListUsers(self, request, context):
        users = [
            user_service_pb2.User(
                id=user["id"],
                name=user["name"],
                email=user["email"]
            ) for user in MOCK_USERS
        ]
        return user_service_pb2.ListUsersResponse(users=users)

    def CreateUser(self, request, context):
        new_id = len(MOCK_USERS) + 1
        new_user = {
            "id": new_id,
            "name": request.name,
            "email": request.email
        }
        MOCK_USERS.append(new_user)
        return user_service_pb2.CreateUserResponse(
            user=user_service_pb2.User(**new_user),
            success=True,
            message="User created successfully."
        )

    def ValidateCoordinates(self, request, context):
        is_valid = -90 <= request.latitude <= 90 and -180 <= request.longitude <= 180
        return user_service_pb2.CoordinatesResponse(is_valid=is_valid)

    def GetGridInfo(self, request, context):
        return user_service_pb2.GridInfoResponse(
            grid_id=MOCK_GRID_DATA["gridId"],
            grid_x=MOCK_GRID_DATA["gridX"],
            grid_y=MOCK_GRID_DATA["gridY"],
            zone=MOCK_GRID_DATA["zone"]
        )

    def GetWeatherForecast(self, request, context):
        return user_service_pb2.WeatherForecastResponse(
            forecast=MOCK_FORECAST["forecast"],
            temperature=MOCK_FORECAST["temperature"],
            wind=MOCK_FORECAST["wind"]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("✅ gRPC Python server is running on port 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
