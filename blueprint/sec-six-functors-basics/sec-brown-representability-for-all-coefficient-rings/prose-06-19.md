+++
id = "prose-06-19"
kind = "hidden"
title = "Brown representability for all coefficient rings"
order = 312
+++
Let $\Lambda$ be an admissible coefficient ring. The functor $Rf_!$ on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$ preserves direct sums and $D^b_{\mathrm{ctf}}(-,\Lambda)$
(Proposition [sk-prop-sf-comp-coherence]). To obtain a right
adjoint $f^!$ from Brown representability, we also need that the objects
of $D^b_{\mathrm{ctf}}(-,\Lambda)$ are compact generators of the localizing category.
The next lemma checks this for every admissible $\Lambda$. For
$\mathcal O_E$ it uses the compactness proved later, in
Section [sec-i-heart], by reduction to torsion coefficients; that proof does
not use $f^!$.

Once the hypotheses hold, the construction is formal. For a fixed $N$,
the functor $M\mapsto\Hom(Rf_!M,N)$ turns direct sums into products
because $Rf_!$ preserves direct sums, and Brown representability produces
an object $f^!N$ representing it. Compactness enters a second time: since
$Rf_!$ maps the compact generators $D^b_{\mathrm{ctf}}(X,\Lambda)$ into
$D^b_{\mathrm{ctf}}(Y,\Lambda)$, which consists of compact objects, the adjoint $f^!$
preserves direct sums as well (Theorem [sk-prop-sf-existence]).
