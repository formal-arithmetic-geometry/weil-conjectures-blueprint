+++
id = "definition-strict-transform--1"
kind = "definition"
title = "Strict transform (1)"
name_showing = false
order = 1428001
aliases = ["bp-r444-1"]
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.strictTransform", "AlgebraicGeometry.Scheme.IdealSheafData.strictTransformι", "AlgebraicGeometry.ker_strictTransformι"]
uses = ["definition-admissible-blow-up", "lemma-schematic-closure-uniqueness"]
+++
Let $b:T'\to T$ be the blow-up of $T$ in a quasi-coherent ideal of
finite type, with exceptional divisor $E\subseteq T'$, and let $W\to T$
be a morphism. The *strict transform* of $W$ is the closed
subscheme of $W\times_TT'$ whose ideal consists of the local sections of
$\mathcal O_{W\times_TT'}$ supported on the inverse image of $E$.
