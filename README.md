# Cerebral Tissue Oxygenation NIRS & Frontal Hypoxia Sentinel Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `monitor_cerebral_oxygenation_nirs`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Processes near-infrared spectroscopy (NIRS) frontal lobe tissue saturation index (TSI/rSO2), oxygen extraction fraction (OEF), and detects cerebral hypoperfusion and cognitive fatigue.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Neuro-Vascular Oxygenation)`

## MCP Tool Specification
### `monitor_cerebral_oxygenation_nirs`
Parameters:
- `baseline_rso2_pct` (float): Baseline resting cerebral regional oxygen saturation % (rSO2)
- `current_rso2_pct` (float): Real-time measured frontal lobe rSO2 %
- `arterial_spo2_pct` (float): Peripheral systemic arterial pulse oximetry % (SpO2)
- `cognitive_workload_duration_mins` (float): Continuous minutes of demanding analytical or cognitive task

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-cerebral-tissue-oxygenation-nirs-hypoxia-sentinel-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-cerebral-tissue-oxygenation-nirs-hypoxia-sentinel-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
