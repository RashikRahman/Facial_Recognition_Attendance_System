# Facial_Recognition_Attendance_System

This is an automation of face recognition attendance system. This project is with out gui so 
there's a loop whole in taking the attendance that I intentionally didn't resolve as I'll develop a 
gui interface on it in near future. You may resolve that loop whole with a simple logic of 'if preson name & current date exists in csv then don't save else save'.

## How to run?
**At first** you'll need to install Visual Studio c++ compiler. [Click here](https://photos.app.goo.gl/M8PzunQB9ZbtusuF8) to see how to run the full project.

**Next** You need to locate to the directory where you clone this repo. You can use command promt
or anaconda powershell. To locate to repo you just need to type in this command. I am using Anaconda PowerShell. Run Anaconda PowerShell as administrator then paste the following commands.

```ini
cd 'path to repo'
```
**Next** you may need to upgrade pip using the following command
```ini
python -m pip install --user --upgrade pip
```

After that type in the following command.

```ini
pip install -r requirement.txt
```

Now to run the program use the following command

```ini
python Face_Attendance.py
```

Now you have installed all the dependencies. So just open the Face_Attendance.py file and run it.
**Make sure** you have a webcam attached to your device.

## Here's an output demo.
![Result](./result.gif)

**The performance of the program depends on CPU**

 
