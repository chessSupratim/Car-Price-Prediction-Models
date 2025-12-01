import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
 
def show_manual_input_prediction(df):

    # ----------------- LOAD MODELS & PREPROCESSOR -----------------
    model_files = {
        "Linear Regression": "linearRegression_model.joblib",
        "Random Forest": "randomForest_model.joblib",
        "XGBoost": "xgboost_model.joblib",
        "DecissionTree": "dt_model.joblib",
        "AdaBoost": "ada_model.joblib",
        "LGBM": "lgbm_model.joblib"
    }
 
    preprocessor_file = "preprocessor.joblib"
    feature_info_file = "feature_info.pkl"
 
    preprocessor = joblib.load(preprocessor_file)
    with open(feature_info_file, "rb") as f:
        feature_info = pd.read_pickle(f) if feature_info_file.endswith(".pkl") else joblib.load(f)
 
    cat_features = feature_info["categorical"]
    num_features = feature_info["numerical"]
 
    # ----------------- USER INPUT FOR FEATURES -----------------
    st.markdown("### ✍️ Manual Car Feature Input")
    st.markdown("Enter values for the following features:")
 
    # Dictionary to store input values
    input_data = {}
 
    # Numeric features
    for feature in num_features:
        min_val = float(df[feature].min())
        max_val = float(df[feature].max())
        step = 1.0 if df[feature].dtype != "float64" else 0.1
        input_data[feature] = st.number_input(
            label=f"{feature} (Numeric)",
            min_value=min_val,
            max_value=max_val,
            value=float(df[feature].median()),
            step=step
        )
 
    # Categorical features
    for feature in cat_features:
        options = df[feature].unique().tolist()
        input_data[feature] = st.selectbox(
            label=f"{feature} (Categorical)",
            options=options,
            index=0
        )
 
    # ----------------- SELECT MODELS -----------------
    selected_models = st.multiselect(
        "Select Model(s) to Predict:",
        options=list(model_files.keys())
    )
 
    # ----------------- PREDICTION -----------------
    if st.button("🔮 Predict Price for Input"):
        if not selected_models:
            st.warning("⚠️ Please select at least one model.")
        else:
            try:
                input_df = pd.DataFrame([input_data])
                X_processed = preprocessor.transform(input_df)
 
                predictions = {}
                for model_name in selected_models:
                    model = joblib.load(model_files[model_name])
                    predictions[model_name] = model.predict(X_processed)[0]
 
                # Display predictions
                for model_name, price in predictions.items():
                    st.success(f"💰 **{model_name} Predicted Price:** ₹{price:,.2f}")
 
                # Plot predictions
                fig = px.bar(
                    x=[*predictions.keys()],
                    y=[*predictions.values()],
                    text=[f"₹{v:,.0f}" for v in predictions.values()],
                    color=[*predictions.keys()],
                    color_discrete_sequence=px.colors.qualitative.Set2,
                    title="Predicted Car Price"
                )
                fig.update_layout(
                    yaxis_title="Price (₹)",
                    xaxis_title="",
                    showlegend=False
                )
                st.plotly_chart(fig, use_container_width=True)
 
            except Exception as e:
                st.error(f"Prediction failed: {e}")