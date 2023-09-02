from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Constants
SOLAR_PANEL_EFFICIENCY = 0.15
COST_PER_UNIT_CURRENT_INR = 75000
WATT_PER_SQUARE_METER = 150
GRID_EMISSIONS_FACTOR = 0.6  # CO2 emissions factor for grid electricity (example value)
CO2_ABSORBED_PER_TREE_PER_YEAR = 22.6  # Example value, CO2 absorbed by one tree per year in kg

class SolarEnergyCalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.units_label = Label(text="Enter monthly electricity consumption (units of current):")
        self.units_entry = TextInput(hint_text="Units of current", multiline=False)
        self.sunlight_label = Label(text="Enter sunlight hours per day:")
        self.sunlight_entry = TextInput(hint_text="Sunlight hours per day", multiline=False)
        self.calculate_button = Button(text="Calculate")
        self.calculate_button.bind(on_press=self.calculate_solar_energy)
        self.result_label = Label(text="", size_hint_y=None, height=300)
        
        self.layout.add_widget(self.units_label)
        self.layout.add_widget(self.units_entry)
        self.layout.add_widget(self.sunlight_label)
        self.layout.add_widget(self.sunlight_entry)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)
        
        return self.layout

    def calculate_solar_energy(self, instance):
        try:
            current_units = float(self.units_entry.text)
            sunlight_hours_per_day = float(self.sunlight_entry.text)

            # Calculate the area required in sqft
            area_required_sqft = (current_units * 1000) / (WATT_PER_SQUARE_METER * SOLAR_PANEL_EFFICIENCY)

            total_cost_inr = current_units * COST_PER_UNIT_CURRENT_INR / 1000

            # Battery storage calculation
            battery_storage_kWh = current_units  # 1 unit of current = 1 kWh of battery storage

            # Solar panels calculation
            solar_panels_kW = area_required_sqft / 100  # Assuming 100 sqft per kW

            electric_bill = 0
            if current_units < 200:
                electric_bill = current_units * 1.49
            else:
                electric_bill = current_units * 2
            
            bill_reduction = electric_bill * 90 / 100

            solar_energy_production = area_required_sqft * sunlight_hours_per_day * SOLAR_PANEL_EFFICIENCY

            co2_reduction = solar_energy_production * GRID_EMISSIONS_FACTOR

            trees_saved = co2_reduction / CO2_ABSORBED_PER_TREE_PER_YEAR

            result_text = f"Estimated Area Required: {area_required_sqft:.2f} square feet\n" \
                         f"Total Cost of Solar Panels: ₹{total_cost_inr:.2f}\n" \
                         f"Battery Storage Required: {battery_storage_kWh:.2f} kWh\n" \
                         f"Solar Panels Required: {solar_panels_kW:.2f} kW\n" \
                         f"Estimated Monthly Electric Bill Reduction: ₹{bill_reduction:.2f}\n" \
                         f"Solar Energy Production per Day: {solar_energy_production:.2f} kWh\n" \
                         f"Estimated CO2 Emissions Reduction per Day: {co2_reduction:.2f} kg\n" \
                         f"Estimated Number of Trees Saved per Day: {trees_saved:.2f} trees"
            self.result_label.text = result_text
        except ValueError:
            pass

if __name__ == '__main__':
    SolarEnergyCalculatorApp().run()
