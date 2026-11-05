+++
id = "lemma-bounds-squared-traces"
kind = "lemma"
title = "Bounds for squared traces"
order = 1205
lean = ["AlgebraicGeometry.WeilSheaf.exists_traceEnergy_le_of_hasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.l2Weight_le_of_hasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.l2Weight_le_of_traceEnergy_le", "AlgebraicGeometry.WeilSheaf.traceEnergy_constantTwist", "AlgebraicGeometry.WeilSheaf.l2Weight_eq_sub_of_traceEnergy_eq"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-weights", "definition-growth-squared-traces"]
+++
Let $X_0$ be a smooth affine curve over $k_0$, and let $a$ be a real
number.

1. If $F$ is a lisse Weil sheaf of rank $r$ on $X_0$, punctually of
   weights $\le a$, then $S_n(F)\le Dr^2q^{n(a+1)}$ for all $n$, with $D$
   as in Lemma [lemma-point-count-bound], and hence $\nu(F)\le a$.
2. If $K$ is a constructible Weil complex on $X_0$ supported at
   finitely many closed points, and every eigenvalue $\alpha$ of
   $\operatorname{Frob}_x$ on every $\mathcal H^i(K)_{\bar x}$ satisfies
   $|\iota(\alpha)|\le q_x^{a/2}$, then there is a constant $C$ with
   $S_n(K)\le Cq^{na}$ for all $n$, and hence $\nu(K)\le a-1$.
3. For every constructible Weil complex $K$ on $X_0$ and every
   $b\in\overline{\mathbf Q}_\ell^\times$, we have
   $\nu(K\otimes\mathcal B_b)=\nu(K)+\lambda_\iota(b)$, with
   $\mathcal B_b$ as in Proposition [proposition-weights-under-usual-operations].
