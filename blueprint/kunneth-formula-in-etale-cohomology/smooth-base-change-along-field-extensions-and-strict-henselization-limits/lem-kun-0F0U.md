+++
id = "lem-kun-0F0U"
kind = "lemma"
title = "Strict henselization as a limit"
order = 6128
lean = ["AlgebraicGeometry.Etale.strictHenselization_isLimit_finiteType"]
uses = ["def-weil-pbc-strict-henselization-limit", "def-kun-dimension", "def-kun-separably-closed"]
+++
Let $K$ be a field, $X$ a scheme of finite type over $K$, and $x\in X$ a
point with $\operatorname{trdeg}_K\kappa(x)=a>0$; put $d=\dim_xX$ and
$X'=\Spec\bigl(\mathcal O^{\mathrm{sh}}_{X,x}\bigr)$, the strict
henselization. Then there is a separably closed field $L\supseteq K$
([def-kun-separably-closed]) and a presentation
$$
 X'=\varprojlim_iX_i
$$
of $X'$ as an inverse limit of affine schemes $X_i$ of finite type over $L$
with affine transition morphisms and $\dim X_i<\dim X$ for every $i$.

(*Source:* the case of Stacks Project,
[Tag `0F0U`](https://stacks.math.columbia.edu/tag/0F0U) that is used in this
chapter, namely the presentation of the strict henselization as a limit of
smaller-dimensional finite type models. In the Stacks Project the proof uses
Noether normalization, Algebra, Lemma 10.115.5,
[Tag `00OZ`](https://stacks.math.columbia.edu/tag/00OZ), a linear change of
coordinates putting the image of $x$ at the generic point of the linear
subspace, the description of the strict henselization as the filtered colimit
of the pointed etale neighbourhoods, and the dimension bound for an algebra
which is quasi-finite over a polynomial ring.)

## Proof

This is the recorded classical input named in the statement, the case
used here of Stacks Project, [Tag 0F0U](https://stacks.math.columbia.edu/tag/0F0U):
the strict henselization of a point of positive transcendence degree over the
base field is an inverse limit of affine finite type models of strictly
smaller dimension. In the Stacks Project the proof uses Noether normalization,
Algebra, Lemma 10.115.5
([Tag 00OZ](https://stacks.math.columbia.edu/tag/00OZ)), together with the
description of the strict henselization as a filtered colimit of pointed etale
neighbourhoods. No separate proof is given.

Unresolved dependencies: def:weil-pbc-scheme-conventions, thm:zl-relative-noether
