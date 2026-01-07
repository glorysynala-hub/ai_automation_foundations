service_name = input("Enter service name: ")

if service_name:
    print(f"Checking status for service: {service_name}")
    print("Service is running (simulated check)")
else:
    print("No service name provided")


# NOTE:
# This script demonstrates the automation flow (input, logic, output).
# The service status check is intentionally simulated.
#
# Actual OS-level service checks require platform-specific libraries
# and elevated permissions, which will be added in later iterations.
#
# Current focus:
# - Python syntax familiarity
# - Automation logic structure
# - Preparing for real service checks and AI integration
