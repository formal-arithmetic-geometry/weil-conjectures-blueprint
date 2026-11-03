+++
kind = "proof"
of = "sk-thm-smooth-base-change"
uses = ["sk-lem-induction", "sk-prop-deg0", "sk-lem-sbc-exchange-compatibility", "sk-thm-pe-direct-image-comparison", "sk-lem-universal-datum", "sk-thm-vanishing", "sk-prop-normal-form"]
+++
A smooth morphism is flat, locally of finite presentation, and has
geometrically reduced fibres, and so the case of degree zero is
Lemma [sk-prop-deg0]. Let $q\geq1$ and assume the theorem in
all degrees less than $q$. Fix $n$ invertible on $Y$. Since smoothness is
stable under base change, we may apply the induction hypothesis after
every base change $T\to Y$, which shows that $\mathrm{BC}(g,n,q-1)$ holds. By étale
coordinates and composition of base change maps, it suffices to treat the case
where $g$ is affine and smooth of relative dimension one.

If $\mathrm{BC}(g,n,q)$ failed, Lemma [sk-lem-universal-datum]
would give $S$, $C$, $h$ and $m$ with $R^qh_*\underline{\mathbf Z/m}\neq0$,
contradicting Proposition [sk-thm-vanishing]. Hence
$\mathrm{BC}(g,n,q)$ holds for affine $g$ of relative dimension one, and
therefore, by the reduction above, for every smooth $g$. Since $f$ and
$f'$ are qcqs, both sides commute with the filtered union
$F=\bigcup_nF[n]$, and we get the theorem for $F$. By
Theorem [sk-thm-pe-direct-image-comparison] the isomorphism and
the base change map transfer from the étale sites to $Y'_{\mathrm{pro}\acute{e}t}$.
