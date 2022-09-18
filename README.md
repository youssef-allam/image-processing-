# image-processing Tasks

<h3> Task 2 </h3>

<h4> 1. Which algorithm gets better results?</h4>
acorrding to my tries, ( Brute-Force Matching with ORB Descriptors ) and (FLANN based Matcher with SIFT Descriptors) were way better in detecting matches than (Brute-Force Matching with SIFT Descriptors) <br/>
<br/>


 BF_matcher_ORB
   <img src="https://user-images.githubusercontent.com/66872519/190897974-80a93259-efd0-4a3f-b6e6-d762098a8ca4.png" />
  <br/>
  <br/>
  
  BF_matcher_SIFT
  <img src="https://user-images.githubusercontent.com/66872519/190900950-8c7a85b9-f742-42c1-8322-e3172d9d0383.png" />
 <br/>
  <br/>
<h4> 2.	time taken by the algorithms </h4>
in small data like two images it is not noticeable but in large data ( FLANN based Matcher ) will be faster than  ( Brute-Force Matching ), as BFMatcher is going to try all the possibilities which will get better results but slower than FLANN based Matcher.

 <br/>
  <br/>
  
  <h4> 3. changing distance function and number of Ks effect </h4>


<h3>Task 4</h3>

Low pass filter: Low pass filter is the type of frequency domain filter that is used for smoothing the image. It attenuates the high frequency components and preserves the low frequency components.
High pass filter: High pass filter is the type of frequency domain filter that is used for sharpening the image. It attenuates the low frequency components and preserves the high frequency components. 

Difference between Low pass filter and High pass filter:

<h4>Low pass filter</h4>	                         
  1. It is used for smoothing the image.<br />
  2. It attenuates the high frequency.<br />
  3. Low frequency is preserved in it.<br />
  4. It allows the frequencies below cut off 
  frequency to pass through it.<br />
  5. It helps in removal of aliasing effect.<br />	

<h4>High pass filter</h4>
  1. It is used for sharpening the image.<br />
	2. It attenuates the low frequency.<br />
 	3. High frequency is preserved in it.<br />
  4. It allows the frequencies above cut off frequency to pass through it.<br />
  5. It helps in removal of noise.<br />
<br />
So we can say that bluring is a low-pass-filter ,While sharpening and edge detection are High-pass-filters. 


<h3>Task 6</h3>

<h4> determine how you chose the arguments ? </h4>
	1. first i tried to set them by just trying different numbers. <br/>
	2. little searh and i found that the most common values are (Upper = 3 * times lower). <br />
	3. The last and easiest way is to use a track bar which i did to find the best values. <br/> 
	<img src="https://user-images.githubusercontent.com/66872519/190879772-f6d01c7f-45d3-4dda-a9ca-d4b086ff8397.png">
