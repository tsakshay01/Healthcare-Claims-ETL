import subprocess
import sys
import os

def run_step(script_name):
    print(f"--- [RUNNING] {script_name} ---")
    # This command uses the SAME Python interpreter that is running this script
    # to avoid the "Path Conflict" errors we had earlier.
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"--- [SUCCESS] {script_name} finished. ---")
        return result.stdout
    else:
        print(f"--- [ERROR] {script_name} failed! ---")
        print(result.stderr)
        sys.exit(1)

# 1. Run Data Generation
output_gen = run_step('generate_data.py')

# 2. Run ETL Pipeline
output_etl = run_step('etl_pipeline.py')

# 3. Run Analysis
output_analysis = run_step('run_analysis.py')

# 4. Save Final Report
report_filename = 'summary_report.txt'
with open(report_filename, 'w') as f:
    f.write("HEALTHCARE DATA PIPELINE - EXECUTION REPORT\n")
    f.write("=============================================\n\n")
    f.write("PHASE 1: GENERATION LOGS\n")
    f.write(output_gen)
    f.write("\n\nPHASE 2: ETL LOGS\n")
    f.write(output_etl)
    f.write("\n\nPHASE 3: ANALYSIS RESULTS\n")
    f.write(output_analysis)

print(f"\n[DONE] Full pipeline complete! Report saved to '{report_filename}'.")