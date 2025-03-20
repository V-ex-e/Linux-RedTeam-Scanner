import os
import subprocess

def install_dependencies():
    print("📦 Installing dependencies...")
    subprocess.run(["pip", "install", "fpdf"], check=True)

def run_tools():
    print("🔍 Running reconnaissance...")
    subprocess.run(["python", "recon.py"], check=True)
    
    print("🛡 Running vulnerability scan...")
    subprocess.run(["python", "vuln_scan.py"], check=True)
    
    print("💣 Running exploit suggester...")
    subprocess.run(["python", "exploit_sugg.py"], check=True)
    
    print("📄 Generating final report...")
    subprocess.run(["python", "report.py"], check=True)

def main():
    install_dependencies()
    run_tools()
    print("✅ Setup and execution complete! Report saved as redteam_report.pdf")

if __name__ == "__main__":
    main()