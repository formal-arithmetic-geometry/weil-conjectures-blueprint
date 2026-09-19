+++
id = "thm-rational-lattice-localization"
kind = "theorem"
title = "Integral lattice localization equivalence"
order = 15
uses = ["def-weil-derived-complete-integral", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$.
Tensoring with $E_Y$ induces an exact equivalence

$$
D^b_c(Y,\mathcal O_E)[1/\varpi_E]
\xrightarrow{\ \sim\ }D^b_c(Y,E),
$$

where the source has the same objects as $D^b_c(Y,\mathcal O_E)$ and,
for every $K,L\in D^b_c(Y,\mathcal O_E)$,

$$
\Hom(K,L)[1/\varpi_E]
=\Hom_{D^b_c(Y,\mathcal O_E)}(K,L)
\otimes_{\mathcal O_E}E.
$$

Every rational constructible complex therefore admits an integral lattice;
two lattices become commensurable after multiplication by powers of
$\varpi_E$.
