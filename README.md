[![](https://img.shields.io/github/v/release/erickyeagle/replit-keep-alive)](https://github.com/erickyeagle/replit-keep-alive/releases)
[![](https://img.shields.io/github/v/tag/erickyeagle/replit-keep-alive)](https://github.com/erickyeagle/replit-keep-alive/tags)
![](https://img.shields.io/github/downloads/erickyeagle/replit-keep-alive/total)

# Replit Keep Alive
Replit Keep Alive is a Python script wrapper meant to, with the help of [UptimeRobot](https://uptimerobot.com), keep [Replit](https://replit.com) from terminating a Python script when the browser tab is closed.

## Installation
The host environment needs to have the following software packages:

* Latest Replit Keep Alive source code
	* [Download a release package](https://github.com/erickyeagle/replit-keep-alive/releases)
	* Clone the repository via Git

		```
		git clone https://github.com/erickyeagle/replit-keep-alive.git
		```
* [Python 3.5+](https://www.python.org/downloads)

## Usage
### Keeping a script alive without modification of the script
1. Copy `requirements.txt` and everything in `/src` to the host environment.
2. Modify `.replit` by replacing `<script>` with the target script file.
3. Configure [UptimeRobot](https://uptimerobot.com) to point to your web server.
4. Install dependencies.

	```
	pip install -r requirements.txt
	```

### Incorporating Replit Keep Alive into another software module
1. Copy all source code files (except for `.replit` as this will interfere with Replit's normal run process) to the host environment.
2. Import the Replit Keep Alive module into your software module.

    ```python
    from replit_keep_alive import keep_alive
    ```
3. Call the `keep_alive()` method where appropriate.
4. Configure [UptimeRobot](https://uptimerobot.com) to point to your web server.

## Contributing
If you would like to contribute to this project, you can [file an issue](https://github.com/erickyeagle/replit-keep-alive/issues/new) or [submit a pull request](https://github.com/erickyeagle/replit-keep-alive/compare) from a forked repository. If you would like to contribute, but don't have any coding experience, you can ask questions or propose changes over at our [discussions page](https://github.com/erickyeagle/replit-keep-alive/discussions).