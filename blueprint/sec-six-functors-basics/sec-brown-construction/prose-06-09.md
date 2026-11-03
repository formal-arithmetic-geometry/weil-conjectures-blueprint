+++
id = "prose-06-09"
kind = "hidden"
title = "The compactly supported direct image and Brown representability"
order = 284
+++
The functor we need is the relative version of cohomology with compact
supports, since its stalks should be the groups $H^i_c$ of the fibres
that appear in the trace formula. On a locally compact Hausdorff space
$X$ with an open embedding $j:X\hookrightarrow\overline X$ into a compact
space, a section of $j_!F$ is a section of $F$ that vanishes near
$\overline X\setminus X$, and $H^i_c(X,F)=H^i(\overline X,j_!F)$; for the
one-point compactification this is cohomology of
$\overline X$ relative to the point at infinity. For example, for
$X=\mathbf R$ and $\overline X$ the circle, $H^1_c(\mathbf R,\mathbf Z)=\mathbf Z$.
The definition by sections with compact support has no direct analogue
for schemes: every scheme of finite type over $k$ is quasi-compact, and the
algebraic substitute for compactness is properness, which is a property
of a morphism and not of a subset. The two-step form does carry over:
$j_!$ imposes compact support along the open immersion, and for a proper
map $p$, as for a map of spaces with compact fibres, the direct image with
compact supports is the ordinary direct image $Rp_*$. That the result does not
depend on the compactification is a consequence of proper base change
(Proposition [sk-prop-sf-comp-coherence]), which also identifies
the stalks of $Rf_!$ with the compactly supported cohomology of the
fibres (Corollary [sk-cor-tf-trace-function-pushforward]).

Let $f:X\to Y$ be a separated morphism of finite type. For a
compactification $f=p\circ j$, with $j$ an open immersion and $p$ proper,
we define $Rf_!=Rp_*\circ j_!$. It remains to show that this functor
preserves direct sums. In the following subsubsection we take
$\Lambda=E$ or $\overline{\mathbf Q}_\ell$, so that
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))=\Loc(\Dbc(X,\Lambda))$.
