Project Title

Predictive Maintenance of Wind Turbine Gearbox Using SCADA Time-Series Data

1. Business Understanding
Objective

The goal of this project is to develop a machine learning model capable of predicting gearbox failures in a utility-scale wind turbine using SCADA time-series data.

Business Motivation

Gearbox failures are among the most expensive and maintenance-intensive issues in wind turbines. Early detection of degradation patterns allows operators to:

Reduce unplanned downtime

Optimize maintenance scheduling

Lower operational costs

Increase turbine lifetime

Research Question

Can gearbox failures be predicted in advance using temperature, vibration, pressure, and oil condition data?

2. Data Understanding
Dataset Description

The dataset contains 5 years of high-resolution SCADA data recorded at 10-minute intervals. The labeled version includes a target variable indicating the operational state or failure mode.

Key Variables

timestamp – time of measurement

gearbox_oil_temp – lubrication oil temperature (°C)

gearbox_bearing_temp – bearing temperature (°C)

vibration_x, vibration_y, vibration_z – vibration levels

oil_pressure – lubrication system pressure (bar)

particle_count – metallic debris concentration

label – operational state / failure indicator

Initial Exploration

Check class distribution

Visualize time trends

Inspect correlations

Identify seasonality and degradation trends

3. Data Preparation
Cleaning and Formatting

Convert timestamp to datetime

Sort chronologically

Handle missing values (if any)

Remove duplicates

Feature Engineering

Extract time-based features (hour, month)

Create rolling statistics:

Rolling mean (1h, 6h, 24h)

Rolling standard deviation

Compute rate of change for:

Vibration

Temperature

Aggregate vibration magnitude

Data Transformation

Normalize or standardize features

Encode labels if necessary

Split dataset:

Train set

Validation set

Test set

Time-aware splitting will be used to avoid data leakage.

4. Modeling
Baseline Model

Logistic Regression

Advanced Models

Random Forest

Gradient Boosting (e.g., XGBoost)

Training Strategy

Time-series aware validation

Hyperparameter tuning

Cross-validation (if appropriate)

5. Evaluation
Evaluation Metrics

Accuracy

Precision

Recall

F1-score

ROC-AUC

Additional Analysis

Confusion Matrix

Feature Importance

False Positive vs False Negative impact

Special focus will be given to recall for failure detection to minimize missed failures.

6. Deployment & Interpretation
Practical Application

The model could be integrated into a SCADA monitoring system to:

Generate early warnings

Support maintenance planning

Reduce emergency repairs

Business Impact

Increased reliability

Lower operational costs

Improved asset management

Expected Outcome

The project aims to demonstrate that gearbox failures can be predicted using sensor-based time-series data and that certain features (e.g., vibration growth and temperature increase) act as early indicators of degradation.