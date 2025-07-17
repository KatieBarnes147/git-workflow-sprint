import sys
import os
import grpc

# Add the 'generated' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated')))

# Now import the generated gRPC Python modules
import user_service_pb2
import user_service_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = user_service_pb2_grpc.UserServiceStub(channel)

    # Validate coordinates
    response = stub.ValidateCoordinates(user_service_pb2.CoordinatesRequest(
        latitude=40.0,
        longitude=-70.0
    ))
    print(f"Coordinate Validation: {response.is_valid}")

    # Get grid info
    grid_info = stub.GetGridInfo(user_service_pb2.CoordinatesRequest(
        latitude=40.0,
        longitude=-70.0
    ))
    print(f"Grid Info: ID={grid_info.grid_id}, X={grid_info.grid_x}, Y={grid_info.grid_y}, Zone={grid_info.zone}")

    # Get weather forecast
    forecast = stub.GetWeatherForecast(user_service_pb2.GridInfoRequest(
        grid_id="BOX123",
        grid_x=45,
        grid_y=62
    ))
    print(f"Forecast: {forecast.forecast}, Temp={forecast.temperature}, Wind={forecast.wind}")

if __name__ == '__main__':
    run()
