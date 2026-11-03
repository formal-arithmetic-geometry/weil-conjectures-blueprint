+++
kind  = "proof"
of    = "prop-constructible-open-closed"
uses = ["def-constructible-finite-locally-constant", "lemma-constructible-iso-invariance", "prop-constructible-pullback"]
+++
``Only if'' is [prop-constructible-pullback]. Conversely let
$(\kappa_l\colon W_l\to U)_{l<m}$ and $(\lambda_k\colon V_k\to Z)_{k<n}$ be
stratifications witnessing the constructibility of $j^*\mathcal F$ and
$i^*\mathcal F$. The family of the $j\circ\kappa_l$ and the
$i\circ\lambda_k$ is a stratification of $X$ with $m+n$ strata: each
composite is an immersion; the images $j(U_l)$ are locally closed in $X$,
being locally closed in the open $U$, and constructible in $X$ because $j$
is quasi-compact (the image of a constructible subset under a quasi-compact
open immersion is constructible); the images $i(Z_k)$ are locally
closed and constructible in $X$, being so in the closed $Z$; and the images are
pairwise disjoint and cover $X$ because the $U_l$ partition $U$, the $Z_k$
partition $Z$, and $X=U\sqcup Z$. Finally
$(j\circ\kappa_l)^*\mathcal F\cong\kappa_l^*j^*\mathcal F$ and
$(i\circ\lambda_k)^*\mathcal F\cong\lambda_k^*i^*\mathcal F$ are finite
locally constant by construction and [lemma-constructible-iso-invariance].
