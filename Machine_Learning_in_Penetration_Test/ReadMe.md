These are the notes taken when I'm quickly going through a book called [Machine Learning in Penetration Testing][1]

## Overall
* I think the machine learning used in this book is too basic, some methods will raise real data scientists' concern. Cannot say I recommend this book. Reading it just to learn some penetration testing related knowledge.

## Malware Analysis Notes
### Static Malware Analysis
* [Static Malware Analysis Python Code][2]
  * This is the tool used to scan a file without executing the file, in order to decide whether it's malware. But when I tried the code, it kept telling me "Scan request successfully queued, come back later for the report" in response. So I cannot say the response is that useful. When I uploaded the file into their online tool, the feedback was immediately.
  * It's using VirusTotal python API: https://www.virustotal.com/en/documentation/public-api/#
    * To get an API key, just join the community, after activating your profile, you can find you API key in their website.
    * Yara-Python: https://github.com/VirusTotal/yara-python
  * Without the code, people can upload their files to check malware: https://www.virustotal.com/#/home/upload
  * You can your own rules with Yara-Python: https://yara.readthedocs.io/en/latest/writingrules.html#


[1]:https://www.amazon.com/Mastering-Machine-Learning-Penetration-Testing/dp/1788997409
[2]:https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/Machine_Learning_in_Penetration_Test/static_malware_analysis.py
