+++
id = "lemma-growth-finite-corrections"
kind = "lemma"
title = "Finite corrections"
order = 1208
lean = ["AlgebraicGeometry.WeilSheaf.l2Weight_le_max_of_traceEnergy_le_add"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-growth-squared-traces"]
+++
Let $K$ and $L$ be constructible Weil complexes on an affine curve
$X_0$, and let $a$ be a real number. Suppose that there is a constant
$C$ with
$\sum_{x\in X_0(k_n)}|\iota(t_{K,n}-t_{L,n})(x)|^2\le Cq^{na}$ for all
$n$. If $\max(\nu(K),\nu(L))>a-1$, then $\nu(K)=\nu(L)$.
