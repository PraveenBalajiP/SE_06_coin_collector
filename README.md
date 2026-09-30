# Coin Collector Lab

This project is a single-topic top-down Coin Collector game using
**Pygame**. It introduces students to per-frame collision bookkeeping,
entity variety, an obstacle/lives system, and round timing, using a
small, readable object-oriented codebase.

---

## What's Provided

A working Coin Collector game with:

- A player that moves around a play area with the arrow keys
- Coins scattered around the play area that award points on contact
- A running score display

It has **one deliberate bug** and **three features** left for you to
build. You are expected to **analyze**, **interact with an AI
assistant**, and **complete/fix** the game to make it fully functional
and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python main.py
```

**Controls:** Arrow keys to move.

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM
suggestions and your critical code review.

### Task 1: Fix the coin-collection bug

> A coin is supposed to be collected exactly once, the moment the
> player touches it. In the current build, `update()` (in
> `game/game_engine.py`) calls `check_collection` every frame and adds
> a coin's value to the score for as long as the player's rectangle
> keeps overlapping it - but the coin is never actually removed after
> being collected. Just walking through a single coin at normal speed
> (without stopping) scores it more than a dozen times in one pass.
> Fix it so each coin is collected exactly once, no matter how long
> the player stands on or walks through it.

### Task 2: Implement multiple coin types

> Introduce at least three coin types with different values - for
> example bronze (1 point), silver (3 points), and gold (5 points).
> Give each type its own color so they're visually distinguishable,
> and make sure the correct value is awarded when each type is
> collected.

### Task 3: Implement obstacles

> Add obstacles to the play area that the player must avoid while
> collecting coins. Colliding with an obstacle should have a clearly
> defined consequence (for example, losing a life). Obstacles should
> stay within the play area and interact correctly with the player.

### Task 4: Implement a timed round

> Add a 30-second countdown for the round. Display the remaining time
> on screen. Once it reaches zero (or lives run out, once Task 3 is
> done), stop the round, show the final score clearly, and provide a
> way to start a new round with the score, lives, and timer all reset.

---

## Expected Behavior

- Walking through or standing on a coin should collect it exactly
  once - the score should not keep climbing the whole time the player
  happens to be touching it.
- Coin types are visually distinguishable and award the correct value.
- Touching an obstacle has a real, clearly defined consequence, but a
  single touch shouldn't repeatedly punish the player every frame
  they're still overlapping it.
- The round ends when time runs out or lives reach zero, whichever
  comes first, with the final score shown clearly and a way to start
  again.

---

## Folder Structure

```
coin-collector/
├── main.py
├── requirements.txt
├── game/
│   ├── game_engine.py
│   ├── player.py
│   ├── coin.py
│   ├── collection.py
│   └── renderer.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [ ] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [ ] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [ ] The Chat/LLM used page link, with the complete chat history

---

## Implemented Changes

The following changes were implemented as part of completing Tasks 1–4.

### Task 1 — One-time coin collection

The original collection logic checked for overlapping coins every
frame. The collected coin was then awarded repeatedly because it
remained in the active coin list.

The implementation now removes a coin from the active coin list
immediately after awarding its value.

Therefore:

- A coin is awarded only once.
- Standing on a collected coin does not continuously increase the
  score.
- Walking through a coin also awards its value only once.
- Collected coins disappear from the play area.

### Task 2 — Multiple coin types

Three visually distinct coin types were added:

| Coin Type | Value |
|---|---:|
| Bronze | 1 point |
| Silver | 3 points |
| Gold | 5 points |

Each coin stores its own value and color. New coins are randomly
assigned one of the available coin types.

The score therefore increases according to the type of coin collected.

Example:

```text
Bronze → +1
Silver → +3
Gold   → +5
```

### Task 3 — Obstacles and lives

Obstacles were added to the play area as rectangular objects.

The player starts each round with **3 lives**.

When the player collides with an obstacle:

- One life is lost.
- The player is returned to the starting position.
- The collision does not continuously remove lives while the player
  remains on the obstacle.
- The game ends when the number of lives reaches zero.

The obstacles remain within the defined game play area.

### Task 4 — Timed round

A **30-second countdown** was added to each round.

The game displays:

```text
Score: <current score>
Lives: <remaining lives>
Time: <remaining seconds>
```

The round ends when either:

1. The timer reaches zero, or
2. The player's lives reach zero.

When the round ends:

- Player movement stops.
- Coin collection stops.
- Obstacle effects stop.
- The final score remains visible.
- A round-over message is displayed.

The player can press **R** to start a new round.

Restarting a round resets:

```text
Score  → 0
Lives  → 3
Timer  → 30 seconds
Coins  → New set of coins
Player → Starting position
```

---

## Controls

During an active round:

```text
↑  Move up
↓  Move down
←  Move left
→  Move right
```

After the round ends:

```text
R  Restart the round
```

---

## Final Game Flow

The completed game follows this general flow:

```text
Start Game
    │
    ▼
30-Second Round
    │
    ├── Collect Bronze → +1
    ├── Collect Silver → +3
    ├── Collect Gold   → +5
    │
    ├── Hit Obstacle → -1 Life
    │
    ├── Time = 0 ──────────────┐
    │                          │
    └── Lives = 0 ─────────────┤
                               ▼
                          ROUND OVER
                               │
                               ▼
                         Final Score
                               │
                               ▼
                         Press R
                               │
                               ▼
                         New Round
```

---

## Testing Checklist

The completed implementation can be verified using the following
tests:

- [ ] Walking through a coin awards its value exactly once.
- [ ] Standing on a collected coin does not repeatedly increase the
      score.
- [ ] Bronze coins award 1 point.
- [ ] Silver coins award 3 points.
- [ ] Gold coins award 5 points.
- [ ] The three coin types are visually distinguishable.
- [ ] Obstacles are visible inside the play area.
- [ ] Hitting an obstacle removes one life.
- [ ] Remaining on an obstacle does not repeatedly remove lives.
- [ ] The player is repositioned after an obstacle collision.
- [ ] The round starts with 3 lives.
- [ ] The timer starts at 30 seconds.
- [ ] The remaining time is displayed.
- [ ] The round ends when the timer reaches zero.
- [ ] The round ends when lives reach zero.
- [ ] The final score is clearly displayed.
- [ ] Pressing `R` starts a new round.
- [ ] Score, lives, timer, player position, and coins are reset after
      restarting.

---

## Gameplay Demonstration

The required gameplay videos should demonstrate the difference between
the original and completed versions.

### Before Changes

The 10-second gameplay video should demonstrate the original coin
collection bug, where a coin can increase the score repeatedly while
the player remains in contact with it.

### After Changes

The 10-second gameplay video should demonstrate the completed
functionality, including as many of the following as practical:

- One-time coin collection
- Different coin types and values
- Obstacle collision
- Lives decreasing after an obstacle collision
- Countdown timer
- Score and lives display
- Round-over behavior

The complete LLM/ChatGPT conversation should also be provided through
the required chat/page link as specified in the submission checklist.
