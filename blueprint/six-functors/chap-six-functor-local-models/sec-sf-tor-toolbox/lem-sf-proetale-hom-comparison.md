+++
id = "lem-sf-proetale-hom-comparison"
kind = "lemma"
title = "The internal-Hom comparison along the site comparison"
order = 3434
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-finite-tor-amplitude", "def-weil-pbc-constructible-complexes", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-site-perfect-complex", "lem-sf-comparison-tor-amplitude", "lem-sf-hom-finite-projective", "prop-sf-dualizable"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$ and $A=A_{E,n}$, let $T$ be a scheme and let
$\nu_T:T_{\Proet}\to T_{\Et}$ be the comparison morphism of sites. Let
$K',M'\in D^b_{ctf}(T_{\Et},A)$ be bounded constructible complexes of
$A$-modules of finite Tor
amplitude on $T_{\Et}$, with the constructibility condition of
[def-weil-pbc-constructible-complexes], and consider the canonical
comparison map of
[def-weil-derived-pullback-tensor-hom],

$$
\nu_T^*R\mathcal H om_A(K',M')\longrightarrow
R\mathcal H om_A(\nu_T^*K',\nu_T^*M').
$$

It is an isomorphism whenever $K'$ is, locally on $T_{\Et}$, a bounded
complex of finite free $A$-modules; that is, whenever $K'$ is
site-perfect.

## Proof

The assertion is local on the site, so assume that $K'$ is represented by
a bounded complex $P'$ of finite free $A_{T,\Et}$-modules, and write
$P'^\vee=R\mathcal H om_A(P',A_T)$. The termwise identity
$\mathcal H om_A(P'^i,N^j)\cong(P'^i)^\vee\otimes_AN^j$, with the usual
total-complex signs, is
[lem-sf-hom-finite-projective], which is stated for a bounded
constructible finite-Tor second variable; it applies to $M'$ by hypothesis
and gives

$$
P'^\vee\otimes_A^LM'\cong R\mathcal H om_A(P',M').
$$

The pullback $\nu_T^*$ is exact and carries finite free modules to finite
free modules, so the same computation after pullback gives
$\nu_T^*(P'^\vee)\cong(\nu_T^*P')^\vee$ and

$$
R\mathcal H om_A(\nu_T^*P',\nu_T^*M')
\cong(\nu_T^*P')^\vee\otimes_A^L\nu_T^*M',
$$

the cited identity being applicable on the pro-étale side as well because
$\nu_T^*M'$ is bounded constructible of finite Tor amplitude there, by
[lem-sf-comparison-tor-amplitude](i).
Monoidality of the inverse image,
[def-weil-derived-pullback-tensor-hom], identifies the pullback of
$P'^\vee\otimes_A^LM'$ with
$(\nu_T^*P')^\vee\otimes_A^L\nu_T^*M'$, so the canonical map is an
isomorphism on this local model. Both maps are adjoint to the pullback of
the evaluation of [prop-sf-dualizable], hence they agree, and the local
identifications glue because the comparison map is natural and
$T_{\Proet}$ is a site.
