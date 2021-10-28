# House Rockets Project
![image](vector-real-estate-for-sale.jpg)

House Rockets is a company whose business model is based on buying and selling real estate, and its objective is to find good deals within an available portfolio, which is to find houses with low prices, in great locations and with great potential for reselling at a higher price, making the maximum profit possible.

The objective of this project is to perform an exploratory analysis of the data provided by the company in order to answer some business questions, as well as generate business insights to guide the company in its future decisions.


## Business Problems

The business team informed that the main difficulty is to determine which properties should be bought and/or sold and at what price. In this way, this project aims to meet the following demands of the business team:

- What properties should House Rocket buy and at what price?
- Once the property is purchased, what is the best time to sell it and for what price?

## Assumptions

- Properties built before 1955 was considered "old_property", after 1955 "new_property"
- Properties without basement have ```sqft_basement``` equals 0
    
- Properties with repeated ID's were excluded from the dataset, leaving only the most recent ID
- If the purchase price is greater than the regional median + seasonality, the sale price will be equal to the purchase price + 10%;
- If the purchase price is less than the region's median price + seasonality, the sale price will be equal to the purchase price + 30%;
- Properties with more than 10 bedrooms will be consider as outlier
- The properties price is affected by the seasons of the year;

## Solution Planning

### Final product:
Creation of a web application with the availability of two reports:
  - Report 1: Real estate purchase recommendation for a specified amount
  - Report 2: Recommendation for the sale of the property with a determined date and value
        

### Tools:
To meet this demand, the tools used were:

  - Programming language: Python
  - IDE for application development: Pycharm
  - Data exploration and visualization tool: Jupyter Notebook
    
    
### Process:

The following steps were part of the project:

- The data collection used as a portfolio for this project was extracted from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Generation of Insights through the creation and validation of business hypotheses
- Creation of a web application to make the results available

## Top 10 Business Hypothesis


|         | Hypothesis          | Validation | Business Insight |
| :-----: | :------------------ | :-----     | :-----           |
| **H1**  | Waterfront properties are 30% more expensive, on average | True | Investing in water view properties |
| **H2**  | Properties built before 1955 are 50% cheaper in average | False | Don't invest in houses built before 1955|
| **H3**  | Properties without basement have, in average, a lot area 50% bigger than properties with basement | False | On average properties without basement have lot are 18% bigger |
| **H4**  | The average growth in property prices YoY (year over year) is 10% | False | The growth of properties prices didn't have significant variation over year (2014-2015) |
| **H5**  | Properties with 3 bathrooms have an average price growth month over month (MoM) about 15% | False | There is no constant average growth in the price of 3-bathroom properties |
| **H6**  | Properties in excellent condition are in average, 25% more expensive than properties in terrible condition | True | Investing in properties with excellent condition |
| **H7**  | The price of properties with more than 50 years of construction and which have renovation is on average, 20% higher than those that have not been renovated | True | for properties over 50 years old, invest in those that have undergone renovation |
| **H8**  | In properties with a water view, the price is on average 20% higher for those with an excellent view, compared to those with a regular view | False | Invest in properties with excellent view rather than regular view which are more expensive |
| **H9**  | The average living room size in high-standard properties is 35% larger than in low-standard properties | True |  The average living room size in high-standard properties is 38.05% larger than in low-standard properties |
| **H10** | The price of the properties are on average 10% higher in summer than in winter | False | The price of the properties are only 5.22% higher in summer compared to winter |



## Financial Results
When the solution proposed in this project is applied, the following financial result is expected:


| Total Purchase Amount | Total Sale Amount | Profit |
| :-----: | :------------------ | :-----     |
| US$ 4079586744.00 | US$ 4729811252.10 | US$ 650224508.10 |


## Conclusion

From the analysis and exploration of the data, it was possible to meet the main needs of the company, indicating the best opportunities for buying and selling real estate in the given region. In addition, important business insights were generated that will guide the company in future decisions.


## Next Steps

Collect new data for the company, in order to expand the property portfolio, as well as expand the area of operation.
