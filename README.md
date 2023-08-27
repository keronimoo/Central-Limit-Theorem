# Central-Limit-Theorem
Central Limit Theorem simulations with python
![Figure 1](/images/img10.png?raw=true "Optional Title")

Figure 1 shows lines produced by points (Xa, U) ,(1 , 1.2)
Since all lines lies on the left it means that slopes are negative and Xa
values are greater than U values .
slopes of the lines converges to infinity while x →0 and x →1
at the rightmost areas of graph , values Xa and U are closer to each
other because slope of lines are almost infinity
at the leftmost areas of graph , values Xa and U are closer to each
other because slope of lines are almost infinity
at the Middle areas of graph , difference between Xa and U are
greater . because slope of lines are decreasing

![Figure 2](/images/img9.png?raw=true "Optional Title")

in Figure 2 blue lines shows uniformly distrubited values between 0
and 1
Orange line = probablity density function of given cumulative density
function.
Given CDF = x^2 → PDF of CDF is equal to 2x (derivation)
if N(sample amount) goes to infinity
Orange line would converge to y = 2x
Blue line would converge to x = 1

![Figure 3](/images/img8.png?raw=true "Optional Title")

in Figure 3 , blue line shows probablity density function of uniform
distribution f(u) = u
Orange line = F(x) = x^2
Obtained by using cumulative sum function .
Given CDF = F(x) = x^2 0<= x <= 1
Convert it to PDF by taking derivation of it
PDF = f(x) = 2x 0<= x <= 1
Theoretical Expected Value(mean) = E(x) = ∫ 𝑥𝑓(𝑥)
1
0 𝑑𝑥 = 2/3 =
0.666666
Theoretical Varince=E(x^2)–(E(x))^2 =∫ 𝑥^2𝑓(𝑥)𝑑𝑥
1
0 –(∫ 𝑥𝑓(𝑥)
1
0 𝑑𝑥)^2
= 1/2 – 4/9
=0.5 – 0.444444
=0.055556

![Figure 4](/images/img7.png?raw=true "Optional Title")

Experimental Expected Value
Converges to Theoretical
Expected Value →0.6666666

![Figure 5](/images/img6.png?raw=true "Optional Title")

Experimental Variance
Converges to Theoretical
Variance →0.055556

![Figure 6](/images/img5.png?raw=true "Optional Title")

![](/images/img4.png?raw=true "Optional Title")

in Figure 6, blue area shows accepted samples .
by looking at the figure we can say: a = 0 , b = 1 and c = 2
a<= x <= b , 0<= f(x) <= c

![Figure 8](/images/img3.png?raw=true "Optional Title")

Blue line shows Cumulative Density Function F(x) = x^2
Obtained by using cumulative sum function .
Given CDF = F(x) = x^2 0<= x <= 1
Convert it to PDF by taking derivation
PDF = f(x) = 2x 0<= x <= 1
Theoretical Expected Value(mean) = E(x) = ∫ 𝑥𝑓(𝑥)
1
0 𝑑𝑥 = 2/3 =
0.666666
Theoretical Variance=E(x^2)–(E(x))^2 =∫ 𝑥^2𝑓(𝑥)𝑑𝑥
1
0 (∫ 𝑥𝑓(𝑥)
1
0 𝑑𝑥)^2
= 1/2 – 4/9
=0.5 – 0.444444
=0.055556

![Figure 9](/images/img2.png?raw=true "Optional Title")

Experimental Expected Value
converges to Theoretical
Expected Value 0.666666

![Figure 10](/images/img1.png?raw=true "Optional Title")

Experimental Variance
converges to Theoretical
Variance 0.055556
