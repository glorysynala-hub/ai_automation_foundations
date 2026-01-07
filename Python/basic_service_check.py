service_name = input("Enter service name: ")

if service_name:
    print(f"Checking status for service: {service_name}")
    print("Service is running (simulated check)")
else:
    print("No service name provided")
