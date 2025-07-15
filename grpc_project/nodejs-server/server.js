const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const path = require("path");

// Load the proto file
const PROTO_PATH = path.join(__dirname, "proto", "user_service.proto");
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const userServiceProto =
  grpc.loadPackageDefinition(packageDefinition).user_service;

// Mock user data
const mockUsers = {
  1: {
    id: 1,
    name: "John Doe",
    email: "john@example.com",
    age: 30,
    created_at: new Date().toISOString(),
  },
  2: {
    id: 2,
    name: "Jane Smith",
    email: "jane@example.com",
    age: 25,
    created_at: new Date().toISOString(),
  },
};

// Implement the GetUser method
function getUser(call, callback) {
  const userId = call.request.user_id;
  console.log(`Node.js Server: GetUser called with user_id: ${userId}`);

  // TODO: Student Task - Implement this method
  // Hint: Look up the user in mockUsers object
  // Return appropriate response with user data, success flag, and message

  // Placeholder implementation - Students should replace this
  const response = {
    user: null,
    success: false,
    message: "Method not implemented yet",
  };

  callback(null, response);
}

// Implement the ListUsers method
function listUsers(call, callback) {
  const page = call.request.page || 1;
  const pageSize = call.request.page_size || 10;
  console.log(
    `Node.js Server: ListUsers called with page: ${page}, page_size: ${pageSize}`
  );

  // TODO: Student Task - Implement this method
  // Hint: Convert mockUsers object to array and handle pagination
  // Return appropriate response with users list, total count, success flag, and message

  // Placeholder implementation - Students should replace this
  const response = {
    users: [],
    total_count: 0,
    success: false,
    message: "Method not implemented yet.",
  };

  callback(null, response);
}

// Implement the CreateUser method
function createUser(call, callback) {
  const { name, email, age } = call.request;
  console.log(
    `Node.js Server: CreateUser called with name: ${name}, email: ${email}, age: ${age}`
  );

  // TODO: Student Task - Implement this method
  // Hint: Create a new user with the next available ID
  // Add to mockUsers object and return the created user

  // Placeholder implementation - Students should replace this
  const response = {
    user: null,
    success: false,
    message: "Method not implemented yet.",
  };

  callback(null, response);
}

// Create and start the server
function main() {
  const server = new grpc.Server();

  // Add the service to the server
  server.addService(userServiceProto.UserService.service, {
    getUser: getUser,
    listUsers: listUsers,
    createUser: createUser,
  });

  // Bind the server to port 50052
  const port = "0.0.0.0:50052";
  server.bindAsync(
    port,
    grpc.ServerCredentials.createInsecure(),
    (error, port) => {
      if (error) {
        console.error("Failed to bind server:", error);
        return;
      }

      console.log(`Node.js gRPC Server starting on port ${port}...`);
      console.log(
        `Server will serve UserService with ${
          Object.keys(mockUsers).length
        } mock users`
      );
      server.start();
    }
  );
}

main();
