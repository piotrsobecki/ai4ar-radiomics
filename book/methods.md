# Methods

We collected mpMRI imaging data from the Dolnośląskie Centrum Onkologii, Pulmonologii i Hematologii in Wrocław, Poland. The data included segmentation masks of the prostate gland and detected lesions, as well as clinical information and biopsy results with International Society of Urological Pathology (ISUP) Gleason grading for each lesion. Three experienced radiologists independently annotated the data with multiple imaging features for each lesion, using the assessment algorithm from the PI-RADS standard. 

In order to verify the hypothesis that radiomics features extracted from mpMRI images can predict the clinical significance of prostate lesions as determined by biopsy results, we used a supervised learning algorithm to train a model on the mpMRI images and the biopsy results.

We extracted the radiomics features using a dedicated library that calculated features based on the intensity, texture, and shape of the lesions. These features included measures such as the mean, standard deviation, skewness, and kurtosis of the intensity values within the lesions, as well as texture features such as the grey-level co-occurrence matrix and the grey-level run-length matrix.

We then split the data into training and testing sets, using a ratio of 80:20. We used the training set to train the model, and the testing set to evaluate the model's performance.

To assess the performance of the model, we used cross-validation to calculate the area under the receiver operating characteristic (AUC-ROC) curve, as well as other measures such as sensitivity, specificity, and F1 score. We also visualized the model's predictions using an ROC curve, which plots the true positive rate against the false positive rate.

In addition, we performed a bootstrap test to estimate the uncertainty in our results. Specifically, we resampled the data with replacement and re-ran the analysis 1000 times, calculating the mean and standard deviation of the AUC-ROC values for each resampling. This allowed us to get a sense of the range of possible values for the AUC-ROC and to determine whether our results were statistically significant.

We used a paired t-test to compare the performance of the model to the performance of radiologists in predicting the clinical significance of the lesions. We considered a p-value of less than 0.05 to be statistically significant.

Finally, we performed a hypothesis test to determine whether the performance of the model was significantly different from a random guess for each predicted imaging feature as assessed by radiologists. We used a one-sample t-test to compare the mean AUC-ROC of the model to a value of 0.5, which represents the performance expected from a random guess.

## Hypotheses

1. **Predictive models for imaging features**

    1. Hypothesis: Radiomics features extracted from mpMRI images can predict the imaging features of prostate lesions as assessed by radiologists.
    2. Hypothesis: Radiomics features can be used to predict the PI-RADS scores.
    3. Hypothesis: Radiomics features can enhance the PI-RADS algorithm to improve the assessment specificity.


2. **Predictive models for clinical significance**

    1. Hypothesis: Radiomics features extracted from mpMRI images can predict the clinical significance of prostate lesions as determined by biopsy results.
    2. Hypothesis: The combination of radiomics features and manually assessed imaging features improves the assessment of lesion clinical significance.


3. **Factors influencing the performance of predictive models for clinical significance**

    1. Hypothesis (factor): the imaging plane of the mpMRI images.
    2. Hypothesis (factor): the MRI sequence.
    3. Hypothesis (factor): the Gleason grade of the biopsy results.
    4. Hypothesis (factor): the size of the lesion.
    5. Hypothesis (factor): the location of the lesion within the prostate gland.
    6. Hypothesis (factor): the presence or absence of other conditions, such as prostate inflammation or benign prostatic hyperplasia.
    7. Hypothesis (factor): the specific radiomics features that are used as inputs (feature selection).
