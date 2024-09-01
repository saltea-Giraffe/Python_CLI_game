from random import random

class Unit():
    def __init__(self, name: str):
        self.name = name
        self.hp = 0
        self.atk = 0
        self.atk_acur = 0
        self.run_acur = 0
    
    # 攻撃
    def is_attack(self) -> bool:
        if random() < self.atk_acur:
            return True
        else:
            return False
    
    # 逃げる
    def is_run(self) -> bool:
        if random() < self.run_acur:
            return True
        else:
            return False
    
    # リストを受け取りステータス初期化
    def set_status(self, status_list: list):
        if len(status_list) != 4:
            raise ValueError("The status only 4 value. Can\'t input over or under 4.")
        else:
            self.hp = status_list[0]
            self.atk = status_list[1]
            self.atk_acur = status_list[2]
            self.run_acur = status_list[3]
    
    # Debug func
    def show_status(self):
        print(f"名前:{self.name}")
        print(f"HP:{self.hp}")

# クラステスト用
if __name__ == "__main__":
    player = Unit("プレイヤー")
    enemy = Unit("デビル")
    
    player.hp = 100
    
    player.show_status()
    enemy.show_status()