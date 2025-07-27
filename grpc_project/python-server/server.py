import grpc
import sys
import os
from concurrent import futures
from datetime import datetime

# Add the generated directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'generated'))

import user_service_pb2
import user_service_pb2_grpc

# Mock user data
mock_users = {
    1: {
        'id': 1,
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 30,
        'created_at': datetime.now().isoformat()
    },
    2: {
        'id': 2,
        'name': 'Jane Smith',
        'email': 'jane@example.com',
        'age': 25,
        'created_at': datetime.now().isoformat()
    }
}

class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    """Provides methods that implement functionality of the UserService server."""
    
    def GetUser(self, request, context):
        """Get user by ID."""
        user_id = request.user_id
        print(f"Python Server: GetUser called with user_id: {user_id}")

        # Look up the user in mock_users
        user_data = mock_users.get(user_id)

        response = user_service_pb2.GetUserResponse()

        if user_data:
            # Populate the User message
            user_message = user_service_pb2.User(
                id=user_data['id'],
                name=user_data['name'],
                email=user_data['email'],
                age=user_data['age'],
                created_at=user_data['created_at']
            )
            response.user.CopyFrom(user_message)
            response.success = True
            response.message = "User found successfully."
        else:
            # If user not found
            response.user.CopyFrom(user_service_pb2.User())  # Empty user
            response.success = False
            response.message = f"User with ID {user_id} not found."

        return response
    
    def ListUsers(self, request, context):
        """List all users with pagination."""
        page = request.page if request.page > 0 else 1
        page_size = request.page_size if request.page_size > 0 else 10
        print(f"Python Server: ListUsers called with page: {page}, page_size: {page_size}")

        # TODO: Student Task - Implement this method
        response = user_service_pb2.ListUsersResponse()
        response.total_count = 0
        response.success = False
        response.message = "Method not implemented yet."

        return response
    
    def CreateUser(self, request, context):
        """Create a new user."""
        name = request.name
        email = request.email
        age = request.age
        print(f"Python Server: CreateUser called with name: {name}, email: {email}, age: {age}")

        # TODO: Student Task - Implement this method
        response = user_service_pb2.CreateUserResponse()
        response.user.CopyFrom(user_service_pb2.User())  # Empty user
        response.success = False
        response.message = "Method not implemented yet."

        return response

def serve():
    """Start the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    
    # Listen on port 50053
    listen_addr = '[::]:50053'
    server.add_insecure_port(listen_addr)
    server.start()
    
    print(f"Python gRPC Server starting on port 50053...")
    print(f"Server will serve UserService with {len(mock_users)} mock users")
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server stopped.")

if __name__ == '__main__':
    serve()
