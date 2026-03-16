# ✈️ AI Flight Assistant – Smart Travel Booking Agent

An intelligent, conversational flight booking assistant powered by Python and natural language processing. This AI agent helps users search for flights, compare options, and complete bookings through an interactive chat interface with real-time decision support.

---

## 📌 Table of Contents

- [🔎 Project Overview](#-project-overview)
- [🚧 Current Technical & Budget Constraints](#-current-technical--budget-constraints)
- [🚀 Final Goals](#-final-goals)
- [🏁 Competitors](#-competitors)
- [❗Key Technical Challenges & Roadblocks](#key-technical-challenges--roadblocks)
- [💡 Proposed Solutions](#-proposed-solutions)
- [📈 System Architecture](#-system-architecture)
- [🔧 Features](#-features)
- [🧪 Agent Workflow Phases](#-agent-workflow-phases)
- [🧬 Conversation Flow Diagram](#-conversation-flow-diagram)
- [🗂 Directory Structure](#-directory-structure)
- [📦 Tech Stack](#-tech-stack)
- [🤖 Agent Design Principles](#-agent-design-principles)
- [🗓 Roadmap](#-roadmap)
- [🧾 License](#-license)
- [👨‍💻 Author](#-author)
- [📬 Future Improvements](#-future-improvements)
- [🙋‍♂️ Contributing](#-contributing)
- [📞 Contact](#-contact)

---

## 🔎 Project Overview

The AI Flight Assistant is a Python-based conversational agent that simulates a complete flight booking experience. It demonstrates how Large Language Models (LLMs) can be integrated with traditional programming to create intelligent, interactive systems that can:

- ✈️ **Understand natural language** flight search requests
- 🔍 **Search for available flights** based on user criteria
- 💰 **Compare prices and options** across airlines
- 📅 **Handle complex booking workflows** with passenger information
- ✅ **Confirm and simulate bookings** with user approval
- 💬 **Maintain conversation context** throughout the interaction

This enables:
- 🧠 **Hands-on learning** of AI agent architecture
- 🔄 **Understanding of tool-use** in LLM applications
- 🛠️ **Practical demonstration** of function calling patterns
- 📊 **State management** in conversational AI systems

---

## 🚧 Current Technical & Budget Constraints

This project operates within a simulated/demo environment with the following constraints:

- **API Integration**: Mock flight data (no real airline APIs)
- **LLM Usage**: Basic intent matching without external LLM API calls
- **Budget**: Zero-cost implementation using only Python standard library
- **Scale**: Single-user, single-session interactions
- **Payment Processing**: Simulated only (no real transactions)
- **Data Persistence**: In-memory only (no database)

---

## 🚀 Final Goals

- ✅ **Intent Recognition**: Understand user requests for flight search and booking
- ✅ **Information Collection**: Gather necessary details (origin, destination, dates)
- ✅ **Flight Search**: Return simulated flight options based on criteria
- ✅ **Option Presentation**: Display flights in readable format with key details
- ✅ **Selection Handling**: Allow users to choose specific flights
- ✅ **Booking Workflow**: Collect passenger information for booking
- ✅ **Confirmation Simulation**: Generate booking references and confirmations
- ✅ **Conversation Reset**: Clear state and start fresh conversations
- ✅ **User Approval Checks**: Confirm before executing actions
- ✅ **Error Handling**: Gracefully handle unexpected inputs

---

## 🏁 Competitors

Several platforms and projects offer AI-powered travel assistance:

- **Expedia's AI Chatbot**: Integrated booking with real inventory but closed source
- **Google Flights**: Excellent search but limited conversational interface
- **Kayak's Explore**: Good for inspiration but not full conversational booking
- **Hopper's AI**: Price prediction focus, limited conversation depth
- **Open-source assistants**: Various chatbot frameworks but few with complete booking flows

This project offers:
- ✅ **Complete open-source implementation**: Full code transparency
- ✅ **Educational focus**: Designed for learning AI agent patterns
- ✅ **Simulated but realistic**: Demonstrates real-world patterns
- ✅ **Extensible architecture**: Easy to add real API integration
- ✅ **Zero-cost operation**: No API keys or subscriptions needed

---

## ❗Key Technical Challenges & Roadblocks

- **Intent Ambiguity**: Users may express the same intent in countless ways
- **Information Extraction**: Parsing dates, airports, and preferences from natural language
- **State Management**: Tracking conversation context across multiple turns
- **Error Recovery**: Handling invalid inputs without breaking the flow
- **Multi-step Workflows**: Managing complex booking processes
- **User Confirmation**: Ensuring users approve before "costly" actions
- **Context Switching**: Allowing users to change their mind mid-process
- **Edge Cases**: Handling unexpected inputs gracefully

---

## 💡 Proposed Solutions

- **Keyword-based Intent Detection**: Simple but effective pattern matching
- **Proactive Information Gathering**: Ask for missing details systematically
- **Conversation State Tracking**: Maintain collected_info dictionary
- **Graceful Degradation**: Friendly error messages and re-prompting
- **Step-by-step Confirmation**: User approval before each major action
- **Reset Capability**: Clear command to start fresh
- **Structured Output**: JSON responses that are both human-readable and parseable
- **Simulated Realism**: Demo mode with realistic flight options

---

## 📈 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                            │
│                      (Command Line / Terminal)                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      CONVERSATION ENGINE                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │ Intent Detection│───▶│State Management │───▶│Response Gen │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────────────┐
        │                   TOOL LAYER                      │
        ├─────────────────────────────────────────────────┤
        │  ┌──────────────┐    ┌──────────────────────┐   │
        │  │search_flights│───▶│confirm_price_and_book│   │
        │  └──────────────┘    └──────────────────────┘   │
        │  ┌──────────────┐    ┌──────────────────────┐   │
        │  │ask_user_approval  │    state management    │   │
        │  └──────────────┘    └──────────────────────┘   │
        └─────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                                 │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────┐    ┌───────────────────────────┐   │
│  │   Mock Flight Database   │    │  In-Memory Session State  │   │
│  │   (Static JSON Data)     │    │   (agent_state dict)      │   │
│  └─────────────────────────┘    └───────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Features

- ✅ **Natural Language Understanding**: Responds to conversational flight requests
- ✅ **Flight Search Simulation**: Returns realistic flight options with prices
- ✅ **Multi-airline Results**: Shows options from different carriers
- ✅ **Price Comparison**: Displays multiple price points for informed decisions
- ✅ **Date Flexibility**: Handles various departure date formats
- ✅ **Passenger Information Collection**: Gathers names, emails, passport details
- ✅ **Booking Simulation**: Generates realistic booking references
- ✅ **User Approval Workflow**: Confirms before "committing" to bookings
- ✅ **Conversation Reset**: Clear command to start over
- ✅ **Graceful Error Handling**: Friendly responses to unexpected inputs
- ✅ **State Persistence**: Maintains context throughout conversation
- ✅ **Demo Mode**: Safe for testing without real-world consequences

---

## 🧪 Agent Workflow Phases

<details>
<summary>✅ Phase 1: Intent Recognition</summary>

**Inputs:**
- User message (natural language)
- Current conversation state

**Process:**
1. Analyze user input for keywords
2. Categorize intent (search, book, reset, help)
3. Extract potential parameters (airports, dates)

**Code Snippet:**
```python
last_user_msg = agent_state["messages"][-1]["content"].lower()

if any(w in last_user_msg for w in ["search", "find", "show flights", "cheap", "from", "to"]):
    # Handle flight search intent
    tool_call = "search_flights"
    
elif any(w in last_user_msg for w in ["book", "reserve", "purchase", "confirm", "pay"]):
    # Handle booking intent
    tool_call = "book_flight"
    
elif "clear" in last_user_msg or "reset" in last_user_msg:
    # Reset conversation
    agent_state["collected_info"] = {k: None for k in agent_state["collected_info"]}
```

**Outputs:**
- Identified intent
- Extracted parameters
- Next action to take

</details>

<details>
<summary>✅ Phase 2: Information Collection</summary>

**Inputs:**
- Current collected_info state
- User intent
- Available parameters from message

**Process:**
1. Check for missing required information
2. Prompt user for missing details
3. Validate inputs (airport codes, date formats)
4. Update state with new information

**Required Information for Search:**
- Origin airport (e.g., CAI, JFK, LHR)
- Destination airport
- Departure date (YYYY-MM-DD)
- Number of adults (optional, default=1)

**Required Information for Booking:**
- Selected flight ID
- Passenger full name
- Email address
- Passport number (simulated)

**Outputs:**
- Updated collected_info dictionary
- Ready flag (all required info present)

</details>

<details>
<summary>✅ Phase 3: Flight Search Simulation</summary>

**Inputs:**
- Origin airport
- Destination airport
- Departure date
- Number of passengers

**Process:**
```python
def search_flights(params: Dict[str, Any]) -> str:
    origin = params.get("origin", "CAI")
    destination = params.get("destination", "CDG")
    departure_date = params.get("departure_date", "2026-04-10")
    
    return json.dumps({
        "status": "success",
        "flights": [
            {
                "id": "off1",
                "price": "€ 324",
                "airline": "EGYPTAIR / Air France",
                "depart": f"{departure_date} 08:15 CAI → 11:50 CDG",
                "duration": "4h 35m direct"
            },
            {
                "id": "off2",
                "price": "€ 289",
                "airline": "Aegean + Wizz",
                "depart": f"{departure_date} 04:40 CAI → 14:20 CDG (1 stop)",
                "duration": "9h 40m"
            }
        ]
    }, indent=2)
```

**Outputs:**
- JSON string with flight options
- Each flight includes: ID, price, airline, schedule, duration
- Status indicator (success/error)

</details>

<details>
<summary>✅ Phase 4: User Approval & Action Execution</summary>

**Inputs:**
- Proposed action description
- Action parameters

**Process:**
```python
def ask_user_approval(message: str) -> bool:
    user_input = input(f"{message} (y/n): ").strip().lower()
    return user_input == "y"

# Example usage
if not ask_user_approval("Proceed with flight search?"):
    print("→ Search cancelled.")
    continue
```

**Key Approval Points:**
- Before executing flight search
- Before confirming booking
- Before any "costly" or irreversible action

**Outputs:**
- Boolean approval status
- Action proceeds only if approved

</details>

<details>
<summary>✅ Phase 5: Booking Simulation</summary>

**Inputs:**
- Selected flight ID
- Passenger information (name, email, passport)

**Process:**
```python
def confirm_price_and_book(flight_id: str, passenger_info: Dict) -> str:
    return json.dumps({
        "status": "booked",
        "booking_reference": "XYZ789",
        "flight_id": flight_id,
        "total_price": "€ 324",
        "passengers": passenger_info,
        "message": "Booking confirmed (demo mode)"
    }, indent=2)
```

**Outputs:**
- Booking confirmation with reference number
- Flight details
- Passenger information
- Demo mode disclaimer

</details>

<details>
<summary>✅ Phase 6: State Management & Reset</summary>

**Inputs:**
- Current agent_state
- Reset command detection

**Process:**
```python
# State structure
agent_state: Dict[str, Any] = {
    "messages": [],  # Conversation history
    "collected_info": {  # User-provided information
        "origin": None,
        "destination": None,
        "departure_date": None,
        "return_date": None,
        "adults": 1,
        "children": 0,
        "cabin": "ECONOMY",
        "preferred_airline": None,
        "max_price": None,
    },
    "last_search_result": None,
    "selected_flight_id": None,
    "booking_reference": None,  # Set when booking complete
}

# Reset functionality
elif "clear" in last_user_msg or "reset" in last_user_msg:
    agent_state["collected_info"] = {k: None for k in agent_state["collected_info"]}
    agent_state["last_search_result"] = None
    agent_state["selected_flight_id"] = None
    print("→ Conversation reset.")
```

**Outputs:**
- Reset state (fresh conversation)
- User notified of reset

</details>

<details>
<summary>✅ Phase 7: Conversation Completion</summary>

**Inputs:**
- Current state
- Booking confirmation status

**Process:**
```python
def is_goal_achieved(state: Dict) -> bool:
    return bool(state.get("booking_reference"))

# Success celebration
if is_goal_achieved(agent_state):
    print("\n" + "="*60)
    print("       🎉  Flight booked successfully!")
    print("       Booking reference →", agent_state.get("booking_reference"))
    print("="*60 + "\n")
```

**Outputs:**
- Success message
- Booking reference display
- Option to start new search

</details>

---

## 🧬 Conversation Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONVERSATION FLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  User: "find flights from CAI to DXB"                            │
│    ↓                                                              │
│  Agent: Asks for departure date                                   │
│    ↓                                                              │
│  User: "next Friday"                                              │
│    ↓                                                              │
│  Agent: Searches flights, shows options                           │
│    ↓                                                              │
│  User: "book the cheapest one"                                    │
│    ↓                                                              │
│  Agent: Asks for passenger details                                │
│    ↓                                                              │
│  User: Provides name, email, passport                             │
│    ↓                                                              │
│  Agent: Confirms booking, shows reference                         │
│    ↓                                                              │
│  🎉 SUCCESS!                                                      │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    STATE TRANSITIONS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  [IDLE]                                                           │
│    │                                                              │
│    ▼                                                              │
│  [COLLECTING_INFO] ←───┐                                          │
│    │                   │                                          │
│    ▼                   │                                          │
│  [SEARCHING]           │ (missing info)                          │
│    │                   │                                          │
│    ▼                   │                                          │
│  [REVIEWING_OPTIONS] ──┘                                          │
│    │                                                              │
│    ▼                                                              │
│  [COLLECTING_PASSENGER]                                           │
│    │                                                              │
│    ▼                                                              │
│  [CONFIRMING]                                                     │
│    │                                                              │
│    ▼                                                              │
│  [BOOKED] 🎉                                                      │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🗂 Directory Structure

```
ai_flight_assistant/
│
├── README.md                          # Project documentation
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore rules
│
├── src/
│   ├── __init__.py
│   ├── agent.py                        # Main agent loop
│   ├── intent_detector.py               # Intent recognition
│   ├── info_collector.py                # Information gathering
│   ├── flight_search.py                  # Mock flight search
│   ├── booking_engine.py                  # Booking simulation
│   ├── state_manager.py                  # State management
│   └── utils.py                          # Helper functions
│
├── data/
│   ├── mock_flights.json                 # Static flight data
│   ├── airports.csv                       # Airport codes
│   └── conversation_logs/                  # Session logs
│
├── tests/
│   ├── test_intent_detector.py
│   ├── test_flight_search.py
│   └── test_booking_engine.py
│
├── examples/
│   ├── sample_conversations.md
│   └── demo_screenshots/
│
├── docs/
│   ├── architecture_diagram.png
│   ├── conversation_flow.png
│   └── api_documentation.md
│
└── outputs/
    ├── booking_references.txt
    └── user_feedback.csv
```

---

## 📦 Tech Stack

| Category             | Tool/Library                | Purpose                               |
|----------------------|----------------------------|---------------------------------------|
| **Language**         | Python 3.8+                 | Core agent logic                      |
| **Standard Library** | json, os, subprocess        | Data handling, system operations      |
| **User Interface**   | Command Line (input/print)  | Simple interaction                     |
| **Data Format**      | JSON                        | Structured data exchange               |
| **State Management** | Python Dictionary           | In-memory conversation tracking        |
| **Testing**          | unittest / pytest           | Function validation                    |
| **Version Control**  | Git + GitHub                | Code management                        |
| **Documentation**    | Markdown                    | Project documentation                  |

**Core Dependencies:**
```txt
# No external dependencies required!
# Uses only Python standard library
```

---

## 🤖 Agent Design Principles

### **1. Simplicity First**
- Minimal external dependencies
- Easy to understand and modify
- Clear, readable code structure

### **2. Safety Through Approval**
- User must confirm all actions
- No automatic "purchases"
- Clear demo mode indicators

### **3. Stateful Conversation**
- Maintains context across turns
- Remembers user preferences
- Progressive information gathering

### **4. Graceful Degradation**
- Friendly error messages
- Help prompts for unclear input
- Reset capability for confusion

### **5. Realistic Simulation**
- Believable flight options
- Realistic pricing
- Authentic booking process feel

### **6. Extensibility**
- Easy to add real API integration
- Modular function design
- Clear separation of concerns

### **7. Educational Value**
- Demonstrates AI agent patterns
- Shows tool-use architecture
- Illustrates state management

---

## 🗓 Roadmap

| Phase | Description | Start Date | End Date | Status |
|-------|-------------|------------|----------|--------|
| ✅ 1 | Core Agent Loop Design | 2026-03-10 | 2026-03-11 | ✅ Done |
| ✅ 2 | Intent Recognition Implementation | 2026-03-11 | 2026-03-12 | ✅ Done |
| ✅ 3 | Information Collection System | 2026-03-12 | 2026-03-13 | ✅ Done |
| ✅ 4 | Flight Search Simulation | 2026-03-13 | 2026-03-14 | ✅ Done |
| ✅ 5 | Booking Engine Development | 2026-03-14 | 2026-03-15 | ✅ Done |
| ✅ 6 | User Approval Workflow | 2026-03-15 | 2026-03-15 | ✅ Done |
| ✅ 7 | State Management & Reset | 2026-03-15 | 2026-03-16 | ✅ Done |
| ✅ 8 | Documentation & Finalization | 2026-03-16 | 2026-03-16 | ✅ Done |
| 🔄 9 | Real API Integration (Future) | TBD | TBD | 📅 Planned |
| 🔄 10 | Web Interface (Future) | TBD | TBD | 📅 Planned |

---

## 🧾 License

No license has been selected for this project yet.
All rights reserved — you may not use, copy, modify, or distribute this code without explicit permission from the author.

---

## 👨‍💻 Author

**Manar Altyp**  
*AI Engineer • Python Developer • Conversational AI Enthusiast*

🌐 [GitHub](https://github.com/manar-Lang) 

*Project completed for: AI Flight Assistant – Smart Travel Booking Agent*  
*Completion Date: March 16, 2026*

---

## 📬 Future Improvements

- **Real API Integration**
  - Connect to actual flight APIs (Amadeus, Skyscanner, Google Flights)
  - Implement live pricing and availability
  - Add airline preference filtering

- **Enhanced NLP**
  - Integrate with actual LLM (GPT, Claude, Llama)
  - Improve intent recognition accuracy
  - Handle complex multi-intent queries

- **Web Interface**
  - Build React/Vue frontend
  - Add voice input capability
  - Create mobile-responsive design

- **Database Integration**
  - Store user profiles and preferences
  - Save booking history
  - Implement user authentication

- **Advanced Features**
  - Round-trip and multi-city booking
  - Hotel and car rental integration
  - Price alerts and monitoring
  - Seat selection simulation

- **Production Readiness**
  - Add comprehensive logging
  - Implement error tracking
  - Create monitoring dashboard
  - Add unit and integration tests

- **Multi-language Support**
  - Interface in multiple languages
  - Handle international date formats
  - Support various currency displays

---

## 🙋‍♂️ Contributing

Contributions are welcome! This is an educational project, and improvements are appreciated. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows PEP 8 guidelines and includes appropriate documentation.

---

## 📞 Contact

For questions, suggestions, or feedback about this project:

**Manar Altyp**
📧 Email: manaraltyp44444@gmail.com
🐙 GitHub: [Manar Altyp](https://github.com/manar-Lang)


---

## 📋 Sample Conversation

```
How can I help you today?
> find flights from CAI to DXB

[Step 1]
→ Destination airport code? DXB
→ Departure date (YYYY-MM-DD)? 2026-04-15
→ Proceed with flight search? (y/n): y

Search result:
{
  "status": "success",
  "flights": [
    {
      "id": "off1",
      "price": "€ 324",
      "airline": "EGYPTAIR / Air France",
      "depart": "2026-04-15 08:15 CAI → 11:50 DXB",
      "duration": "4h 35m direct"
    },
    {
      "id": "off2",
      "price": "€ 289",
      "airline": "Aegean + Wizz",
      "depart": "2026-04-15 04:40 CAI → 14:20 DXB (1 stop)",
      "duration": "9h 40m"
    }
  ]
}

> book the cheapest one

[Step 2]
→ Enter flight ID to book (e.g. off1): off2
→ Passenger full name: Manar Altyp
→ Email: manaraltyp44444@gmail.com
→ Passport number (demo): A12345678
→ CONFIRM BOOKING (this is a real action in production!) (y/n): y

Booking result:
{
  "status": "booked",
  "booking_reference": "XYZ789",
  "flight_id": "off2",
  "total_price": "€ 289",
  "passengers": {
    "name": "Manar Altyp",
    "email": "manaraltyp44444@gmail.com",
    "passport": "A12345678"
  },
  "message": "Booking confirmed (demo mode)"
}

============================================================
       🎉  Flight booked successfully!
       Booking reference → XYZ789
============================================================
```

---

## 🎯 Key Takeaways

This project demonstrates:

1. **Conversational AI Architecture**: How to build stateful, interactive agents
2. **Tool-Use Pattern**: Integrating functions with conversational flow
3. **Safety by Design**: User approval for important actions
4. **State Management**: Maintaining context across conversation turns
5. **Extensibility**: Easy to enhance with real APIs and LLMs
6. **Educational Value**: Perfect for learning AI agent development

---

*Last Updated: March 16, 2026*
