import math

print("1. WGS '84")
print("2. GRS '67")
print("3. Sinta Alfi")
pilih = int(input("referernsi(1-3) = "))

if pilih == 1:
    a = 6378137
    f = 1/298.257223563

elif pilih == 2:
    a = 6378160
    f = 1/298.247

elif pilih == 3:
    a = 6378252
    f = 1/298.482

list_d = []
list_m = []
list_s = []
list_lintang = []
for i in range(1, 11):
    print("\nlintang ke ", i)
    d = int(input("nilai derajat D = "))
    m = int(input("nilai derajat M = "))
    s = float(input("nilai derajat S = "))
    print(str(d)+"°", str(m)+"'", str("{:.2f}".format(s))+"\"")
    lintang = d+(m/60)+(s/3600)
    list_d.append(d)
    list_m.append(m)
    list_s.append(s)
    list_lintang.append(lintang)


nilai_N = []
nilai_M = []
nilai_nm = []
for ltg in list_lintang:
    b = a * (1 - f)
    e2 = (a * a - b * b) / (a * a)
    x = (1 - (e2 * math.sin(ltg * math.pi / 180) * math.sin(ltg * math.pi / 180)))
    N = a / (x ** 0.5)
    M = (a * (1 - e2)) / (x ** 1.5)
    n_m = N - M
    nilai_N.append(N)
    nilai_M.append(M)
    nilai_nm.append(n_m)


print("\nNo.".center(4), "Lintang(ϕ)".center(17), "N(m)".center(15), "M(m)".center(15), "N-M(m)".center(15))

for z in range(len(list_d)):
    print(str(z).center(4), (str(list_d[z])+"°").center(4), (str(list_m[z])+"'").center(3), (str("{:.2f}".format(list_s[z]))+"\"").center(9), "{:.3f}".format(nilai_N[z]).center(15), "{:.3f}".format(nilai_M[z]).center(15), "{:.3f}".format(nilai_nm[z]).center(15))