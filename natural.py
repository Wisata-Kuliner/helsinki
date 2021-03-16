import coremltools
from sklearn.linear_model import LinearRegression
from sklearn import svm
import pandas as pd

from sklearn import preprocessing

def main():
    # # Convert a Caffe model to a classifier in Core ML
    # coreml_model = coremltools.converters.caffe.convert(
    #     ('bvlc_alexnet.caffemodel', 'deploy.prototxt'), predicted_feature_name='class_labels.txt'
    # )

    # # Now save the model
    # coreml_model.save('BVLCObjectClassifier.mlmodel')

    # Load data
    data = pd.read_csv('split.csv')

    le = preprocessing.LabelEncoder()
    for i in range(4):
        data[:,i] = le.fit_transform(data[:,i])

    # Train a model
    model = LinearRegression()
    # model = svm.SVC()
    # model.fit(data[["bedroom", "bath", "size"]], data["price"])
    model.fit(data['raw_address'], data[['POI', 'street']])

    # # Convert and save the scikit-learn model
    # import coremltools

    # coreml_model = coremltools.converters.sklearn.convert(model, ["bedroom", "bath", "size"], "price")
    coreml_model = coremltools.converters.sklearn.convert(model, "raw_address", ["POI", "street"])

    model.author = 'John Smith'
    model.license = 'BSD'
    # model.short_description = 'Predicts the price of a house in the Seattle area.'

    # Set feature descriptions manually
    # model.input_description['bedroom'] = 'Number of bedrooms'
    # model.input_description['bathrooms'] = 'Number of bathrooms'
    # model.input_description['size'] = 'Size (in square feet)'

    # Set the output descriptions
    # model.output_description['price'] = 'Price of the house'

    # Save the model
    model.save('HousePricer.mlmodel')

    # import coremltools

    # # Load the model
    # model = coremltools.models.MLModel('HousePricer.mlmodel')

    # # Make predictions
    # predictions = model.predict({'bedroom': 1.0, 'bath': 1.0, 'size': 1240})

    # import coremltools

    # # Load the model
    # model = coremltools.models.MLModel('HousePricer.mlmodel')

    # # Visualize the model
    # model.visualize_spec()

if __name__ == "__main__":
    main()