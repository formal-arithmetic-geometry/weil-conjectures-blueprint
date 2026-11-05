+++
id = "lemma-tangent-cones-on-cover--2"
kind = "lemma"
title = "Separation of the tangent cones in the strict local ring"
order = 985003
aliases = ["bp-r300-2"]
lean = ["AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.tangentConesMeetAtOrigin"]
+++
In the setting of [lemma-tangent-cones-on-cover--1], the tangent cone of
$D'=(\Gamma'\cup V')_{\mathrm{red}}$ at $y'$ meets the tangent cones of
$\Delta'_{\mathrm{red}}$ and of $H'_{\mathrm{red}}$ only in $0$.

More precisely, let $R'$ be the strictly local ring of $T'$, with
maximal ideal $\mathfrak m$, and let
$I_D,I_\Delta,I_H$ be the ideals of these three reduced curves. For each
$J\in\{I_\Delta,I_H\}$ there is an integer $n$ such that, for all $N\geq n$,

$$
\mathfrak m^N\subseteq
(I_D\cap\mathfrak m^N)+(J\cap\mathfrak m^N)+\mathfrak m^{N+1}.
$$

Equivalently, the initial ideals of $I_D$ and $J$ together contain every
homogeneous element of sufficiently large degree in the associated graded
ring of $R'$.
