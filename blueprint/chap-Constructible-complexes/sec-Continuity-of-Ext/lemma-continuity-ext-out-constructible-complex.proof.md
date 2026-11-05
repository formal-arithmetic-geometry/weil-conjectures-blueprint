+++
kind = "proof"
of = "lemma-continuity-ext-out-constructible-complex"
order = 282
uses = ["definition-lisse-sheaves", "corollary-coefficient-heart-b"]
+++
We reduce to a single generator $a_!L$ and then use
(3.1) to turn Hom into cohomology on the stratum $S$,
where Corollary [corollary-continuity-cohomology] applies. The common lower bound
is used at the end, to compare the abutments of two spectral sequences.

In both cases $M$ is obtained by finitely many extensions and shifts from
sheaves $a_!L$, with $a:S\hookrightarrow X$ a locally closed immersion and
$L$ a finite locally free $\Lambda_S$-module: in case (1) by
Corollary [corollary-coefficient-heart-b], and in case (2) by assumption.
Both sides are cohomological functors of $M$. By the five lemma, the class
of objects $M$ for which the claim holds is therefore closed under
extensions and shifts, so it suffices to treat $M=a_!L$, with $a=i\circ
u:S\hookrightarrow Z\hookrightarrow X$ as in
Lemma [lemma-sections-support-closed-subscheme]. The only property of $L$ used
below is that $L^\vee\otimes-$ is exact.

By (3.1), we must show that the cohomology of
$R\Gamma(S,L^\vee\otimes u^*R\underline\Gamma_ZK)$ commutes with the
colimit, where $K=\varinjlim_\alpha K_\alpha^\bullet$. To this end we apply the exact
functor
$L^\vee\otimes u^*i^*(-):D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(S_{\mathrm{pro}\acute{e}t},\Lambda)$
to the triangle $i_*R\underline\Gamma_ZK\to K\to Rj_*j^*K\to$ and to the
corresponding triangles for the $K_\alpha^\bullet$. By the
long exact sequence and the five lemma, it suffices to treat the two
terms

$$
R\Gamma\bigl(S,L^\vee\otimes u^*i^*K\bigr)
\quad\text{and}\quad
R\Gamma\bigl(S,L^\vee\otimes u^*i^*Rj_*j^*K\bigr).
$$

For the first term, Corollary [corollary-continuity-cohomology] on $S$
applies, because the functor $L^\vee\otimes u^*i^*(-)$ is exact, commutes
with colimits and preserves the lower bound. For the second term, consider the
hypercohomology spectral sequence

$$
E_2^{p,r}=H^p\bigl(S,L^\vee\otimes u^*i^*R^rj_*(j^*K)\bigr)
\Longrightarrow
H^{p+r}\bigl(S,L^\vee\otimes u^*i^*Rj_*j^*K\bigr)
$$

which is functorial in $K$. The sheaves $R^rj_*(j^*K_\alpha)$ commute with the
colimit by the second part of Corollary [corollary-continuity-cohomology], and
$H^p(S,-)$ does by its first part. Hence, after passing to the
colimit, the map of spectral sequences is an isomorphism on $E_2$. The
abutments agree as well, since by the common lower bound only finitely
many $E_2^{p,r}$ contribute to a given total degree.
