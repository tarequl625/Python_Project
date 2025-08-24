import pdfplumber
import re
import pandas as pd
import os

# 📂 Folder containing PDFs
pdf_folder = r""

# 📊 Output Excel file
output_file = r"D:\Demographics\demographics_extracted.xlsx"

# 📝 Regex patterns for different demographic fields
population_pattern = r"2024 Population\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)"
household_pattern = r"2024 Households\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)"
home_value_pattern = r"Median Home Value\s+\$([\d,]+)\s+\$([\d,]+)\s+\$([\d,]+)"
degree_pattern = r"Bachelor's Degree or Higher\s+([\d\.%]+)\s+([\d\.%]+)\s+([\d\.%]+)"
median_age_pattern = r"Median Age\s+([\d\.]+)\s+([\d\.]+)\s+([\d\.]+)"

growth_pattern = (
    r"Annual Growth 2020-2024\s+([\-–]?[\d\.%]+)\s+([\-–]?[\d\.%]+)\s+([\-–]?[\d\.%]+).*?"
    r"Annual Growth 2024-2029\s+([\-–]?[\d\.%]+)\s+([\-–]?[\d\.%]+)\s+([\-–]?[\d\.%]+)"
)

income_pattern = (
    r"Avg Household Income\s+\$([\d,]+)\s+\$([\d,]+)\s+\$([\d,]+).*?"
    r"Median Household Income\s+\$([\d,]+)\s+\$([\d,]+)\s+\$([\d,]+)"
)


# 🔧 Helper function to clean extracted values
def clean_number(val, is_percent=False, is_float=False):
    if val is None:
        return None

    # Remove commas, dollar signs, and en-dashes
    val = val.replace(",", "").replace("$", "").replace("–", "-")

    # Handle percentages
    if is_percent:
        val = val.replace("%", "")
        try:
            return float(val)
        except:
            return None

    # Handle float values (e.g., median age)
    if is_float:
        try:
            return float(val)
        except:
            return None

    # Default: convert to integer
    try:
        return int(val)
    except:
        return None


# 📋 List for storing extracted results
all_data = []

# 🔄 Loop through all PDF files in the folder
for file in os.listdir(pdf_folder):
    if file.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, file)

        # 📖 Extract text from the PDF
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # 📄 Prepare dictionary for current PDF results
        row = {"File": file}

        # --- Population ---
        pop_match = re.search(population_pattern, text, re.S)
        if pop_match:
            row.update({
                "2024 Population (3mi)": clean_number(pop_match.group(1)),
                "2024 Population (5mi)": clean_number(pop_match.group(2)),
                "2024 Population (10mi)": clean_number(pop_match.group(3)),
            })

        # --- Households ---
        hh_match = re.search(household_pattern, text, re.S)
        if hh_match:
            row.update({
                "2024 Households (3mi)": clean_number(hh_match.group(1)),
                "2024 Households (5mi)": clean_number(hh_match.group(2)),
                "2024 Households (10mi)": clean_number(hh_match.group(3)),
            })

        # --- Median Home Value ---
        home_match = re.search(home_value_pattern, text, re.S)
        if home_match:
            row.update({
                "Median Home Value (3mi)": clean_number(home_match.group(1)),
                "Median Home Value (5mi)": clean_number(home_match.group(2)),
                "Median Home Value (10mi)": clean_number(home_match.group(3)),
            })

        # --- Bachelor's Degree or Higher ---
        deg_match = re.search(degree_pattern, text, re.S)
        if deg_match:
            row.update({
                "Bachelor's Degree+ (3mi)": clean_number(deg_match.group(1), is_percent=True),
                "Bachelor's Degree+ (5mi)": clean_number(deg_match.group(2), is_percent=True),
                "Bachelor's Degree+ (10mi)": clean_number(deg_match.group(3), is_percent=True),
            })

        # --- Median Age ---
        age_match = re.search(median_age_pattern, text, re.S)
        if age_match:
            row.update({
                "Median Age (3mi)": clean_number(age_match.group(1), is_float=True),
                "Median Age (5mi)": clean_number(age_match.group(2), is_float=True),
                "Median Age (10mi)": clean_number(age_match.group(3), is_float=True),
            })

        # --- Growth ---
        growth_match = re.search(growth_pattern, text, re.S)
        if growth_match:
            row.update({
                "Annual Growth 2020-2024 (3mi)": clean_number(growth_match.group(1), is_percent=True),
                "Annual Growth 2020-2024 (5mi)": clean_number(growth_match.group(2), is_percent=True),
                "Annual Growth 2020-2024 (10mi)": clean_number(growth_match.group(3), is_percent=True),
                "Annual Growth 2024-2029 (3mi)": clean_number(growth_match.group(4), is_percent=True),
                "Annual Growth 2024-2029 (5mi)": clean_number(growth_match.group(5), is_percent=True),
                "Annual Growth 2024-2029 (10mi)": clean_number(growth_match.group(6), is_percent=True),
            })

        # --- Income ---
        income_match = re.search(income_pattern, text, re.S)
        if income_match:
            row.update({
                "Avg Income (3mi)": clean_number(income_match.group(1)),
                "Avg Income (5mi)": clean_number(income_match.group(2)),
                "Avg Income (10mi)": clean_number(income_match.group(3)),
                "Median Income (3mi)": clean_number(income_match.group(4)),
                "Median Income (5mi)": clean_number(income_match.group(5)),
                "Median Income (10mi)": clean_number(income_match.group(6)),
            })

        # ➕ Append extracted row to results
        all_data.append(row)

# 📊 Convert list of dicts to DataFrame
df = pd.DataFrame(all_data)

# 💾 Save results to Excel
df.to_excel(output_file, index=False)

# ✅ Status messages
print("✅ Data extracted for", len(all_data), "PDFs")
print("📂 Saved to:", output_file)