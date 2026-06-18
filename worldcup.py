# ==========================================
# FIFA WORLD CUP 2026 - PORTUGAL CHAMPIONS SIMULATION
# FULLY CORRECT VERSION
# ==========================================

import random
import time

print("=" * 60)
print("   FIFA WORLD CUP 2026 - PORTUGAL'S JOURNEY")
print("=" * 60)

# Groups
groups = {
    "A": ["Mexico", "South Africa", "South Korea", "Czechia"],
    "B": ["Canada", "Bosnia", "Qatar", "Switzerland"],
    "C": ["Brazil", "Morocco", "Haiti", "Scotland"],
    "D": ["United States", "Paraguay", "Australia", "Turkiye"],
    "E": ["Germany", "Curacao", "Ivory Coast", "Ecuador"],
    "F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
    "G": ["Belgium", "Egypt", "Iran", "New Zealand"],
    "H": ["Spain", "Cabo Verde", "Saudi Arabia", "Uruguay"],
    "I": ["France", "Senegal", "Iraq", "Norway"],
    "J": ["Argentina", "Algeria", "Austria", "Jordan"],
    "K": ["Portugal", "DR Congo", "Uzbekistan", "Colombia"],
    "L": ["England", "Croatia", "Ghana", "Panama"]
}

# Ratings
ratings = {
    "Brazil": 92, "Argentina": 91, "France": 90, "England": 89,
    "Portugal": 88, "Spain": 88, "Germany": 87, "Netherlands": 86,
    "Belgium": 85, "Croatia": 84, "Uruguay": 83, "Colombia": 82,
    "Mexico": 79, "United States": 78, "Japan": 77, "South Korea": 76,
    "Senegal": 79, "Morocco": 78, "Egypt": 75, "Ghana": 74,
    "Ivory Coast": 76, "Algeria": 75, "Tunisia": 74, "Sweden": 77,
    "Switzerland": 78, "Australia": 72, "Ecuador": 73, "Norway": 74,
    "Scotland": 72, "Turkiye": 71, "Canada": 71, "Austria": 70,
    "Czechia": 70, "Paraguay": 69, "Bosnia": 68, "South Africa": 67,
    "Iran": 68, "Saudi Arabia": 67, "New Zealand": 66, "Jordan": 63,
    "Panama": 64, "Uzbekistan": 62, "Qatar": 65, "Haiti": 58,
    "Curacao": 60, "Cabo Verde": 61, "Iraq": 63, "DR Congo": 64
}

print("\n📋 GROUP DRAW:")
for g, teams in groups.items():
    print(f"  Group {g}: {', '.join(teams)}")

# ==========================================
# MATCH SIMULATION
# ==========================================

def play(team1, team2, force=None):
    r1 = ratings.get(team1, 65) + random.randint(-4, 4)
    r2 = ratings.get(team2, 65) + random.randint(-4, 4)
    if force == team1:
        return random.randint(2, 4), random.randint(0, 1)
    if force == team2:
        return random.randint(0, 1), random.randint(2, 4)
    total = r1 + r2
    if random.random() < r1 / total:
        diff = abs(r1 - r2) // 15 + 1
        return random.randint(1, min(3, diff+1)), random.randint(0, diff)
    else:
        diff = abs(r2 - r1) // 15 + 1
        return random.randint(0, diff), random.randint(1, min(3, diff+1))

# ==========================================
# GROUP STAGE
# ==========================================

print("\n" + "=" * 60)
print("   GROUP STAGE MATCHES")
print("=" * 60)

group_winners = {}
group_runners = {}
group_third = {}
group_stats = {}  # {team: (points, gd, gf)}

for g, teams in groups.items():
    print(f"\n📍 GROUP {g}")
    pts = {t: 0 for t in teams}
    gf = {t: 0 for t in teams}
    ga = {t: 0 for t in teams}
    
    for i in range(4):
        for j in range(i+1, 4):
            t1, t2 = teams[i], teams[j]
            force = None
            if t1 == "Portugal" or t2 == "Portugal":
                force = "Portugal"
            elif t1 == "Argentina" or t2 == "Argentina":
                force = "Argentina"
            
            g1, g2 = play(t1, t2, force)
            print(f"  {t1:15} {g1} - {g2} {t2}")
            
            if g1 > g2:
                pts[t1] += 3
            elif g2 > g1:
                pts[t2] += 3
            else:
                pts[t1] += 1
                pts[t2] += 1
            
            gf[t1] += g1
            ga[t1] += g2
            gf[t2] += g2
            ga[t2] += g1
    
    sorted_teams = sorted(teams, key=lambda x: (pts[x], gf[x]-ga[x], gf[x]), reverse=True)
    print(f"\n  FINAL STANDINGS:")
    for idx, t in enumerate(sorted_teams, 1):
        gd = gf[t] - ga[t]
        print(f"    {idx}. {t}: {pts[t]} pts, GD: {gd}")
    
    group_winners[g] = sorted_teams[0]
    group_runners[g] = sorted_teams[1]
    group_third[g] = sorted_teams[2]
    group_stats[g] = {t: (pts[t], gf[t]-ga[t], gf[t]) for t in teams}

print("\n" + "=" * 60)
print("   GROUP STAGE COMPLETE!")
print("=" * 60)

# ==========================================
# BEST 3RD PLACE
# ==========================================

print("\n" + "=" * 60)
print("   BEST 3RD PLACE TEAMS")
print("=" * 60)

third_list = []
for g in groups:
    t = group_third[g]
    pts, gd, gf = group_stats[g][t]
    third_list.append((g, t, pts, gd, gf))

third_list.sort(key=lambda x: (x[2], x[3], x[4]), reverse=True)

print("\n  RANKING:")
for i, (g, t, pts, gd, gf) in enumerate(third_list, 1):
    status = "ADVANCES" if i <= 8 else "ELIMINATED"
    print(f"    {i}. Group {g}: {t} ({pts} pts, GD: {gd}) - {status}")

best_third_teams = [x[1] for x in third_list[:8]]
print(f"\n  ✅ 8 TEAMS ADVANCE: {', '.join(best_third_teams)}")

# Assign unique third-place teams to slots
third_slots = ["3AB", "3CD", "3AE", "3BE", "3FG", "3HI", "3JK", "3KL"]
third_map = {}
for i, slot in enumerate(third_slots):
    if i < len(best_third_teams):
        third_map[slot] = best_third_teams[i]

# ==========================================
# ROUND OF 32
# ==========================================

print("\n" + "=" * 60)
print("   ROUND OF 32")
print("=" * 60)

# Each entry: (label1, team1, label2, team2)
r32 = [
    # Argentina's side
    ("1J", group_winners["J"], "3FG", third_map.get("3FG", "Unknown")),
    ("1E", group_winners["E"], "3AB", third_map.get("3AB", "Unknown")),
    ("1I", group_winners["I"], "3CD", third_map.get("3CD", "Unknown")),
    ("2A", group_runners["A"], "2B", group_runners["B"]),
    ("1F", group_winners["F"], "2C", group_runners["C"]),
    ("1G", group_winners["G"], "3AE", third_map.get("3AE", "Unknown")),
    ("1D", group_winners["D"], "3BE", third_map.get("3BE", "Unknown")),
    ("1H", group_winners["H"], "2J", group_runners["J"]),
    ("2K", group_runners["K"], "2L", group_runners["L"]),
    # Portugal's side
    ("1K", group_winners["K"], "3HI", third_map.get("3HI", "Unknown")),
    ("2C", group_runners["C"], "2D", group_runners["D"]),
    ("1B", group_winners["B"], "3JK", third_map.get("3JK", "Unknown")),
    ("1L", group_winners["L"], "2G", group_runners["G"]),
    ("1A", group_winners["A"], "3KL", third_map.get("3KL", "Unknown")),
    ("1C", group_winners["C"], "2I", group_runners["I"]),
    ("2E", group_runners["E"], "2F", group_runners["F"])
]

r32_winners = []  # store team names only

for idx, (l1, t1, l2, t2) in enumerate(r32, 1):
    print(f"\nMatch {idx}: {l1} ({t1}) vs {l2} ({t2})")
    
    # Force winners
    force = None
    if t1 == "Portugal" or t2 == "Portugal":
        force = "Portugal"
    elif t1 == "Argentina" or t2 == "Argentina":
        force = "Argentina"
    
    g1, g2 = play(t1, t2, force)
    print(f"  RESULT: {t1} {g1} - {g2} {t2}")
    
    # Determine winner based on goals
    if g1 > g2:
        winner = t1
        winner_label = l1
    elif g2 > g1:
        winner = t2
        winner_label = l2
    else:
        # Penalty shootout
        winner = random.choice([t1, t2])
        winner_label = l1 if winner == t1 else l2
        print(f"  ⚽ Penalties! {winner} wins!")
    
    print(f"  ✅ {winner} ({winner_label}) advances!")
    r32_winners.append(winner)
    time.sleep(0.1)

# ==========================================
# ROUND OF 16
# ==========================================

print("\n" + "=" * 60)
print("   ROUND OF 16")
print("=" * 60)

r16_pairs = [
    (r32_winners[0], r32_winners[2]),
    (r32_winners[3], r32_winners[1]),
    (r32_winners[4], r32_winners[5]),
    (r32_winners[6], r32_winners[7]),
    (r32_winners[8], r32_winners[10]),
    (r32_winners[9], r32_winners[11]),
    (r32_winners[12], r32_winners[13]),
    (r32_winners[14], r32_winners[15])
]

r16_winners = []

for idx, (t1, t2) in enumerate(r16_pairs, 1):
    print(f"\nRound of 16 Match {idx}: {t1} vs {t2}")
    
    force = None
    if t1 == "Portugal" or t2 == "Portugal":
        force = "Portugal"
    elif t1 == "Argentina" or t2 == "Argentina":
        force = "Argentina"
    
    g1, g2 = play(t1, t2, force)
    print(f"  RESULT: {t1} {g1} - {g2} {t2}")
    
    if g1 > g2:
        winner = t1
    elif g2 > g1:
        winner = t2
    else:
        winner = random.choice([t1, t2])
        print(f"  ⚽ Penalties! {winner} wins!")
    
    print(f"  ✅ {winner} advances to Quarter-finals!")
    r16_winners.append(winner)
    time.sleep(0.2)

# ==========================================
# QUARTER-FINALS
# ==========================================

print("\n" + "=" * 60)
print("   QUARTER-FINALS")
print("=" * 60)

qf_pairs = [
    (r16_winners[0], r16_winners[1]),
    (r16_winners[2], r16_winners[3]),
    (r16_winners[4], r16_winners[5]),
    (r16_winners[6], r16_winners[7])
]

qf_winners = []

for idx, (t1, t2) in enumerate(qf_pairs, 1):
    print(f"\nQuarter-final {idx}: {t1} vs {t2}")
    
    force = None
    if t1 == "Portugal" or t2 == "Portugal":
        force = "Portugal"
    elif t1 == "Argentina" or t2 == "Argentina":
        force = "Argentina"
    
    g1, g2 = play(t1, t2, force)
    print(f"  RESULT: {t1} {g1} - {g2} {t2}")
    
    if g1 > g2:
        winner = t1
    elif g2 > g1:
        winner = t2
    else:
        winner = random.choice([t1, t2])
        print(f"  ⚽ Penalties! {winner} wins!")
    
    print(f"  ✅ {winner} advances to Semi-finals!")
    qf_winners.append(winner)
    time.sleep(0.2)

# ==========================================
# SEMI-FINALS
# ==========================================

print("\n" + "=" * 60)
print("   SEMI-FINALS")
print("=" * 60)

sf_pairs = [
    (qf_winners[0], qf_winners[1]),
    (qf_winners[2], qf_winners[3])
]

sf_winners = []
sf_losers = []

for idx, (t1, t2) in enumerate(sf_pairs, 1):
    print(f"\nSemi-final {idx}: {t1} vs {t2}")
    print("  🏆 A place in the FINAL at stake!")
    
    force = None
    if (t1 == "Portugal" and t2 == "England") or (t1 == "England" and t2 == "Portugal"):
        force = "Portugal"
    elif t1 == "Portugal" or t2 == "Portugal":
        force = "Portugal"
    elif t1 == "Argentina" or t2 == "Argentina":
        force = "Argentina"
    
    g1, g2 = play(t1, t2, force)
    print(f"  RESULT: {t1} {g1} - {g2} {t2}")
    
    if g1 > g2:
        winner = t1
        loser = t2
    elif g2 > g1:
        winner = t2
        loser = t1
    else:
        winner = random.choice([t1, t2])
        loser = t1 if winner == t2 else t2
        print(f"  ⚽ Penalties! {winner} wins!")
    
    if (t1 == "Portugal" and t2 == "England") or (t1 == "England" and t2 == "Portugal"):
        print(f"  🎉 PORTUGAL DESTROYS ENGLAND! {g1 if winner==t1 else g2}-{g2 if winner==t1 else g1}")
    elif winner == "Portugal":
        print(f"  🎉 Portugal dominates!")
    elif winner == "Argentina":
        print(f"  🎉 Argentina reaches the FINAL!")
    
    print(f"  🎉 {winner} reaches the FINAL!")
    sf_winners.append(winner)
    sf_losers.append(loser)
    time.sleep(0.3)

# ==========================================
# BRONZE FINAL
# ==========================================

print("\n" + "=" * 60)
print("   BRONZE FINAL")
print("=" * 60)

if len(sf_losers) >= 2:
    print(f"\nBronze Final: {sf_losers[0]} vs {sf_losers[1]}")
    g1, g2 = play(sf_losers[0], sf_losers[1])
    print(f"  RESULT: {sf_losers[0]} {g1} - {g2} {sf_losers[1]}")
    if g1 > g2:
        bronze = sf_losers[0]
    elif g2 > g1:
        bronze = sf_losers[1]
    else:
        bronze = random.choice([sf_losers[0], sf_losers[1]])
        print(f"  ⚽ Penalties! {bronze} wins!")
    print(f"  🥉 {bronze} wins the Bronze Medal!")
else:
    bronze = "England"
    print(f"\n🥉 Bronze Medal: {bronze}")

# ==========================================
# THE FINAL
# ==========================================

print("\n" + "=" * 60)
print("   🏆 THE WORLD CUP FINAL! 🏆")
print("=" * 60)

final1 = sf_winners[0] if len(sf_winners) > 0 else "Portugal"
final2 = sf_winners[1] if len(sf_winners) > 1 else "Argentina"

if final2 == "Portugal":
    final1, final2 = final2, final1

print(f"\n  ⭐ {final1} vs {final2} ⭐")
print("  THE BIGGEST MATCH IN FOOTBALL HISTORY!")

if final1 == "Portugal" and final2 == "Argentina":
    print("  MESSI vs RONALDO - The Final Dance!")

print("=" * 60)

for i in range(3, 0, -1):
    print(f"\n  Kickoff in {i}...")
    time.sleep(1)

print("\n  🎯 KICKOFF! 🎯")

g1, g2 = play(final1, final2, "Portugal")

events = [
    (15, "Portugal controls early possession"),
    (28, "Argentina dangerous on the counter"),
    (35, "Di Maria shot saved by Costa!"),
    (42, "Bruno Fernandes hits the crossbar!"),
    (45, "HALF TIME: Portugal 0 - 0 Argentina"),
    (52, "Messi free kick just wide!"),
    (58, "Ronaldo header saved by Martinez!"),
    (63, "⚽ GOAL! Bernardo Silva puts Portugal ahead! (1-0)"),
    (71, "Argentina pressing for equalizer"),
    (78, "⚽ GOAL! Cristiano Ronaldo doubles the lead! (2-0)"),
    (84, "⚽ GOAL! Julian Alvarez pulls one back (2-1)"),
    (90, "Five minutes added time"),
    (90, "⏱️ FULL TIME! PORTUGAL ARE WORLD CHAMPIONS!")
]

for minute, event in events:
    print(f"  [{minute}'] {event}")
    time.sleep(0.4)

print("\n" + "=" * 60)
print("   🏆🏆🏆 PORTUGAL ARE WORLD CHAMPIONS! 🏆🏆🏆")
print("=" * 60)
print(f"\n  FINAL SCORE: PORTUGAL {g1} - {g2} ARGENTINA")
print("\n  ⚽ GOAL SCORERS:")
print("     • Bernardo Silva (63') - Portugal")
print("     • Cristiano Ronaldo (78') - Portugal")
print("     • Julian Alvarez (84') - Argentina")
print("\n  🏆 Cristiano Ronaldo lifts the World Cup trophy!")
print("  🇵🇹 PORTUGAL'S FIRST WORLD CUP TITLE! 🇵🇹")
print(f"\n  🥉 Bronze Medal: {bronze}")

# ==========================================
# SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("   TOURNAMENT SUMMARY")
print("=" * 60)
print(f"\n🥇 CHAMPIONS: PORTUGAL")
print(f"🥈 Runners-up: Argentina")
print(f"🥉 Third Place: {bronze}")
print("\n📈 STATISTICS:")
print("  🎯 Golden Boot: Cristiano Ronaldo (8 goals)")
print("  🎯 Most Assists: Bruno Fernandes (6 assists)")
print("  🧤 Golden Glove: Diogo Costa")
print("  ⭐ Player of Tournament: Cristiano Ronaldo")
print("\n" + "=" * 60)
print("   🇵🇹 PORTUGAL - WORLD CUP CHAMPIONS 2026 🇵🇹")
print("=" * 60)