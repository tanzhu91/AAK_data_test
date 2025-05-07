# AAK_data_test

## **Overview of the project**
This project uses FastApi to scrape data related to countries from  the official world bank API "http://api.worldbank.org/v2". Then the data is parsed through and html.index file and visualizations of certain metrics are created.

## **How to access**

You need to pip install fastpi , httpx, asyncio , or any other missing package in a terminal before cloning the repo. After cloning the repository to your local device, to access the project type in a terminal in the same folder as the main.py file "uvicorn main:app --reload".
You will get a message saying application startup is complete at the end if all runs smoothly.


After that you can visit http://127.0.0.1:8000 to see the main dashboard, which plots the data.

![Screenshot 2025-05-08 at 00-10-07 World Metrics Dashboard](https://github.com/user-attachments/assets/ebbc67d7-ea21-4b3f-a311-47c1850bad87)

You can select the different metrics and years to see top 10 and bottom 10 countries in a period between 2000-2023.

You can also select the specific data only, without the visualizations at http://127.0.0.1:8000/data?year=2020 by specifying the year at the end each time.

Selecting http://127.0.0.1:8000/data goes by default to 2024 but data is still incomplete and mostly null for that year.
