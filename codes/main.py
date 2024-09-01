from Unit import Unit
from System import System

def main():
    # ユニット作成
    player = Unit("プレイヤー")
    enemy = Unit("デビル")
    
    # ステータス初期化
    player.set_status([200, 30, 0.8, 0.5])
    enemy.set_status([100, 50, 0.6, 0])
    
    # バトル生成
    battle = System(player, enemy)
    battle.encount()
    # バトルループ
    while True:
        battle.show_data()
        selection = battle.player_select()
        if selection == 1:
            battle.p1_attack()
            if battle.is_zero(2):
                break
            battle.p2_attack()
            if battle.is_zero(1):
                break
        else:
            battle.p1_run()

        battle.next_turn()
        

if __name__ == "__main__":
    main()