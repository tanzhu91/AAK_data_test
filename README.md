# AAK_data_test

To access the project type in a terminal in the same folder as main.py the file "uvicorn main:app --reload"
You will get a message  saying application startup is complete.


After that you can visit http://127.0.0.1:8000 to see the main dashboard, which plots the data.

![Screenshot 2025-05-08 at 00-10-07 World Metrics Dashboard](https://github.com/user-attachments/assets/ebbc67d7-ea21-4b3f-a311-47c1850bad87)

You can select the different metrics and years to see top 10 and bottom 10 countries in a period between 2000-2023.

You can also select the specific data only, without the visualizations at http://127.0.0.1:8000/data?year=2020 by specifying the year at the end each time.

Selecting http://127.0.0.1:8000/data goes by default to 2024 but data is still incomplete and mostly null for that year.
