import socket

def get_ip_address(website):
    try:
        # Remove protocol if present
        if website.startswith('http://'):
            website = website[7:]
        elif website.startswith('https://'):
            website = website[8:]
        
        # Remove any paths
        website = website.split('/')[0]
        
        # Get IP address
        ip_address = socket.gethostbyname(website)
        return ip_address
    except socket.gaierror:
        return "Error: Could not find that website. Please check the spelling and try again."
    except Exception as e:
        return f"Error: Something went wrong - {str(e)}"

# Get user input and process
website = input("Enter a website to lookup (e.g., google.com): ")
result = get_ip_address(website)

# Display result
print(f"\nWebsite: {website}")
print(f"IP Address: {result}")