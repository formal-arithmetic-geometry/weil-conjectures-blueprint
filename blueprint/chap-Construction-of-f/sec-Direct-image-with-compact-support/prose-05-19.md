+++
id = "prose-05-19"
kind = "hidden"
title = "Direct image with compact support"
order = 480
+++
The trace formula needs a relative version of cohomology with compact
supports, whose stalks are the groups $H^i_c$ of the fibres. Consider
first a locally compact Hausdorff space
$X$ with an open embedding $j:X\hookrightarrow\overline X$ into a compact
space. A section of $j_!F$ is a section of $F$ that vanishes near
$\overline X\setminus X$, and $H^i_c(X,F)=H^i(\overline X,j_!F)$. For
example, for $X=\mathbf R$ and $\overline X$ the circle, we find
$H^1_c(\mathbf R,\mathbf Z)=\mathbf Z$.

The definition by sections with compact support has no direct analogue
for schemes, because every scheme of finite type over $k$ is quasi-compact, and the
algebraic substitute for compactness is properness, which is a property
of a morphism and not of a subset. The two-step form, however, does carry over.
In it, the functor $j_!$ imposes compact support along the open immersion, while for
a proper map $p$, as for a map of spaces with compact fibres, the direct
image with compact supports is the ordinary direct image $Rp_*$. By
proper base change, the result does not depend on the compactification
(Proposition [proposition-construction-independence-rf-shriek]).
Proper base change also identifies
the stalks of $Rf_!$ with the compactly supported cohomology of the
fibres (Corollary [corollary-trace-functions-direct-image-compact]).

Let $f:X\to Y$ be a separated morphism of finite type. For a
compactification $f=p\circ j$, with $j$ an open immersion and $p$ proper,
we define $Rf_!=Rp_*\circ j_!$. We must show that this functor
preserves direct sums. In the following subsubsection we take
$\Lambda=E$ or $\overline{\mathbf Q}_\ell$, so that
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))=\Loc(\Dbc(X,\Lambda))$.
