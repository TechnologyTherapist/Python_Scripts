import tkinter as tk
from tkinter import filedialog
from selenium import webdriver

# Function to handle sending the WhatsApp message
def send_whatsapp_message():
    number = number_entry.get()
    message = message_entry.get("1.0", "end-1c")
    file_path = file_path_label["text"]

    # Launch Chrome browser using Selenium
    driver = webdriver.Chrome()

    # Open WhatsApp web
    driver.get("https://web.whatsapp.com/")

    # Wait for user to scan the QR code and log in

    # Find the search input field and enter the recipient's number
    search_input = driver.find_element_by_xpath('//div[contains(@class, "_2_1wd")]//input[@type="text"]')
    search_input.send_keys(number)

    # Wait for the search results to appear and click on the correct contact

    # Find the message input field and enter the message
    message_input = driver.find_element_by_xpath('//div[contains(@class, "_3u328")]//div[@contenteditable="true"]')
    message_input.send_keys(message)

    # Find the send button and click it
    send_button = driver.find_element_by_xpath('//div[contains(@class, "_3M-N-")]//span[@data-testid="send"]')
    send_button.click()

    # Close the browser
    driver.quit()

# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename()
    file_path_label["text"] = file_path

# Create the GUI window
window = tk.Tk()
window.title("WhatsApp Message Sender")

# Create the number input field
number_label = tk.Label(window, text="Enter Phone Number:")
number_label.pack()
number_entry = tk.Entry(window)
number_entry.pack()

# Create the message input field
message_label = tk.Label(window, text="Enter Message:")
message_label.pack()
message_entry = tk.Text(window, height=5)
message_entry.pack()

# Create the file selection button
file_button = tk.Button(window, text="Select File", command=select_file)
file_button.pack()

# Create the label to display the selected file path
file_path_label = tk.Label(window)
file_path_label.pack()

# Create the send button
send_button = tk.Button(window, text="Send Message", command=send_whatsapp_message)
send_button.pack()

# Run the GUI
window.mainloop()
