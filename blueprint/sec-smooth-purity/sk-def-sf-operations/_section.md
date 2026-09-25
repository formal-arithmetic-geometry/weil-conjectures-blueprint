+++
id = "sk-def-sf-operations"
kind = "section"
title = "The six operations: ambient typing"
order = 1453
+++
*Definition (sketch).*

For a separated finite-type $f:X\to Y$ the six operations are the following
functors of ambient categories, with the framework and proper-base-change
chapters supplying the definitions:

3pt
1. **(i)** the derived pullback, the derived tensor product and the derived
internal Hom
$$
\begin{aligned}
Lf^*&:D(Y,\Lambda)\longrightarrow D(X,\Lambda),\\
-\otimes^L_\Lambda-&:D(Y,\Lambda)\times D(Y,\Lambda)\longrightarrow D(Y,\Lambda),\\
\RHom_\Lambda(-,-)&:D(Y,\Lambda)^{\mathrm{op}}\times D(Y,\Lambda)\longrightarrow D(Y,\Lambda),
\end{aligned}
$$
as in def:weil-derived-pullback-tensor-hom;
1. **(ii)** the derived direct image
$Rf_*:D^+(X,\Lambda)\to D^+(Y,\Lambda)$, as in
def:weil-derived-direct-image;
1. **(iii)** extension by zero $j_!:D^+(U,\Lambda)\to D^+(X,\Lambda)$ for an
open immersion $j:U\hookrightarrow X$, as in def:weil-extension-by-zero;
1. **(iv)** the compact-support direct image $Rf_!=R\bar f_*j_!$ attached to a
compactification $X\xrightarrow{j}\overline X\xrightarrow{p}Y$, as a functor of
ambient categories, the compactification-independence being asserted only on
the étale-origin complexes of def:compact-support-direct-image;
1. **(v)** *the ambient exceptional right adjoint* $Rf^{\times}$. This is
not defined, it is *assumed*: it is the functor of ambient categories
$$
Rf^{\times}:D(Y,\Lambda)\longrightarrow D(X,\Lambda)
$$
which is right adjoint to $Rf_!$ of (iv), and its *existence*, together
with the compatibility of units and counits with refinements, is exactly the
ambient datum of [sk-def-sf-admissible];
1. **(vi)** *the exceptional inverse image* $Rf^!$, the functor
$$
Rf^!:=Rf^{\times}\big|_{\Dctf(Y,\Lambda)}:\ \Dctf(Y,\Lambda)\longrightarrow
\Dctf(X,\Lambda),
$$
*defined* by restricting the ambient right adjoint of (v) to the small
subcategories. A restriction of a functor to full subcategories is a functor
only when the source subcategory is carried into the target one; so the
existence of this restriction is *not* part of the definition, it is the
preservation clause, stated as [sk-prop-sf-rf-shriek-preservation] and
[sk-thm-sf-ctf-stability] (v) and proved there for open immersions, finite
étale morphisms, closed immersions, smooth morphisms and every $f$ carrying
the ambient datum. Equivalently, $Rf^!$ is characterised by
$\operatorname{Hom}_Y(Rf_!K,L)\cong\operatorname{Hom}_X(K,Rf^!L)$ for
$K\in\Dctf(X,\Lambda)$ and $L\in\Dctf(Y,\Lambda)$. Thus in this blueprint
$Rf^{\times}$ always denotes the ambient functor and $Rf^!$ always denotes its
restriction to the small categories.

The exchange and projection transformations of [sk-def-sf-exchanges] are
natural transformations between composites of these functors, and are
therefore typed by the above. Whether an operation descends to a small
category is *not* part of this definition; it is [sk-rem-sf-typing].
