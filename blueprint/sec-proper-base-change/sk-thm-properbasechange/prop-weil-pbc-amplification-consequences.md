+++
id = "prop-weil-pbc-amplification-consequences"
kind = "theorem"
title = "Amplitude containments implied by amplification"
order = 1391
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-cartesian-square", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-derived-categories", "def-weil-pbc-finite-level-amplification", "def-weil-pbc-proetale-operations", "lem-weil-pbc-pullback-preserves-bounded-constructible", "prop-weil-pbc-restriction-direct-image"]
tags = ["latex:proposition"]
+++
Let $\square$ be a cartesian square [def-weil-pbc-cartesian-square] with
$\Lambda$-coefficient data as in the adic coefficient datum and suppose that
$\mathrm{AMP}(\square;c)$ of [def-weil-pbc-finite-level-amplification]
holds. Then for every $n\geq1$, with $P_n=A/I^n$, and all $a\leq b$,
$$
 \begin{aligned}
  Rf_*\bigl(D^b_c(X_{\Proet},P_n)^{[a,b]}\bigr)
  &\subset D^b_c(Y_{\Proet},P_n)^{[a,b+c]},\\
  Rf'_*\bigl(D^b_c(X'_{\Proet},P_n)^{[a,b]}\bigr)
  &\subset D^b_c(Y'_{\Proet},P_n)^{[a,b+c]},\\
  Lg_n^*\bigl(D^b_c(Y_{\Proet},P_n)^{[a,b]}\bigr)
  &\subset D^b_c(Y'_{\Proet},P_n)^{[a,b]},\\
  Lg_n'^*\bigl(D^b_c(X_{\Proet},P_n)^{[a,b]}\bigr)
  &\subset D^b_c(X'_{\Proet},P_n)^{[a,b]}.
 \end{aligned}
$$
