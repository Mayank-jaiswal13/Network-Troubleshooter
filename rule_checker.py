import csv
from collections import Counter


def check_case(row):
    issues = []
    output = (row.get('show_output') or '').lower()
    symptom = (row.get('symptom') or '').lower()
    concept = (row.get('concept') or '').lower()

    if 'duplicate ip' in output or 'duplicate' in symptom:
        issues.append('Duplicate IP found')
    if 'wrong mask' in output or '255.255.255.0' not in output and 'mask' in symptom:
        issues.append('Subnet mask mismatch')
    if 'gateway' in symptom and 'gateway' not in output:
        issues.append('Gateway configuration missing')
    if 'interface' in output and 'down' in output:
        issues.append('Interface is down')
    if 'vlan' in symptom and 'vlan' not in output:
        issues.append('VLAN missing or misconfigured')
    if 'route' in symptom and 'ip route' not in output:
        issues.append('Route missing')
    if 'nat' in concept and 'nat' not in output:
        issues.append('NAT configuration missing')
    if 'acl' in concept and 'access-list' not in output:
        issues.append('ACL rule missing')

    return issues


def main():
    with (Path(__file__).resolve().parent / 'cases.csv').open(newline='') as f:
        rows = list(csv.DictReader(f))

    findings = []
    for row in rows:
        issues = check_case(row)
        findings.append((row['case_id'], row['expected_fault'], issues))

    errors = 0
    for case_id, expected_fault, issues in findings:
        if issues:
            print(f'Case {case_id}: {expected_fault} -> {issues}')
            errors += 1

    print(f'Total flagged issues: {errors}')


if __name__ == '__main__':
    main()
