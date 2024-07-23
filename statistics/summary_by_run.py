# Databricks notebook source
# MAGIC %pip install matplotlib
# MAGIC
# MAGIC import matplotlib.pyplot as plt
# MAGIC
# MAGIC # Dummy Precision and Recall values
# MAGIC precision = [0.8, 0.85, 0.9, 0.95, 1.0]
# MAGIC recall = [0.5, 0.6, 0.7, 0.8, 0.9]
# MAGIC
# MAGIC plt.figure(figsize=(10, 6))
# MAGIC plt.plot(recall, precision, marker='o', color='b', label='Precision-Recall Curve')
# MAGIC plt.xlabel('Recall')
# MAGIC plt.ylabel('Precision')
# MAGIC plt.title('Precision vs Recall')
# MAGIC plt.legend()
# MAGIC plt.grid(True)
# MAGIC display(plt)
