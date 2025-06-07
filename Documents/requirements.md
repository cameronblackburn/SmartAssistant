# Requirements
(2025-06-04) *All dates are formatted YYYY-MM-DD*

## Version X
(YYYY-MM-DD)

### 1. Design Decisions

### 2. Requirements

### 2.2 Functional Requirements


### 2.2 Non-Functional Requirements


### Future Steps to Consider

---

## Version 0.02
(2025-06-05)

### 1. Design Decisions

### 2. Requirements

### 2.2 Functional Requirements

- Retrieve and utilise user's current location
- Fetch and present current weather conditions based on location
- Store and retrieve persistent user profile data (e.g. name, preferences)
- Provide a simple graphical user interface (GUI) for interaction (presenting data only)

### 2.2 Non-Functional Requirements

### Future Steps to Consider

- Code refactorisation into classes
- Implementing dependency for customisable TTS (API)
- True sanitization and tokenisation of CLI inputs

---

## Version 0.01
(2025-06-04)

### 1. Design Decisions

At this stage it is important to realise the scope and set realistic goals to avoid feature creep.
* Programming Language - Python
** This has been chosen as it is a modular language with a lot of ML and AI support, something that later iterations will be using.

* AI type - Symbolic
** At this stage it is important to get a functioning prototype in order to check feasability, I am focusing on getting the barebones down before additional functionality.

* TTS Technology - pyttsx3
** No dependencies, this will allow for early focus elsewhere.

### 2. Requirements

### 2.2 Functional Requirements

 - Accept CLI and parse basic commands
 - Recognise predefined commands such as "time", "date", "exit"
 - Give output in terms of text and TTS

### 2.2 Non-Functional Requirements

- Runs offline and needs no external dependencies or APIs
- Minimal latency in responses
- Modular design for feature addition

### 3. Future Steps to Consider

- Add online API functionality to gather information such as "weather"
- Add additional commands set and improve parsing logic
- Implement an online TTS for better quality voices

---