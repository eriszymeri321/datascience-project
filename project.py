import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import numpy as np

# Shfaq numrin 5 me ngjyrë të verdhë
print("\033[93m5\033[0m")

# 1. EKSPLORIMI I TË DHËNAVE

print("=" * 50)
print("1. LEXIMI DHE EKSPLORIMI I TË DHËNAVE")
print("=" * 50)

# Leximi i të dhënave
df = pd.read_csv("StudentsPerformance.csv")

# Ketu shfaq rreshtat e parë
print("\nRreshtat e parë të të dhënave:")
print(df.head())

# Ketu informacion për kolonat
print("\nInformacion për të dhënat:")
print(df.info())

# Statistika përmbledhëse
print("\nStatistika përmbledhëse:")
print(df.describe())


# PASTRIMI I TË DHËNAVE

print("\n" + "=" * 50)
print("PASTRIMI I TË DHËNAVE")
print("=" * 50)

# Kontrollo vlerat që mungojnë
print("\nVlerat që mungojnë për çdo kolonë:")
print(df.isnull().sum())

# Largo duplikatet
numri_para = len(df)
df = df.drop_duplicates()
numri_pas = len(df)
print(f"\nDuplikate të larguar: {numri_para - numri_pas}")

# Trajto vlerat që mungojnë (largo rreshtat me vlera që mungojnë)
df = df.dropna()
print(f"Rreshta të mbetur pas pastrimit: {len(df)}")


# 2. ANALIZA E TË DHËNAVE


print("\n" + "=" * 50)
print("2. ANALIZA E VARIABLAVE")
print("=" * 50)

# Analiza e variablave individuale - Histogram për notat e matematikës
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
df['math score'].hist(bins=20, edgecolor='black', color='steelblue')
plt.title('Shpërndarja e Notave të Matematikës')
plt.xlabel('Nota e Matematikës')
plt.ylabel('Frekuenca')
plt.grid(alpha=0.3)

# Bar chart për gjininë
plt.subplot(2, 2, 2)
df['gender'].value_counts().plot(kind='bar', color=['lightcoral', 'skyblue'], edgecolor='black')
plt.title('Shpërndarja sipas Gjinisë')
plt.xlabel('Gjinia')
plt.ylabel('Numri i Studentëve')
plt.xticks(rotation=0)
plt.grid(alpha=0.3, axis='y')

# Box plot për krahasimin e notave sipas gjinisë
plt.subplot(2, 2, 3)
df.boxplot(column='math score', by='gender', patch_artist=True)
plt.title('Krahasimi i Notave sipas Gjinisë (Box Plot)')
plt.suptitle('')
plt.xlabel('Gjinia')
plt.ylabel('Nota e Matematikës')

# Shto një subplot për statistika
plt.subplot(2, 2, 4)
plt.axis('off')
stats_text = f"Statistika Përmbledhëse:\n\n"
stats_text += f"Mashkull:\n"
stats_text += f"  Mesatarja: {df[df['gender']=='male']['math score'].mean():.2f}\n"
stats_text += f"  Mediana: {df[df['gender']=='male']['math score'].median():.2f}\n"
stats_text += f"  Std Dev: {df[df['gender']=='male']['math score'].std():.2f}\n\n"
stats_text += f"Femen:\n"
stats_text += f"  Mean: {df[df['gender']=='female']['math score'].mean():.2f}\n"
stats_text += f"  Median: {df[df['gender']=='female']['math score'].median():.2f}\n"
stats_text += f"  Std Dev: {df[df['gender']=='female']['math score'].std():.2f}"
plt.text(0.1, 0.5, stats_text, fontsize=11, verticalalignment='center', family='monospace')

plt.tight_layout()
plt.show()

# Statistika përmbledhëse për grup
print("\nStatistika për nota sipas gjinisë:")
print(df.groupby('gender')['math score'].describe())


# 3. TESTIMI I HIPOTEZAVE

print("\n" + "=" * 50)
print("3. TESTIMI I HIPOTEZAVE")
print("=" * 50)

# Formulimi i hipotezës
print("\nHIPOTEZAT:")
print("H0 (Hipoteza Zero): Nuk ka dallim të konsiderueshëm statistikor")
print("                     mes notave të matematikës të mashkulljve dhe femrave.")
print("H1 (Hipoteza Alternative): Ka dallim të konsiderueshëm statistikor")
print("                            mes notave të matematikës të mashkulljve dhe femrave.")
print("\nNiveli i rëndësisë: α = 0.05")

# Ndarë të dhënat sipas gjinisë
maskhkull = df[df['gender']=='male']['math score']
femen = df[df['gender']=='female']['math score']

print(f"\nNumri i mashkulljve: {len(maskhkull)}")
print(f"Numri i femrave: {len(femen)}")
print(f"Mesatarja e mashkulljve: {maskhkull.mean():.2f}")
print(f"Mesatarja e femrave: {femen.mean():.2f}")
print(f"Devijimi standard (mashkull): {maskhkull.std():.2f}")
print(f"Devijimi standard (femen): {femen.std():.2f}")

# Kryej t-test të pavarur
stat, p = ttest_ind(maskhkull, femen)

print("\n" + "-" * 50)
print("REZULTATET E T-TEST:")
print("-" * 50)
print(f"Statistika t: {stat:.4f}")
print(f"p-value: {p:.4f}")

# Interpretimi i rezultateve
print("\nINTERPRETIMI:")
if p < 0.05:
    print(f"✓ p-value ({p:.4f}) < 0.05")
    print("VENDIM: Refuzojmë H0")
    print("KONKLUZIONI: Ka një dallim statistikisht të konsiderueshëm")
    print("             mes notave të matematikës të mashkulljve dhe femrave.")
else:
    print(f"✗ p-value ({p:.4f}) ≥ 0.05")
    print("VENDIM: Nuk mund të refuzojmë H0")
    print("KONKLUZIONI: Nuk ka evidencë të mjaftueshme për të thënë se")
    print("             ka dallim të konsiderueshëm mes notave.")

# ============================================
# 4. HIPOTEZA 2: NOTA MESATARE
# ============================================

print("\n" + "=" * 50)
print("4. HIPOTEZA 2: NOTA MESATARE PER GJITHE STUDENTET")
print("=" * 50)

nota_mesatare_shtet = 60  # Supozojmë standardi kombëtar
print(f"\nHIPOTEZAT:")
print(f"H0: Mesatarja e notave = {nota_mesatare_shtet}")
print(f"H1: Mesatarja e notave ≠ {nota_mesatare_shtet}")

from scipy.stats import ttest_1samp

stat2, p2 = ttest_1samp(df['math score'], nota_mesatare_shtet)

print(f"\nMesatarja e notave në klasën tonë: {df['math score'].mean():.2f}")
print(f"Statistika t: {stat2:.4f}")
print(f"p-value: {p2:.4f}")

if p2 < 0.05:
    print(f"✓ KONKLUZIONI: Mesatarja e notave në klasën tonë")
    print(f"  ({df['math score'].mean():.2f}) është statistikisht e ndryshme nga {nota_mesatare_shtet}")
else:
    print(f"✗ KONKLUZIONI: Mesatarja e notave nuk ka diferenca të rëndësishme")

# ============================================
# 5. HIPOTEZA 3: NIVELI I EDUKIMIT PRINDËROR
# ============================================

print("\n" + "=" * 50)
print("5. HIPOTEZA 3: NDIKIMI I NIVELIT TË EDUKIMIT PRINDËROR")
print("=" * 50)

print(f"\nNivelet e edukimit prindëror:")
print(df['parental level of education'].value_counts())

print(f"\nMesatarja e notave sipas nivelit të edukimit prindëror:")
print(df.groupby('parental level of education')['math score'].agg(['count', 'mean', 'std']).round(2))

# Krahasim për dy grupe: high school vs college+
high_school = df[df['parental level of education'] == 'high school']['math score']
college_plus = df[df['parental level of education'].isin(['associate\'s degree', 'bachelor\'s degree', 'master\'s degree'])]['math score']

stat3, p3 = ttest_ind(college_plus, high_school)

print(f"\nHIPOTEZAT:")
print(f"H0: Nuk ka dallim mes notave të studentëve me prindër me high school vs college+")
print(f"H1: Ka dallim")

print(f"\nMesatarja (High School): {high_school.mean():.2f}")
print(f"Mesatarja (College+): {college_plus.mean():.2f}")
print(f"Statistika t: {stat3:.4f}")
print(f"p-value: {p3:.4f}")

if p3 < 0.05:
    print(f"✓ KONKLUZIONI: Niveli i edukimit prindëror KA ndikim statistikor")
    print(f"  në notat e matematikës të studentëve.")
else:
    print(f"✗ KONKLUZIONI: Niveli i edukimit prindëror nuk ka ndikim të rëndësishëm.")

# ============================================
# 6. HIPOTEZA 4: PËRGATITJA PER PROVIM
# ============================================

print("\n" + "=" * 50)
print("6. HIPOTEZA 4: NDIKIMI I PËRGATITJES PER PROVIM")
print("=" * 50)

print(f"\nPërgatitja për provim:")
print(df['test preparation course'].value_counts())

print(f"\nMesatarja e notave sipas përgatitjes:")
print(df.groupby('test preparation course')['math score'].agg(['count', 'mean', 'std']).round(2))

completed = df[df['test preparation course'] == 'completed']['math score']
none = df[df['test preparation course'] == 'none']['math score']

stat4, p4 = ttest_ind(completed, none)

print(f"\nHIPOTEZAT:")
print(f"H0: Përgatitja për provim nuk ndikon në notat e matematikës")
print(f"H1: Përgatitja për provim ndikon në notat")

print(f"\nMesatarja (Përgatitje kompletuar): {completed.mean():.2f}")
print(f"Mesatarja (Pa përgatitje): {none.mean():.2f}")
print(f"Dallimi: {completed.mean() - none.mean():.2f} pikë")
print(f"Statistika t: {stat4:.4f}")
print(f"p-value: {p4:.4f}")

if p4 < 0.05:
    print(f"✓ KONKLUZIONI: Përgatitja për provim KA ndikim statistikor POZITIV")
    print(f"  në notat e matematikës.")
else:
    print(f"✗ KONKLUZIONI: Përgatitja për provim nuk ka ndikim të rëndësishëm.")

print("\n" + "=" * 50)
print("PROJEKTI PËRFUNDOI ME SUKSES - 4 HIPOTEZA TË TESTUARA")
print("=" * 50)
