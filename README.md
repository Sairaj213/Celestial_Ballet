# 🌌 **`Project`: _Celestial Ballet_** 
<div align="center">
  
### ✨ `Three-Body Simulation`: **“The project uses `SymPy` and `PyDy` Liberies of Python.”** <br>



</div>

<br>



<br>

<img src="./assets/main.png" width="70%" align="right" style="border-radius: 29px; margin-left: 20px;">

> 🚀 **Project provides a `minutely, interactive simulation environment` for exploring the `three-body problem` under mutual gravitational attraction.**

>🌍 **_Simulator_ has a powerful _symbolic-to-numeric workflow_, It uses `SymPy` library to mathematically derive the exact differential equations of motion from `first principles`.**

>⚙️ **These symbolic expressions are then converted into _optimized NumPy functions_ that are solved over time using high-performance ordinary differential equation integrators from `SciPy`.** 


---

<br>

<div align="left">

# 🗂️ Project Structure

<br>

</div>

```markdown-tree
📁 three_body_lab/
├── main.py                         # Application entry point (runs the Streamlit app)
├── config.yaml                     # Central configuration for UI and simulation defaults
├── requirements.txt                # List of Python dependencies for pip
└── README.md                       # Project documentation and setup guide
|
├── 📁 core/                         # --- Core Simulation & Physics Logic ---
│   ├── symbolic_setup.py           # Defines the system symbolically (masses, positions)
│   ├── equations_builder.py        # Derives the equations of motion using SymPy
│   ├── system_converter.py         # Converts 2nd-order ODEs to a 1st-order system
│   ├── numeric_engine.py           # Creates the fast numeric solver function
│   ├── state_manager.py            # Handles saving/loading of simulation presets (JSON)
│   ├── chaos_tools.py              # Provides functions for chaotic analysis (e.g., perturbation)
│   └── data_logger.py              # Configures and provides the application logger
│
├── 📁 ui/                           # --- Streamlit User Interface Layer ---
│   ├── dashboard.py                # Main layout controller; assembles all tabs
│   ├── sidebar_controls.py         # Renders the sidebar with all user controls
│   ├── tab_simulation.py           # Renders the live 3D visualization and metrics
│   ├── tab_equations.py            # Renders the symbolic LaTeX equations
│   ├── tab_diagnostics.py          # Renders solver performance and logs
│   ├── tab_analysis.py             # Renders energy/CoM plots and data export
│   ├── tab_comparison.py           # Renders the side-by-side chaos experiment
│   ├── tab_aesthetic.py            # Renders UI customization controls
│   └── tab_educational.py          # Renders the help and physics explanation text
│   │
│   └── 📁 components/               # --- Reusable UI Widgets ---
│       ├── live_metrics.py         # The real-time telemetry HUD
│       ├── equations_viewer.py     # The expandable LaTeX equation display
│       └── parameter_sliders.py    # The mass/position/velocity input widgets
│
├── 📁 utils/                        # --- General Helper Functions ---
│   ├── latex_utils.py              # Formats SymPy equations into LaTeX strings
│   ├── visualization_tools.py      # Contains Plotly functions for 3D and energy plots
│   ├── performance_monitor.py      # Provides the @performance_timer decorator
│   ├── config_loader.py            # Loads and parses the main config.yaml
│   └── math_utils.py               # Contains physics helper functions (e.g., CoM)
│
├── 📁 tests/                        # --- Unit & Integration Tests ---
│   ├── test_symbolic.py            # Validates the symbolic setup and derivation
│   ├── test_numeric.py             # Validates the numeric engine and ODE conversion
│   ├── test_state_manager.py       # Validates the saving/loading of presets
│   ├── test_ui_sync.py             # Validates the data contracts between UI modules
│   └── test_data_integrity.py      # Validates the math and visualization helper functions
│
├── 📁 data/                         # --- Stored Simulation Data ---
│   ├── 📁 presets/                  # --- Ready-to-load initial setups ---
│   │   └── figure_eight.json
│   └── 📁 logs/                     # (Created at runtime to store diagnostic logs)
│
└── 📁 assets/                       # --- Visual & Style Assets (Optional) ---
```

<br>


<div align="left">

# ⚙️ **Customization / Parameters**


</div>

---

<div align="left"; style="display: flex; align-items: flex-start; justify-content: space-between; gap: 30px; flex-wrap: wrap;">

  <!-- LEFT SIDE -->
  <div style="flex: 1; min-width: 320px;">

  <h3>🌌 <b>Physical Parameters</b></h3>

  <ul>
    <li><b>Preset Scenarios</b> — Instantly load well-known configurations like the stable <code>figure_eight.json</code> orbit.</li>
    <li><b>Body Masses</b> — Individually define the mass for each of the three celestial bodies (m₁, m₂, m₃).</li>
    <li><b>Initial State Vector</b> — Precisely set the starting 3D coordinates and velocity vectors for each body.</li>
    <li><b>Simulation Duration</b> — Control the total time the simulation runs, defining the length of the trajectory.</li>
    <li><b>Time Steps</b> — Adjust the number of integration points, trading resolution for computational speed.</li>
  </ul>

  <h3>🎨 <b>Aesthetic Controls</b></h3>

  <ul>
    <li><b>Body Colors</b> — Assign a unique color to each body for clear visual tracking in the 3D plot.</li>
    <li><b>Trail Length / Persistence</b> — Adjust the percentage of the past trajectory that remains visible on screen.</li>
    <li><b>Camera Mode</b> — Select the 3D camera behavior: <code>Static</code>, <code>Auto-Rotate</code>, or <code>Follow Body</code>.</li>
    <li><b>Velocity Vectors</b> — Toggle the display of vector arrows on each body to visualize their current momentum.</li>
  </ul>

</div>
</div>

---

<div style="text-align: center;">

### 🔬 **Analytical & Experimental Settings**

| Parameter | Description | Location |
|:------------|:--------------|:----------------|
| `Perturbation Magnitude` | Scalar size of the ε-perturbation for the chaos experiment. | `Chaos Lab Controls` |
| `Energy Analysis Plot` | Displays real-time energy conservation and drift analysis. | `Analytical Insights` |
| `Center of Mass Analysis` | Plots the velocity of the system's CoM to verify stability. | `Analytical Insights` |
| `Data Export` | Allows downloading the full simulation trajectory data. | `Analytical Insights` |
| `Log File Viewer` | Displays the raw, timestamped event log from the engine. | `System Diagnostics` |

</div>

---


<br>


---

<div align="left">

# 🚀 Getting Started


</div>

---

### **📋 1. Prerequisites**

Before you begin, ensure you have the following essential tools installed on your system.

*   **Python 3.8+**: The core programming language.
*   **Git**: For cloning the repository.
*   `pip` and `venv`: Standard Python package and environment managers.

---

### **⚙️ 2. Installation & Setup**

This step-by-step guide will set up the entire project environment. Open your terminal or command prompt and execute the following commands.

**1. Clone the Repository**  
First, clone this repository to your local machine.

```bash
git clone https://github.com/Sairaj213/Celestial_Ballet.git
```

**2. Navigate to the Project Directory**  
Change into the newly created folder.

```bash
cd three_body_lab
```

**3. Create and Activate a Virtual Environment**  
This is a crucial best practice that isolates the project's dependencies from your system-wide Python installation.

*   **On Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
*   **On macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *(Your terminal prompt should now be prefixed with `(venv)`)*

**4. Install Required Dependencies**  
This single command reads the `requirements.txt` file and installs all necessary libraries (Streamlit, SymPy, NumPy, etc.) into your virtual environment.

```bash
pip install -r requirements.txt
```

---

### **🛰️ 3. Launch the Simulator!**

With the setup complete, you are now ready to launch the application.

```bash
streamlit run main.py
```

Your default web browser will automatically open a new tab containing the **Three-Body Interactive Lab**. The symbolic engine will initialize on the first run, and then you are free to explore the cosmos.

# 📷 Sample Images 
<img src="./assets/analytic.png" width="70%" align="center" style="border-radius: 29px; margin-left: 20px;">
<img src="./assets/aesthetic.png" width="70%" align="center" style="border-radius: 29px; margin-left: 20px;">
<img src="./assets/analytic_2.png" width="70%" align="center" style="border-radius: 29px; margin-left: 20px;">
<img src="./assets/guide.png" width="70%" align="center" style="border-radius: 29px; margin-left: 20px;">
<img src="./assets/symbolic.png" width="70%" align="center" style="border-radius: 29px; margin-left: 20px;">
<img src="./assets/system_diagnostics.png" width="70%" align="center" style="border-radius: 29px; margin-left: 20px;">
<img src="./assets/telemetry.png" width="70%" align="center" style="border-radius: 29px; margin-left: 20px;">
