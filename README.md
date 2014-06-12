#Controlled Assessment: Task 1 
==============================
##What I Am Going To Need:

1) The exchange rates must be able to be changed by the user.

2) The user should be able to enter a amount that can be converted.

3) The user needs to be able to select the chosen exchanging currencys.

4) The returned figure needs to be to two decimal places.

##Pseudocode:

```
BEGIN
INPUT currency to be converted, currency converting to (Pound Sterling/Euro/US Dollar/Japanese Yen)
ASSIGN to variables: c_type1, c_type2
MATCH c_type1, c_type2 to key in dictionary
IF c_type1 != Pound Sterling and c_type2 != Pound Sterling:
    CONVERT c_type1 into Pound Sterling
    CONVERT Pound Sterling into c_type2
    RETURN int of c_type2
ELSE:
    IDENTIFY Pound Sterling as c_type1 or c_type2
    CHANGE this value to or from Pound Sterling
    RETURN int of c_type2
```

