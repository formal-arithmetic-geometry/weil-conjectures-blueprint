+++
id = "thm-pod-finite-reduction"
kind = "theorem"
title = "Finite reduction of the Poincare pairing"
order = 3562
uses = ["def-pod-coefficient-dual-on-x", "def-pod-conventions", "def-pod-derived-poincare-pairing", "def-pur-smooth-trace", "def-weil-site-perfect-complex", "lem-fix-operation-reduction", "thm-pod-identification-of-the-comparison", "thm-pod-point-perfectness", "thm-pur-finite-reduction-of-purity", "thm-sf-dual-perfect"]
+++
Use the smooth Poincare setting, with
the admissible structure morphism and normalized smooth orientation.
Let $n\geq m\geq1$, put $A_n=\mathcal O_E/\pi_E^n$ and
$A_m=\mathcal O_E/\pi_E^m$, and let $K_n$ be a
site-perfect constructible
$A_n$-complex. Put $K_m=K_n\otimes^L_{A_n}A_m$.
The coefficient comparisons identify the reduction of the
derived Poincare pairing
for $K_n$ with the pairing for $K_m$. In particular, writing
$K_n^\vee$ for its coefficient dual,
the canonical isomorphisms make the square

$$
\begin{array}{ccc}
R\Gamma_c(X,K_n)^\vee\otimes^L_{A_n}A_m
&\xrightarrow{\beta_{K_n}^{\sharp,-1}\otimes1}&
R\Gamma(X,K_n^\vee(d))[2d]\otimes^L_{A_n}A_m\\
\downarrow\wr&&\downarrow\wr\\
R\Gamma_c(X,K_m)^\vee
&\xrightarrow{\beta_{K_m}^{\sharp,-1}}&
R\Gamma(X,K_m^\vee(d))[2d]
\end{array}
$$

commute. Here $\beta^{\sharp,-1}$ denotes the inverse of the
tensor–Hom adjoint of the pairing.
