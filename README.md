# international_result

XML parser for extracting international swimming competition results, including entry times, semi-final, and final performances.

## Overview

This tool parses LENEX-format XML files (the standard data exchange format for international swimming competitions) and extracts structured athlete and race data into a CSV file. It is useful for coaches and analysts working with results from FINA/World Aquatics competitions.

## Features

- **XML Parsing**: Extracts athlete information (name, gender, birthdate) and event entries from LENEX XML files.
- **Multi-Round Data**: Captures entry times, semi-final split/lap times, and final split/lap times with placements.
- **CSV Export**: Outputs a clean, flat CSV file for further analysis in Excel, R, or Python.

## Requirements

- Python 3.8+
- pandas

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python international_result.py <xml_file_path>
# Example:
python international_result.py results_2024_worlds.xml
```

## Output

- `athletes_entries_finals_results.csv`: Structured race data with columns for athlete info, entry times, semi-final results, and final results.
