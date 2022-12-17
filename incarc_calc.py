# This program will calculate and display the total cost of incarceration 
# fees for a federal facility.

# These parameters were retrieved from the Federal Bureau of Prisons'
# FY 2020 Annual Determination of Average Cost of Incarceration Fee Report.

# The user will be prompted for inmate and time(day) quantities.

#Developer: Angela D. Tackett   Class: CMIS102    Date: May 27, 2022


    
#Display title
print("-----------**BAD BOYS, BAD BOYS, WHATCHA GONNA DO???**-----------")
print("\n----------***Welcome to the Incarceration Calculator***----------\n\n")

#Prompt user for inputs
inmates = eval(input("How many inmates would you like incarcerated? "))
days = eval(input("How many days would you like these inmates incarcerated for? "))


#Calculate total cost of incarceration
total_cost = float(inmates * days * 120.59)
    
#Display total cost of incarceration(s)
print("\nIt would cost $",format(total_cost,".2f"),"to incarcerate these inmates!\n\nEnjoy your freedom, Patriot!")



