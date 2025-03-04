import streamlit as st
import math

def main():
    st.set_page_config(page_title="Universal Unit Converter", page_icon="🔄")
    
    st.title("Universal Unit Converter")
    st.write("Convert between different units across various categories")
    
    # Categories and their units
    categories = {
        "Length": {
            "Meter": 1.0,
            "Kilometer": 1000.0,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254
        },
        "Weight/Mass": {
            "Kilogram": 1.0,
            "Gram": 0.001,
            "Milligram": 0.000001,
            "Metric Ton": 1000.0,
            "Pound": 0.453592,
            "Ounce": 0.0283495,
            "Stone": 6.35029
        },
        "Temperature": {
            "Celsius": "C",
            "Fahrenheit": "F",
            "Kelvin": "K"
        },
        "Area": {
            "Square Meter": 1.0,
            "Square Kilometer": 1000000.0,
            "Square Centimeter": 0.0001,
            "Square Millimeter": 0.000001,
            "Square Mile": 2590000.0,
            "Square Yard": 0.836127,
            "Square Foot": 0.092903,
            "Square Inch": 0.00064516,
            "Acre": 4046.86,
            "Hectare": 10000.0
        },
        "Volume": {
            "Cubic Meter": 1.0,
            "Cubic Centimeter": 0.000001,
            "Liter": 0.001,
            "Milliliter": 0.000001,
            "Gallon (US)": 0.00378541,
            "Quart (US)": 0.000946353,
            "Pint (US)": 0.000473176,
            "Cup (US)": 0.000236588,
            "Fluid Ounce (US)": 0.0000295735,
            "Cubic Inch": 0.0000163871,
            "Cubic Foot": 0.0283168
        },
        "Time": {
            "Second": 1.0,
            "Millisecond": 0.001,
            "Microsecond": 0.000001,
            "Nanosecond": 1e-9,
            "Minute": 60.0,
            "Hour": 3600.0,
            "Day": 86400.0,
            "Week": 604800.0,
            "Month (30 days)": 2592000.0,
            "Year (365 days)": 31536000.0
        },
        "Speed": {
            "Meter per second": 1.0,
            "Kilometer per hour": 0.277778,
            "Mile per hour": 0.44704,
            "Knot": 0.514444,
            "Foot per second": 0.3048
        },
        "Pressure": {
            "Pascal": 1.0,
            "Kilopascal": 1000.0,
            "Bar": 100000.0,
            "PSI": 6894.76,
            "Atmosphere": 101325.0,
            "Torr": 133.322
        },
        "Energy": {
            "Joule": 1.0,
            "Kilojoule": 1000.0,
            "Calorie": 4.184,
            "Kilocalorie": 4184.0,
            "Watt-hour": 3600.0,
            "Kilowatt-hour": 3600000.0,
            "Electronvolt": 1.602176634e-19,
            "British Thermal Unit": 1055.06
        },
        "Data": {
            "Bit": 1.0,
            "Byte": 8.0,
            "Kilobit": 1000.0,
            "Kilobyte": 8000.0,
            "Megabit": 1000000.0,
            "Megabyte": 8000000.0,
            "Gigabit": 1000000000.0,
            "Gigabyte": 8000000000.0,
            "Terabit": 1000000000000.0,
            "Terabyte": 8000000000000.0
        }
    }
    
    # Sidebar for category selection
    category = st.sidebar.selectbox("Select Category", list(categories.keys()))
    
    # Main area for conversion
    st.header(f"{category} Conversion")
    
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From", list(categories[category].keys()), key="from")
        from_value = st.number_input("Value", value=1.0, key="from_value")
    
    with col2:
        to_unit = st.selectbox("To", list(categories[category].keys()), key="to")
        
    # Perform conversion
    if st.button("Convert"):
        result = convert(from_value, from_unit, to_unit, category, categories)
        st.success(f"{from_value} {from_unit} = {result} {to_unit}")
        
    # Add a conversion table for quick reference
    if st.checkbox("Show Conversion Table"):
        if from_unit:
            st.subheader(f"Conversion Table for 1 {from_unit}")
            data = []
            for unit in categories[category].keys():
                if unit != from_unit:
                    converted_value = convert(1.0, from_unit, unit, category, categories)
                    data.append({"Unit": unit, "Value": converted_value})
            
            if data:
                st.table(data)

def convert(value, from_unit, to_unit, category, categories):
    # Special case for temperature
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    # For other categories, use the conversion factors
    from_factor = categories[category][from_unit]
    to_factor = categories[category][to_unit]
    
    # Convert to base unit then to target unit
    base_value = value * from_factor
    result = base_value / to_factor
    
    return round(result, 10)

def convert_temperature(value, from_unit, to_unit):
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:  # Already Celsius
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        result = celsius * 9/5 + 32
    elif to_unit == "Kelvin":
        result = celsius + 273.15
    else:  # Target is Celsius
        result = celsius
    
    return round(result, 4)

if __name__ == "__main__":
    main()