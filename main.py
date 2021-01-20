# DEVELOPED BY PRASHANT AND TEAM 12 (FIT3164)
# START OF FIT3164 CODE (main.py)

# THIS FILE CONTAINS CODE FOR DATA LOADING/CLEANING, FEATURE SELECTION, AND ENSEMBLE CLASSIFIER MODELLING.
# ALL SECTIONS ARE DIVIDED BY A COMMENT DIVIDER AND A HEADER.

################################################################
# DATA CLEANING AND RESHAPING PROCESS
################################################################

# Import pandas library for dataframe
import pandas as pd
# Dataset provided by Z-Alizadeh Sani (refer to final report for documentation)
dataset = pd.read_csv("CAD4.csv")

# Convert dataset to dataframe
df = pd.DataFrame(dataset)
print("Start of code output:\n")
print("Viewing initial dataframe:")
print(df)

# View the data types and summary
print("Viewing data types and description:")
print(df.dtypes)
print(df.describe())

print("\n")

# First, check if there are any null values in the dataframe
total_empty_values = (df.isnull().sum().sum())
print("Number of missing or null values in the dataframe:" + str(total_empty_values))
# Print a simple diagnosis to show if data imputation/further cleaning is needed.
if total_empty_values == 0:
    print("Data imputation is not needed.")
else:
    print("Data imputation is required to resolve null values in the dataframe.")
    # Note that there are many packages that offer data imputation methods in the event that the
    # dataset is not of a satisfactory level in terms of data quality/cleanliness.

# Next, shape the data into appropriate type and columns.
# Note that when the data types were checked at the start, it was found that the
# dataset had many categorical columns which are non-binary, along with binary columns
# that are not in the 0/1 format. These columns will have to be reshaped to form a
# proper binary column.

# First convert binary columns that are not in the correct format, to a 0/1 format

# Convert "Sex" column into 1,0
# The "count" variable is used in here, and the following segments of code, to
# indicate the row number.
count = 0
# 0 for male, 1 for female
for row in df['Sex']:
    if row == "Male":
        df.at[count, 'Sex'] = 0
    if row == "Fmale":
        df.at[count, 'Sex'] = 1
    count += 1
# Convert the column to numeric type
df['Sex'] = pd.to_numeric(df['Sex'])


# Convert "Cath" column into 1,0
count = 0
# 0 for Normal, 1 for Cad
for row in df['Cath']:
    if row == "Normal":
        df.at[count, 'Cath'] = 0
    if row == "Cad":
        df.at[count, 'Cath'] = 1
    count += 1
# Convert the column to numeric type
df['Cath'] = pd.to_numeric(df['Cath'])


# Function to convert other Y/N columns to 1/0
def convert_categorical(df, column):
    """Function to convert Yes/No categorical columns
    into a 0/1 format."""
    count = 0
    # 0 for NO, 1 for YES
    for row in df[column]:
        if row == "N":
            df.at[count, column] = 0
        if row == "Y":
            df.at[count, column] = 1
        count += 1
    # Convert the column to numeric type
    df[column] = pd.to_numeric(df[column])


# Call function on all other columns that have Y/N values to convert them into 1/0
convert_categorical(df, "Obesity")
convert_categorical(df, "CRF")
convert_categorical(df, "CVA")
convert_categorical(df, "Airway disease")
convert_categorical(df, "Thyroid Disease")
convert_categorical(df, "CHF")
convert_categorical(df, "DLP")
convert_categorical(df, "Weak Peripheral Pulse")
convert_categorical(df, "Lung rales")
convert_categorical(df, "Systolic Murmur")
convert_categorical(df, "Diastolic Murmur")
convert_categorical(df, "Dyspnea")
convert_categorical(df, "Atypical")
convert_categorical(df, "Nonanginal")
convert_categorical(df, "Exertional CP")
convert_categorical(df, "LowTH Ang")
convert_categorical(df, "LVH")
convert_categorical(df, "Poor R Progression")


# Now we will convert non-binary categorical columns into separate
# columns that can hold binary 0/1 values.

# Convert Male/Female into separate columns
# First create empty columns for both and Male and Female
df["Male"] = ""
df["Female"] = ""
# Put 0 if the gender is not the value labelled in the column name,
# and 1 if it is equal to the gender labelled in the column name.
count = 0
# 0 for NO, 1 for YES
for row in df["Sex"]:
    if row == 0:
        df.at[count, "Male"] = 1
        df.at[count, "Female"] = 0
    if row == 1:
        df.at[count, "Male"] = 0
        df.at[count, "Female"] = 1
    count += 1
# Convert new columns to numeric, and delete the previous "Sex" column.
df["Male"] = pd.to_numeric(df["Male"])
df["Female"] = pd.to_numeric(df["Female"])
df = df.drop(['Sex'], axis=1)


# Next is to convert function class into separate columns
# First create empty columns for all 5 Function Classes
df["Function Class 0"] = ""
df["Function Class 1"] = ""
df["Function Class 2"] = ""
df["Function Class 3"] = ""
df["Function Class 4"] = ""
# Put 0 if the Function Class is not the value labelled in the column name,
# and 1 if it is equal to the Function Class labelled in the column name.
count = 0
# 0 for NO, 1 for YES
for row in df["Function Class"]:
    if row == 0:
        df.at[count, "Function Class 0"] = 1
        df.at[count, "Function Class 1"] = 0
        df.at[count, "Function Class 2"] = 0
        df.at[count, "Function Class 3"] = 0
        df.at[count, "Function Class 4"] = 0
    if row == 1:
        df.at[count, "Function Class 0"] = 0
        df.at[count, "Function Class 1"] = 1
        df.at[count, "Function Class 2"] = 0
        df.at[count, "Function Class 3"] = 0
        df.at[count, "Function Class 4"] = 0
    if row == 2:
        df.at[count, "Function Class 0"] = 0
        df.at[count, "Function Class 1"] = 0
        df.at[count, "Function Class 2"] = 1
        df.at[count, "Function Class 3"] = 0
        df.at[count, "Function Class 4"] = 0
    if row == 3:
        df.at[count, "Function Class 0"] = 0
        df.at[count, "Function Class 1"] = 0
        df.at[count, "Function Class 2"] = 0
        df.at[count, "Function Class 3"] = 1
        df.at[count, "Function Class 4"] = 0
    if row == 4:
        df.at[count, "Function Class 0"] = 0
        df.at[count, "Function Class 1"] = 0
        df.at[count, "Function Class 2"] = 0
        df.at[count, "Function Class 3"] = 0
        df.at[count, "Function Class 4"] = 1
    count += 1
# Convert new columns to numeric, and delete the previous "Function Class" column.
df["Function Class 0"] = pd.to_numeric(df["Function Class 0"])
df["Function Class 1"] = pd.to_numeric(df["Function Class 1"])
df["Function Class 2"] = pd.to_numeric(df["Function Class 2"])
df["Function Class 3"] = pd.to_numeric(df["Function Class 3"])
df["Function Class 4"] = pd.to_numeric(df["Function Class 4"])
df = df.drop(['Function Class'], axis=1)


# Next is to convert the BBB attribute into separate columns
# First create empty columns for all 3 types of "BBB"
df["BBB_LBBB"] = ""
df["BBB_N"] = ""
df["BBB_RBBB"] = ""
# Put 0 if the BBB type is not the value labelled in the column name,
# and 1 if it is equal to the BBB type labelled in the column name.
count = 0
# 0 for NO, 1 for YES
for row in df["BBB"]:
    if row == "LBBB":
        df.at[count, "BBB_LBBB"] = 1
        df.at[count, "BBB_N"] = 0
        df.at[count, "BBB_RBBB"] = 0
    if row == "N":
        df.at[count, "BBB_LBBB"] = 0
        df.at[count, "BBB_N"] = 1
        df.at[count, "BBB_RBBB"] = 0
    if row == "RBBB":
        df.at[count, "BBB_LBBB"] = 0
        df.at[count, "BBB_N"] = 0
        df.at[count, "BBB_RBBB"] = 1
    count += 1
# Convert new columns to numeric, and delete the previous "BBB" column.
df["BBB_LBBB"] = pd.to_numeric(df["BBB_LBBB"])
df["BBB_N"] = pd.to_numeric(df["BBB_N"])
df["BBB_RBBB"] = pd.to_numeric(df["BBB_RBBB"])
df = df.drop(['BBB'], axis=1)


# Next is to convert the Region RWMA attribute into separate columns
# First create empty columns for all 5 RWMA's.
df["Region RWMA 0"] = ""
df["Region RWMA 1"] = ""
df["Region RWMA 2"] = ""
df["Region RWMA 3"] = ""
df["Region RWMA 4"] = ""
# Put 0 if the Region RWMA value is not the value labelled in the column name,
# and 1 if it is equal to the Region RWMA value labelled in the column name.
count = 0
# 0 for NO, 1 for YES
for row in df["Region RWMA"]:
    if row == 0:
        df.at[count, "Region RWMA 0"] = 1
        df.at[count, "Region RWMA 1"] = 0
        df.at[count, "Region RWMA 2"] = 0
        df.at[count, "Region RWMA 3"] = 0
        df.at[count, "Region RWMA 4"] = 0
    if row == 1:
        df.at[count, "Region RWMA 0"] = 0
        df.at[count, "Region RWMA 1"] = 1
        df.at[count, "Region RWMA 2"] = 0
        df.at[count, "Region RWMA 3"] = 0
        df.at[count, "Region RWMA 4"] = 0
    if row == 2:
        df.at[count, "Region RWMA 0"] = 0
        df.at[count, "Region RWMA 1"] = 0
        df.at[count, "Region RWMA 2"] = 1
        df.at[count, "Region RWMA 3"] = 0
        df.at[count, "Region RWMA 4"] = 0
    if row == 3:
        df.at[count, "Region RWMA 0"] = 0
        df.at[count, "Region RWMA 1"] = 0
        df.at[count, "Region RWMA 2"] = 0
        df.at[count, "Region RWMA 3"] = 1
        df.at[count, "Region RWMA 4"] = 0
    if row == 4:
        df.at[count, "Region RWMA 0"] = 0
        df.at[count, "Region RWMA 1"] = 0
        df.at[count, "Region RWMA 2"] = 0
        df.at[count, "Region RWMA 3"] = 0
        df.at[count, "Region RWMA 4"] = 1
    count += 1
# Convert new columns to numeric, and delete the previous Region RWMA column.
df["Region RWMA 0"] = pd.to_numeric(df["Region RWMA 0"])
df["Region RWMA 1"] = pd.to_numeric(df["Region RWMA 1"])
df["Region RWMA 2"] = pd.to_numeric(df["Region RWMA 2"])
df["Region RWMA 3"] = pd.to_numeric(df["Region RWMA 3"])
df["Region RWMA 4"] = pd.to_numeric(df["Region RWMA 4"])
df = df.drop(['Region RWMA'], axis=1)


# Lastly, convert the VHD attribute into separate columns
# First create empty columns for all 4 VHD levels.
df["VHD_N"] = ""
df["VHD_Mild"] = ""
df["VHD_Severe"] = ""
df["VHD_Moderate"] = ""
# Put 0 if the VHD value is not the value labelled in the column name,
# and 1 if it is equal to the VHD value labelled in the column name.
count = 0
# 0 for NO, 1 for YES
for row in df["VHD"]:
    if row == "N":
        df.at[count, "VHD_N"] = 1
        df.at[count, "VHD_Mild"] = 0
        df.at[count, "VHD_Severe"] = 0
        df.at[count, "VHD_Moderate"] = 0
    if row == "mild":
        df.at[count, "VHD_N"] = 0
        df.at[count, "VHD_Mild"] = 1
        df.at[count, "VHD_Severe"] = 0
        df.at[count, "VHD_Moderate"] = 0
    if row == "Severe":
        df.at[count, "VHD_N"] = 0
        df.at[count, "VHD_Mild"] = 0
        df.at[count, "VHD_Severe"] = 1
        df.at[count, "VHD_Moderate"] = 0
    if row == "Moderate":
        df.at[count, "VHD_N"] = 0
        df.at[count, "VHD_Mild"] = 0
        df.at[count, "VHD_Severe"] = 0
        df.at[count, "VHD_Moderate"] = 1
    count += 1
# Convert new columns to numeric, and delete the previous VHD column.
df["VHD_N"] = pd.to_numeric(df["VHD_N"])
df["VHD_Mild"] = pd.to_numeric(df["VHD_Mild"])
df["VHD_Severe"] = pd.to_numeric(df["VHD_Severe"])
df["VHD_Moderate"] = pd.to_numeric(df["VHD_Moderate"])
df = df.drop(['VHD'], axis=1)

# Output the modified dataset to a csv to see it clearly.
# This modified dataset can be found in the project's working directory.
df.to_csv("CAD4_Updated.csv")
# Print a newline before producing any outputs from the next segment.
print("\n")


################################################################
# FEATURE SELECTION PROCESS
################################################################

# Import ExtraTreeClassifier for feature importance
from sklearn.ensemble import ExtraTreesClassifier
# Import matplotlib for plotting correlation heatmap
import matplotlib.pyplot as plt
# Import item getter for sorting key in feature importance list
from operator import itemgetter


# Attempting to view feature importance using extra trees
# Fit all 70 rows into the model, and print it's importance
# value for each attribute.
array = df.values
X = array[:, 0:69]
Y = array[:, 69]
model = ExtraTreesClassifier(n_estimators=10)
model.fit(X, Y)

# Set all_cols to have all column names (attributes)
all_cols = list(df.columns.values)

# Now print all the importance values that correlate with
# the column names.
# The index value acts as a counter when appending column names
# to the list.
index = 0
importance_table = []
for value in model.feature_importances_:
    importance_table.append(list((str(all_cols[index]), value)))
    index += 1

# Now, sort the list in descending order to see the top most important
# values.
print("Feature importance using ExtraTrees:")
sorted_importance_table = (sorted(importance_table, key=itemgetter(1), reverse=True))
for item in sorted_importance_table:
    # We can now see a list of features with its importance value
    print(item)

# NOTE: The feature importance values will be used as one of the referrals
#       when selecting the final set of features (attributes).

# Next, a simple correlation method provided by the pandas package will be
# used to create a simple table and map to see the correlation of all
# attributes against CAD.

# Get the correlation values
correlation_df = df.corr()
print("\nFeature correlation values:")
print(correlation_df)
# Print these correlation values into a csv file to view the
# data better.
correlation_df.to_csv("all_correlation.csv")

# Plot the heatmap for all variables
# Editing the parameters of the heatmap style
f = plt.figure(figsize=(19, 15))
plt.matshow(df.corr(), fignum=f.number)
plt.xticks(range(df.shape[1]), df.columns, fontsize=14, rotation=45)
plt.yticks(range(df.shape[1]), df.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)

# To plot the heatmap - UNCOMMENT BELOW TO LAUNCH HEATMAP
# plt.matshow(correlation_df.corr())
# plt.show()

# The plot above is quite big, hence it's heatmap is commented out.
# Instead, we can look closer between Cath and all variables.
print("\nDisplay correlation of features against 'cath' as a list of values:")
corr_list = []
# Print and look at all the correlation values between Cath and all other attributes.
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(correlation_df["Cath"])

# NOTE: The appropriate features are selected by comparing the feature importance and correlation found
#       from above, along with the code developers discretion and research done regarding attributes involving CAD.

# Once the selected attributes are chosen, unwanted attributes will be dropped from the dataframe.
df = df.drop(['DM', 'BP', 'Current Smoker', 'EX-Smoker', 'FH', 'Obesity', 'CRF', 'CVA', 'Airway disease'], axis=1)
df = df.drop(['Thyroid Disease', 'CHF', 'DLP', 'Edema', 'Weak Peripheral Pulse', 'Lung rales', 'Tinversion'], axis=1)
df = df.drop(['FBS', 'Dyspnea', 'Atypical', 'LowTH Ang', 'Q Wave', 'St Elevation', 'LVH', 'Poor R Progression'], axis=1)
df = df.drop(['TG', 'LDL', 'HDL', 'Na', 'WBC', 'Nonanginal', 'Exertional CP', 'Neut', 'Male', 'Female'], axis=1)
df = df.drop(['Function Class 0', 'Function Class 1', 'Function Class 2', 'Function Class 3'], axis=1)
df = df.drop(['Function Class 4', 'BBB_LBBB', 'BBB_N', 'BBB_RBBB'], axis=1)

# Feature selection is now done, and we can print this data into a csv file to view it clearly.
df.to_csv("CAD4_FeatureUpdated.csv")


################################################################
# GETTING THE USER INPUT DATA
################################################################
# MinMaxScaler used for data normalization
from sklearn.preprocessing import MinMaxScaler

# Since there are 20 features, 20 variables are created to hold each feature name and value

# Feature/Attribute names
# These variables will be passed onto the UI, hence changing the variable values here will directly
# change the values displayed in the UI. This aids in reproducibility or changes in the feature selection.
feature1 = 'Age'
feature2 = 'Weight'
feature3 = 'Height'
feature4 = 'BMI'
feature5 = 'HTN'
feature6 = 'PR'
feature7 = 'Systolic Murmur'
feature8 = 'Diastolic Murmur'
feature9 = 'Typical Chest Pain'
feature10 = 'St Depression'
feature11 = 'CR'
feature12 = 'BUN'
feature13 = 'ESR'
feature14 = 'HB'
feature15 = 'K'
feature16 = 'Lymph'
feature17 = 'PLT'
feature18 = 'EF-TTE'
feature19 = 'Region RWMA'
feature20 = 'VHD'

# This list is declared to store the value of the predicted outcome at the end.
result_list = []


# Get the first 10 attribute inputs from the user
def get_input1(userinput1, userinput2, userinput3, userinput4, userinput5, userinput6, userinput7, userinput8,
               userinput9, userinput10):
    """ This function takes in all the user inputs from the UI, and converts into a float value, before storing them
    as a global variable for the classifier model to use later.
    :param All user inputs: User inputs for the first 10 fields from the user interface.
    :type All user inputs: str
    :return : List of inputs
    :rtype: List """
    global input1
    input1 = float(userinput1)
    global input2
    input2 = float(userinput2)
    global input3
    input3 = float(userinput3)
    global input4
    input4 = float(userinput4)
    global input5
    input5 = float(userinput5)
    global input6
    input6 = float(userinput6)
    global input7
    input7 = float(userinput7)
    global input8
    input8 = float(userinput8)
    global input9
    input9 = float(userinput9)
    global input10
    input10 = float(userinput10)

    # Test list used for testing in testing file
    test_list = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10]
    return test_list


# Get the next 10 attribute inputs from the user
# Note that attributes such as Region RWMA and VHD will have additional attributes created to store
# its values accordingly.
def get_input2(userinput11, userinput12, userinput13, userinput14, userinput15, userinput16, userinput17,
               userinput18, userinput19, userinput20):
    """ Just as above, this function takes in the next 10 inputs from the UI, and stores them in global
    variables with appropriate variable types. Once all inputs are stored, the classifier model will be run.
    :param All user inputs: User inputs for the second 10 fields from the user interface.
    :type All user inputs: str
    :return : List of inputs
    :rtype: List """
    global input11
    input11 = float(userinput11)
    global input12
    input12 = float(userinput12)
    global input13
    input13 = float(userinput13)
    global input14
    input14 = float(userinput14)
    global input15
    input15 = float(userinput15)
    global input16
    input16 = float(userinput16)
    global input17
    input17 = float(userinput17)
    global input18
    input18 = float(userinput18)
    global input19
    input19 = float(userinput19)
    global input19_0
    input19_0 = 0
    global input19_1
    input19_1 = 0
    global input19_2
    input19_2 = 0
    global input19_3
    input19_3 = 0
    global input19_4
    input19_4 = 0
    global input20
    input20 = str(userinput20)
    global input20_1
    input20_1 = 0
    global input20_2
    input20_2 = 0
    global input20_3
    input20_3 = 0
    global input20_4
    input20_4 = 0

    # Once all inputs are stored, the classifier model will immediately be run
    run_model()

    # Test list used for testing in testing file
    test_list = [input11, input12, input13, input14, input15, input16, input17, input18, input19, input20]
    return test_list


# This function runs the Classifier Model
def run_model():
    """ Calls the classifier model with it's required dataframe and user inputs. """
    classifier_model(df, input1, input2, input3, input4, input5, input6, input7, input8, input9, input10,
                     input11, input12, input13, input14, input15, input16, input17, input18, input19, input19_0,
                     input19_1, input19_2, input19_3, input19_4, input20, input20_1, input20_2, input20_3, input20_4)


# This function contains all the code that models the data and makes the prediction
def classifier_model(df, input1, input2, input3, input4, input5, input6, input7, input8, input9, input10,
                     input11, input12, input13, input14, input15, input16, input17, input18, input19, input19_0,
                     input19_1, input19_2, input19_3, input19_4, input20, input20_1, input20_2, input20_3, input20_4):
    """ This function reshapes any necessary inputs and scales all the data, including the users' input, before
    finally running the classifier model - (ensemble voting stack with a combination of Logistic Regression,
    Naive Bayes, and Random Forest).
    :param df: Dataframe of cleaned dataset.
    :param All user inputs: All user inputs including additional fields.
    :type df: Dataframe
    :type All user inputs: str
    :return : Prediction result
    :rtype: str """
    # First reshape two of the inputs as required

    # For Region RWMA
    # Set the appropriate variable to 1 according to the user's input.
    if input19 == 0:
        input19_0 = 1
    if input19 == 1:
        input19_1 = 1
    if input19 == 2:
        input19_2 = 1
    if input19 == 3:
        input19_3 = 1
    if input19 == 4:
        input19_4 = 1

    # For VHD
    # Set the appropriate variable to 1 according to the user's input.
    input20 = input20.lower()
    if input20 == 'no':
        input20_1 = 1
    if input20 == 'mild':
        input20_2 = 1
    if input20 == 'severe':
        input20_3 = 1
    if input20 == 'moderate':
        input20_4 = 1

    # Set up the users' input and turn it into a dataframe
    input_data = {'Age': [input1], 'Weight': [input2], 'Length': [input3], 'BMI': [input4], 'HTN': [input5],
                  'PR': [input6], 'Systolic Murmur': [input7], 'Diastolic Murmur': [input8],
                  'Typical Chest Pain': [input9], 'St Depression': [input10], 'CR': [input11], 'BUN': [input12],
                  'ESR': [input13], 'HB': [input14], 'K': [input15], 'Lymph': [input16], 'PLT': [input17],
                  'EF-TTE': [input18], 'Cath': [0], 'Region RWMA 0': [input19_0], 'Region RWMA 1': [input19_1],
                  'Region RWMA 2': [input19_2], 'Region RWMA 3': [input19_3], 'Region RWMA 4': [input19_4],
                  'VHD_N': [input20_1], 'VHD_Mild': [input20_2], 'VHD_Severe': [input20_3], 'VHD_Moderate': [input20_4]}

    # Convert the input data to dataframe
    input_df = pd.DataFrame(input_data, columns=['Age', 'Weight', 'Length', 'BMI', 'HTN', 'PR', 'Systolic Murmur',
                                                 'Diastolic Murmur', 'Typical Chest Pain', 'St Depression', 'CR', 'BUN',
                                                 'ESR', 'HB', 'K', 'Lymph', 'PLT', 'EF-TTE', 'Cath', 'Region RWMA 0',
                                                 'Region RWMA 1', 'Region RWMA 2', 'Region RWMA 3', 'Region RWMA 4',
                                                 'VHD_N', 'VHD_Mild', 'VHD_Severe', 'VHD_Moderate'])

    # Now, join the input data with the original dataset for scaling.
    # When joined, only the first row of the dataframe would be the user's input.
    # The data will be scaled together, and after that, the user's input (first row) will be removed.
    to_scale_df = pd.concat([input_df, df])

    # Scale/normalize the data.
    scaler = MinMaxScaler()
    cols = ['Age', 'Weight', 'Length', 'BMI', 'HTN', 'PR', 'Systolic Murmur', 'Diastolic Murmur', 'Typical Chest Pain',
            'St Depression', 'CR', 'BUN', 'ESR', 'HB', 'K', 'Lymph', 'PLT', 'EF-TTE', 'Cath', 'Region RWMA 0',
            'Region RWMA 1', 'Region RWMA 2', 'Region RWMA 3', 'Region RWMA 4', 'VHD_N', 'VHD_Mild', 'VHD_Severe',
            'VHD_Moderate']

    # Run the scaler and display the scaled data
    scaled_df = to_scale_df[cols] = scaler.fit_transform(to_scale_df[cols])
    print("\n")
    # Re-assign the initial df to this scaled dataset
    df = pd.DataFrame(scaled_df)
    df.columns = cols
    # Have a look at the scaled dataset
    print("Scaled dataset:")
    print(df)

    # Now remove the user's input which was placed in the first row. This user input
    # will later be used in the classifier model.
    final_user_input = (df.iloc[0])
    final_user_input = final_user_input.to_frame()
    final_user_input = final_user_input.transpose()

    # Re-assign the scaled dataframe without the first row.
    df = df.iloc[1:]
    print('\n')

    # The data, and the user input, is now ready to be fitted to the model.

    ################################################################
    # CLASSIFIER MODELLING
    ################################################################
    # Library for splitting test and training data
    from sklearn.model_selection import train_test_split
    # Library for logistic regression
    from sklearn.linear_model import LogisticRegression
    # Library for naive bayes
    from sklearn.naive_bayes import GaussianNB
    # Library for random forest
    from sklearn.ensemble import RandomForestClassifier
    # Library for stack/voting classifier
    from sklearn.ensemble import VotingClassifier
    # Library for support vector machine
    from sklearn import svm
    # Library for performance and model accuracy metrics
    from sklearn.metrics import accuracy_score, f1_score, log_loss, roc_auc_score

    # First, split the test and training data

    print(df)
    # Pop the variable to be predicted
    predict = df.pop('Cath')

    # Drop the "Cath" column from the user input as well
    final_user_input = final_user_input.drop("Cath", axis=1)

    # Split the test and training data by 30% and 70% respectively
    # Testing data is still used even though the user's input will be predicted later
    # because the testing data can provide us with performance metrics.
    df_train, df_test, y_train, y_test = train_test_split(df, predict, test_size=0.3)

    # Fit the 4 different classifier models
    lr_clf = LogisticRegression(max_iter=1000)

    nb_clf = GaussianNB()

    rf_clf = RandomForestClassifier()

    svm_clf = svm.SVC()

    # Fit the first meta learner - LR + NB + RF (Ensemble method)
    voting_clf = VotingClassifier(estimators=[('LR', lr_clf), ('NB', nb_clf), ('RF', rf_clf)], voting='hard')

    # Fit BOTH user input and testing data.
    voting_clf.fit(df_train, y_train)
    # Using user's input
    model_outcome = voting_clf.predict(final_user_input)
    # Using test data
    testing_outcome = voting_clf.predict(df_test)

    # We can now see the performance metrics of this model on the 30% test data
    acc = accuracy_score(y_test, testing_outcome)
    l_loss = log_loss(y_test, testing_outcome)
    f1 = f1_score(y_test, testing_outcome)
    roc = roc_auc_score(y_test, testing_outcome)

    # Display the performance metrics
    print("Accuracy and performance metrics for Meta-learner 1")
    print("Accuracy is: " + str(acc))
    print("Log Loss is: " + str(l_loss))
    print("F1 Score is: " + str(f1))
    print("ROC Score is: " + str(roc))
    print('\n')

    # Finally, here is the predicted output for the user's input data.
    if model_outcome == [1.0]:
        diagnosis = "High Risk"
    else:
        diagnosis = "Low Risk"

    # The outcome of the diagnosis will be stored in the result_list for use later in the UI

    # Clear the list if it's not empty
    if result_list != []:
        # Remove twice because in each round, an outcome and the accuracy value is added
        result_list.pop()
        result_list.pop()
    # Append the outcome into list, along with its accuracy
    result_list.append(diagnosis)
    result_list.append(acc)
    # Display the outcome to the python console
    print("Heart Disease Risk:", diagnosis)
    return diagnosis

    # NOTE: As planned, all 4 combinations of the meta-learners were used, and the above, meta-learner 1,
    # is found to have produced the best and most stable predictions, therefore it is used for this software.
    # In the event that the technical user or developer would like to change the combination of classifier models,
    # simply change the classifiers in Line 681 above to the desired classifier combination.

# END OF FILE
# DEVELOPED BY PRASHANT & TEAM 12 (FIT3164)
