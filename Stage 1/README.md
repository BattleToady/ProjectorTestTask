## Stage 1. Create any model for this dataset and save it into file. Write in README how to reproduce this solution.

# General ml-algorithm:
1. Import data
2. Fit TfidfVectorizer with min_df = 0.05, max_df = 0.95 for [excerpt] feature
3. Learn LinearRegression with y as [target] feature and x as result of step 2 feature
4. Combine it into pipeline.

# Reruning code:
Run all cells except analysis and researching ones - [Import Data, Splitting Data into train/test sets, Applying Tf-Idf vectorizer, Training Linear Regression, Metrics, Creating Pipeline, Saving Model]
