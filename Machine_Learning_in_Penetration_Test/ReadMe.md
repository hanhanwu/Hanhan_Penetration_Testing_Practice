These are the notes taken when I'm quickly going through a book [Machine Learning in Penetration Testing][1]

## Overall
* I think the machine learning used in this book is too basic, some methods will raise real data scientists' concern, such as the evaluation methods are not proper without necessary preprocessing or the evaluation methods can lead to bias. Meanwhile, the postive side that the book is trying to use many different data science methods and models, but it didn't explain why. When working in the industry, it is very important to understand why we are choosing this model or this method, because data science finally has to face customers, stakeholders or any other business people. I think machine learning related books, even if it's in other areas, the authors still should know why and help readers understand why.
* <b>I don't recommend this book for data scientist.</b> Reading it just to learn some penetration testing related knowledge, it's also very easy to quickly go through.
* You can find all the code used in this book [here][5]

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

## Adversary Machine Learning
* The basic idea is to find ways to attack machine learning models.
### Evasion Attacks
* Attackers kept changing data input and observe the output, trying to find patterns which can help attacks bypass
### Posinioning Attacks
* It's trying to add malicious data in the training data to reduce machine learning performance
* [An example that flip the labels to attack SVM][7]
* Adversarial Clustering
* Adversarial Features
  * [CleverHans][8]
    * [Its list of attacks][9] - attack different machine learning models
  * [Adversarial Machine Learning (AML)][10]
    * Scroll down, you will see multiple types of attack, not only adversarial features
    * Game theory here means the study of mathematical models of cooperation between intelligent decision making agents.
  * [EvadeML-Zoo][11]
### Bypassing Neural Network
* [Deep Pwning][14] - evaluates the robustness of the machine learning models against the adversarial machine learning
* [Foolbox][12] - used to fool neural network
  * [Supported attacks][13]
    * It seems that it's [decision based attacks][16] are better, since they will try to guarantee the changed image will be misclassified. I tried some gradient based, the changed images can still be classified correctly.
  ![foolbox attacks](https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/Machine_Learning_in_Penetration_Test/foolbox_attacks.PNG)
* [EvadeML][15] - it is an evolutionary framework based on genetic programming, for automatically finding variants that evade detection by machine learning based malware classifiers. 
  * Its website: https://evademl.org/
* Generative Adversarial Networks
  * Generative adversarial networks have the ability to generate images from a random noise.

## Other
### Bonet Detection
* [A popular botnet dataset]
  * It contains the mix of botnet, normal and background traffic. Labeled data.
### Anomalous Detection
* The 2 anomalous detection packages mentioned (they are very old, no longer active any more...):
  * Skyline: http://github.com/etsy/skyline  
  * Oculus: http://github.com/etsy/oculus


[1]:https://www.amazon.com/Mastering-Machine-Learning-Penetration-Testing/dp/1788997409
[2]:https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/Machine_Learning_in_Penetration_Test/static_malware_analysis.py
[3]:https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md#introduction
[4]:https://github.com/erocarrera/pefile
[5]:https://github.com/PacktPublishing/Mastering-Machine-Learning-for-Penetration-Testing
[6]:https://mcfp.weebly.com/the-ctu-13-dataset-a-labeled-dataset-with-botnet-normal-and-background-traffic.html
[7]:https://github.com/feuerchop/ALFASVMLib
[8]:https://github.com/tensorflow/cleverhans
[9]:https://cleverhans.readthedocs.io/en/latest/source/attacks.html
[10]:https://github.com/vu-aml/adlib/blob/master/Adversarial%20Machine%20Learning%20Library.ipynb
[11]:https://github.com/mzweilin/EvadeML-Zoo/tree/master/attacks
[12]:https://github.com/bethgelab/foolbox
[13]:https://github.com/bethgelab/foolbox/tree/master/foolbox/attacks
[14]:https://github.com/cchio/deep-pwning
[15]:https://github.com/uvasrg/EvadeML
[16]:https://foolbox.readthedocs.io/en/latest/modules/attacks/decision.html
