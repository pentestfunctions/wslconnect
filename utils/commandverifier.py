import subprocess

def check_wsl_commands_and_files():
    commands = [
        "ping",
        "nslookup",
        "whois",
        "dig",
        "traceroute",
        "sslscan",
        "hashid",
        "john",
        "hashcat",
        "md5sum",
        "sha1sum",
        "base64",
        "theHarvester",
        "sherlock",
        "masscan",
        "nmap",
        "rustscan",
        "wfuzz",
        "curl",
        "grep",
        "sort",
        "httpx",
        "whatweb",
        "wafw00f",
        "wpscan",
        "dirsearch",
        "wget",
        "hydra",
        "sqlmap",
        "nikto",
    ]

    files = [
        "/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt",
        "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt",
        "/usr/share/wordlists/dirb/common.txt",
        "/usr/share/wordlists/rockyou.txt",
        "/usr/share/wordlists/metasploit/adobe_top100_pass.txt",
    ]

    missing_elements = {'commands': [], 'files': []}

    for cmd in commands:
        try:
            subprocess.run(f"wsl command -v {cmd}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            missing_elements['commands'].append(cmd)

    for file in files:
        try:
            subprocess.run(f"wsl test -f {file}", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            missing_elements['files'].append(file)

    return missing_elements
