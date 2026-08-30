# This is advance if elif statement example in python

age = 25 


status = {
   (age < 18): " You are a minor.",
   (age ==  18): "Still too Young.", 
   (18 < age < 20): "You are a young adult.",
   (20 <= age < 30): "Perfect age to start your career.",
   (age >= 40): "You are getting older."
}[True]

print(status)