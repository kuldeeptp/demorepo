# Databricks notebook source
# MAGIC %fs ls 

# COMMAND ----------

# MAGIC %run ./notebook2

# COMMAND ----------

print("Hello ", name1)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title1
# MAGIC ## Title2
# MAGIC ### Title3
# MAGIC
# MAGIC Orderes list
# MAGIC 1. one
# MAGIC 1. tow
# MAGIC 1. three 
# MAGIC
# MAGIC Unorders list
# MAGIC * Apple
# MAGIC * Mango
# MAGIC * Banana
# MAGIC
# MAGIC Tables
# MAGIC |user_id | user_name |
# MAGIC |--------|-----------|
# MAGIC | KKK    | Pal       |
# MAGIC
# MAGIC
# MAGIC <a href="https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Resources/QuickstartTutorialBlade/checklistId/get-started-with-azure/sectionId/get-started-navigating-the-portal/lessonId/get-started-navigating-azure-portal"> Manage and organize Azure resources</a>
# MAGIC
# MAGIC

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
display(files)

# COMMAND ----------

# MAGIC %run ../demo/notebook2
