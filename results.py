import csv
from collections import defaultdict

def calculate_average_scores_by_ai_version(csv_file):
    # Dictionary to store total scores and counts per AI Version
    scores_by_ai_version = defaultdict(lambda: {"total": 0, "count": 0})

    # Read the CSV file
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ai_version = row["AI Version"]
            score = int(row["Score"])

            # Update total and count for this AI Version
            scores_by_ai_version[ai_version]["total"] += score
            scores_by_ai_version[ai_version]["count"] += 1

    # Calculate and display averages
    print("Average Scores by AI Version:")
    averages = {}
    for ai_version, data in scores_by_ai_version.items():
        average_score = data["total"] / data["count"]
        averages[ai_version] = average_score
        print(f"{ai_version}: {average_score:.2f}")

    return averages

# Call the function with your CSV file name
csv_file = "results.csv"  # Replace with your actual CSV file path
calculate_average_scores_by_ai_version(csv_file)
