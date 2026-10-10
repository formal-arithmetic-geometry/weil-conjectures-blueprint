+++
id = "lem-weil-derived-direct-image-composition"
kind = "lemma"
title = "Composition of derived direct images"
order = 1470
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-derived-complete", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-derived-limit", "def-weil-derived-pullback-tensor-hom", "def-weil-pbc-kinjective-resolutions", "def-weil-rationalization-karoubi", "lem-sp-kinjective-computes", "lem-weil-pbc-direct-image-preserves-injectives", "lem-weil-restriction-of-scalars-exact", "lem-weil-scalar-extension-composition"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be morphisms of schemes on which
$\ell$ is invertible, and use the derived direct images of
[def-weil-derived-direct-image]. There is a canonical isomorphism

$$
 c_{g,f}:R(g\circ f)_*\xrightarrow{\ \sim\ }Rg_*\circ Rf_*
$$

at each coefficient stage of that definition:

1. at finite level $A_{E,n}$, as functors
$D(X_{\mathrm{proet}},A_{E,n})\to D(Z_{\mathrm{proet}},A_{E,n})$;
1. for $\Lambda=\mathcal O_E$, on those $K\in D^b_c(X,\mathcal O_E)$ with
$Rf_*K\in D^b_c(Y,\mathcal O_E)$ (so that the right side is defined);
1. for $\Lambda=E$, on the rationalized category of
[def-weil-rationalization-karoubi], for the same $K$;
1. for $\Lambda=\Qlb$, on the common-stage category of
[def-weil-algebraically-closed-coefficients], for objects $(E,K)$ with $K$
as in (3);
1. on the small étale site, for any ring $A$, as functors
$D(X_{\mathrm{et}},A)\to D(Z_{\mathrm{et}},A)$ between the ordinary
derived categories of étale sheaves of $A$-modules.

The isomorphism $c_{g,f}$ is natural in $K$, is the identity when $f$ or $g$
is an identity, and is associative: for a further morphism $h:Z\to W$ the
two isomorphisms $R(hgf)_*\cong Rh_*Rg_*Rf_*$ built from $c$ agree. In
particular it is compatible with transport of structure along automorphisms
of $X,Y,Z$ commuting with $f$ and $g$ (such as Frobenius), since the direct
image along an automorphism $\sigma$ is the inverse image along
$\sigma^{-1}$.
