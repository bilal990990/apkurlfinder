Slaw(Hi)

gaapkurls is a good tool to extract urls inside an android apk.

Prerequisites

Install apktool: This tool is used to decompile and recompile APK files.
$$$$$ sudo apt-get install apktool $$$$$

Install Python libraries: You'll need beautifulsoup4 and lxml for parsing.
$$$$$ pip install beautifulsoup4 lxml $$$$$

!!!!!!!!!! you need to specify the apk path in the code at the line before the end !!!!!!!!!

Explanation
1. Decompile the APK: The decompile_apk function uses apktool to decompile the APK into a directory.
2. Extract URLs: The extract_urls_from_directory function walks through the decompiled directory, parsing XML and HTML files using BeautifulSoup and searching for URLs using a regular expression.
3. Print URLs: All found URLs are printed out.

Usage:
Save the script to a file, e.g., extract_urls.py.
Run the script with the path to your APK file:

python extract_urls.py
This script should help you extract URLs from an Android APK efficiently.

-------------------------------------------------------------------------------------------------------------------USE IT WITH CAUTION AND MAKE SURE YOU HAVE PERMISION TO DO IT----------------------------------------------------------------------------------------------------------------------------------
