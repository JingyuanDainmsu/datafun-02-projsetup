''' This module provides a reusable byline for Jingyuan's consulting services. '''
import math
import statistics
# Define variables of different types
company_name: str = "Jingyuan Financial Consulting Analytics Inc."
count_major_employees: int = 10
count_other_corporations: int = 2
main_services_list: list = ["Artificial Intelligence Driven Financial Solutions", "Dynamic Portfolio Solutions", "Tax-saving Consulting"]
top_10_rates_scores: list = [5.0, 4.9, 4.9, 4.9, 4.9, 4.8, 4.8, 4.8, 4.8, 4.7]
# Define formatted strings
major_employees_string: str = f"Number of major employees in the company: {count_major_employees}"
other_corporations_string: str = f"The number of other corporations that we are currenting working with: {count_other_corporations}"
# Calculate descriptive statistics
smallest= min(top_10_rates_scores)
largest= max(top_10_rates_scores)
total= sum(top_10_rates_scores)
count= len(top_10_rates_scores)
mean= statistics.mean(top_10_rates_scores)
mode= statistics.mode(top_10_rates_scores)
median= statistics.median(top_10_rates_scores)
standard_deviation=statistics.stdev(top_10_rates_scores)
stats_string: str = f"""
Descriptive Statistics for Our Top Ten Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""
# Create a multiline string to display the formatted information.
byline: str = f"""
{company_name}
{major_employees_string}
{other_corporations_string}

"""

# Define main function
def main():
    ''' Display all output'''
    print(company_name)
    print(major_employees_string)
    print(other_corporations_string)

    # If all of the above works, then the byline should work too:
    print(byline)
   
# Execution    
if __name__ == '__main__':
    main()
