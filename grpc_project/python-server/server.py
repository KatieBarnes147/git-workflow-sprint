# server.py
from concurrent import futures
import grpc
import time

# Import the generated classes
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../proto'))  # for module import
import user_service_pb2
import user_service_pb2_grpc

# Mock Data
MOCK_GRID_DATA = {
    "gridId": "BOX123",
    "gridX": 45,
    "gridY": 62,
    "zone": "NorthEast"
}

MOCK_FORECAST = {
    "forecast": "Sunny with a breeze ☀️",
    "temperature": "72°F",
    "wind": "NE 10 mph"
}

# Implement the service
class WeatherService(user_service_pb2_grpc.WeatherServiceServicer):

    def ValidateCoordinates(self, request, context):
        is_valid = -90 <= request.latitude <= 90 and -180 <= request.longitude <= 180
        return user_service_pb2.ValidationResponse(is_valid=is_valid)

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
    user_service_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Python server is running on port 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()