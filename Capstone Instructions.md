PGD AIML Capstone Project

Learning Outcome Addressed
-Develop a robust foundational understanding of artificial intelligence (AI) and machine learning (ML) concepts and technologies
-Equip learners with the knowledge and skills to identify and implement AI solutions across various sectors effectively.
-Develop proficiency in AI/ML tools and frameworks.
-Develop a holistic understanding of AI concepts and techniques, enabling them to effectively address complex real-world problems by designing, implementing and evaluating AI and ML models.
-Develop hands-on skills in modelling, training and deploying these models in real-world applications.

Assignment instructions:
-You must attempt all the given tasks.
-This assignment carries a maximum of 100 points.
-Ensure clarity, depth and relevance in your answers to maximise your score. 

"To demonstrate the end-to-end application of the machine learning lifecycle—including problem framing, data preprocessing, modelling, evaluation and result communication—on a real-world, industry-relevant dataset of choice."

Project Domain: Cybersecurity: Detect anomalies in network traffic

Step-by-Step Instructions

Step 1: Problem Understanding & Framing 
Frame the business and data science problem clearly.
Define whether it's a classification, regression, recommendation, anomaly detection, or clustering task.
Specify success metrics (e.g., Accuracy, AUC, RMSE, Silhouette Score) and business KPIs (e.g., cost savings, uplift).
Capstone linkage: Module 1 output maps to Capstone Steps 1–3.
Deliverable: Clear problem statement + task type + target metric.
 
Step 2: Data Collection & Understanding
Use public datasets (Kaggle, UCI, APIs, etc.) or approved custom data.
Summarise feature types, missing values, outliers, etc.
Provide a data dictionary (variables, types, units, allowed values).
Deliverable: Dataset overview + data dictionary.

Step 3: Data Preprocessing, Applied EDA & Feature Engineering 
Clean data: Handle nulls, duplicates and outliers.
Engineer features: Scaling, encoding, binning and domain-derived features.
Applied EDA: Distributions, relationships, clustering tendency (if unsupervised).
Feature importance & explainability: SHAP, LIME, or model-based importances.
Feature selection: At least one approach (filter, wrapper, or embedded).
Dimensionality reduction: PCA (and t-SNE/UMAP for visualisation if needed).
Deliverable: "EDA + Feature Engineering Report" with reproducible code & justifications.

Step 4: Model Implementation 
Experiment with appropriate models:
Supervised: Logistic Regression, Decision Trees, Random Forest, XGBoost, SVM, etc.
Unsupervised: K-Means, DBSCAN, Hierarchical (Elbow, Silhouette).
Recommendation: Collaborative or content-based.
Deep Learning: RNNs, CNNs, LSTMs, Transformers (if appropriate).
Evaluation: compare with relevant metrics.
Reproducibility: save configs and artefacts (models/).
Deliverables: Trained models, metrics and comparison between models.

Step 5: Critical Thinking → Ethical AI & Bias Auditing 
Explain model decisions (SHAP, LIME, PDP, ICE).
Address limitations (imbalance, leakage, overfitting).
Bias detection & fairness audits:
Check outputs across sensitive groups (gender, race, age, socioeconomic status).
Use fairness metrics (demographic parity, equalised odds, disparate impact).
Propose mitigations (reweighting, thresholds, augmentation, post-processing).
Deliverable: "Bias & Fairness Analysis" section in the final report.

Step 6: Final Presentation & Communication 
Two deliverables for mixed audiences:
Technical presentation (Jupyter slides / LaTeX Beamer) → peers.
Business-facing presentation (PowerPoint / Canva) → executives (ROI, risks, strategy).
8–12 slides per deck recommended.
Deliverables: Two slide decks (technical + business).

Step 7: GitHub Profile & Upload 
Create a public GitHub repo  structured like an Open Source project:
Include: src/ for scripts, notebooks/, data/, models/ directories.
Deliverables: GitHub repo link + final report + reproducible code.