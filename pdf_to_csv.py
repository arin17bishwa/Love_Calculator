import tabula
pdf_path=("/home/bishwajit/Downloads/RESULT_OF_B_TECH_B.TECH_AND_M_TECH_DUAL_DEGREE.pdf")
tabula.convert_into("/home/bishwajit/Downloads/RESULT_OF_B_TECH_B.TECH_AND_M_TECH_DUAL_DEGREE.pdf","BTech_result.csv", output_format="csv",lattice=True,pages='all')
