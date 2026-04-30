# from character import Character


# class Warrior(Character):
#     def init(self, name, health, damage, armor):
#         super().init(name, health, damage)  
#         self.armor = armor
#         self.blocking = False  

#     def take_damage(self, damage):
        
#         if self.blocking:
#             damage = max(0, damage - self.armor)
#             print(f"{self.name} блокирует! Урон уменьшен до {damage}")
#             self.blocking = False  

#         super().take_damage(damage)

#     def block(self):
#         print(f"{self.name} готовится блокировать следующий удар")
#         self.blocking = True

#     def get_info(self):
#         return f"Воин: {self.name}, HP: {self._health}, Урон: {self._damage}, Броня: {self.armor}"


