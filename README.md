# RedvsBlue
Elliott Fix
Begun December 2016
0.1.4
(Major version).(Minor version).(Revision number)

This is a client/server program that handles two players, attack and defense. 
The server must be started before either client. 


```
    sudo apt-get install python3-pip python3-tk git
    git clone https://github.com/lbaitemple/RedvsBlue
    cd RedvsBlue
    pip3 install -r requirements.txt
```

To start a server  
```
  python3 RedBlueServer.py
  
```

To start a blue client  
```
python3 BlueClient.py 
  
```

To start a red client  
```
python3 RedClient.py 
  
```

Red client starts the first move, then they are alternating their moves.
