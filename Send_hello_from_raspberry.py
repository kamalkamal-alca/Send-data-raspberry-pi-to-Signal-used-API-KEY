import urllib.parse
import requests

# Your API credentials
apiKey = "xxxxxx"
uuid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def send_signal_message(message_text):
    """Send message to Signal app via CallMeBot API"""
    encoded_message = urllib.parse.quote_plus(message_text)
    
    url = f"https://signal.callmebot.com/signal/send.php?phone={uuid}&apikey={apiKey}&text={encoded_message}"
    
    try:
        response = requests.post(url)
        
        if response.status_code == 200:
            print("✓ Message sent successfully!")
            return True
        else:
            print(f"✗ Error: HTTP Status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Network error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    send_signal_message("hello from Signal")
    
    # You can now send any message you want:
    # send_signal_message("This is another test message")
    # send_signal_message("Alert: Something happened!")
