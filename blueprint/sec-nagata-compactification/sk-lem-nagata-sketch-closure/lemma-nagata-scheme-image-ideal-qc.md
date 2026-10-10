+++
id = "lemma-nagata-scheme-image-ideal-qc"
kind = "lemma"
title = "Mathlib scheme-theoretic image interface"
order = 64
lean = ["AlgebraicGeometry.Scheme.Hom.image"]
+++
For a morphism $g\colon T\to Y$, the scheme-theoretic image is the closed
subscheme $\operatorname{SIm}(g)$ cut out by the quasi-coherent ideal sheaf
$\operatorname{ker}(g)$; it comes with the closed immersion
$g_{\mathrm{im}}\colon\operatorname{SIm}(g)\hookrightarrow Y$ and a factor
map $g^{\mathrm{im}}\colon T\to\operatorname{SIm}(g)$ with
$g_{\mathrm{im}}\circ g^{\mathrm{im}}=g$.
When $g$ is quasi-compact, the maps on sections and stalks
$\mathcal O_{\operatorname{SIm}(g)}\to g^{\mathrm{im}}_*\mathcal O_T$ are
injective and the support of $\operatorname{ker}(g)$ is the closure of the
topological range of $g$.

## Proof

Write $K=\ker(\mathcal O_Y\to g_*\mathcal O_T)$. By definition $\ker(g)$ is a
quasi-coherent ideal contained in $K$, so every local section of $\ker(g)$
pulls back to $0$ on $T$. Hence $g^\sharp\colon\mathcal O_Y\to g_*\mathcal O_T$
factors through $\mathcal O_Y/\ker(g)$, which is the pushforward of the
structure sheaf of the closed subscheme $\operatorname{SIm}(g)$; this is the
factor map $g^{\mathrm{im}}$, and $g_{\mathrm{im}}\circ g^{\mathrm{im}}=g$
holds by construction.

Now let $g$ be quasi-compact. Then $K$ is itself quasi-coherent: on an
affine open $V=\operatorname{Spec}(A)$ of $Y$, cover $g^{-1}(V)$ by finitely
many affine opens $\operatorname{Spec}(C_k)$; by the sheaf property,
$g_*\mathcal O_T|_V\to\bigoplus_k(g_k)_*\mathcal O_{\operatorname{Spec}C_k}$
is injective, so $K|_V$ is the kernel of a map between quasi-coherent
$\mathcal O_V$-modules, namely the ideal associated with
$\ker(A\to\prod_kC_k)$. Therefore $\ker(g)=K$. The map
$\mathcal O_{\operatorname{SIm}(g)}=\mathcal O_Y/K\to g_*\mathcal O_T$ is then
injective on sections over every open of $Y$, i.e. the map
$\mathcal O_{\operatorname{SIm}(g)}\to g^{\mathrm{im}}_*\mathcal O_T$ is
injective on sections; passing to filtered colimits, it is injective on
stalks.

Finally, $V(K)$ is closed and contains $g(T)$, because at a point $g(t)$
every section of $K$ maps to $0$ in the local ring
$\mathcal O_{T,t}$ and hence lies in the maximal ideal of
$\mathcal O_{Y,g(t)}$. Conversely, if $y\notin\overline{g(T)}$, choose an open
neighbourhood $W$ of $y$ with $g^{-1}(W)=\varnothing$; then
$(g_*\mathcal O_T)|_W=0$, so $K|_W=\mathcal O_W$ and $y\notin V(K)$. Hence the
support of $\ker(g)$ is $\overline{g(T)}$.
