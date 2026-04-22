class Patient:
    def __init__(self, name, age, medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history

    def add_medical_history(self, condition):
        self.medical_history.append(condition)

    def delete_medical_history(self, condition):
        if condition in self.medical_history:
            self.medical_history.remove(condition)
    
    def view_medical_history(self):
        return f"{self.name}'s medical history: {', '.join(self.medical_history)}"