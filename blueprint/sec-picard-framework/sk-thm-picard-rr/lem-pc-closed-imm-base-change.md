+++
id = "lem-pc-closed-imm-base-change"
kind = "lemma"
title = "The ideal sheaf of a base-changed closed immersion"
order = 733
lean = ["AlgebraicGeometry.closedSubscheme_baseChange_ideal_image", "AlgebraicGeometry.flat_module_pullback_exact_pushforward_injective", "AlgebraicGeometry.Flat.of_field"]
uses = ["def-pc-scheme", "lem-pc-flat-field"]
+++
Closed immersions are stable under arbitrary base change: if $i:Z\to X$ is a
closed immersion with ideal sheaf $\mathcal{I}_Z$ and $g:X'\to X$ is a
morphism, then $Z'=Z\times_XX'$ is a closed subscheme of $X'$, and its ideal
sheaf is the image of the canonical map $g^*\mathcal{I}_Z\to\mathcal{O}_{X'}$
(Schemes, Lemma 26.17.6, Tag [01JU](https://stacks.math.columbia.edu/tag/01JU)).
If $g$ is flat, this map is injective, so that
$\mathcal{I}_{Z'}=g^*\mathcal{I}_Z$; in particular, for a scheme $X$ over a
field $k$, a closed subscheme $x\subset X$ (for instance a $k$-rational point)
and a field extension $K/k$, the base change $X_K\to X$ is flat and
$\mathcal{I}_{x_K}=\mathcal{I}_x\otimes_{\mathcal{O}_X}\mathcal{O}_{X_K}$.
Without flatness the equality fails: for $X=\operatorname{Spec}k[t]$,
$Z=V(t)$ and $g:X'=Z\to X$ the closed immersion itself, $g^*\mathcal{I}_Z\cong k$,
while $Z'=Z$ has ideal sheaf $0$ in $\mathcal{O}_{X'}=k$.
