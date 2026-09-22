+++
id = "lem-weil-pbc-proper-open-comparison-proetale"
kind = "lemma"
title = "Proper-open comparison for complexes from the etale site"
order = 3313
lean = ["AlgebraicGeometry.Proetale.properOpenComparison_isIso_of_etaleOrigin"]
uses = ["lem-weil-pbc-proper-open-comparison-iso", "lem-weil-pbc-proper-open-comparison-composition"]
+++
Let $u:T_1\to T_2$ be a proper morphism between Noetherian schemes, and
$j_i:X\hookrightarrow T_i$ open immersions with $uj_1=j_2$. Fix a finite
coefficient ring $\Lambda=A_{E,n}$, and a bounded-below etale complex
$L\in D^+(X_{\Et},\Lambda)$. Writing $K=\nu_X^*L$ for pullback along the
comparison morphism, there is a canonical isomorphism on the pro-etale site
$$
 j_{2!}K\xrightarrow{\sim}Ru_*j_{1!}K.
$$
Here $j_!$ is extension by zero and $Ru_*$ is the derived direct image. These
maps are the identity for the identity proper map and commute with
composition of proper maps fixing $X$.

## Proof

Apply the exact functor $\nu^*$ of the site comparison to the etale
isomorphism [lem-weil-pbc-proper-open-comparison-iso]. The right side is
identified with the pro-etale direct image by the comparison of direct images;
properness gives its quasi-compact and quasi-separated hypothesis.

For the left side, the comparison morphism satisfies
$j_{\Et}^{-1}\nu_{T,*}G=\nu_{X,*}j_{\Proet}^{-1}G$: both evaluate a pro-etale
sheaf $G$ on the same etale objects over the open $X$. Taking left adjoints,
using the two extension-by-zero adjunctions, gives
$$
 \nu_T^*j_{\Et,!}\simeq j_{\Proet,!}\nu_X^*.
$$
All these functors are exact, so the identity holds on complexes. It
transports the etale comparison map to the displayed map. The identifications
are natural and commute with composition; thus
[lem-weil-pbc-proper-open-comparison-composition] transports its identity and
composition law as well.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-derived-categories, def:weil-pbc-site-comparison-morphism, def:weil-extension-by-zero, def:weil-pbc-proetale-operations, prop:weil-pbc-comparison-direct-image, def:weil-pbc-extension-by-zero, thm:weil-pbc-site-comparison
