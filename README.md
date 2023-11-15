# FetchProject

## Project Description

FetchProject is a Python tool designed for implementing and monitoring the health of network requests. It determines the health of specific endpoints by checking their response time and status, aiming to provide real-time health monitoring for critical network services.

## Installation Instructions

To install and run FetchProject, follow these steps:

1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/your-username/FetchProject.git

2. **Navigate to the project directory:**

   ```bash
   cd FetchProject
   
3. **To run FetchProject and start monitoring endpoints:**
   
   ```bash
   python main.py

## Important Note on results 

Please be aware that the response latency observed in the FetchProject is subject to variability due to a multitude of environmental and technical factors. These include, but are not limited to, prevailing network conditions, the processing efficiency of the server, and the geographical distance between the client and server endpoints. Given the inherently dynamic nature of these factors, the latency metrics obtained during operational execution may deviate from any pre-determined or expected outcomes as outlined in the exercise. Users should therefore consider these results as indicative, reflecting real-time network and server conditions, rather than absolute measures. 

For instance, an endpoint such as `fetch.com careers page` might exhibit a HTTP response code 200 with a latency of 600 ms, categorizing it as 'DOWN' due to the latency exceeding the 500 ms threshold. However, this status is not fixed and can change in subsequent checks. In a different scenario, its latency might be 300 ms, resulting in an 'UP' status and a higher availability percentage for fetch.com. This illustrates that the designation of 'DOWN' or 'UP' for an endpoint is conditional and can vary based on real-time network performance and server response.





