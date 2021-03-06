#!/bin/bash

#Extract features
python baseline_implementation/extract_features.py pretrained_model/hotels50k_snapshot/hotels50k

#Produce CSV file needed for the retrieval evaluation
python baseline_implementation/feats_to_csv.py

#Convert Retrieval results to probabilities:
python evaluate/convert_knn_to_probabilities.py baseline_implementation/csv_output/unoccluded.csv baseline_implementation/csv_output/unoccluded_class_probabilities.csv
python evaluate/convert_knn_to_probabilities.py baseline_implementation/csv_output/low_occlusions.csv baseline_implementation/csv_output/low_occlusions_class_probabilities.csv
python evaluate/convert_knn_to_probabilities.py baseline_implementation/csv_output/medium_occlusions.csv baseline_implementation/csv_output/medium_occlusions_class_probabilities.csv
python evaluate/convert_knn_to_probabilities.py baseline_implementation/csv_output/high_occlusions.csv baseline_implementation/csv_output/high_occlusions_class_probabilities.csv

#Evaluate
python evaluate/retrieval.py baseline_implementation/csv_output/unoccluded.csv
python evaluate/retrieval.py baseline_implementation/csv_output/low_occlusions.csv
python evaluate/retrieval.py baseline_implementation/csv_output/medium_occlusions.csv
python evaluate/retrieval.py baseline_implementation/csv_output/high_occlusions.csv

#Calculate posterior probabilities for classification
python evaluate/log_loss.py baseline_implementation/csv_output/unoccluded_class_probabilities.csv
python evaluate/log_loss.py baseline_implementation/csv_output/low_occlusions_class_probabilities.csv
python evaluate/log_loss.py baseline_implementation/csv_output/medium_occlusions_class_probabilities.csv
python evaluate/log_loss.py baseline_implementation/csv_output/high_occlusions_class_probabilities.csv