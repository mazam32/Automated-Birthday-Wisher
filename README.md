# Automated-Birthday-Wisher README


## Introduction

This project sends personalized birthday emails to recipients whose birthdays match the current date. It reads recipient information from a CSV file and selects a random birthday letter template to personalize and send via email.

## Requirements

- Python 3.x
- pandas
- smtplib
- os
- datetime

## Setup

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   ```

2. **Navigate to the project directory**:
   ```sh
   cd <project_directory>
   ```

3. **Install dependencies**:
   Ensure you have the necessary Python libraries installed. You can install `pandas` if you don't already have it:
   ```sh
   pip install pandas
   ```

4. **Prepare the CSV file**:
   Ensure you have a `birthdays.csv` file in the project directory with the following columns:
   - `name`: Name of the recipient
   - `email`: Email address of the recipient
   - `month`: Birth month of the recipient (integer)
   - `day`: Birth day of the recipient (integer)

5. **Create letter templates**:
   Create a directory named `letter_templates` in the project directory and add letter templates named `letter_1.txt`, `letter_2.txt`, `letter_3.txt`. Each template should contain the placeholder `[NAME]` where the recipient's name will be inserted.

6. **Update email credentials**:
   Replace `my_email` and `password` in the script with your own email address and app password respectively:
   ```python
   my_email = "youremail@example.com"
   password = "yourapppassword"
   ```

## Running the Script

1. **Navigate to the project directory**:
   ```sh
   cd <project_directory>
   ```

2. **Run the script**:
   ```sh
   python send_birthday_emails.py
   ```

## Script Explanation

The script performs the following steps:

1. **Read the current date**:
   ```python
   now = dt.datetime.now()
   todays_day = now.day
   todays_month = now.month
   ```

2. **Load recipient information**:
   Reads the `birthdays.csv` file and filters the rows where the birthday matches the current date:
   ```python
   info = pd.read_csv(path)
   email_list = info[(info.month == todays_month) & (info.day == todays_day)].email.tolist()
   name_list = info[(info.month == todays_month) & (info.day == todays_day)].name.tolist()
   ```

3. **Send personalized emails**:
   For each recipient, selects a random letter template, personalizes it, and sends an email:
   ```python
   for name in name_list:
       letter_number = random.randint(1,3)
       letter_path = os.path.join(base_dir, f"letter_templates/letter_{letter_number}.txt")
       with open(letter_path, mode= "r") as file:
           default_text = file.read()
           new_text = default_text.replace("[NAME]", name)
           new_text = new_text.replace("Angela", "Muhammad Hamd")
           with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
               connection.starttls()
               connection.login(user= my_email, password= password)
               connection.sendmail(
                   from_addr=my_email, 
                   to_addrs=email_list[index], 
                   msg= f"Subject:Happy Birthday!\n\n{new_text}"
               )
       index += 1
   ```

## Note

Ensure you use an app password instead of your email account password for `smtplib` due to security reasons. You can generate an app password from your email account's security settings.

## License

This project is licensed under the MIT License. See the LICENSE file for details.