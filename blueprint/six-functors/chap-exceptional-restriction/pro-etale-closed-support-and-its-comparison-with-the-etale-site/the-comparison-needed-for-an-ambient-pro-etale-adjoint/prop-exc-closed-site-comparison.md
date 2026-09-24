+++
id = "prop-exc-closed-site-comparison"
kind = "theorem"
title = "Closed exceptional image commutes with site comparison"
order = 3333
tags = ["latex:proposition"]
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-proetale-operations", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-exc-closed-ambient", "lem-exc-closed-localization", "lem-exc-closed-support-triangle", "lem-exc-proetale-closed-exact", "lem-exc-proetale-closed-fully-faithful", "lem-exc-proetale-closed-support", "lem-exc-proetale-support-triangle", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image", "prop-weil-pbc-site-comparison-finite-level"]
+++
Let $T$ be Noetherian, let $i:Z\hookrightarrow T$ be a
closed immersion, and
let $A$ be a finite ring. With
site comparison
$\nu$, the canonical map is an isomorphism

$$
\nu_Z^*Ri^!_{\mathrm{et}}K
\xrightarrow{\sim}Ri^!_{\mathrm{proet}}\nu_T^*K,
\qquad K\in D^+(T_{\mathrm{et}},A).
$$

Both exceptional functors here are ambient right adjoints on ordinary
derived categories; their
constructible restrictions are not used to construct this map.

## Proof

Write $j:U\hookrightarrow T$ for the open complement. Both
$i$ and $j$ are quasi-compact and quasi-separated. Apply the
exact $\nu_T^*$ of
[prop-weil-pbc-site-comparison-finite-level] to the etale
triangle of [lem-exc-closed-support-triangle], for the right
adjoint $Ri^!_{\mathrm{et}}$ of [lem-exc-closed-ambient].
Direct-image comparison
[prop-weil-pbc-comparison-direct-image] for $i$ identifies its
first term with $i_{\mathrm{proet},*}\nu_Z^*Ri^!_{\mathrm{et}}K$.
Comparison for $j$, together with
[lem-weil-pbc-comparison-pullback], identifies its third term
with $Rj_{\mathrm{proet},*}j_{\mathrm{proet}}^*\nu_T^*K$.
All these comparisons apply to bounded-below objects: the sheaf
right adjoint $i^!$ is left exact, hence its right derived functor
takes $D^+$ to $D^+$, irrespective of any upper bound.

The transported counit $i_*\nu_Z^*Ri^!_{\mathrm{et}}K\to\nu_T^*K$
is adjoint, under [lem-exc-proetale-closed-support], to the
specified comparison $\beta$. We verify this particular map
by the universal property of support, rather than choosing an
unspecified map between cones. Put
$Q=\nu_Z^*Ri^!_{\mathrm{et}}K$ and $N=\nu_T^*K$.
For every $M\in D(Z_{\mathrm{proet}},A)$, the equality
$j^*i_*M=0$ follows from [lem-exc-closed-localization]
and exactness in [lem-exc-proetale-closed-exact].
Derived adjunction in [def-weil-pbc-proetale-operations]
therefore gives, for every integer $r$,

$$
\operatorname{Hom}(i_*M,Rj_*j^*N[r])
=\operatorname{Hom}(j^*i_*M,j^*N[r])=0.
$$

Applying $\operatorname{Hom}(i_*M,-)$ to the transported
etale triangle consequently identifies
$\operatorname{Hom}(i_*M,i_*Q)$ with
$\operatorname{Hom}(i_*M,N)$, by composition with its
counit. Full faithfulness from
[lem-exc-proetale-closed-fully-faithful] passes to ordinary
derived categories here because both $i_*$ and $i^*$
are exact and their counit is an isomorphism. Hence the last
identification is

$$
\operatorname{Hom}(M,Q)\xrightarrow{\sim}
\operatorname{Hom}(M,Ri^!_{\mathrm{proet}}N).
$$

By construction this map is composition with $\beta$.
Equivalently the pro-etale support triangle in
[lem-exc-proetale-support-triangle] represents the same
support functor as the transported triangle, with the same
counit. Yoneda, for all ambient objects $M$, proves that
$\beta$ is an isomorphism. This identifies the actual
ambient right adjoints, without assuming their constructible
restrictions or using full faithfulness of $\nu^*$ as a
substitute for the support argument.
