# CS361-FinlayMS
Finlay's Graphs and Charts MS

## Prerequisites
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Ensure Docker is running (`docker --version` to confirm).
   #### I'm using the AMD download, I dont think it matters.

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chart-service
   ```
## Verification 

Verify Files: Ensure the following files exist in the repository:

1. charts.py (contains the charts microservice)
2. requirements.txt (Relevant Python dependencies for microservice)
3. Dockerfile (Docker configuration)

## Build Docker Image:
#### Can be done in bash
   docker build -t chart-service .
## Run the Docker Container:
   docker run -p {PORT}:{PORT} chart-service

# Example Request
   ```
   {
       "chart_type": "bar",
       "data": [10, 20, 30, 40],
       "labels": ["Q1", "Q2", "Q3", "Q4"],
       "title": "Quarterly Sales"
   }
   ```
# Example Response
   #### Successful Response
   ```
   {
       "chart": "iVBORw0KGgoAAAANSUhEUgAAB4AAAAQACAIAAAB..."
   }
   ```
   The "chart" field contains a Base64-encoded string representing the generated chart image.

# Testing Locally

All testing was performed in Postman, which is free for lightweight requests. 
   ```
   {
       "chart_type": "bar",
       "data": [10, 20, 30, 40],
       "labels": ["Q1", "Q2", "Q3", "Q4"],
       "title": "Quarterly Sales"
   }
   ```
## Example cURL Command:
   ```
   curl -X POST "http://127.0.0.1:{PORT}/generate-chart" \
   -H "Content-Type: application/json" \
   -d '{
       "chart_type": "bar",
       "data": [10, 20, 30, 40],
       "labels": ["Q1", "Q2", "Q3", "Q4"],
       "title": "Quarterly Sales"
   }'
   ```
## Decoding Response:
The response will include a Base64-encoded image:
   '''
   {
       "chart": "iVBORw0KGgoAAAANSUhEUgAAB4AAAAQACAIAAAB..."
   }
   '''
### Decode the Base64 string using an online tool like Base64 Image Decoder or render it in HTML:

   <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAB4AAAAQACAIAAAB..." />

