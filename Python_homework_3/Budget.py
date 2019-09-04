import os
import csv
csvpath = os.path.join ('budget_data.csv')
with open(csvpath, newline ="") as csvfile:
    csv_reader  = csv.reader(csvfile, delimiter = ",")
    #Read through each row of data after the header for row in csv_reader:
        #Date = Str(row[0])
        #ProfitLoss = int(row[1])
        #The total number of months included in the dataset 
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}") 


         
        #Profit/Losses over entire period
    
    sum_profit = 0
    sum_loss = 0
    total_profit_loss = 0
    row_count = 0
    greatest_change = 0
    greatest_loss = 0
    profit_list = []
    month_list = []
    change_list = []
    previous_profit = 0

    for row in csv_reader:
        profit = int(row[1])
        sum_profit = sum_profit + profit
        row_count = row_count + 1  
        profit_list.append(profit)
        month_list.append(row[0])

    
    for i in range(1, len(profit_list)):
        change = profit_list[i] - profit_list[i-1]
        change_list.append(change)

    total_months = row_count 
    #Average of the changes in "Profit/Losses" over the entire period 
    
    avg_change = sum(change_list)/len(change_list)
    #Greatest increase in profits over the entire period
    max_change = max(change_list)
    max_month = month_list[change_list.index(max_change) + 1]
    profit_list 

    
    #profit_list 
    #previous_profit = int(row[1])
     
    #Greatest decrease in losses over the entire period
    min_change = min(change_list)
    min_month = month_list[change_list.index(min_change) + 1]
    
    
    #Analysis output
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: ${str(sum_profit)}")
    print(f"Average: ${str(round(avg_change,2))}")
    print(f"greatest increase in profits:{max_month} ${max_change}")
    print(f"greatest decrease in profits:{min_month} (${min_change})")

with open("budget_data.txt", "w") as output: 
    output.write("budget_data\n")
    output.write("Financial Analysis\n")
    output.write("----------------------\n")
    output.write(f"Total Months: {str(total_months)}\n")
    output.write(f"Total: ${str(sum_profit)}\n")
    output.write(f"Average: ${str(round(avg_change,2))}\n")
    output.write(f"greatest increase in profits:{max_month} ${max_change}\n")
    output.write(f"greatest decrease in profits:{min_month} (${min_change})\n")

