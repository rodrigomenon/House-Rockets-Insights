# imports
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')


# load data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data

def overview_data(data):
    overview_bar = st.sidebar
    with overview_bar:
        st.header("Choose the elements to compose the dashboard")

    overview_container = st.container()
    with overview_container:
        st.title("Web Aplication for House Rockets portfolio's dashboard")
        st.header('Sample of the portfolio')
        st.dataframe(data.head(20))
        st.write(f"This dataset contains {data.shape[0]} registers and"
                 f" {data.shape[1]} columns")
        return None

def statistics(data):
    statistics_container = st.container()
    with statistics_container:
        f_statistics = st.sidebar.checkbox(label="Descriptive Statistics")
        if f_statistics:
            st.subheader("Descriptive Statistics")
            descriptive_statistics = data.describe().T
            descriptive_statistics.drop(index=['id', 'zipcode', 'lat', 'long'], inplace=True)
            st.dataframe(descriptive_statistics)

    return None

def insights(data):
    business_container = st.container()
    f_business = st.sidebar.checkbox(label="Business Hypothesis")
    if f_business:

        with business_container:
            st.header("Business Hypothesis")
            c1, c2 = st.columns(2)
            with c1:
                st.subheader("H1- Waterfront properties are 30% more expensive, on average")
                # data
                avg_waterfront_price = data[['price', 'is_waterfront']].groupby('is_waterfront').mean().sort_values(
                    by='price', ascending=False).reset_index()

                # plot
                fig = px.bar(x='is_waterfront', y='price', data_frame=avg_waterfront_price)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h1_test = (avg_waterfront_price.loc[0, 'price'] - avg_waterfront_price.loc[1, 'price']) / \
                          avg_waterfront_price.loc[1, 'price'] * 100
                st.markdown(f"**TRUE: Waterfront properties are on average {h1_test:.2f}% more expensive than properties with no water view**")

            with c2:
                st.subheader("H2- Properties built before 1955 are 50% cheaper in average")
                #data
                avg_house_age_price = data[['price', 'house_age']].groupby('house_age').mean().reset_index()

                #plot
                fig = px.bar(x='house_age', y='price', data_frame=avg_house_age_price)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h2_test = (avg_house_age_price.loc[0, 'price'] - avg_house_age_price.loc[1, 'price']) / \
                          avg_house_age_price.loc[1, 'price'] * 100
                st.markdown(f"**FALSE: Properties built before 1955 are only {h2_test:.2f} cheaper than those built after 1955**")

            c3, c4 = st.columns(2)
            with c3:
                st.subheader("H3: Properties without basement have, in average,sqft_lot 50% bigger than properties with basement")

                # data
                avg_sqftlot_basement = data[['sqft_lot', 'basement']].groupby('basement').mean().reset_index()

                # plot
                fig = px.bar(x='basement', y='sqft_lot', data_frame=avg_sqftlot_basement)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h3_test = (avg_sqftlot_basement.loc[0, 'sqft_lot'] - avg_sqftlot_basement.loc[1, 'sqft_lot']) /\
                          avg_sqftlot_basement.loc[0, 'sqft_lot'] * 100
                st.markdown(f"**FALSE: Properties without basement have sqft_lot {h3_test:.2f}% bigger than properties with basement**")

            with c4:
                st.subheader("H4: The average growth in property prices YoY (year over year) is 10%")

                # data
                avg_price_year = data[['price', 'year']].groupby('year').mean().reset_index()

                # plot
                fig = px.bar(x='year', y='price', data_frame=avg_price_year)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h4_test = (avg_price_year.loc[1, 'price'] - avg_price_year.loc[0, 'price']) /\
                          avg_price_year.loc[1, 'price'] * 100
                st.markdown(f"**FALSE: The average price growth year over year is {h4_test:.2f}%**")


            c5, c6 = st.columns(2)
            with c5:
                st.subheader("H5: Properties with 3 bathrooms have an average price growth month over month (MoM) about 15%")

                # data
                avg_price_bathroom = data.loc[data['bathrooms'] == 3, ['price', 'month']].groupby('month').mean().reset_index()

                variation = [0]
                for i in range(0, 12):
                    if i == 0:
                        pass
                    else:
                        variation.append((avg_price_bathroom.loc[i, 'price'] - avg_price_bathroom.loc[i - 1, 'price']) /
                                         avg_price_bathroom.loc[i - 1, 'price'] * 100)

                avg_price_bathroom['% variation'] = variation

                # plot
                fig = px.line(x='month', y='price', data_frame=avg_price_bathroom)
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("**FALSE: There is no constant average growth in the price of 3-bathroom properties**")


            with c6:
                st.subheader("H6: Properties in excellent condition are in average, 25% more expensive than properties in terrible condition")

                # data
                avg_price_condition = data.loc[
                    data['condition_type'].isin(['terrible', 'excellent']), ['price', 'condition_type']].groupby(
                    'condition_type').mean().reset_index()

                # plot
                fig = px.bar(x='condition_type', y='price', data_frame=avg_price_condition)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis test
                h6_test = (avg_price_condition.loc[0, 'price'] - avg_price_condition.loc[1, 'price']) / \
                          avg_price_condition.loc[0, 'price'] * 100
                st.markdown(f"**TRUE: Properties in excellent condition are, in average {h6_test:.2f}% more expensive than properties in terrible condition**")

            c7, c8 = st.columns(2)
            with c7:
                st.subheader("H7: The price of properties with more than 50 years of construction and which have undergone renovation"
                             " is in average, 20% higher than those that have not been renovated")

                # data
                avg_price_renovated = data.loc[data['yr_built'] < 1965, ['price', 'renovated']].groupby(
                    'renovated').mean().reset_index()

                # plot
                fig = px.bar(x='renovated', y='price', data_frame=avg_price_renovated)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h7_test = (avg_price_renovated.loc[1, 'price'] - avg_price_renovated.loc[0, 'price']) / \
                          avg_price_renovated.loc[1, 'price'] * 100

                st.markdown(f"**TRUE: The price of properties with more than 50 years of construction and undergone renovation"
                            f" are in average {h7_test:.2f}% higher than those that haven't been renovated **")

            with c8:
                st.subheader("H8: In properties with water view, the price is on average 20% higher for those with an"
                             " excellent view, compared to those with a regular view")

                # data
                avg_waterfront_view = data.loc[
                    (data['is_waterfront'] == 'yes') & (data['view_type'].isin(['regular', 'excellent'])), ['price',
                                                                                                            'view_type']].groupby(
                    'view_type').mean().reset_index()

                # plot
                fig = px.bar(x='view_type', y='price', data_frame=avg_waterfront_view)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h8_test = (avg_waterfront_view.loc[1, 'price'] - avg_waterfront_view.loc[0, 'price']) / \
                          avg_waterfront_view.loc[0, 'price'] * 100
                st.markdown(f"**FALSE: The average price of properties with water view is {h8_test:.2f}% higher for those with"
                            f" regular view, compared to those with excellent view**")

            c9, c10 = st.columns(2)
            with c9:
                st.subheader("H9: The average living room size in high-standard properties is 35% larger than in low-standard properties")

                # data
                avg_sqft_living_standard = data[['sqft_living', 'standard']].groupby('standard').mean().reset_index()

                # plot
                fig = px.bar(x='standard', y='sqft_living', data_frame=avg_sqft_living_standard)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h9_test = (avg_sqft_living_standard.loc[0, 'sqft_living'] - avg_sqft_living_standard.loc[1, 'sqft_living']) / \
                          avg_sqft_living_standard.loc[0, 'sqft_living'] * 100

                st.markdown(f"**TRUE: The average living room size in high-standard properties is {h9_test:.2f}% larger than in low-standard properties**")


            with c10:
                st.subheader("H10: The price of the properties are on average 10% higher in summer than in winter")

                # data
                avg_price_season = data.loc[data['seasons'].isin(['summer', 'winter']), ['seasons', 'price']].groupby(
                    'seasons').mean().reset_index()

                # plot
                fig = px.bar(x='seasons', y='price', data_frame=avg_price_season)
                st.plotly_chart(fig, use_container_width=True)

                # hypothesis_test
                h10_test = (avg_price_season.loc[0, 'price'] - avg_price_season.loc[1, 'price']) / avg_price_season.loc[0, 'price'] * 100

                st.markdown(f"**FALSE: The price of the properties are {h10_test:.2f}% higher in summer compared to winter**")
    return None

def business_questions(data):
    business_questions_container_1 = st.container()
    with business_questions_container_1:
        st.title("Business Problem 1 - What properties should House Rockets buy and for which price?")

        # data
        df = data[['price', 'zipcode']].groupby('zipcode').median().sort_values(by='price').reset_index()
        df.rename(columns={'price': 'median_price'}, inplace=True)

        data = pd.merge(data, df, how='inner')
        data['buy'] = data[['price', 'median_price', 'condition']].apply(
            lambda x: 'yes' if (x['price'] < x['median_price']) & (x['condition'] >= 3) else 'no', axis=1)

        df_buy_opportunities = data.loc[data['buy'] == 'yes', ['id', 'zipcode', 'lat', 'long', 'yr_built', 'yr_renovated',
                                                               'condition', 'condition_type', 'view_type',
                                                               'dormitory_type', 'bedrooms', 'bathrooms', 'sqft_living',
                                                               'sqft_lot', 'floors', 'standard', 'seasons', 'price',
                                                               'median_price', 'buy']].sort_values(
            by=['price', 'condition'], ascending=[True, False]).reset_index(drop=True)


        # create side bar
        attributes_side_bar = st.sidebar
        attributes_side_bar.header("Choose the filters for the 1st business problem")
        attributes_side_bar.subheader("Attributes")

        # filters
        f_zipcode = attributes_side_bar.multiselect('zipcode',
                           options=sorted(df_buy_opportunities['zipcode'].unique().tolist()))

        f_yr_built = attributes_side_bar.multiselect('Year built',
                           options=sorted(df_buy_opportunities['yr_built'].unique().tolist()))

        # data
        st.write(f"From the initial portfolio, {df_buy_opportunities.shape[0]} properties were recommended")

        # show data
        if (f_zipcode != []) and (f_yr_built != []):
            df = df_buy_opportunities[(df_buy_opportunities['zipcode'].isin(f_zipcode) & (df_buy_opportunities['yr_built'].isin(f_yr_built)))]
        elif (f_zipcode != []) and (f_yr_built == []):
            df = df_buy_opportunities[df_buy_opportunities['zipcode'].isin(f_zipcode)]
        elif (f_zipcode == []) and (f_yr_built != []):
            df = df_buy_opportunities[df_buy_opportunities['yr_built'].isin(f_yr_built)]
        else:
            df = df_buy_opportunities
        st.dataframe(df)

    business_questions_container_2 = st.container()
    with business_questions_container_2:
        st.title("Business Problem 2 - Once the property is purchased, what is the best moment to sell it and for what price?")

        # data
        df2 = df_buy_opportunities[['zipcode', 'seasons', 'price']].groupby(
            ['zipcode', 'seasons']).median().reset_index()
        df2.rename(columns={'price': 'median_seasons_price'}, inplace=True)

        df3 = pd.merge(df_buy_opportunities, df2, how='inner', on=['zipcode', 'seasons'])
        for i in range(len(df3)):
            if df3.loc[i, 'price'] > df3.loc[i, 'median_seasons_price']:
                df3.loc[i, 'sale_price'] = (df3.loc[i, 'price'] * 1.1)

            elif df3.loc[i, 'price'] < df3.loc[i, 'median_seasons_price']:
                df3.loc[i, 'sale_price'] = df3.loc[i, 'price'] * 1.3

        # create side bar
        attributes_side_bar_1 = st.sidebar
        attributes_side_bar_1.header("Choose the filters for the 2nd business problem")
        attributes_side_bar_1.subheader("Attributes")

        # filters
        f_zipcode_1 = attributes_side_bar_1.multiselect('zipcode', key='ok',
                                                    options=sorted(df3['zipcode'].unique().tolist()))

        f_yr_built_1 = attributes_side_bar_1.multiselect('Year built',key='ok',
                                                     options=sorted(df3['yr_built'].unique().tolist()))

        # data
        st.write(f"Once purchased, the properties bellow were identified as potential for sale.")
        df_sale = df3.copy()

        # show data
        if (f_zipcode_1 != []) and (f_yr_built_1 != []):
            df_sale = df3[
                (df3['zipcode'].isin(f_zipcode_1) & (df3['yr_built'].isin(f_yr_built_1)))]
        elif (f_zipcode_1 != []) and (f_yr_built_1 == []):
            df_sale = df3[df3['zipcode'].isin(f_zipcode_1)]
        elif (f_zipcode_1 == []) and (f_yr_built_1 != []):
            df_sale = df3[df3['yr_built'].isin(f_yr_built_1)]
        else:
            df_sale = df3

        st.dataframe(df_sale)

    return None



if __name__ == "__main__":
    path = "data/kc_cleaned.csv"

    data = get_data(path)
    overview_data(data)
    statistics(data)
    insights(data)
    business_questions(data)
