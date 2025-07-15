# 🌞 Solar Energy Calculator

A cross-platform **Solar Energy Calculator** built during my first year of engineering. Available as both Windows EXE and Android APK, this tool estimates your solar power needs, system cost, bill savings, and environmental impact based on your electricity usage and sunlight availability.

---

## 🚀 Features

- Input **monthly electricity consumption** (in units of current).
- Calculate:
  - Required **solar panel count** and **minimum rooftop area**.
  - **Total system cost** including panels, installation, inverter, GST/utility charges.
  - Monthly **bill reduction** and **extra income** from surplus generation.
  - **Daily solar energy production**, **CO₂ emissions reduction**, and **equivalent trees saved**.

---

## 📸 Sample Outputs

- **Monthly usage**: 456 units → **10 panels**, ~500 ft².
- **Total cost**: ₹376,000 (₹150,000 for panels + other charges).
- **Monthly savings**: ₹4,531 → **zero electricity bill**.
- **Extra income**: ₹648/month (600 kWh surplus).
- **With 6 sunlight hours/day**:
  - Daily energy: ~450 kWh
  - CO₂ reduced: ~270 kg/day
  - Trees equivalent: ~12 per day

---

installation: email thereason you want to use this app or windows exe and will be sent a package for testing as it is still a developing product.

---

## 🧠 How It Works

1. **Input** monthly units.
2. **Enter** sunlight hours/day.
3. Behind the scenes, the app:
   - Converts units to kWh/day.
   - Estimates panel count (assumes standard panel specs).
   - Calculates costs (panels, installation, inverter, 12% GST + utility charges).
   - Computes monthly generation & savings (@ assumed ₹/unit rate).
   - Estimates CO₂ offset and tree-equivalent savings.

---

## ⚙️ Dependencies & Technologies
GUI: tkinter and kivy used
- Packaging:
  - **Windows**: Inno Setup / PyInstaller (for EXE)
  - **Android**: Android Studio / Gradle
- Currency: INR
- GST & utility charges: 12% + BESCOM (example utility)
- Environment factors: CO₂ offset & tree savings based on industry-standard conversion rates
- Panel specs: assumed fixed; user provides sunlight hours

---

## 🎯 Usage Guide

1. Run the app.
2. Input monthly usage (e.g., `456` units).
3. Click **Calculate**.
4. View system size, cost, and savings.
5. Click **Next**.
6. Enter sunlight hours/day (e.g., `6`).
7. View daily energy, CO₂ savings, and tree equivalents.

---

## 📊 Sample Output

| Input (units/mo) | Sunlight (hrs) | Panels | Area (ft²) | Cost (₹) | Savings/mo (₹) | Extra Income (₹) | kWh/day | CO₂/day (kg) | Trees/day |
|------------------|----------------|--------|------------|----------|----------------|------------------|---------|----------------|-----------|
| 456              | 6              | 10     | 500        | 3,76,000 | 4,531          | 648              | 450     | 270            | 11.95     |

---

## 🌱 Environmental Estimations

- CO₂ reduction is calculated using a factor (e.g., ~0.6 kg CO₂ per kWh) aligning with U.S. and global averages.
- Tree savings estimated at ~0.012 trees per kWh generated :contentReference[oaicite:1]{index=1}.

---

## 🔭 Roadmap & Future Enhancements

- User-defined panel specs and unit rates
- Support for macOS/Linux
- Exportable reports (CSV/PDF)
- Integration with geo-sunlight APIs for location-based estimates
- More accurate CO₂ factors based on local grid data

---

## 📜 License & Contact

- **License**: MIT  
- **Author**: Rocky Harsha  
- **Contact**: [YourEmail@example.com](mailto:YourEmail@example.com) or [GitHub Profile](https://github.com/Rockyharsha)

---

## ⚠️ Disclaimer

- **Estimation tool only** — consult a qualified solar provider for installation.
- All outputs rely on assumed values and user inputs.
- Sunlight hours should be entered accurately for reliable estimations.

---

## 👍 Quick Start

1. Download the EXE or APK.
2. Install and open.
3. Enter your monthly units → **Calculate**.
4. Enter sunlight hours → **Calculate Solar Energy Production**.
5. Review results.

---
## 📸 Sample Outputs

### 1. Input: Monthly Electricity Usage: *Here you enter, for example, 456 units/month.*
<img width="1920" height="1017" alt="Solar Energy Calculator 10_12_2023 9_48_33 PM (1)" src="https://github.com/user-attachments/assets/0286cb70-b546-4e74-bbf0-612e470824fb" />

### 2. Initial Results (Panels, Cost, Monthly Savings): *Displays area required, panel count, cost breakdown, bill savings, and extra income.*
<img width="1920" height="1017" alt="Solar Energy Calculator 9_3_2023 10_23_07 PM" src="https://github.com/user-attachments/assets/ec0fc35b-23ed-408d-8951-b78615492943" />

### 3. Input: Sunlight Hours per Day: *You input sunlight hours (e.g., 6 hrs/day).*
### 4. Environmental Impact Results: *Shows daily energy production, CO₂ savings, and trees-equivalent per day.*
<img width="1920" height="1017" alt="Solar Energy Calculator 9_3_2023 10_23_15 PM" src="https://github.com/user-attachments/assets/45977d9e-0c5a-4fe0-a9ad-1f281e85360c" />

### 5. ANDROID APK: output
![mobile output look apk file of app ](https://github.com/user-attachments/assets/7414927c-f7c3-480a-ba74-55a80176c892)

Thanks for trying out this Solar Energy Calculator! Feel free to suggest features or improvements!
