import schedule

def job():
    delete_old_files(DIRECTORY, FILE_LIFETIME_DAYS)

schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  
    
