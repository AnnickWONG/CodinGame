# Defibrillators
[puzzle link](https://www.codingame.com/training/easy/defibrillators)

Practice using these concepts:
* Loops
* Distance
* Trigonometry

## The Goal
The city of Montpellier has equipped its streets with defibrillators to help save victims of cardiac arrests. The data corresponding to [the position of all defibrillators](https://data.montpellier3m.fr/dataset/defibrillateurs-de-montpellier) is available online.

Based on the data we provide in the tests, write a program that will allow users to find the defibrillator nearest to their location using their mobile phone.

### 	Rules
The input data you require for your program is provided in text format.
This data is comprised of lines, each of which represents a defibrillator. Each defibrillator is represented by the following fields:
* A number identifying the defibrillator
* Name
* Address
* Contact Phone number
* Longitude (degrees)
* Latitude (degrees)

These fields are separated by a semicolon (**;**).

***Beware:** the decimal numbers use the comma (**,**) as decimal separator. Remember to turn the comma (**,**) into dot (**.**) if necessary in order to use the data in your program.*
 
#### DISTANCE
The distance `d` between two points `A` and `B` will be calculated using the following formula:

<img src="https://latex.codecogs.com/svg.image?x=(longitudeB-longitudeA)\times&space;cos(\frac{latitudeA&plus;latitudeB}{2})" title="https://latex.codecogs.com/svg.image?x=(longitudeB-longitudeA)\times cos(\frac{latitudeA+latitudeB}{2})" />

<img src="https://latex.codecogs.com/svg.image?y=(latitudeB-latitudeA)" title="https://latex.codecogs.com/svg.image?y=(latitudeB-latitudeA)" />

<img src="https://latex.codecogs.com/svg.image?d=\sqrt{x^{2}&plus;y^{2}}\times&space;6371" title="https://latex.codecogs.com/svg.image?d=\sqrt{x^{2}+y^{2}}\times 6371" />

*Note: In this formula, the latitudes and longitudes are expressed in **radians**. 6371 corresponds to the radius of the earth in km.*

The program will display the name of the defibrillator located the closest to the user’s position. This position is given as input to the program.

## Conditions
### Input
**Line 1:** User's longitude (in degrees)

**Line 2:** User's latitude (in degrees)

**Line 3:** The number N of defibrillators located in the streets of Montpellier

`N` **next lines:** a description of each defibrillator

### Output
The name of the defibrillator located the closest to the user’s position.

### Constraints
0 < `N` < 10000


## Example
**Input**
```
3,879483
43,608177
3
1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217
2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849
3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854
```

**Output**
```
Maison de la Prevention Sante
```
