import streamlit as st
import plotly.express as px
import pandas as pd
 
def show_analysis_visuals(df):

    st.markdown("### 📊🔎 Data Analysis")

    # Count of Cars by Brand

    brand_counts = df['brand'].value_counts().reset_index()
    brand_counts.columns = ['brand', 'count']
    fig_brand = px.bar(
        brand_counts, x='brand', y='count', color='brand',
        color_discrete_sequence=px.colors.sequential.Viridis,
        title='Count of Cars by Brand'
    )

    fig_brand.update_layout(xaxis_title='Brand', yaxis_title='Count', showlegend=True)
    st.plotly_chart(fig_brand, use_container_width=True)

    # Count of Brands by Car Type
    brand_by_type = df.groupby(['car_type', 'brand']).size().reset_index(name='count')
    fig_type_brand = px.bar(
        brand_by_type,
        x='count',
        y='car_type',
        color='brand',
        orientation='h',
        title='Count of Brands by Car Type',
        color_discrete_sequence=px.colors.sequential.Inferno
    )

    fig_type_brand.update_layout(
        xaxis_title='Count',
        yaxis_title='Car Type',
        barmode='stack',
        legend_title='Brand',
        yaxis={'categoryorder': 'total ascending'}
    )
    st.plotly_chart(fig_type_brand, use_container_width=True)
 
    # Average Price by Brand

    avg_price_brand = df.groupby('brand')['price'].mean().reset_index()
    fig_avg_brand = px.line(
        avg_price_brand,
        x='brand',
        y='price',
        markers=True,
        title='Average Price by Brand',
        labels={'brand': 'Brand', 'price': 'Average Price'}
    )
    fig_avg_brand.update_layout(
        xaxis_tickangle=-45,
        xaxis_title='Brand',
        yaxis_title='Average Price',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(showgrid=True, gridcolor='lightgray', gridwidth=1)
    )
    st.plotly_chart(fig_avg_brand, use_container_width=True)
 
    # Average Price by Owner Type
    avg_price_owner = df.groupby('owner')['price'].mean().reset_index()

    fig_avg_owner = px.bar(
        avg_price_owner,
        x='owner',
        y='price',
        color='owner',
        color_discrete_sequence=px.colors.sequential.Inferno,
        title='Average Price by Owner Type',
        labels={'owner': 'Owner Type', 'price': 'Average Price'}
    )

    fig_avg_owner.update_layout(
        xaxis_title='Owner Type',
        yaxis_title='Average Price',
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig_avg_owner, use_container_width=True)
 
    # Average Price by Kilometers Driven (Binned)

    df_sorted = df.sort_values('kilometers')
    df_sorted['kilometers_bins'] = pd.cut(df_sorted['kilometers'], bins=20, include_lowest=True)
    avg_price_km = df_sorted.groupby('kilometers_bins')['price'].mean().reset_index()
    avg_price_km['kilometers_bins_str'] = avg_price_km['kilometers_bins'].astype(str)

    fig_km = px.line(
        avg_price_km,
        x='kilometers_bins_str',
        y='price',
        markers=True,
        title='Average Price by Kilometers Driven (Binned)',
        labels={'kilometers_bins_str': 'Kilometers Driven Bins', 'price': 'Average Price'}
    )

    fig_km.update_layout(
        xaxis_tickangle=-45,
        xaxis_title='Kilometers Driven Bins',
        yaxis_title='Average Price',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(showgrid=True, gridcolor='lightgray', gridwidth=1)
    )
    st.plotly_chart(fig_km, use_container_width=True)

    # Average Price by Year
    avg_price_year = df.groupby('year')['price'].mean().reset_index()
 
    fig_year = px.line(
        avg_price_year,
        x='year',
        y='price',
        markers=True,
        title='Average Price by Year',
        labels={'year': 'Year', 'price': 'Average Price'}
    )

    fig_year.update_layout(
        xaxis_title='Year',
        yaxis_title='Average Price',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(showgrid=True, gridcolor='lightgray', gridwidth=1)
    )
    st.plotly_chart(fig_year, use_container_width=True)

