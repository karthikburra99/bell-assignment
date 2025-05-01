
# 📡 Bell Senior Data Engineer Assignment – Design Summary

For this assignment, I implemented a scalable, modular ETL pipeline using Azure-native tools combined with Python for data generation and visualization. My goal was to ensure the solution is production-minded while keeping it lightweight and cost-effective (free-tier compatible).

## 🧱 Architecture & Tools

- **Data Generation**: Python with Faker and pandas to generate ~10K–20K rows for customers, usage, and billing tables, simulating realistic variability.

- **Storage**: Azure Blob Storage (hierarchical namespace enabled) to keep the solution cloud-native and cost-efficient.

- **ETL Pipeline**: Azure Data Factory orchestrates ingestion. For this scope, I focused on file landing and validation.

- **SQL Analytics**: Synapse Analytics Serverless SQL Pool allows querying raw CSVs in Blob using `OPENROWSET` without provisioning costs.

- **Insights**:
   1. Top 10 customers by total billing (joins customers + billing)
   2. Average data usage by plan type (joins customers + usage)

- **Visualization**: Python (Matplotlib + Seaborn), since Power BI Desktop is unavailable on macOS. Charts are clear, minimal, and actionable.

## ⚙️ Design Considerations

- **Scalability**: Blob + Serverless SQL can scale to 100K+ rows without architecture change.
- **Maintainability**: Modular code, clean folder structure, extensible design.
- **Cost Efficiency**: Fully serverless solution—ideal for ad-hoc analytics.

## 🚀 Production Considerations

- Add data validation + deduplication in ADF
- Schedule pipelines with triggers
- Add logging via Log Analytics
- Publish Power BI dashboards
- Manage infra with Terraform or Bicep
