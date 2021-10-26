"""
Yksinkertainen GRON job
"""

from datetime import datetime


def do_the_job():
    try:
        with open("timestamp.txt", "a") as file_open:
            timenow = datetime.now()
            str_time = timenow.strftime("%d-%m-%Y, %H:%M:%S")
            
            file_open.write(f"Timestamp made by GRON: {str_time}\n")

    except OSError:
        print("File not found.")

if __name__ == "__main__":
    do_the_job()