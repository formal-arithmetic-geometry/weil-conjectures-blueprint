+++
id = "lemma-radius-squared-traces"
kind = "lemma"
title = "Radius of convergence"
order = 1202
lean = ["AlgebraicGeometry.WeilSheaf.l2Series", "AlgebraicGeometry.WeilSheaf.lt_l2Weight_iff"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-growth-squared-traces"]
+++
Let $K$ be a constructible Weil complex on an affine curve $X_0$. The
series $\varphi_K(t)=\sum_{n\ge1}S_n(K)t^{n-1}$ has radius of
convergence $q^{-\nu(K)-1}$, where this number is read as $+\infty$ if
$\nu(K)=-\infty$ and as $0$ if $\nu(K)=+\infty$.
