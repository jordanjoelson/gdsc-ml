import pandas as pd
import os   
folder_path = r'C:\Users\alvin\Downloads\Projects\DataVal\ISIC_2020_Training_JPEG\train'
df = pd.read_csv('ISIC_2020_Training_GroundTruth.csv')

class CheckType:
    def __init__(self, df):
        self.df = df

    def get_age_stats(self, col='age_approx'):
        age_data = self.df[col].dropna()
        return {
            "Count": f"{len(age_data):,}",
            "Mean": f"{age_data.mean():.1f} years",
            "Median": f"{age_data.median():.1f} years",
            "Range": f"{int(age_data.min())} - {int(age_data.max())} years"
        }

    def get_distribution(self, col):
        counts = self.df[col].value_counts(dropna=False)
        total = len(self.df)
        dist = {}
        for val, count in counts.items():
            percentage = (count / total) * 100
            label = "unknown" if pd.isna(val) else str(val)
            dist[label] = f"{count:,} ({percentage:.1f}%)"
        return dist
    
    def get_diagnosis_counts(self, df):
        """
        Returns the integer counts for both malignant and benign cases.
        """
        # Counting occurrences in the 'benign_malignant' column
        counts = df['benign_malignant'].value_counts()
        
        # Using .get() ensures the code doesn't crash if a category is missing
        benign_count = counts.get('benign', 0)
        malignant_count = counts.get('malignant', 0)
        
        return benign_count, malignant_count
    
    def get_diagnosis_distribution(self, df):
        mydict = {}
        for diagnosis in df['diagnosis']:
            if diagnosis in mydict:
                mydict[diagnosis] += 1
            else:
                mydict[diagnosis] = 1
        
        return mydict
    


report = CheckType(df)

b_total, m_total = report.get_diagnosis_counts(df)

# 1. Get Age Stats
age = report.get_age_stats()
print("Age Statistics:")
for key, val in age.items():
    print(f"  {key}: {val}")

# 2. Get Sex Distribution
print("\nSex Distribution:")
sex_dist = report.get_distribution('sex')
for label, val in sex_dist.items():
    print(f"  {label}: {val}")

# 3. Get Top 5 Body Locations
print("\nTop 5 Body Locations:")
loc_dist = report.get_distribution('anatom_site_general_challenge')
for label, val in list(loc_dist.items())[:5]:
    print(f"  {label}: {val}")
#print how many benign and malignant cases there are in the dataset
print(f"Total Benign: {b_total}")
print(f"Total Malignant: {m_total}")

# print the diagnosis types and their counts
diagnosis_dist = report.get_diagnosis_distribution(df)
print("\nDiagnosis Distribution:")
for diagnosis, count in diagnosis_dist.items():
    print(f"  {diagnosis}: {count}")

"""
count = 0
for img_id in df['image_name']:
    #print(img_id)
    count += 1
image_count = len(os.listdir(folder_path))
print(count)
print(image_count)

csv_images = set(df['image_name'] + '.jpg')


folder_images = set(os.listdir(folder_path))


missing_images = csv_images - folder_images

print(f"Missing image: {missing_images}")
"""


