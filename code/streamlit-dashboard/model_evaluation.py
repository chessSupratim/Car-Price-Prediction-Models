import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from pathlib import Path
 
def show_model_evaluation(df):

    # Build consistent paths
    model_files = {
        "Linear Regression": "linearRegression_model.joblib",
        "Random Forest": "randomForest_model.joblib",
        "XGBoost": "xgboost_model.joblib",
        "AdaBoost": "ada_model.joblib",
        "DecissionTree": "dt_model.joblib",
        "LGBM": "lgbm_model.joblib",
    }

    preprocessor_file = "preprocessor.joblib"
    feature_info_file = "feature_info.pkl"

    preprocessor = joblib.load(preprocessor_file)
    with open(feature_info_file, "rb") as f:
         feature_info = pd.read_pickle(f) if feature_info_file.endswith(".pkl") else joblib.load(f)
 
    cat_features = feature_info["categorical"]
    num_features = feature_info["numerical"]
 
    #USER INPUT------------------------------------------------------------
    st.markdown("### 🧠 Predict Car Price")
    selected_row = st.selectbox(
        "Select a car by index:",
        options=[None] + list(df.index)
    )
    selected_models = st.multiselect(
        "Select Model(s):",
        options=list(model_files.keys())
    )
 
    #PREDICTION---------------------------------------------------------------------------
    if selected_row is not None and selected_models:
        input_data = df.loc[selected_row, cat_features + num_features].to_dict()
        actual_price = df.loc[selected_row, "price"]
 
        # Display features
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("Numerical Features")
            num_table = pd.DataFrame({
                "Feature": num_features,
                "Value": [input_data[col] for col in num_features]
            })
            st.dataframe(num_table, use_container_width=True)
        with col2:
            st.markdown("Categorical Features")
            cat_table = pd.DataFrame({
                "Feature": cat_features,
                "Value": [input_data[col] for col in cat_features]
            })
            st.dataframe(cat_table, use_container_width=True)
 
        input_df = pd.DataFrame([input_data])
 
        # Predict button
        if st.button("🔮 Predict Price"):
            try:
                X_processed = preprocessor.transform(input_df)
                predictions = {}
                for model_name in selected_models:
                    model = joblib.load(model_files[model_name])
                    predictions[model_name] = model.predict(X_processed)[0]
 
                # Display predictions
                for model_name, price in predictions.items():
                    st.success(f"💰 **{model_name} Predicted Price:** ₹{price:,.2f}")
                st.info(f"🏷️ **Actual Price:** ₹{actual_price:,.2f}")
 
                # Plot predictions
                fig = px.bar(
                    x=[*predictions.keys(), "Actual Price"],
                    y=[*predictions.values(), actual_price],
                    text=[f"₹{v:,.0f}" for v in predictions.values()] + [f"₹{actual_price:,.0f}"],
                    color=[*predictions.keys(), "Actual Price"],
                    color_discrete_sequence=px.colors.qualitative.Set2
                )
                fig.update_layout(
                    yaxis_title="Price (₹)",
                    xaxis_title="",
                    showlegend=False,
                    title="Predicted vs Actual Car Price"
                )
                st.plotly_chart(fig, use_container_width=True)
 
                # Automatically display best model based on smallest error
                errors = {model: abs(actual_price - pred) for model, pred in predictions.items()}
                best_model = min(errors, key=errors.get)
                st.success(f"🏅 Best Model for this car: {best_model} (smallest error: ₹{errors[best_model]:,.2f})")
 
            except Exception as e:
                st.error(f"Prediction failed: {e}")
 
    elif selected_row is None:
        st.warning("⚠️ Please select a valid row index from the dropdown to make a prediction.")
    elif not selected_models:
        st.warning("⚠️ Please select at least one model to predict.")