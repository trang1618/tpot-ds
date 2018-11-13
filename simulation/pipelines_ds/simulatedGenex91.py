import numpy as np
import pandas as pd
from sklearn.kernel_approximation import RBFSampler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import make_pipeline
from tpot.builtins import DatasetSelector

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=91)

# Average CV score on the training set was:0.6334816462736375
exported_pipeline = make_pipeline(
    DatasetSelector(sel_subset=10, subset_list="subsets.csv"),
    RBFSampler(gamma=0.7000000000000001),
    BernoulliNB(alpha=0.001, fit_prior=True)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
