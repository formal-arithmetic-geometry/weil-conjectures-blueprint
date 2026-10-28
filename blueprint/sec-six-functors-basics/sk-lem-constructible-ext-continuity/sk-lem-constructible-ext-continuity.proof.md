+++
kind  = "proof"
of    = "sk-lem-constructible-ext-continuity"
uses = ["sk-lem-formal-closed-support", "sk-cor-pe-bounded-continuity"]
+++
Both sides are cohomological functors of $M$. Hence, by the five lemma, the class of objects
$M$ for which the claim holds is closed under extensions and shifts, and it suffices to treat
$M=a_!L$, with $a=i\circ u\colon S\hookrightarrow Z\hookrightarrow X$ as in
[sk-lem-formal-closed-support]. The only property of $L$ used below is that $L^\vee\otimes-$
is exact. Details: [det-lem-constructible-ext-continuity-devissage].

By the stratum formula [sk-lem-formal-closed-support] (2), we must show that the cohomology
of $R\Gamma(S,L^\vee\otimes u^*R\underline\Gamma_ZK)$ commutes with the colimit, where
$K=\varinjlim_\alpha K_\alpha^\bullet$. To this end we apply the exact functor
$L^\vee\otimes u^*i^*(-)\colon D(X_{\mathrm{proét}},\Lambda)\to D(S_{\mathrm{proét}},\Lambda)$ to the
triangle $i_*R\underline\Gamma_ZK\to K\to Rj_*j^*K\to$ and to the corresponding triangles for
the $K_\alpha^\bullet$. By the long exact sequence and the five lemma, it suffices to treat the
two terms
$$
R\Gamma\bigl(S,L^\vee\otimes u^*i^*K\bigr)\quad\text{and}\quad
R\Gamma\bigl(S,L^\vee\otimes u^*i^*Rj_*j^*K\bigr).
$$
The functor $L^\vee\otimes u^*i^*(-)$ is exact, commutes with colimits and preserves the lower
bound. Hence [sk-cor-pe-bounded-continuity] on $S$ proves the claim for the first term. For the
second term, consider the hypercohomology spectral sequence
$$
E_2^{p,r}=H^p\bigl(S,L^\vee\otimes u^*i^*R^rj_*(j^*K)\bigr)\Longrightarrow
H^{p+r}\bigl(S,L^\vee\otimes u^*i^*Rj_*j^*K\bigr)
$$
which is functorial in $K$. The sheaves $R^rj_*(j^*K_\alpha)$ commute with the colimit by the
second part of [sk-cor-pe-bounded-continuity], and by its first part so does $H^p(S,-)$. Thus,
after passing to the colimit, the map of spectral sequences is an isomorphism on $E_2$.
Because of the common lower bound, only finitely many $E_2^{p,r}$ contribute to a given total
degree, and therefore the abutments agree as well. Details:
[det-lem-constructible-ext-continuity-stratum].
