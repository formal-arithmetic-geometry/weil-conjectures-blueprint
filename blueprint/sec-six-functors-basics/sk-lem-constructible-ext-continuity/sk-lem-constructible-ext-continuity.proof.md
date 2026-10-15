+++
kind  = "proof"
of    = "sk-lem-constructible-ext-continuity"
+++
Both sides are cohomological functors of $C$, so by the five lemma the class of $C$ for which
the claim holds is closed under extensions and shifts. It therefore suffices to treat
$C=a_!L$, with $a=i\circ u\colon S\hookrightarrow Z\hookrightarrow X$ as in
[sk-lem-formal-closed-support]. The only property of $L$ used below is that $L^\vee\otimes-$
is exact. Details: [det-lem-constructible-ext-continuity-devissage].

By the stratum formula of [sk-lem-formal-closed-support] (2) we must show that the
cohomology of $R\Gamma(S,L^\vee\otimes u^*R\underline\Gamma_ZK)$ commutes with the colimit.
Apply the exact functor
$L^\vee\otimes u^*i^*(-)\colon D(X_{\mathrm{proét}},\Lambda)\to D(S_{\mathrm{proét}},\Lambda)$ to the
triangle $K\to Rj_*j^*K$ whose fiber defines $R\underline\Gamma_Z$. By the long exact sequence
and the five lemma, it suffices to treat the two terms
$$
R\Gamma\bigl(S,L^\vee\otimes u^*i^*K\bigr)\quad\text{and}\quad
R\Gamma\bigl(S,L^\vee\otimes u^*i^*Rj_*j^*K\bigr).
$$
The functor $L^\vee\otimes u^*i^*(-)$ is exact, commutes with colimits and preserves the lower
bound, so [sk-lem-bounded-continuity] on $S$ handles the first term. For the second, the
hypercohomology spectral sequence
$$
E_2^{p,r}=H^p\bigl(S,L^\vee\otimes u^*i^*R^rj_*(j^*K)\bigr)\Longrightarrow
H^{p+r}\bigl(S,L^\vee\otimes u^*i^*Rj_*j^*K\bigr)
$$
is functorial in $K$. The sheaves $R^rj_*(j^*K_i)$ commute with the colimit by the second
part of [sk-lem-bounded-continuity], and then $H^p(S,-)$ does by its first part. So the map of
spectral sequences is an isomorphism on $E_2$, after passing to the colimit. Because of the
common lower bound, only finitely many $E_2^{p,r}$ contribute to a given total degree, so the
abutments agree as well. Details: [det-lem-constructible-ext-continuity-stratum].
