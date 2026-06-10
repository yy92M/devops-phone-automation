import datetime

# Get current date and time
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define the report content
report_content = f"Automated Report Generated at: {timestamp}\nStatus: System Health Check OK"

# Write to a file
with open("daily_report.txt", "w") as f:
    f.write(report_content)

print(f"Report created: daily_report.txt at {timestamp}")
