# MY PORTFOLIO
Some of my recent projects 


## 1) ROCK SCISSOR PAPER WITH ML AND MEDIAPIPE 
(IRONHACK DATA ANALITICS BOOTCAMP'S FINAL PROJECT)
### Play rock scissor paper with computer vision
#### Description
I trained ML classification alghorithms in order to recognize rock, scissor or paper through the camera. By showing your hand-move to the camera, it will recognize wich move you current move. 

https://user-images.githubusercontent.com/66441052/191326791-2c56c4a6-747c-4e10-9ddd-66a5cb3b01c3.mp4


#### How 
I used Mediapipe API to transform video-frames into landmarks. This translates every image/frame into a group of coordinates. In order to train the model, I asked people to send me videos of them doing rock, scissor and paper (separatly), that then I translated in coordiantes with Mediapipe. This gave me classified groups of data that I used to train various ML models. Aftern training them, I uploaded in Toocudesigner, This allows me to transform every frame (ideally, it runs at 5fps) into an information: rock, scissor or paper.

#### Game
I created a basic game as a demo. By toggling GameMode "ON", you can play rock, scissor, paper against the CPU (CPU moves are random). Since the move-recognition is not 100% perfect, to actually input your move you need to keep it stand for a few seconds (showed by the colored bars in the left-top). 
Enjoy!

https://user-images.githubusercontent.com/66441052/191326820-1a49d55f-9f2c-413d-ba1c-f8c14f9626dd.mp4

Full project [here](https://github.com/tommella90/Rock-Scissor-Paper-move-recognition)


## 2) Scatterplot generator with Touchdesigner
### The projcet contains a scatterplot generator in a touchdesigner file. Without any cooding needed, you only need to upload a csv file, write down the x and y variables, and it's done. 
Plus, it contains many more features, good both for data visualization and data exploration. 

https://user-images.githubusercontent.com/66441052/191326662-39af976e-0913-44a4-87b6-0c2f44ed841e.mp4

Open source [here](https://github.com/tommella90/Scatterplot-generator-Touchdesigner)
 
## 3) Predicting sexual discrimination 
I use Harvard University data on implicit discrimiation to spot predictors of sexual discrimiation (exploratory analysis and machine learning). The fig. shows variables correlated (OLS exploratory regression) with implicit discrimination. 
![iat](https://user-images.githubusercontent.com/66441052/190933239-2138148c-28d9-4ffa-a0c4-aa139a63c7c4.png)
Find all the notebooks [here](https://github.com/tommella90/Predicting-sexual-discrimination)


### 4) Song recommender with Spotipy API
I use unsupervised machine learning to create a song recommendation system with Spotify        
<video src="https://user-images.githubusercontent.com/66441052/190932717-a2cc9244-8fab-458a-b40f-00dba5cf0743.mp4" width="300" height="200">
</video>
Fine the notebooks [here](https://github.com/tommella90/SongRecommender)

