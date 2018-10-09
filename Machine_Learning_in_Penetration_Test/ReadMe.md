These are the notes taken when I'm quickly going through a book called [Machine Learning in Penetration Testing][1]

## Overall
* I think the machine learning used in this book is too basic, some methods will raise real data scientists' concern, such as the evaluation methods are not proper without necessary preprocessing or the evaluation methods can lead to bias. Meanwhile, the postive side that the book is trying to use many different data science methods and models, but it didn't explain why. When working in the industry, it is very important to understand why we are choosing this model or this method, because data science finally has to face customers, stakeholders or any other business people. I think machine learning related books, even if it's in other areas, the authors still should know why and help readers understand why.
* Cannot say I recommend this book. Reading it just to learn some penetration testing related knowledge.

## Malware Analysis Notes
### Static Malware Analysis
* [Static Malware Analysis Python Code][2]
  * This is the tool used to scan a file without executing the file, in order to decide whether it's malware. But when I tried the code, it kept telling me "Scan request successfully queued, come back later for the report" in response. So I cannot say the response is that useful. When I uploaded the file into their online tool, the feedback was immediately.
  * It's using VirusTotal python API: https://www.virustotal.com/en/documentation/public-api/#
    * To get an API key, just join the community, after activating your profile, you can find you API key in their website.
    * Yara-Python: https://github.com/VirusTotal/yara-python
  * Without the code, people can upload their files to check malware: https://www.virustotal.com/#/home/upload
  * You can your own rules with Yara-Python: https://yara.readthedocs.io/en/latest/writingrules.html#
### Portable Executable (PE) Files
* Some walware detection methods are using PE headers such as [pefile][4]
* [pefile example][3]


[1]:https://www.amazon.com/Mastering-Machine-Learning-Penetration-Testing/dp/1788997409
[2]:https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/Machine_Learning_in_Penetration_Test/static_malware_analysis.py
[3]:https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#introduction
[4]:https://github.com/erocarrera/pefile
