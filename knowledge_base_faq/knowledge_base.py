# knowledge_base_faq/knowledge_base.py

```python
class KnowledgeBase:
    def __init__(self):
        self.faq = {}

    def add_faq(self, question, answer):
        self.faq[question] = answer

    def get_answer(self, question):
        if question in self.faq:
            return self.faq[question]
        else:
            return "I'm sorry, but I don't have an answer to that question."

    def remove_faq(self, question):
        if question in self.faq:
            del self.faq[question]
        else:
            raise ValueError("Question not found in the knowledge base.")
```

This code defines a `KnowledgeBase` class that represents a knowledge base for frequently asked questions (FAQs). It has methods to add FAQs, get answers for questions, and remove FAQs. The FAQs are stored in a dictionary where the question is the key and the answer is the value. If a question is not found in the knowledge base, a default message is returned.