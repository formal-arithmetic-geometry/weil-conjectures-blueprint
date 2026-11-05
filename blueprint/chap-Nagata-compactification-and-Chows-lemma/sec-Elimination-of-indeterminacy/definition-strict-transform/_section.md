+++
id = "definition-strict-transform"
kind = "definition"
title = "Strict transform"
order = 1428
lean = ["AlgebraicGeometry.strictTransform", "AlgebraicGeometry.Scheme.IdealSheafData.strictTransform", "AlgebraicGeometry.Scheme.IdealSheafData.strictTransformι"]
uses = ["lemma-schematic-closure-uniqueness"]
+++
Let $b:T'\to T$ be the blow-up of $T$ in a quasi-coherent ideal of
finite type, with exceptional divisor $E\subseteq T'$, and let $W\to T$
be a morphism. The *strict transform* of $W$ is the closed
subscheme of $W\times_TT'$ whose ideal consists of the local sections of
$\mathcal O_{W\times_TT'}$ supported on the inverse image of $E$.
