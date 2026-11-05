+++
kind = "proof"
of = "theorem-comparison-direct-images--1"
order = 133002
uses = ["proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison"]
+++
Restriction to the étale subsite commutes with direct image:
$\nu_{Y,*}g_{\mathrm{pro}\acute{e}t,*}\simeq
g_{\acute{e}t,*}\nu_{X,*}$. Taking its mate under
$\nu_X^*\dashv\nu_{X,*}$ and $\nu_Y^*\dashv\nu_{Y,*}$ defines
$c_g^0$. After restriction to the étale subsite this map is an
isomorphism, since the units of the comparison adjunctions are
isomorphisms by [theorem-classical-sheaves-essential-image].

Suppose now that $g$ is quasi-compact and quasi-separated. We can
test whether $c_g^0$ is an isomorphism on the affine pro-étale basis
[proposition-pro-etale-affines-form-basis]. Write a basis object as
$V=\varprojlim_iV_i$, with $V_i$ affine and étale over $Y$.
The schemes $X\times_YV_i$ are quasi-compact and quasi-separated,
their transition maps are affine, and their limit is $X\times_YV$.
The continuity description of $\nu^*$ in
[proposition-comparison-morphism-inverse-image] expresses both sides
of $c_g^0$ on $V$ as filtered colimits of their values on $V_i$.
The comparison is an isomorphism at every stage, hence also on $V$.

For acyclicity, it suffices to show that
$H^q((X\times_YV)_{\mathrm{pro}\acute{e}t},(\nu_X^*I)|_{X\times_YV})=0$
for every such $V$ and $q>0$. Indeed, an injective resolution computes
the higher direct images, and exactness of its complexes of sections
over the affine pro-étale basis implies exactness of the resulting
complex of sheaves in positive degrees. Compatibility of $\nu^*$ with
pullback and the global cohomology comparison
[theorem-bounded-below-cohomology-comparison], obtained from
[lemma-acyclicity-pulled-back-injectives], reduce this vanishing to
étale cohomology on $X\times_YV$.
The restriction of $I$ to each $(X\times_YV_i)_{\acute{e}t}$ is
injective, since étale pullback preserves injectives, so its positive
cohomology vanishes. Continuity of étale cohomology under cofiltered
limits of quasi-compact quasi-separated schemes with affine transition
maps gives the required vanishing on $X\times_YV$.
