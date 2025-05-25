import gzip
import shutil
import os
from datetime import datetime, timedelta

# Get date range input
start_date_str = input("Enter start date (YYYY-MM-DD): ")
end_date_str = input("Enter end date (YYYY-MM-DD): ")

start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# Loop over date range
current_date = start_date
while current_date <= end_date:
    # Format date parts
    date_str = current_date.strftime("%Y%m%d")      # For original file
    new_name = current_date.strftime("%Y-%m-%d")     # For renamed .csv

    # Define filenames
    gz_filename = [f"G244066_{date_str}_0000.csv.gz", f"G244066_{date_str}_0000_bis.csv.gz"]
    csv_filename = [f"G244066_{date_str}_0000.csv", f"G244066_{date_str}_0000_bis.csv"]
    renamed_csv = [f"IITB_AWS_{new_name}_1m.csv",f"IITB_AWS_{new_name}_1hr.csv"] 

    # Check,extract and rename file
    for i in [0,1]:
        if os.path.exists(gz_filename[i]):
            print(f"Processing: {gz_filename[i]}")
            with gzip.open(gz_filename[i], 'rb') as f_in:
                with open(csv_filename[i], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.rename(csv_filename[i], renamed_csv[i])
            print(f"Renamed to: {renamed_csv[i]}")
            
    # Compress the renamed .csv back to .csv.gz
            compressed_name = renamed_csv[i] + ".gz"
            with open(renamed_csv[i], 'rb') as f_in:
                with gzip.open(compressed_name, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            print(f"Compressed to: {compressed_name}")
        
            
        else:
            print(f"File not found: {gz_filename[i]}")
    
    # Move to next date
    current_date += timedelta(days=1)
