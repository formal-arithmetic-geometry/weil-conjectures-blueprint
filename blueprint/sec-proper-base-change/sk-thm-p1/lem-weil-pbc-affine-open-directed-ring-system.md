+++
id = "lem-weil-pbc-affine-open-directed-ring-system"
kind = "lemma"
title = "Compatible spectrum presentations of one affine open along a directed limit"
uses = ["def-pc-scheme", "pqf-def-affine-morphism"]
lean = ["AlgebraicGeometry.exists_affineOpen_directedRingSystem"]
source = "literature/stacks-project/limits.tex, Tags 01YX (lemma-directed-inverse-system-has-limit) and 01YW (lemma-directed-inverse-system-affine-schemes-has-limit)"
+++
Let $I$ be a directed preordered set, $D:I^{\mathrm{op}}\to\mathrm{Scheme}$ a diagram of schemes [def-pc-scheme] with affine transition morphisms [pqf-def-affine-morphism], $c$ a limiting cone `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)), $i_0\in I$, and $W\subset D(i_0)$ an affine open. Write $J=\{i\in I\mid i_0\le i\}$ and $o=(i_0,i_0\le i_0)$. There are a functor $F:J\to\mathrm{CommRing}$ and an isomorphism $e_0:W\cong\operatorname{Spec}(F(o))$ such that for every $i\in J$ there is an isomorphism $e_i:W_i\cong\operatorname{Spec}(F(i))$, where $W_i$ is the inverse image of $W$ under $D(i\to i_0)$, and $e_0\circ(W_i\to W)=\operatorname{Spec}(F(o\to i))\circ e_i$. There is also an isomorphism $e_L:W_L\cong\operatorname{Spec}(\operatorname{colim}F)$, where $W_L$ is the inverse image of $W$ under $c_L\to D(i_0)$, such that $e_0\circ(W_L\to W)=\operatorname{Spec}(\iota_o)\circ e_L$, with $\iota_o$ the colimit coprojection. All maps from inverse-image opens to $W$ are restrictions of the specified structure maps.
