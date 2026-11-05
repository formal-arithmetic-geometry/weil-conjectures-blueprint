+++
id = "lemma-normality-geometric-monodromy--1"
kind = "lemma"
title = "Reduced monodromy groups and their inclusion"
name_showing = false
order = 1130001
aliases = ["bp-r347-1"]
lean = ["Matrix.GeneralLinearGroup.isRadical_vanishingIdeal", "Matrix.GeneralLinearGroup.instIsHopfIdealVanishingIdeal", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromy_le_geometricMonodromy"]
uses = ["definition-monodromy-groups"]
+++
Lean bypasses a separate normality lemma, using subgroup inclusion and
commutator containment.

Let $k$ be a field, $n$ a finite set, and $W$ a group with a surjective
homomorphism $\deg:W\to\mathbf Z$ and a chosen element of degree one.
Let $\rho:W\to\GL(k^n)$ be a representation and put $P=\ker(\deg)$.
As in [definition-monodromy-groups], let $H$ and $G$ be the Zariski
closures of $\rho(P)$ and $\rho(W)$. Their defining ideals
$$
I_H=I(\rho(P)),\qquad I_G=I(\rho(W))
$$
in $k[\GL(k^n)]$ are radical Hopf ideals, and $I_G\subseteq I_H$.
Thus $H$ and $G$ are reduced closed algebraic subgroups of $\GL(k^n)$,
with $H\subseteq G$.
