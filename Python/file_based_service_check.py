with open("services.txt", "r") as file:
    services = file.readlines() #stores each line as a list

for service in services:
    service_name = service.strip()

    if service_name:
        print(f"Checking status for service: {service_name}")
        print("Service is running (simulated check)")

#with ensures the file is automatically closed after use
#Strip will remove spaces and newline char
