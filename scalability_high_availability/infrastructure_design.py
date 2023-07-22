# File: scalability_high_availability/infrastructure_design.py

```python
class CallCenterInfrastructure:
    def __init__(self, call_capacity, availability_zones):
        self.call_capacity = call_capacity
        self.availability_zones = availability_zones

    def handle_call(self, call):
        if self.is_available():
            self.process_call(call)
        else:
            self.redirect_call(call)

    def is_available(self):
        # Check if the call center has available capacity
        return self.call_capacity > 0

    def process_call(self, call):
        # Process the call and provide appropriate response
        print(f"Processing call: {call}")

    def redirect_call(self, call):
        # Redirect the call to another availability zone or backup call center
        print(f"Redirecting call: {call}")


class AvailabilityZone:
    def __init__(self, zone_name, capacity):
        self.zone_name = zone_name
        self.capacity = capacity

    def is_available(self):
        # Check if the availability zone has available capacity
        return self.capacity > 0


# Example usage
if __name__ == "__main__":
    # Create availability zones
    zone1 = AvailabilityZone("Zone 1", 100)
    zone2 = AvailabilityZone("Zone 2", 150)
    zone3 = AvailabilityZone("Zone 3", 200)

    # Create call center infrastructure with multiple availability zones
    infrastructure = CallCenterInfrastructure(450, [zone1, zone2, zone3])

    # Simulate incoming calls
    calls = ["Call 1", "Call 2", "Call 3", "Call 4", "Call 5"]

    for call in calls:
        infrastructure.handle_call(call)
```

This code represents the infrastructure design for a scalable and highly available AI call center. The `CallCenterInfrastructure` class represents the overall call center infrastructure, which includes the call capacity and a list of availability zones. Each availability zone is represented by the `AvailabilityZone` class, which has a zone name and capacity.

The `CallCenterInfrastructure` class has methods to handle incoming calls. The `handle_call` method checks if the call center has available capacity and either processes the call or redirects it to another availability zone. The `is_available` method checks if the call center has available capacity, and the `process_call` and `redirect_call` methods handle the call processing logic.

In the example usage section, we create three availability zones with different capacities and create the call center infrastructure with a total call capacity of 450. We simulate incoming calls and handle them using the `handle_call` method of the `CallCenterInfrastructure` class.

This infrastructure design allows for scalability and high availability by distributing the call processing across multiple availability zones. If one availability zone reaches its capacity, the calls can be redirected to other available zones.