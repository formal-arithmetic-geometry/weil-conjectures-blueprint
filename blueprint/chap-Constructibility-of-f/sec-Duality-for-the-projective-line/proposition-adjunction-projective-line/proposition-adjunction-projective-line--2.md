+++
id = "proposition-adjunction-projective-line--2"
kind = "proposition"
title = "Base change for the unit"
order = 553003
aliases = ["bp-r167-2"]
lean = []
uses = ["proposition-adjunction-projective-line--1", "proposition-adjunction-projective-line--3"]
+++
The separate assertion of base change for the unit is bypassed by the
Lean route: it uses the counit compatibility of
[proposition-adjunction-projective-line--3] to identify the mate defining
exceptional base change with the pullback, twist and shift isomorphism.

The retained assertion is that, for every $g:S'\to S$ with $S$ and $S'$ of
finite type over $k$, the unit of the projective-line adjunction is
compatible with base change along $g$. No separate declaration of this
unit equation is used by that argument.
