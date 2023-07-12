from creature import heroes, dummies
from weapon import weapons_onehanded, weapons_twohanded

N = 10_000

weapons = weapons_twohanded

if __name__ == "__main__":
    for monster_name, monster in dummies.items():
        print("monster -", monster_name)
        for hero_name, hero in heroes.items():
            print("\thero -", hero_name.rjust(12))
            calculation_results = []
            for weapon in weapons:
                hero.equip_weapon(weapon)
                monster.damage_taken = 0
                for _ in range(N):
                    monster.take_hit(hero.make_hit())
                calculation_results.append(
                    (
                        monster.damage_taken,
                        f"\t\tweapon - {weapon} >>> {monster.damage_taken / N}",
                    )
                )
            print(*[a[1] for a in sorted(calculation_results, reverse=True)], sep="\n")
