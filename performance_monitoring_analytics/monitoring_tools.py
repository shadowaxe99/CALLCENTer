# performance_monitoring_analytics/monitoring_tools.py

```python
class MonitoringTools:
    def __init__(self):
        self.ai_agent_performance = {}
        self.call_success_rates = {}
        self.user_satisfaction = {}

    def track_ai_agent_performance(self, ai_agent_id, performance_metrics):
        self.ai_agent_performance[ai_agent_id] = performance_metrics

    def track_call_success_rate(self, call_id, success_rate):
        self.call_success_rates[call_id] = success_rate

    def track_user_satisfaction(self, user_id, satisfaction_score):
        self.user_satisfaction[user_id] = satisfaction_score

    def get_ai_agent_performance(self, ai_agent_id):
        return self.ai_agent_performance.get(ai_agent_id)

    def get_call_success_rate(self, call_id):
        return self.call_success_rates.get(call_id)

    def get_user_satisfaction(self, user_id):
        return self.user_satisfaction.get(user_id)
```

This code defines a `MonitoringTools` class that can be used to track and store performance metrics, call success rates, and user satisfaction in an automated AI call center. The class has methods to track and retrieve performance data for AI agents, call success rates, and user satisfaction scores.