from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import matplotlib.pyplot as plt
import io
import base64

# Initializing App
app = FastAPI()


# Basic Pydantic Instance to ensure data integrity
# Use it at my job all the time, in LOVE with this package
# It also keeps me up at night.
class ChartRequest(BaseModel):
    chart_type: str
    data: list[float]
    labels: list[str]
    title: str


@app.post("/generate-chart")
def generate_chart(request: ChartRequest):
    # Validate input
    if request.chart_type not in ["bar", "line", "pie"]:
        raise HTTPException(status_code=400, detail="Invalid chart type")

    # Generate a chart
    plt.figure(figsize=(10, 8))
    if request.chart_type == "bar":
        plt.bar(request.labels, request.data)
    elif request.chart_type == "line":
        plt.plot(request.labels, request.data)
    elif request.chart_type == "pie":
        plt.pie(request.data, labels=request.labels, autopct='%1.1f%%')

    # Adding title
    plt.title(request.title)

    # Saving chart to memory
    buf = io.BytesIO()
    plt.savefig(buf, format="png")  # Requested Format by Finlay
    buf.seek(0)
    encoded_chart = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()
    plt.close()

    return {"chart": encoded_chart}
