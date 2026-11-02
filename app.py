from flask import Flask, render_template, request
from dashboard import build_summary

app = Flask(__name__)

@app.route('/')
def home():
    summary = build_summary()
    return render_template('index.html', summary=summary)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    selected_symptoms = request.form.getlist('symptoms')
    other_symptom = request.form.get('other_symptom', '').strip()
    show_output = request.form.get('show_output', '')

    symptom_parts = []
    if selected_symptoms:
        symptom_parts.extend(selected_symptoms)
    if other_symptom:
        symptom_parts.append(other_symptom)

    symptom = '; '.join(symptom_parts)

    if not symptom:
        return render_template('index.html', summary=build_summary(), error='Please select a symptom or type one in the other box.')

    root_cause = 'Likely inter-VLAN routing issue'
    confidence = 'medium'
    evidence = 'Based on connectivity symptom and show-output evidence'
    next_command = 'show ip route'
    fix_steps = ['Verify VLAN routing', 'Check access-lists', 'Confirm default gateway']

    lowered = symptom.lower()
    if 'dhcp' in lowered or 'ip address' in lowered:
        root_cause = 'DHCP or addressing problem'
        next_command = 'show ip dhcp binding'
    elif 'dns' in lowered:
        root_cause = 'DNS resolution issue'
        next_command = 'show ip dns view'
    elif 'acl' in lowered or 'access list' in lowered or 'access-list' in lowered:
        root_cause = 'ACL or security policy issue'
        next_command = 'show access-lists'
    elif 'nat' in lowered:
        root_cause = 'NAT or translation problem'
        next_command = 'show ip nat translations'
    elif 'wireless' in lowered or 'ssid' in lowered:
        root_cause = 'Wireless authentication or WLAN policy issue'
        next_command = 'show wireless client summary'
    elif 'gateway' in lowered or 'route' in lowered:
        root_cause = 'Routing or default gateway misconfiguration'
        next_command = 'show ip route'

    result = {
        'root_cause': root_cause,
        'confidence': confidence,
        'evidence': evidence if not show_output else show_output[:220],
        'next_command': next_command,
        'fix_steps': fix_steps,
        'osi_layer': 'L3 or L4',
        'concept_tag': 'Troubleshooting'
    }

    return render_template('index.html', summary=build_summary(), diagnosis=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
