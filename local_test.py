import requests
import base64

# Base URL of your FastAPI application
URL = "http://127.0.0.1:8000"  # My port is 8000


# Function to save the generated chart locally
def save_chart(chart_base64, file_name):
    try:
        # Decode Base64 string
        chart_binary = base64.b64decode(chart_base64)
        # Save image as a file
        with open(file_name, "wb") as file:
            file.write(chart_binary)
        print(f"Chart saved as '{file_name}'")
    except Exception as e:
        print(f"Error saving chart: {e}")


# Test Cases
# We'll use requests to send post requests to our local instance.
def test_pie_chart():
    print("\nTesting Pie Chart...")
    # This is an example of monthly spend
    payload = {
        "chart_type": "pie",
        "data": [800, 300, 150, 100, 50],
        "labels": ["Rent", "Groceries", "Transportation", "Entertainment", "Miscellaneous"],
        "title": "Monthly Spending Breakdown"
    }

    response = requests.post(f"{URL}/generate-chart", json=payload)
    if response.status_code == 200:
        save_chart(response.json()["chart"], "example_images/pie_chart.png")
    else:
        print(f"Error: {response.status_code}, {response.json()}")


def test_line_chart():
    print("\nTesting Line Chart...")
    # This is an example of investment growth over time
    payload = {
        "chart_type": "line",
        "data": [1000, 1500, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 10000, 11000, 12000],
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "title": "Investment Growth Over 2024"
    }

    response = requests.post(f"{URL}/generate-chart", json=payload)
    if response.status_code == 200:
        save_chart(response.json()["chart"], "example_images/line_chart.png")
    else:
        print(f"Error: {response.status_code}, {response.json()}")


def test_bar_chart():
    print("\nTesting Bar Chart...")
    # This is an example of daily revenue
    payload = {
        "chart_type": "bar",
        "data": [500, 300, 200, 100, 50],
        "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "title": "Daily Revenue for the Week"
    }

    response = requests.post(f"{URL}/generate-chart", json=payload)
    if response.status_code == 200:
        save_chart(response.json()["chart"], "example_images/bar_chart.png")
    else:
        print(f"Error: {response.status_code}, {response.json()}")


# Run Tests
if __name__ == "__main__":
    test_pie_chart()
    test_line_chart()
    test_bar_chart()
