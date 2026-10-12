+++
id = "def-weil-pbc-finite-level-amplification"
kind = "definition"
title = "Finite-level amplification condition"
order = 1350
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-cartesian-square", "def-weil-pbc-constructible-direct-image-finiteness", "def-weil-pbc-derived-categories", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-proetale-operations"]
+++
For a cartesian square [def-weil-pbc-cartesian-square] $\square$ with
$\Lambda$-coefficient data as in the adic coefficient datum, write
$\mathrm{AMP}(\square;c)$ if, for every $n\geq1$, with $P_n=A/I^n$ and
$\Lambda=P_n$:

1. the finite-level direct images satisfy the finiteness conditions
   [def-weil-pbc-constructible-direct-image-finiteness]
   $\mathrm{FIN}(f,P_n;c)$ and $\mathrm{FIN}(f',P_n;c)$;
2. the finite-level pullbacks $Lg_n^*,Lg_n'^*$ restrict to exact
   triangulated functors
   $$
    \begin{aligned}
     Lg_n^* &:D^b_c(Y_{\Proet},P_n)\longrightarrow
              D^b_c(Y'_{\Proet},P_n),\\
     Lg_n'^* &:D^b_c(X_{\Proet},P_n)\longrightarrow
               D^b_c(X'_{\Proet},P_n)
    \end{aligned}
   $$
   which carry objects with cohomology in $[a,b]$ into objects with
   cohomology in $[a,b]$.

Here $D^b_c(Z_{\Proet},P_n)^{[a,b]}$ denotes the full class of objects of
$D^b_c(Z_{\Proet},P_n)$ whose cohomology vanishes outside $[a,b]$.

Conditions (1) and (2) imply the amplitude containments for
$Rf_*,Rf'_*,Lg_n^*,Lg_n'^*$.
