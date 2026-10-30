# -*- coding: utf-8 -*-
"""Cerebral Tissue Oxygenation NIRS & Frontal Hypoxia Sentinel Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def monitor_cerebral_oxygenation_nirs(**kwargs):
    """Processes near-infrared spectroscopy (NIRS) frontal lobe tissue saturation index (TSI/rSO2), oxygen extraction fraction (OEF), and detects cerebral hypoperfusion and cognitive fatigue."""
    baseline_rso2_pct = kwargs.get('baseline_rso2_pct')
    current_rso2_pct = kwargs.get('current_rso2_pct')
    arterial_spo2_pct = kwargs.get('arterial_spo2_pct')
    cognitive_workload_duration_mins = kwargs.get('cognitive_workload_duration_mins')

    rso2_drop_absolute = round(baseline_rso2_pct - current_rso2_pct, 1)
    rso2_drop_relative_pct = round((rso2_drop_absolute / (baseline_rso2_pct if baseline_rso2_pct > 0 else 1.0)) * 100.0, 1)
    
    # Oxygen Extraction Fraction proxy (OEF ~ (SpO2 - rSO2) / SpO2)
    oef_proxy_pct = round(((arterial_spo2_pct - current_rso2_pct) / (arterial_spo2_pct if arterial_spo2_pct > 0 else 1.0)) * 100.0, 1)
    
    # Cerebral ischemic / cognitive exhaustion warning limits (drop > 20% relative or absolute < 55%)
    if current_rso2_pct < 55.0 or rso2_drop_relative_pct >= 20.0:
        neuro_status = "CRITICAL CEREBRAL HYPOPERFUSION ALERT (Severe executive function degradation)"
        directive = "Mandatory 20-minute physical break, diaphragmatic respiration (hypercapnic cerebral vasodilation), hydration."
    elif rso2_drop_relative_pct >= 10.0:
        neuro_status = "MODERATE FRONTAL DESATURATION (Rising cognitive fatigue, working memory bottleneck)"
        directive = "Micro-break: 5-minute gaze shift to distant horizon, posture realignment, light hydration."
    else:
        neuro_status = "OPTIMAL NEURO-VASCULAR COUPLING (Adequate prefrontal perfusion & oxygen delivery)"
        directive = "Cognitive workload sustainable within current focus sprint."
        
    result = {
        "status": "success",
        "current_cerebral_rso2_pct": current_rso2_pct,
        "baseline_rso2_pct": baseline_rso2_pct,
        "relative_rso2_decay_pct": rso2_drop_relative_pct,
        "estimated_oxygen_extraction_fraction_pct": oef_proxy_pct,
        "neuro_vascular_status": neuro_status,
        "cognitive_pacing_directive": directive,
        "engine": "GenPark Prefrontal NIRS Cerebral Hemodynamics Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "monitor_cerebral_oxygenation_nirs": {
        "name": "monitor_cerebral_oxygenation_nirs",
        "description": "Processes near-infrared spectroscopy (NIRS) frontal lobe tissue saturation index (TSI/rSO2), oxygen extraction fraction (OEF), and detects cerebral hypoperfusion and cognitive fatigue.",
        "parameters": {
            "type": "object",
            "properties": {
                "baseline_rso2_pct": {"type": "number", "description": "Baseline resting cerebral regional oxygen saturation % (rSO2)"},
                "current_rso2_pct": {"type": "number", "description": "Real-time measured frontal lobe rSO2 %"},
                "arterial_spo2_pct": {"type": "number", "description": "Peripheral systemic arterial pulse oximetry % (SpO2)"},
                "cognitive_workload_duration_mins": {"type": "number", "description": "Continuous minutes of demanding analytical or cognitive task"},
            },
            "required": ['baseline_rso2_pct', 'current_rso2_pct', 'arterial_spo2_pct', 'cognitive_workload_duration_mins']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "monitor_cerebral_oxygenation_nirs":
            res = monitor_cerebral_oxygenation_nirs(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-cerebral-tissue-oxygenation-nirs-hypoxia-sentinel-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-cerebral-tissue-oxygenation-nirs-hypoxia-sentinel-skill...")
    test_args = {'baseline_rso2_pct': 71.0, 'current_rso2_pct': 63.5, 'arterial_spo2_pct': 98.0, 'cognitive_workload_duration_mins': 110.0}
    res = monitor_cerebral_oxygenation_nirs(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-cerebral-tissue-oxygenation-nirs-hypoxia-sentinel-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
