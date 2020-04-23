# Data Preparation

The data from the OCR is [unstructured](https://en.wikipedia.org/wiki/Unstructured_data) and [unlabelled](https://www.techopedia.com/definition/33696/unlabeled-data), and hence could not be used directly for machine learning. We tried to convert the data to a structured and labelled data.

The columns of the table contained:
* **word**: The text extracted from the ocr
* **marker type**: Upright or flat marker type
* **location**: Front or back of the headstone
* **coordinates**: The (x,y) coordinates of the rectangular polygon
* **category**: The column in which the word belongs in the database

Used the [**min-cost max flow algorithm**](https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/tutorial/) to find the column of the word that was extracted from the OCR.
