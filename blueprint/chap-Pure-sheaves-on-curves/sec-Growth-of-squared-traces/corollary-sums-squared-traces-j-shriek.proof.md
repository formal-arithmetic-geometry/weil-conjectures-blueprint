+++
kind = "proof"
of = "corollary-sums-squared-traces-j-shriek"
order = 1215
uses = ["proposition-sp-unique-adjoint", "definition-trace-function", "theorem-trace-formula-euler-product", "lemma-point-count-bound", "lemma-extreme-degrees-affine-curve", "lemma-growth-finite-corrections", "theorem-weights-sums-squared-traces", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For $j_!$ the trace function is that of $\mathcal G$ extended by zero,
and for $j_*$ it differs from this at finitely many points of small
weight, which Lemma [lemma-growth-finite-corrections] allows us to
ignore.

The open curve $U_0$ is again smooth, geometrically connected and
affine, and Theorem [theorem-weights-sums-squared-traces] on $U_0$ gives
$\nu(\mathcal G)=w$. Extension by zero only adds zero traces, so
$\nu(j_!\mathcal G)=w$. The trace functions of $j_*$
and of the extension by zero differ only at the points of
$X_0-U_0$, by the trace function of the boundary stalks. These stalks
have weights at most $w$ by
Proposition [proposition-weights-j-boundary-points], so if $i$
denotes the inclusion of $X_0-U_0$, then
Lemma [lemma-bounds-squared-traces](2), applied to the sheaf
$i_*i^*j_*\mathcal G$, bounds the squared sum of the difference by
$Cq^{nw}$. Since $\nu(j_!\mathcal G)=w>w-1$,
Lemma [lemma-growth-finite-corrections] shows that
$\nu(j_*\mathcal G)$ is still $w$.
