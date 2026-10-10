+++
id = "lemma-weil-pbc-curve-normalization-constant"
kind = "lemma"
title = "Normalization and smooth constant case"
order = 1181
uses = ["lemma-weil-pbc-curve-dense-open-reduction", "lemma-weil-pbc-normalization-exact-sequence", "lemma-weil-pbc-smooth-curve-artin-schreier", "lemma-weil-pbc-smooth-curve-kummer-localization"]
+++
Let $X$ be a reduced separated curve of finite type over an algebraically
closed field $k$, let $j:U\hookrightarrow X$ be an open immersion, and let
$\ell$ be a prime (possibly $\ell=\operatorname{char}k$). Then all applicable
assertions among the eight curve assertions $\mathcal C_1,\dots,\mathcal C_8$
(vanishing, finiteness, invariance under algebraically closed extension of
$k$, and surjectivity of $H^2$ onto opens)
hold for the sheaf $j_!\underline{\mathbf F_\ell}$ on $X$.

## Proof

Let $\nu:X^\nu\to X$ be the finite normalization and $j^\nu:U^\nu\hookrightarrow X^\nu$
the pullback of $j$. The normalization $X^\nu$ is a finite disjoint union of smooth curves and
points. On a component disjoint from $U^\nu$ the extension-by-zero sheaf is
zero and every assertion is immediate; on every other component $U^\nu$ is
dense. The dense-open localization lemma on $X^\nu$ therefore reduces
$j^\nu_!\underline{\mathbf F_\ell}$ to the constant sheaf on each remaining
smooth component, with the five-term sequence and all comparison maps
already specified there. If $\ell\ne\operatorname{char}k$, apply the Kummer and
localization calculation; if $\ell=\operatorname{char}k$, apply the
Artin–Schreier calculation. Thus all applicable eight assertions hold for
$j^\nu_!\underline{\mathbf F_\ell}$.

Exact finite direct image transfers them to
$\nu_*j^\nu_!\underline{\mathbf F_\ell}$. The normalization exact sequence
then transfers them to $j_!\underline{\mathbf F_\ell}$, including the
low-degree comparison maps and assertion (8). Properness is preserved by
finite normalization; affineness is preserved because a finite morphism
over an affine is affine. This completes the normalization, proper/affine
localization, prime-to-characteristic, and characteristic-$\ell$ branches.
