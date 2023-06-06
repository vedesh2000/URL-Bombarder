import requests
import time
import tkinter as tk

def generate_analytics():
    try:
        NUM_REQUESTS = int(NUM_REQUESTS_input.get())  
    except :
        output.insert(tk.END, "Invalid requests count so taking as 1 request by default\n") 
        NUM_REQUESTS = 1
        
    url = url_input.get()
    response_times = []
    output.insert(tk.END, "URL : " + str(url)+ "\n")
    try: 
        response = requests.get(url)
    except: 
        output.insert(tk.END, "Invalid URL\n")

    for i in range(NUM_REQUESTS):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_time = end_time - start_time
        response_times.append(response_time)
        output.insert(tk.END, "Request %d took %.3f seconds\n" % (i+1, response_time))

    # Calculate and display statistics
    avg_response_time = sum(response_times) / len(response_times)
    max_response_time = max(response_times)
    min_response_time = min(response_times)
    output.insert(tk.END, "\nStatistics:\n")
    output.insert(tk.END, "Number of requests: %d\n" % NUM_REQUESTS)
    output.insert(tk.END, "Average response time: %.3f seconds\n" % avg_response_time)
    output.insert(tk.END, "Maximum response time: %.3f seconds\n" % max_response_time)
    output.insert(tk.END, "Minimum response time: %.3f seconds\n" % min_response_time)
    output.insert(tk.END, " ---------------------------------\n")

# Create a window
window = tk.Tk()
window.title('URL responses Generator')

# Create a label and input field for the URL
url_label = tk.Label(window, text='Enter URL:')
url_label.pack()
url_input = tk.Entry(window, width=50)
url_input.pack()
NUM_REQUESTS_input_label = tk.Label(window, text='Enter Number of requests:')
NUM_REQUESTS_input_label.pack()
NUM_REQUESTS_input = tk.Entry(window, width=50)
NUM_REQUESTS_input.pack()
# Create a button to generate the tree
generate_button = tk.Button(window, text='Generate', command=generate_analytics)
generate_button.pack()

# Create a text box to display the generated tree
output = tk.Text(window, height=40, width=100)
output.pack()

# Start the main event loop
window.mainloop()
