currencies= {Pound Sterling: 1, Euro: 1.2, US Dollar: 1.6, Japanese Yen: 200}
c_type1 = input("What Currency are you converting from? (Pound Sterling/Euro/US Dollar/Japanese Yen)")
c_type2 = input("What Currency are you converting to? (Pound Sterling/Euro/US Dollar/Japanese Yen)")

if c_type1 != "Pound Sterling" or "Euro" or "US Dollar" or "Japanese Yen":
    c_type1 = input(Please enter a valid currency to convert from (Pound Sterling/Euro/US Dollar/Japanese Yen)")
