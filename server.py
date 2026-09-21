from importlib import import_module

FastMCP = import_module("fastmcp").FastMCP

mcp = FastMCP("Brand New Utilities Server")

@mcp.tool()
def convert_units(value: float, from_unit: str, to_unit: str) -> str:
    """Convert basic units like km to miles or celius to fahrenheit."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == "km" and to_unit == "miles":
        result = value * 0.621371
        return f"{value} km is equal to {result:.2f} miles."
    elif from_unit == "miles" and to_unit == "km":
        result = value * 1.60934
        return f"{value} miles is equal to {result:.2f} km."
    elif from_unit == "c" and to_unit == "f":
        result = (value * 9/5) + 32
        return f"{value}°C is equal to {result:.2f}°F."
    elif from_unit == "f" and to_unit == "c":
        result = (value - 32) * 5/9
        return f"{value}°F is equal to {result:.2f}°C."

    return f"Unsupported conversion from {from_unit} to {to_unit}."

@mcp.tool()
def analyze_text(text: str) -> str:
    """Perform a quick structural analysis of input text (word count, char count, vowels)."""
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    vowels = sum(1 for char in text.lower() if char in "aeiou")

    return (f"Text Analysis Results:\n"
            f"- Words: {word_count}\n"
            f"- Characters: {char_count}\n"
            f"- Vowels: {vowels}")

if __name__ == "__main__":
    mcp.run()