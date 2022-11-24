class Human:
  emotions = ["love", "angry", "lust", "sad"]
  abilities = ["walk", "speak"]
  
class Man(Human):
  body_weight = "Large"
  emotion_level = "Small"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"""
      Name {self.name}
      Age {self.age}
      Emotion {self.emotions}
      Abilities {self.abilities}
      emotion_level {self.emotion_level}
      body_weight {self.body_weight}\n"""
      
class Woman(Human):
  body_weight = "Small"
  emotion_level = "High"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f"""
      Name {self.name}
      Age {self.age}
      Emotion {self.emotions}
      Abilities {self.abilities}
      emotion_level {self.emotion_level}
      body_weight {self.body_weight}\n"""

prabhu = Man("Prabhu", 23)
print(prabhu)
# Man.abilities += ["Care"]
krishna = Man("Krishna Moorthy", 53)
krishna.abilities += ["care"]
print(prabhu, krishna)

# ammu = Woman("Ammu", 19)
# anbarasi = Woman("Anbarasi", 43)
