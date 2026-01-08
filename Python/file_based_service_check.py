with open("services.txt", "r") as file:
    services = file.readlines()

for service in services:
    service_name = service.strip()

    if service_name:
        print(f"Checking status for service: {service_name}")
        print("Service is running (simulated check)")
