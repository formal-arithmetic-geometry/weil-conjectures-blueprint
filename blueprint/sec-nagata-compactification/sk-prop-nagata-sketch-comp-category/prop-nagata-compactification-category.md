+++
id = "prop-nagata-compactification-category"
kind = "theorem"
title = "The compactification category is nonempty, cofiltered, and base-changes"
order = 414
tags = ["latex:proposition"]
uses = ["def-nagata-compactification", "def-nagata-compactification-base-change", "def-nagata-dense-compactification", "def-nagata-immersion-compactification", "def-nagata-scheme-theoretic-image", "lemma-nagata-compactification-base-change", "lemma-nagata-dense-flat-pullback", "lemma-nagata-immersion-into-proper", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-universal", "thm-nagata-compactification"]
+++
Let $S$ be a quasi-compact, quasi-separated scheme and let $f\colon X\to S$
be separated and of finite type. Let $\operatorname{Comp}(f)$ be the
category whose objects are the compactifications
$c=(X\xrightarrow{j}\overline X\xrightarrow{\bar f}S)$ of $f$ in the sense of
[def-nagata-compactification] ($j$ a quasi-compact open immersion, $\bar f$
proper, $\bar f\circ j=f$; scheme-theoretic density of $j$ is *not*
required), and whose morphisms $u\colon c_1\to c_2$, the *refinements*, are
the proper $S$-morphisms $u\colon\overline X_1\to\overline X_2$ with
$u\circ j_1=j_2$. Then:

1. $\operatorname{Comp}(f)$ is nonempty.
1. **(i)** Any two objects $c_1,c_2$ admit a common refinement
$c\to c_1$, $c\to c_2$; hence every finite family of objects admits one.
One such $c$ is the scheme-theoretic image $\overline X$ of
$(j_1,j_2)\colon X\to\overline X_1\times_S\overline X_2$, and for it
$j$ is scheme-theoretically dense.
1. **(ii)** Any two parallel refinements $u,v\colon c_1\to c_2$ are
equalized by a further refinement $c'\to c_1$.

In particular $\operatorname{Comp}(f)$ is cofiltered. Moreover it is
compatible with base change: let $g\colon S'\to S$ be any morphism and
$f'\colon X'=X\times_SS'\to S'$ the base change of $f$.

1. For every object $c$ of $\operatorname{Comp}(f)$, its base change
$c_{S'}=(X'\xrightarrow{j'}\overline X\times_SS'\to S')$ is an object of
$\operatorname{Comp}(f')$, and for every refinement $u\colon c_1\to c_2$ the
base change $u'=u\times_SS'$ is a refinement $c_{1,S'}\to c_{2,S'}$,
functorially in $u$. Consequently base change carries a common refinement
$c\to c_1,\ c\to c_2$ to a common refinement
$c_{S'}\to c_{1,S'},\ c_{S'}\to c_{2,S'}$, and equalizing refinements to
equalizing refinements.
1. If $c$ is the common refinement constructed in (i) from $c_1,c_2$ and
$c'$ the one constructed from $c_{1,S'},c_{2,S'}$, then the ambient scheme
of $c'$ is a closed subscheme of that of $c_{S'}$, and the inclusion is a
refinement $c'\to c_{S'}$ over the two projections. If $g$ is flat, this
inclusion is an isomorphism, i.e. the construction of (i) commutes with
flat base change.

Scheme-theoretic density is not preserved by arbitrary base change, which
is why it is not part of the objects: $c_{S'}$ need not be
scheme-theoretically dense ([def-nagata-dense-compactification]) even if
$c$ is, but it always is when $g$ is flat.
