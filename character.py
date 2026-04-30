class Character:
    def init(self, name, health, damage):
        self.name = name
        self._health = health      # инкапсуляция
        self._damage = damage

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} не может атаковать (мертв)")
            return

        print(f"{self.name} атакует {target.name} и наносит {self._damage} урона")
        target.take_damage(self._damage)

    def take_damage(self, damage):
        self._health -= damage
        print(f"{self.name} получает {damage} урона. Осталось {self._health} HP")

    def is_alive(self):
        return self._health > 0

    def get_info(self):
        return f"Имя: {self.name}, HP: {self._health}, Урон: {self._damage}"
            
