class Warrior:
    '''Hero'''
    def __init__(self):
        '''Initiate a Hero'''
        self.__level = 1
        self.__rank = 'Pushover'
        self.__experience = 100
        self.__achievements = []

# Work with levels
    def level(self):
        '''State of Hero level'''
        level = self.__level
        return level

    def level_up(self):
        '''Upgrade level of Hero'''
        self.__level = self.__experience // 100

# Work with ranks
    def rank(self):
        '''State of Hero rank'''
        rank = self.__rank
        return rank

    def rank_up(self):
        '''Upgrade rank of Hero'''
        RANKS = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage',
                 'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
        rank_index = self.__level // 10
        self.__rank = RANKS[rank_index]

# Work with experience, skills and achievements
    def experience(self):
        '''State of Hero rank'''
        if self.__experience > 10000:
            self.__experience = 10000
        experience = self.__experience
        return experience

    def skill_up(self):
        '''Upgrade all skills of Hero'''
        self.level_up()
        self.rank_up()

    def achievements(self):
        '''State of Hero achievements'''
        achievements = self.__achievements
        return achievements

# Battle logic
    def battle(self, enemy_level):
        '''Battle logic'''
        if  100 > self.__level < 1:
            return 'Invalid level'

        elif enemy_level == self.__level:
            self.__experience += 10
            self.skill_up()
            return "A good fight"

        elif enemy_level == self.__level - 1:
            self.__experience += 5
            self.skill_up()
            return "A good fight"

        elif enemy_level < self.__level - 1:
            return "Easy fight"

        elif enemy_level > self.__level:
            diff = enemy_level - self.__level
            enemy_rank = 'Pushover'
            RANKS = ['Pushover', 'Novice', 'Fighter', 'Warrior', 'Veteran', 'Sage',
                     'Elite', 'Conqueror', 'Champion', 'Master', 'Greatest']
            if RANKS.index(enemy_rank) > RANKS.index(self.__rank) and diff > 5: 
                return "You've been defeated"
            else:
                self.__experience += 20 * diff ** 2
                self.skill_up()
                return "An intense fight"

# Training logic
    def training(self, name_training, amount_of_experience, min_level):
        '''Training of Hero'''
        if self.__level >= min_level:
            self.__achievements += [name_training]
            self.__experience += amount_of_experience
            self.skill_up()
            return name_training
        else:
            pass

if __name__ == "__main__":
    bruce_lee = Warrior()
    print(bruce_lee.level())         # => 1
    print(bruce_lee.experience())    # => 100
    print(bruce_lee.rank())          # => "Pushover"
    print(bruce_lee.achievements())  # => []
    print(bruce_lee.training("Defeated Chuck Norris", 9000, 1)) # => "Defeated Chuck Norris"
    print(bruce_lee.experience())    # => 9100
    print(bruce_lee.level())         # => 91
    print(bruce_lee.rank())          # => "Master"
    print(bruce_lee.battle(90))    # => "A good fight"
    print(bruce_lee.experience())    # => 9105
    print(bruce_lee.achievements())  # => ["Defeated Chuck Norris"]

# EOF

