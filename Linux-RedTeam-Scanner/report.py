from fpdf import FPDF

class ReportGenerator:
    def __init__(self, filename="redteam_report.pdf"):
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_title(self, title):
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(200, 10, title, ln=True, align="C")

    def add_text(self, text):
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, text)

    def save(self):
        self.pdf.output(self.filename)

if __name__ == "__main__":
    report = ReportGenerator()
    report.add_title("🔴 Red Team Recon & Exploit Report")
    
    report.add_text("📌 System Information:\n" + str(get_system_info()))
    report.add_text("\n📌 Running Processes:\n" + get_running_processes())
    report.add_text("\n📌 Network Info:\n" + str(get_network_info()))
    
    report.add_text("\n⚠️ Vulnerability Scan:\n" + check_sudo_perms())
    report.add_text("\n⚠️ World-Writable Directories:\n" + check_world_writable())
    
    report.add_text("\n🚀 Exploit Suggestions:\n" + check_kernel_vulns())
    report.add_text("\n🚀 SUID Binaries:\n" + check_suid_binaries())

    report.save()
    print("📄 Report generated: redteam_report.pdf")
