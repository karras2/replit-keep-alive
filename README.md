[![](https://img.shields.io/github/v/release/erickyeagle/replit-keep-alive)](https://github.com/erickyeagle/replit-keep-alive/releases)

# Replit Keep Alive
Replit Keep Alive is a Python script wrapper meant to, with the help of [UptimeRobot](https://uptimerobot.com), keep [Replit](https://replit.com) from terminating the bot when the browser tab is closed.

## Installation
The host environment needs to have the following software packages:

* [Latest Replit Keep Alive source code](https://github.com/erickyeagle/replit-keep-alive/releases)
* [Python 3.0+](https://www.python.org/downloads)
* [Poetry](https://python-poetry.org)

## Usage
### Keeping a script alive without modification of the script
1. Deploy the source code to your host.
2. Install Poetry dependencies.

    ```
    poetry install --no-dev
    ```
2. Run the Replit Keep Alive wrapper around another script.

    ```
    poetry run replit_keep_alive.py <script>
    ```

### Incorporating Replit Keep Alive into another software module
1. Deploy the source code to your host.
2. Import the Replit Keep Alive module into your software module.

    ```python
    import replit_keep_alive.py
    ```
3. Call the ```keep_alive()``` method where appropriate.

## Contributing
If you would like to contribute to this project, you can [file an issue](https://github.com/erickyeagle/replit-keep-alive/issues/new) or [submit a pull request](https://github.com/erickyeagle/replit-keep-alive/compare) from a forked repository. If you would like to contribute, but don't have any coding experience, you can ask questions or propose changes over at our [discussions page](https://github.com/erickyeagle/replit-keep-alive/discussions).