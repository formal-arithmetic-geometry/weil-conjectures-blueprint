+++
id = "def-weil-pbc-epsilon-direct-image-comparison"
kind = "definition"
title = "Canonical direct-image comparison"
order = 819
uses = ["def-weil-pbc-epsilon-unit-counit"]
+++
Let $f:X\to Y$ be quasi-compact and quasi-separated. For an $A$-module
sheaf $F$ on $X_{\mathrm{et}}$, define

$$
\delta_{f,F}:\epsilon_Y^{-1}f_{\mathrm{et},*}F
\longrightarrow f_{\mathrm{proet},*}\epsilon_X^{-1}F
$$

to be adjoint to

$$
f_{\mathrm{et},*}F\xrightarrow{f_{\mathrm{et},*}\eta^X_F}
f_{\mathrm{et},*}\epsilon_{X,*}\epsilon_X^{-1}F
=\epsilon_{Y,*}f_{\mathrm{proet},*}\epsilon_X^{-1}F.
$$

The equality follows by evaluating both restrictions on an etale object of
$Y$. Right deriving this natural transformation and using exactness of
$\epsilon_Y^{-1}$ defines

$$
D_f(L):\epsilon_Y^{-1}Rf_{\mathrm{et},*}L
\longrightarrow Rf_{\mathrm{proet},*}\epsilon_X^{-1}L
$$

for $L\in D^+(X_{\mathrm{et}},A)$.
