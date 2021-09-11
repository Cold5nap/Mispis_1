import matplotlib.pyplot as plt


def savings(savings, num_years, interest_rate):
    first_year = 2021
    begin_savings =savings
    years =[]
    arr_savings = []
    for i in range(num_years):
        interest = savings * interest_rate
        savings = savings + interest
        arr_savings.append(savings)
        years.append(first_year + i)
    print(arr_savings,years)
    plt.axis([first_year-1, first_year + num_years,begin_savings, savings+10])#arr_savings[-1:]
    plt.plot(years,arr_savings,'ro')
    plt.show()


if __name__ == '__main__':
    years = int(input("Введите кол-во лет:"))
    sum_savings = int(input("Введите сумму начальных сбережений:"))
    interest_rate = float(input("Введите ставку десятичной дробью:"))

    savings(sum_savings, years, interest_rate)
