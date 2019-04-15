import numpy as np

R_1 = 0.1725

Vin = 19.5
omega = 2* np.pi * 60
X_m = omega * 0.0086529
X_l1 = omega * 0.000731913
X_l2 = X_l1

Z_th_real = (-X_m**2*R_1 - X_m*X_l1*R_1 + R_1*X_m*X_l1) / (-(X_l1+ X_m)**2 - R_1**2)

Z_th_img = (-R_1**2*X_m - X_m**2*X_l1 - X_m * X_l1**2) / (-(X_l1+ X_m)**2 - R_1**2)

Vth = Vin * X_m / (np.sqrt((X_m+X_l1)**2+R_1**2)) 

print(Vth)
print(Z_th_real)
print(Z_th_img)




