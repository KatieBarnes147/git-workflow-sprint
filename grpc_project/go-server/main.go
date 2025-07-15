package main

import (
	"context"
	"log"
	"net"
	"time"

	pb "go-server/proto"

	"google.golang.org/grpc"
)

// Here is a comment just added
// Mock user data
var mockUsers = map[int32]*pb.User{
	1: {
		Id:        1,
		Name:      "John Doe",
		Email:     "john@example.com",
		Age:       30,
		CreatedAt: time.Now().Format(time.RFC3339),
	},
	2: {
		Id:        2,
		Name:      "Jane Smith",
		Email:     "jane@example.com",
		Age:       25,
		CreatedAt: time.Now().Format(time.RFC3339),
	},
}

// Server struct implements the UserService
type server struct {
	pb.UnimplementedUserServiceServer
}

// GetUser implements the GetUser RPC method
func (s *server) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.GetUserResponse, error) {
	log.Printf("Go Server: GetUser called with user_id: %d", req.GetUserId())

	// TODO: Student Task - Implement this method
	// Hint: Look up the user in mockUsers map
	// Return appropriate response with user data, success flag, and message

	// Placeholder implementation - Students should replace this
	return &pb.GetUserResponse{
		User:    nil,
		Success: false,
		Message: "Method not implemented yet.",
	}, nil
}

// ListUsers implements the ListUsers RPC method
func (s *server) ListUsers(ctx context.Context, req *pb.ListUsersRequest) (*pb.ListUsersResponse, error) {
	log.Printf("Go Server: ListUsers called with page: %d, page_size: %d", req.GetPage(), req.GetPageSize())

	// TODO: Student Task - Implement this method
	// Hint: Convert mockUsers map to slice and handle pagination
	// Return appropriate response with users list, total count, success flag, and message

	// Placeholder implementation - Students should replace this
	return &pb.ListUsersResponse{
		Users:      []*pb.User{},
		TotalCount: 0,
		Success:    false,
		Message:    "Method not implemented yet.",
	}, nil
}

// CreateUser implements the CreateUser RPC method
func (s *server) CreateUser(ctx context.Context, req *pb.CreateUserRequest) (*pb.CreateUserResponse, error) {
	log.Printf("Go Server: CreateUser called with name: %s, email: %s, age: %d",
		req.GetName(), req.GetEmail(), req.GetAge())

	// TODO: Student Task - Implement this method
	// Hint: Create a new user with the next available ID
	// Add to mockUsers map and return the created user

	// Placeholder implementation - Students should replace this
	return &pb.CreateUserResponse{
		User:    nil,
		Success: false,
		Message: "Method not implemented yet.",
	}, nil
}

func main() {
	// Listen on port 50051
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	// Create gRPC server
	s := grpc.NewServer()

	// Register our service
	pb.RegisterUserServiceServer(s, &server{})

	log.Println("Go gRPC Server starting on port 50051...")
	log.Printf("Server will serve UserService with %d mock users", len(mockUsers))

	// Start serving
	if err := s.Serve(lis); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
