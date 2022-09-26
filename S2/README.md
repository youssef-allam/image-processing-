<h2> How is the gray scale of an image produced ? </h2>
There are a number of commonly used methods to convert an RGB image to a grayscale image, such as :-
<h3> The lightness method : </h3> averages the most prominent and least prominent colors: (max(R, G, B) + min(R, G, B)) / 2. <br/>

<h3> The average method : </h3> Looking at just red or blue or green in isolation, it's hard to tell which pixel is brightest or darkest. The average combines and summarizes the three values into one number 0..255. The average shows how bright the pixel is, ignoring hue: 0 = totally dark, 255=totally bright, with intermediate average values corresponding to intermediate brightnesses, simply averages the values: (R + G + B) / 3. <br/>

<h3> The luminosity method : </h3> is a more complex version of the average method. It also averages the values, but it forms a weighted average to account for human perception. We’re more sensitive to green than other colors, so green is weighted most heavily. The formula for luminosity is 0.21 R + 0.72 G + 0.07 B.
<br/>
<img src = "https://user-images.githubusercontent.com/66872519/191521297-3b112448-9d9b-47c5-88a0-c18e8c15d797.png"/>
And this is the formula used in Opencv library : 
<h4> RGB[A] to Gray : Y ← 0.299⋅R + 0.587⋅G + 0.114⋅B </h4> (luminosity method)
