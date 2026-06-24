# Project 2: Stateful Expense Tracker Engine

### DecodeLabs Industrial Training Kit | 

---

## Project Overview

This script acts as a vital structural bridge to professional backend development. Rather than relying on simple arithmetic, this project focuses heavily on **Data Accumulation** and real-time state manipulation. The objective is to design a digital foundation that processes continuous incoming data entry with absolute architectural precision.

### Core Specifications

* 
**Goal:** Create a backend script where users enter a series of sequential expense amounts (e.g., 100, 50, 20). The system cleanly accumulates them and presents the compiled **Total Spent** reality.


* 
**Key Skills Implemented:** Stateful accumulation logic ($total = total + new\_expense$), continuous loop orchestration, and defensive programming.


* 
**Relevance:** Mastering this architecture is essential for handling persistent calculations and data routing pipelines within backend logic streams.



---

## Technical Architecture

The architecture of this script mimics a real-world manufacturing line divided into three linear phases:

```
 INPUT: THE GATE       -->      PROCESS: THE ENGINE      -->    OUTPUT: THE DISPLAY
(Raw Material Input)       (Validation & Transformation)       (Actionable Final Reality)

```

[Architecture Blueprint Map ]

### 1. Initialization Phase (Memory Bank)

To bypass the "Volatile Trap" and avoid system amnesia where values are discarded on every loop iteration, the `total` tracking variable is initialized strictly **outside** the running cycle block. This safely preserves state within the database simulation.

### 2. Processing Phase (The Engine)

* 
**The Continuous Audit Loop (`while True:`):** Establishes an infinite execution line that continuously accepts sequential raw transactional feed parameters from standard input.


* 
**The Sentinel Kill Switch:** Monitored via a specific stop value (`'quit'`). When triggered, execution gracefully breaks out of the loop and routes directly to the closing ledger display.


* 
**The Digital Poka-Yoke (Defensive Coding):** A programmatic shield interface wrapped in a `try-except ValueError` core logic engine. If a structurally malformed entry like `"ten"` is injected into the feed, the transformation mechanism safely intercepts it to prevent a fatal stack crash, outputting an "Invalid Data" notification.



### 3. Presentation Phase (Output Stream)

Decoupled cleanly from the processing layers, the script converts the accumulated mathematical data into a refined, human-readable monetary format (`Total.00`), verifying the financial ledger truth.

---

## Qualification & Audit Checklist

Before submitting this project code to the verification station for quality mapping, ensure it clears all criteria listed below:

* [ ] **State Boundary Check:** Is the `total` tracking mechanism safely initialized outside the loop cycle to prevent amnesia?


* [ ] **Digital Poka-Yoke Check:** Does the system capture unexpected strings via a `ValueError` block without breaking execution?


* [ ] **Sentinel Control Check:** Does typing `'quit'` smoothly halt operations and route to the final screen?


* [ ] **Stability Validation:** Can the core execution line effortlessly process 5+ consecutive transactions back-to-back?



---

## How to Run the Script

1. Ensure you have Python installed on your local environment.
2. Clone or copy the provided `main.py` code into a directory workspace.
3. Open a system terminal and execute the backend program line:
```bash
python main.py

```


4. Step through input entry loops to test operational precision. Type `quit` to cleanly exit the system matrix.