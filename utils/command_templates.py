command_templates = {
    "url reconnaissance": {
        "ping": {
            "command": "wsl ping {}",
            "required_files": ["ping"],
            "Explanation": "Sends ICMP packets to the target URL to check connectivity and measure response time."
        },
        "nslookup": {
            "command": "wsl nslookup {}",
            "required_files": ["nslookup"],
            "Explanation": "Resolves DNS queries, useful for finding the IP address associated with a hostname."
        },
        "whois": {
            "command": "wsl whois {}",
            "required_files": ["whois"],
            "Explanation": "Gathers domain or IP owner information, registration data, and more."
        },
        "dig": {
            "command": "wsl dig {}",
            "required_files": ["dig"],
            "Explanation": "Performs DNS lookups and queries DNS servers directly."
        },
        "traceroute": {
            "command": "wsl traceroute {}",
            "required_files": ["traceroute"],
            "Explanation": "Traces the path packets take to reach a host, showing each hop."
        },
        "SSLscan": {
            "command": "wsl sslscan {}",
            "required_files": ["sslscan"],
            "Explanation": "Tests SSL/TLS enabled services for supported cipher suites and vulnerabilities."
        }
    },
    "network scanning": {
        "masscan": {
            "command": "wsl masscan -p1-65535 {}",
            "required_files": ["masscan"],
            "Explanation": "Performs very fast port scanning over a large network or range of IP addresses."
        },
        "nmap full": {
            "command": "wsl nmap -vv -Pn -A -sC -sS -T 4 -p- {}",
            "required_files": ["nmap"],
            "Explanation": "Runs a verbose Nmap scan with various scripts and options to gather detailed information about the target."
        },
        "nmap fast": {
            "command": "wsl nmap -v -sS -A -T4 {}",
            "required_files": ["nmap"],
            "Explanation": "Performs a faster Nmap scan focusing on speed and efficiency."
        },
        "rustscan": {
            "command": "wsl rustscan -a {}",
            "required_files": ["rustscan"],
           "Explanation": "Uses Rustscan to quickly scan for open ports."
        }
    },
    "web scanning": {
        "wfuzz subdomains": {
            "command": "wsl wfuzz -v -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -Z -H 'Host: FUZZ.{}' http://{}",
            "required_files": ["/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt"],
            "Explanation": "Uses Wfuzz to brute-force subdomains of a target website."
        },
        "waybackurls": {
            "command": "wsl bash -c 'curl -s 'https://web.archive.org/cdx/search/cdx?url=*.owlsec.io&output=xml&fl=original&collapse=urlkey' | grep -oP 'https?://[^/]*' | sort -u | httpx -silent'",
            "required_files": ["curl"],
            "Explanation": "Gathers historical URLs from the Wayback Machine and analyzes them with httpx."
        },
        "httpx check": {
            "command": "wsl httpx -u {} -silent",
            "required_files": ["httpx"],
            "Explanation": "Performs a detailed web server analysis using httpx."
        },
        "whatweb check": {
            "command": "wsl whatweb {}",
            "required_files": ["whatweb"],
            "Explanation": "Identifies websites with WhatWeb, revealing technologies and services used."
        },
        "Detect WAF": {
            "command": "wsl wafw00f {}",
            "required_files": ["wafw00f"],
            "Explanation": "Detects and identifies Web Application Firewalls (WAF) protecting a site."
        },
        "wpscan": {
            "command": "wsl wpscan --url http://{} --enumerate u,vp,vt --follow-redirect",
            "required_files": ["wpscan"],
            "Explanation": "Scans WordPress websites for vulnerabilities and enumerates users, plugins, and themes."
        }
    },
    "directory scanning": {
        "dirsearch quick": {
            "command": "wsl dirsearch -u {} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -q -x 404 --exit-on-error -t 20 --exclude-subdirs=js,css",
            "required_files": ["/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"],
            "Explanation": "Performs directory and file brute-force search using a medium wordlist, ignoring certain subdirectories."
        },
        "dirsearch medium": {
            "command": "wsl dirsearch -u {} -w /usr/share/wordlists/dirb/common.txt -f -e php,tar.gz,config,conf,zip,rar,txt,sh,py -H 'X-Custom-IP-Authorization: 127.0.0.1'",
            "required_files": ["/usr/share/wordlists/dirb/common.txt"],
            "Explanation": "Performs directory and file brute-force searches on web servers."
        },
        "dirsearch long": {
            "command": "wsl dirsearch -u {} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -f -e php,tar.gz,config,conf,zip,rar,txt,sh,py -H 'X-Custom-IP-Authorization: 127.0.0.1'",
            "required_files": ["/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"],
            "Explanation": "Conducts a thorough directory search with custom headers and file extensions."
        },
    },
    "brute force": {
        "hydra_commands": {
            "command": "wsl hydra -l root -P /usr/share/wordlists/rockyou.txt {}",
            "required_files": ["/usr/share/wordlists/rockyou.txt"],
            "Explanation": "Performs brute-force password attacks using Hydra."
        }
    },
    "username reconnaissance": {
        "theHarvester": {
            "command": "wsl theHarvester {}",
            "required_files": ["theHarvester"],
            "Explanation": "Gathers emails, names, subdomains, IPs, and URLs using different public sources."
        },
        "sherlock": {
            "command": "wsl sherlock {}",
            "required_files": ["sherlock"],
            "Explanation": "Searches for usernames across social networks."
        }
    },
    "hashes": {
        "hashid": {
            "command": "wsl hashid {}",
            "required_files": ["hashid"],
            "Explanation": "Identifies the types of hashes used."
        },
        "john": {
            "command": "wsl john {}",
            "required_files": ["/usr/share/wordlists/rockyou.txt"],
            "Explanation": "John the Ripper, a password cracking tool, often used for hash cracking."
        },
        "hashcat": {
            "command": "wsl hashcat {}",
            "required_files": ["hashcat"],
            "Explanation": "Advanced password recovery tool, supports a variety of hash types."
        },
        "md5sum": {
            "command": "wsl md5sum {}",
            "required_files": ["md5sum"],
            "Explanation": "Generates or checks MD5 hashes."
        },
        "sha1sum": {
            "command": "wsl sha1sum {}",
            "required_files": ["sha1sum"],
            "Explanation": "Generates or checks SHA1 hashes."
        },
        "base64": {
            "command": "wsl echo {} | wsl base64 --decode",
            "required_files": ["base64"],
            "Explanation": "Decodes a string from Base64 encoding."
        }
    },
    "miscellaneous": {
        "sqlmap": {
            "command": "wsl sqlmap -u '{}' --dbs",
            "required_files": ["sqlmap"],
            "Explanation": "Automated SQL injection and database takeover tool."
        },
        "nikto": {
            "command": "wsl nikto -h {}",
            "required_files": ["nikto"],
            "Explanation": "Web server scanner that detects dangerous files, outdated software, and other issues."
        },
        "ssh hydra": {
            "command": "wsl hydra -l {} -P /usr/share/wordlists/metasploit/adobe_top100_pass.txt ssh://{}",
            "required_files": ["/usr/share/wordlists/metasploit/adobe_top100_pass.txt"],
            "Explanation": "Performs brute-force password attacks on SSH services."
        }
    }
}
