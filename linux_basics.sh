1. Find the Sum of Even and Odd Numbers Separately from 1 to N

#!/bin/bash
echo "Enter a number (N):"
read n
even_sum=0
odd_sum=0

for ((i=1; i<=n; i++))
do
    if [ $((i % 2)) -eq 0 ]; then
        even_sum=$((even_sum + i))
    else
        odd_sum=$((odd_sum + i))
    fi
done

echo "Sum of Even Numbers: $even_sum"
echo "Sum of Odd Numbers: $odd_sum"

2. Convert Days into Years, Weeks, and Days

#!/bin/bash
echo "Enter number of days:"
read days

years=$((days / 365))
weeks=$(((days % 365) / 7))
remaining_days=$(((days % 365) % 7))

echo "$days days = $years years, $weeks weeks, and $remaining_days days"

