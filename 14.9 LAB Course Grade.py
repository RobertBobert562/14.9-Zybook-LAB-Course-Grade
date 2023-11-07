# Declare necessary variables
student_data = {}  # Dictionary to store student data
exam_averages = []  # List to store exam averages

# Function to compute the average of a list of exam scores
def compute_average(exam_scores):
    return sum(exam_scores) / len(exam_scores)

# Function to compute the letter grade based on the average score
def compute_letter_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

# Read the file name from the user
file_name = input()

# Open the report file for writing
with open('report.txt', 'w') as report_file:
    # Code for writing the report goes here

    with open(file_name, 'r') as file:
        exam_scores = []  # List to store exam scores

        # Read and process each line in the input file
        for line in file:
            parts = line.strip().split('\t')
            last_name, first_name, *scores = parts
            scores = [int(score) for score in scores]
            student_data[(last_name, first_name)] = scores
            exam_scores.append(scores)
            
            # Write student data, exam scores, and letter grades to the report file
            average_score = compute_average(scores)
            letter_grade = compute_letter_grade(average_score)
            scores_str = '\t'.join(map(str, scores))  # Join scores with tabs
            report_file.write(f"{student[0]}\t{student[1]}\t{scores_str}\t{letter_grade}\n")

        report_file.write('\n')  # Separate student data and exam averages

        # Calculate exam averages
        for i in range(len(exam_scores[0])):
            exam_average = compute_average([scores[i] for scores in exam_scores])
            exam_averages.append(exam_average)

        # Write exam averages to the report file
        report_file.write(f"Averages: midterm1 {exam_averages[0]:.2f}, midterm2 {exam_averages[1]:.2f}, final {exam_averages[2]:.2f}\n")

# Print a message to indicate the report has been generated
print("Report generated in report.txt")
