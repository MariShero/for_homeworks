class Person:
    def __init__(self, age, gender, pulse):
        self.age = age
        self.gender = gender
        self.pulse = pulse

    def __str__(self):
        return f"ასაკი- {self.age}, სქესი- {self.gender}, პულსი- {self.pulse}დარტყმა/წუთში"

    def sashualo_sicocxle(self):
        dartyma_weliwadshi = self.pulse * (60*24*365)
        sash = 2600000000 / dartyma_weliwadshi
        return f"საშუალო სიცოცხლის ხანგრძლივობაა- {round(sash)} წელი"


    def max_pulse(self):
        if self.gender == "F":
            x = 226 - (0.9 * self.age)
            return x
        elif self.gender == "M":
            x = 223 - (0.9 * self.age)
            return x

    def max_exercise_pulse(self, factor):
        if factor == "ინტენსიური":
            max = (self.max_pulse() - self.pulse) * 0.8 + self.pulse
            return max
        elif factor == "საშუალო":
            max = (self.max_pulse() - self.pulse) * 0.6 + self.pulse
            return max
        else:
            max = (self.max_pulse() - self.pulse) * 0.5 + self.pulse
            return max

z = Person(15, "F", 70)
print(z)
print(z.sashualo_sicocxle())
print(z.max_pulse())
print(z.max_exercise_pulse("ინტენსიური"))