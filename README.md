# RAM_cleaner
Clears RAM in one shot by closing all applications. Useful for devices with low memory to resolve the problem of memory bottleneck.

This programm uses os module in python to send command in CMD to terminate processes which were initiated by the user after boot up.

Commad to terminate process in CMD:
  " taskkill /f /im [process_name] /t "   
  example>>>   taskkill /f /im chrome.exe /t
  
  
  Instructions to use:    
  1. Python 3.X must be installed on system
  2. File "auto startup ram.py" needs to be copied to system startup folder (i.e C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp)   
  3. Run "Jai Shree ram.pyw"     
            
  // AUTHOR karan kumar  
  //https://github.com/karan10072002/RAM_cleaner/    
  //https://www.instagram.com/karan10072002/
