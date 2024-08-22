import os
import requests
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display a welcome banner with a cat logo
def display_welcome_banner():
    banner = f"""
{Fore.CYAN}Welcome to UserFinder{Style.RESET_ALL}
{Fore.RED}
 /\_/\  
( o.o ) 
 > ^ <
{Style.RESET_ALL}
    """
    print(banner)

def check_username(username, sites):
    found_sites = []
    total_sites = len(sites)
    start_time = time.time()

    for site, url in sites.items():
        full_url = url.format(username=username)
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] Found account on {site}: {full_url}{Style.RESET_ALL}")
                found_sites.append((site, full_url))
            else:
                print(f"{Fore.RED}[-] No account found on {site}. Status code: {response.status_code}{Style.RESET_ALL}")
        except requests.ConnectionError:
            print(f"{Fore.RED}[!] Connection error when checking {site}: {full_url}{Style.RESET_ALL}")
        except requests.Timeout:
            print(f"{Fore.YELLOW}[!] Timeout error when checking {site}: {full_url}{Style.RESET_ALL}")
        except requests.TooManyRedirects:
            print(f"{Fore.YELLOW}[!] Too many redirects when checking {site}: {full_url}{Style.RESET_ALL}")
        except requests.RequestException as e:
            print(f"{Fore.YELLOW}[!] Request exception when checking {site}: {e}{Style.RESET_ALL}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    return found_sites, elapsed_time, total_sites

def save_to_file(found_sites, filename):
    with open(filename, 'w') as file:
        if found_sites:
            file.write(f"Summary of accounts found:\n")
            for site, url in found_sites:
                file.write(f"{site}: {url}\n")
        else:
            file.write("No accounts found.\n")
    print(f"{Fore.CYAN}Results have been saved to {filename}{Style.RESET_ALL}")

def main():
    # Clear the terminal before running the program
    clear_terminal()

    # Display the welcome banner
    display_welcome_banner()

    # Define the sites and their URL patterns
    sites = {
        "GitHub": "https://github.com/{username}",
        "Twitter": "https://twitter.com/{username}",
        "Instagram": "https://www.instagram.com/{username}/",
        "Blogspot": "https://{username}.blogspot.com/",
        "Reddit": "https://www.reddit.com/user/{username}",
        "Quora": "https://www.quora.com/profile/{username}",
        "Alibaba": "https://{username}.alibaba.com/",
        "eBay": "https://www.ebay.com/usr/{username}",
        "Shopify": "https://{username}.myshopify.com/",
        "YouTube": "https://www.youtube.com/{username}",
        "Venmo": "https://venmo.com/{username}",
        "Tumblr": "https://{username}.tumblr.com/",
        "Pinterest": "https://www.pinterest.com/{username}",
        "Flickr": "https://www.flickr.com/photos/{username}",
        "SoundCloud": "https://soundcloud.com/{username}",
        "DeviantArt": "https://www.deviantart.com/{username}",
        "Twitch": "https://www.twitch.tv/{username}",
        "Discord": "https://discord.com/users/{username}",
        "Mix": "https://mix.com/{username}",
        "Patreon": "https://www.patreon.com/{username}",
        "Steam": "https://steamcommunity.com/id/{username}",
        "LinkedIn": "https://www.linkedin.com/in/{username}",
        "Dailymotion": "https://www.dailymotion.com/user/{username}",
        "Vimeo": "https://vimeo.com/{username}",
        "GitLab": "https://gitlab.com/{username}",
        "Bitbucket": "https://bitbucket.org/{username}",
        "Medium": "https://medium.com/@{username}",
        "WordPress": "https://{username}.wordpress.com/",
        "Gmail": "https://mail.google.com/mail/u/0/#search/{username}",
        "Yahoo": "https://login.yahoo.com/username/{username}",
    }

    # Enter the username you want to check
    username = input(f"{Fore.CYAN}Enter the username to check: {Style.RESET_ALL}")
    print(f"\n{Fore.MAGENTA}Checking accounts for username: {username}{Style.RESET_ALL}\n")

    # Check the username on each site
    found_sites, elapsed_time, total_sites = check_username(username, sites)

    if found_sites:
        print(f"\n{Fore.GREEN}Summary of accounts found:{Style.RESET_ALL}")
        for site, url in found_sites:
            print(f"{Fore.GREEN}- {site}: {url}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}No accounts found.{Style.RESET_ALL}")

    # Display time taken, number of websites checked, and number of websites where accounts were found
    num_found_sites = len(found_sites)
    print(f"{Fore.CYAN}Time taken to search: {elapsed_time:.2f} seconds{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Number of websites checked: {total_sites}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Number of websites where accounts were found: {num_found_sites}{Style.RESET_ALL}")

    # Ask if the user wants to save the results
    save_option = input(f"{Fore.CYAN}Do you want to save the results to a file? (Y/n): {Style.RESET_ALL}")
    if save_option.lower() == 'y':
        filename = input(f"{Fore.CYAN}Enter the filename to save the results (e.g., result.txt): {Style.RESET_ALL}")
        save_to_file(found_sites, filename)
    else:
        print(f"{Fore.YELLOW}Results will not be saved.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()

