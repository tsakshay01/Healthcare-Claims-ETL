import subprocess
import sys
import os

def run_step(script_name):
    print(f"--- [RUNNING] {script_name} ---")
   
    result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"--- [SUCCESS] {script_name} finished. ---")
        return result.stdout
    else:
        print(f"--- [ERROR] {script_name} failed! ---")
        print(result.stderr)
        sys.exit(1)


output_gen = run_step('generate_data.py')


output_etl = run_step('etl_pipeline.py')


output_analysis = run_step('run_analysis.py')


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