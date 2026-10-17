+++
id = "lem-weil-local-frobenius-conjugacy-class"
kind = "lemma"
title = "Independence of the local Frobenius operator from the embedding"
lean = ["AlgebraicGeometry.WeilSheaf.nonempty_equiv_stalkAtGeometricFiberPoint", "AlgebraicGeometry.WeilComplex.nonempty_equiv_stalkAtGeometricFiberPoint"]
order = 2773
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-frobenius-detailed", "def-weil-local-frobenius-trace", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex"]
+++
Fix the finite-field datum $p,a,q,k_0,k$, a prime $\ell\neq p$, a finite
extension $E/\Ql$, $\Lambda\in\{E,\Qlb\}$, a finite-type $k_0$-scheme $Y_0$ with
$Y=Y_0\times_{k_0}k$, a Weil complex $(K,\theta)$ with $K\in\Dbc(Y,\Lambda)$ as in
[def-weil-local-frobenius-trace], a closed
point $y\in|Y_0|$ of degree $r=[\kappa(y):\Fq]$, and an integer $j\in\mathbf
Z$. For two embeddings $\kappa(y)\hookrightarrow k$ with associated geometric
points $\bar y,\bar y'\to Y$, the local operators $F_y$ and $F'_y$ on the
stalks of the cohomology sheaf $\mathcal H^j(K)$
constructed in [def-weil-local-frobenius-trace] are conjugate: there is an
isomorphism $\mathcal H^j(K)_{\bar y}\cong \mathcal
H^j(K)_{\bar y'}$ carrying $F_y$ to $F'_y$.
