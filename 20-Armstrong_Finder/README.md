# Armstrong-Finder
#### **_This is the file which contain the code to check whether a entered number is a Armstrong number or not_**


### What is a Armstrong number ?

	• Armstrong numbers are numbers which are in the form with the numbers X, Y, Z such that 
	=> XYZ = X^n+ Y^n + Z^n
	Where n is the number of terms

	• Numbers in such form are called Armstrong numbers
	E.g.:  153 = 1^3 + 5^3 + 3^3
	        = 1    + 125 + 27
	153 = 153	
    Therefore, This is a Armstrong number



### Strategy used to find the armstrong number

Let the number be 8891:

	1. N = 8891
	2. We will take each digit of the number using modular division
		• 8891 % 10 = 1
		•   889 % 10 = 9
		•     88 % 10 = 8
		•       8 % 10 =8
 
	3. A variable to store the digits of the number sum = 0
	4. By some way we need to find the number of digits in the number which is the order
	5. Each time after calculation we will change the value of n = n//10
	6. We can assign the value of each digit raise to order This will form the number
