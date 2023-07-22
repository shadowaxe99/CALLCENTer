# File: outbound_calls/outbound_call_capabilities.py

class OutboundCallCapabilities:
    def __init__(self):
        self.appointment_reminders = []
        self.customer_follow_ups = []

    def add_appointment_reminder(self, reminder):
        self.appointment_reminders.append(reminder)

    def add_customer_follow_up(self, follow_up):
        self.customer_follow_ups.append(follow_up)

    def handle_outbound_calls(self):
        for reminder in self.appointment_reminders:
            self.make_outbound_call(reminder)

        for follow_up in self.customer_follow_ups:
            self.make_outbound_call(follow_up)

    def make_outbound_call(self, recipient):
        # Code to make an outbound call to the recipient
        pass

# Usage example:

outbound_call_capabilities = OutboundCallCapabilities()

outbound_call_capabilities.add_appointment_reminder("John Doe - Appointment on 2022-01-01 at 10:00 AM")
outbound_call_capabilities.add_appointment_reminder("Jane Smith - Appointment on 2022-01-02 at 2:00 PM")

outbound_call_capabilities.add_customer_follow_up("John Doe - Follow-up call after purchase")
outbound_call_capabilities.add_customer_follow_up("Jane Smith - Follow-up call after support ticket")

outbound_call_capabilities.handle_outbound_calls()