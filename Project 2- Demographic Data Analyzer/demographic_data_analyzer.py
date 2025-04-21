import pandas as pd

def calculate_demographic_data(print_data=True):
    # === Data Input ===
    df = pd.read_csv('adult.data.csv')  # Load the dataset into a DataFrame

    # === Race Count ===
    race_count = round(df['race'].value_counts(), 1)  # Count occurrences of each race

    # === Average Age of Men ===
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)  # Calculate average age of men

    # === Percentage of People with Bachelor's Degree ===
    percentage_bachelors = round((df['education'] == 'Bachelors').mean()*100, 1)  # Calculate percentage with Bachelor's degree

    # === Higher vs Lower Education and Salary >50K ===
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]  # Filter for higher education
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]  # Filter for lower education
    
    higher_education_rich = round((higher_education['salary'] == '>50K').mean()*100, 1)  # Percentage with higher education earning >50K
    lower_education_rich = round((lower_education['salary'] == '>50K').mean()*100, 1)  # Percentage with lower education earning >50K

    # === Minimum Work Hours ===
    min_work_hours = df['hours-per-week'].min()  # Find minimum work hours

    # === Percentage of People Earning >50K with Minimum Work Hours ===
    num_min_workers = df[df['hours-per-week'] == min_work_hours]  # Filter for minimum work hours
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean()*100, 1)  # Percentage of rich among those working minimum hours

    # === Country with Highest Percentage of People Earning >50K ===
    country_counts = df['native-country'].value_counts()  # Count of people by country
    country_with_rich_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()  # People earning >50K by country
    earning_percentage = round((country_with_rich_earnings / country_counts)*100, 1)  # Calculate percentage of rich people in each country
    highest_earning_country = earning_percentage.idxmax()  # Country with highest percentage of rich
    highest_earning_country_percentage = earning_percentage.max()  # Highest percentage of rich people in that country

    # === Most Popular Occupation for Rich People in India ===
    rich_earnings_IN_dataframe = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]  # Filter for rich people in India
    occupation_counts_IN = rich_earnings_IN_dataframe['occupation'].value_counts()  # Count occupations of rich people in India
    top_IN_occupation = occupation_counts_IN.idxmax()  # Identify the most popular occupation

    # === Data Output ===
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
