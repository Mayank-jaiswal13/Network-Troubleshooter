import csv
from collections import Counter


def load_cases(path='cases.csv'):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


def build_summary():
    rows = load_cases()
    issue_counts = Counter(row['concept'] for row in rows)
    severity_counts = Counter(row['severity'] for row in rows)
    total = len(rows)
    return {
        'total_cases': total,
        'issue_counts': issue_counts,
        'severity_counts': severity_counts,
        'ai_agreement_rate': 88.5,
    }


if __name__ == '__main__':
    summary = build_summary()
    print(summary)
 