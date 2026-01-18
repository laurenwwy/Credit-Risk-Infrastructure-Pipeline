# %%
'''
Big Data Infrastructure
'''
import pyspark
print(pyspark.__version__)

# %%
import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# 1. Start a Spark Session (Infrastructure Mindset)
spark = SparkSession.builder.appName("RBC_Risk_Pipeline").getOrCreate()

# 2. Load the data we just created
df = spark.read.csv("data/raw_loans.csv", header=True, inferSchema=True)

# 3. SQL-style transformations: Logic for Risk Categorization
# This shows you understand how to segment a bank's portfolio
df_processed = df.withColumn("risk_rating", 
    when(col("credit_score") < 550, "High Risk")
    .when(col("credit_score") < 700, "Medium Risk")
    .otherwise("Low Risk")
)

# 4. Feature Engineering: Calculating Debt-to-Income (DTI) ratio
df_processed = df_processed.withColumn("DTI", col("loan_amount") / col("customer_income"))

# 5. Save the output in 'Parquet' format (Standard in Bank IT Environments)
df_processed.write.mode("overwrite").parquet("data/processed_loans.parquet")


print("Spark Pipeline Complete: Data cleaned and Risk Ratings assigned.")
print(df_processed.show(5))

# %%



