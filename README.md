
# 📡 Bell Senior Data Engineer Assignment

## 📘 Overview

This project delivers an end-to-end, cloud-native ETL solution that processes synthetic telecom data, executes analytical SQL queries, and generates actionable insights through visualizations.

The architecture emphasizes scalability, simplicity, and modularity, using Azure and Python tools that align with industry best practices.

---

## 🚀 Architecture Summary

### 📦 Data Generation
- Python script (`scripts/generate_telecom_data.py`) creates:
  - `data/customers.csv`
  - `data/usage.csv`
  - `data/billing.csv`

### ☁️ Cloud Storage
- Azure Blob Storage (`synapse-data` container)  
- Data ingested and stored for analytics

### 🔄 ETL Pipeline
- Azure Data Factory pipelines to ingest and land data into Blob Storage

### 💬 SQL Analytics
- Synapse Analytics (Serverless SQL pool)
- Queries using `OPENROWSET` directly on raw CSVs in Blob

### 📊 Visualization
- Python (`scripts/visualize_assignment_improved.py`)  
- Matplotlib + Seaborn to produce:
  - `outputs/top_10_customers_improved.png`
  - `outputs/avg_data_usage_by_plan_improved.png`

---

## 💡 SQL Queries

1. **Top 10 Customers by Total Billing**
   - Aggregated `billing.csv` + `customers.csv`
   - Ranked by total billed amount (descending)

2. **Average Data Usage by Plan Type**
   - Aggregated `usage.csv` + `customers.csv`
   - Grouped by plan type, showing average GB usage

---

---

## 💥 Bonus: Terraform Infrastructure Automation

The project includes Terraform scripts to automate cloud resource setup.

- **Infra components provisioned:**
  - Resource Group (`telecom-assignment-rg`)
  - Storage Account (`telecomdatalake123`) with ADLS Gen2
  - Filesystem Container (`synapse-data`)
  - Synapse Workspace (`telecom-synapse`)
  - Firewall Rule (AllowAll)

- **Azure region:**  
  `East US 2` (due to SQL provisioning restrictions in East US)

- **Import management:**  
  Existing Azure resources were imported into Terraform state using:
  ```
  terraform import azurerm_resource_group.rg ...
  terraform import azurerm_storage_account.storage ...
  terraform import azurerm_storage_data_lake_gen2_filesystem.synapse_fs ...
  terraform import azurerm_synapse_workspace.synapse ...
  ```

- **CI/CD automation:**  
  GitHub Actions pipeline defined in `.github/workflows/terraform.yml` for plan/apply on push.

---

## 📁 Folder Structure

```
bell-assignment/
├── data/
│   ├── customers.csv
│   ├── usage.csv
│   └── billing.csv
├── scripts/
│   ├── generate_telecom_data.py
│   └── visualize_assignment_improved.py
├── sql/
│   └── queries.sql
├── outputs/
│   ├── top_10_customers_improved.png
│   └── avg_data_usage_by_plan_improved.png
├── infra/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
└── README.md
```


## 📧 Contact

Karthik B
https://www.linkedin.com/in/karthikburra/


