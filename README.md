# Data Science Project: Student Performance Analysis

This project explores student exam results and uses statistical tests to compare mathematics scores across student groups.

## What it does

- Loads and inspects the student performance dataset.
- Checks for missing values, removes duplicate rows, and drops rows with missing data.
- Creates charts for mathematics scores and gender, including a histogram, bar chart, and box plot.
- Summarizes mathematics scores by gender and parental education level.
- Tests four hypotheses with independent-samples and one-sample t-tests:
  1. Whether mathematics scores differ by gender.
  2. Whether the average mathematics score differs from the assumed benchmark of 60.
  3. Whether scores differ between students whose parents completed high school and those whose parents have selected college degrees.
  4. Whether scores differ based on completion of the test preparation course.

The script uses a significance threshold of 0.05 and prints each test's t-statistic, p-value, and interpretation. Statistical associations do not by themselves establish causation.

## Built with

- **Python** — runs the analysis.
- **pandas** — reads, cleans, groups, and summarizes the tabular data.
- **Matplotlib** — creates the charts.
- **SciPy** — performs the t-tests.
- **NumPy** — imported for numerical work.

## Dataset

`StudentsPerformance.csv` contains student attributes and exam scores, including gender, parental education, test preparation course, and math, reading, and writing scores.

## Run the project

Use Python 3. Install the dependencies and run the script from the project directory:

```bash
python3 -m pip install -r requirements.txt
python3 project.py
```

The script prints summaries and test results in the terminal. Matplotlib opens the charts in a window.

## Files

- `project.py` — data exploration, visualizations, and hypothesis tests.
- `StudentsPerformance.csv` — input dataset.
- `requirements.txt` — Python package dependencies.
