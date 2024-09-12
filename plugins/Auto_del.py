import asyncio

def job():
    delete_old_files(DIRECTORY, FILE_LIFETIME_DAYS)

asyncio.every().day.at("01:00").do(job)

while True:
    asyncio.run_pending()
    time.sleep(60)  
    
