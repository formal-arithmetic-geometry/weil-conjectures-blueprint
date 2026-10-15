+++
id = "det-curve-artin-schreier-proper"
kind = "proposition"
title = "Artin–Schreier computation on a smooth proper curve"
uses = ["lem-sc-as-sequence", "lem-sc-ga-cohomology", "lem-sc-global-functions", "lem-sc-artin-schreier-k", "lem-sc-lang-steinberg", "lem-sc-fixed-points-finite", "lem-sc-frobenius-fixed-invariance", "lem-pc-flat-base-change-cohom", "def-pc-genus", "lem-sc-base-change-curve", "def-sc-field-extension"]
+++
Let $k$ be algebraically closed of characteristic $p>0$, $C$ a smooth proper
connected curve of genus $g=\dim_kH^1(C,\cO_C)$ ([def-pc-genus]) over $k$,
$E=H^1(C,\cO_C)$, and $F:E\to E$ the $p$-linear map induced by the absolute
Frobenius $a\mapsto a^p$ of $\cO_C$. Then the Artin–Schreier sequence
induces

$$
H^0(C_{\mathrm{ét}},\mathbf F_p)=\mathbf F_p,\qquad
H^1(C_{\mathrm{ét}},\mathbf F_p)\xrightarrow{\sim}\ker(F-1:E\to E),\qquad
H^q(C_{\mathrm{ét}},\mathbf F_p)=0\ (q\geq2),
$$

and $\dim_{\mathbf F_p}H^1(C_{\mathrm{ét}},\mathbf F_p)\leq g$. For an
extension $k\subseteq k'$ of algebraically closed fields, the pullback maps
$\rho^q_{k'/k}(C,\mathbf F_p)$ of [def-sc-field-extension] are isomorphisms
for all $q$.
