# wslconnect 🚀

<p align="center">
  <img src="utils/logo.png">
</p>

![GitHub top language](https://img.shields.io/github/languages/top/pentestfunctions/wslconnect)
![GitHub issues](https://img.shields.io/github/issues/pentestfunctions/wslconnect)
![GitHub forks](https://img.shields.io/github/forks/pentestfunctions/wslconnect)
![GitHub stars](https://img.shields.io/github/stars/pentestfunctions/wslconnect)
![GitHub license](https://img.shields.io/github/license/pentestfunctions/wslconnect)


🔨 **Status:** Still work in progress.

### Build yourself an executable:
```bash
pyinstaller --onefile --windowed --add-data "utils/logo.png;." wslconnect.py
```

### Usage:

Basically just interacts with WSL and allows for some quick command usage for messing around.

<p align="center">
  <img src="examplevideos/whatyathink.gif">
</p>


### Extras:
So this uses WSL, preferably kali-linux-headless as it comes with most tools already, you will need some wordlists etc.

- Also to get the proper version of httpx

```bash
sudo apt install golang-go
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
cp /home/robot/go/bin/httpx /usr/bin/httpx
```

Just check the commands in command_templates for example 

```python
        "ping": {
            "command": "wsl ping {}",
            "required_files": ["ping"],
            "Explanation": "Sends ICMP packets to the target URL to check connectivity and measure response time."
        },
```

- Thaat's the format and it will auto add any you put in that file as long as they have the right structure.


## Ideas

1. Verify installed tools more fluidly (update colors etc based on missing info)
2. Add proper help docs
3. Adjust for user input (http/httpx as well as hashtype and report back if output failed etc)
4. Position terminals using cmd /k around the screen for full hacker vibe

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
