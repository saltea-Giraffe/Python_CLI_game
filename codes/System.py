from Unit import Unit

class System():
    def __init__(self, p1: Unit, p2: Unit):
        self.player1 = p1
        self.player2 = p2
        
        self.turn = 0
    
    # 遭遇
    def encount(self):
        print("{}は{}に遭遇した！"\
            .format(self.player1.name, self.player2.name))
        self.turn = 1
    
    # プレイヤー選択
    def player_select(self) -> int:
        # print("ターン:{}".format(self.turn))
        print("{}はどうしますか？".format(self.player1.name), end = "")
        select_index = -1
        select_index = int(input("1:戦う 2:逃げる => "))
        print()
        while not 1 <= select_index <= 2:
            print("該当する選択肢が存在しません。")
            print("再度入力してください。")
            select_index = int(input("1:戦う 2:逃げる => "))
        return select_index
    
    # プレイヤー攻撃
    def p1_attack(self):
        print("=>" * 15)
        print("{}は{}に攻撃しました！".format(self.player1.name, self.player2.name))
        # 攻撃確率判定
        if self.player1.is_attack():
            self.player2.hp -= self.player1.atk      # 新敵HP = 旧敵HP - プレイヤー攻撃力
            print("{}に{}ダメージを与えました！".format(self.player2.name, self.player1.atk))
        else:
            print("{}の攻撃は命中しなかった！".format(self.player1.name))
        print()
    
    # エネミー攻撃
    def p2_attack(self):
        print("<=" * 15)
        print("{}が攻撃してきました！".format(self.player2.name))
        # 攻撃確率判定
        if self.player2.is_attack():
            self.player1.hp -= self.player2.atk      # 新プレイヤーHP = 旧プレイヤーHP - 敵攻撃力
            print("{}は{}のダメージを受けました！".format(self.player1.name, self.player2.atk))
        else:
            print("{}は{}の攻撃を受け流しました！".format(self.player1.name, self.player2.name))
        print()
    
    # プレイヤー逃げる
    def p1_run(self):
        if self.player1.is_run():
            print("{}は逃げ出しました！".format(self.player1.name))
        else:
            print("{}は逃げきれなかった！".format(self.player1.name))
    # ターン進行
    def next_turn(self):
        self.turn += 1
    
    # HP確認
    def is_zero(self, player_id: int) -> bool:
        if player_id == 1:
            if self.player1.hp <= 0:
                print("{}は倒され、敗北しました・・・".format(self.player1.name))
                return True
        else:
            if self.player2.hp <= 0:
                print("{}は{}を倒しました！".format(self.player1.name, self.player2.name))
                return True
        return False
    
    # 情報開示
    def show_data(self):
        # ターン表示
        print("ターン : {}".format(self.turn))
        print("=" * 30)
        
        # プレイヤーステータス表示
        print("{}のステータス:".format(self.player1.name))
        print("HP:{}".format(self.player1.hp))
        print("-" * 5)
        
        # 敵ステータス表示
        print("敵のステータス:")
        print("名前:{}".format(self.player2.name))
        print("HP:{}".format(self.player2.hp))
        print("=" * 30)