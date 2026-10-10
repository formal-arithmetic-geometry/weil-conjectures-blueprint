+++
id = "lemma-nagata-extend-admissible-blowup"
kind = "lemma"
title = "Property of the extended admissible blow-up, [stacks-project]"
order = 174
lean = ["AlgebraicGeometry.IsAdmissible.exists_extend", "AlgebraicGeometry.IsAdmissible.exists_extend_of_disjoint", "AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq_of_disjoint"]
uses = ["def-nagata-admissible-blowup", "def-nagata-constructible-closed-support", "def-nagata-effective-cartier-ideal", "def-nagata-extended-admissible-blowup", "def-nagata-extended-ideal", "def-nagata-finite-type-ideal-extension", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "def-nagata-qc-open-complement-ideal", "lemma-nagata-constructible-closed-support", "lemma-nagata-dense-flat-pullback", "lemma-nagata-extend-finite-type-ideal", "lemma-nagata-finite-type-ideal-extension-exists", "lemma-nagata-qc-open-complement-ideal", "lemma-nagata-qc-open-complement-ideal-exists", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-flat-base-change", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property"]
+++
Let $X$ be quasi-compact and quasi-separated, let $A,B\subseteq X$ be
quasi-compact opens, and let $\mathcal J$ be a finite type quasi-coherent
ideal on $A$ with $V(\mathcal J)\cap B=\varnothing$. Then:

1. there is a finite type quasi-coherent ideal $\mathcal K$ on $X$ with
   $\mathcal K|_A=\mathcal J$ and $V(\mathcal K)\cap B=\varnothing$;
2. there are a $B$-admissible blow-up
   $\operatorname{Bl}_{\mathcal K'}(X)\to X$ and a morphism
   $h\colon\operatorname{Bl}_{\mathcal J}(A)\to\operatorname{Bl}_{\mathcal K'}(X)$
   over the inclusion $A\hookrightarrow X$ such that $h$ and the blow-up map
   $\operatorname{Bl}_{\mathcal J}(A)\to A$ identify
   $\operatorname{Bl}_{\mathcal J}(A)$ with the fibre product
   $A\times_X\operatorname{Bl}_{\mathcal K'}(X)$.

If $B\subseteq A$, assertion 2 holds for an arbitrary open $B\subseteq A$,
not necessarily quasi-compact.

## Proof

By [lemma-nagata-extend-finite-type-ideal], the ideal
$\mathcal I_X(\mathcal J)$ is finite type, restricts to $\mathcal J$ on
$W$, and restricts to the unit ideal on $U$. Its blow-up is therefore
$U$-admissible. The open immersion $W\to X$ is flat, so
[thm-nagata-blowup-flat-base-change] identifies the pullback of the
constructed blow-up with $\operatorname{Bl}_{\mathcal J}(W)$. On an
affine chart, that comparison is induced degreewise by the canonical map
from the pullback of the Rees algebra to the Rees algebra of the restricted
ideal; it sends every standard chart generator to itself. Hence the local
comparisons commute with restriction to basic overlaps and glue to the
stated canonical isomorphism. Over $U\cap W$ both ideals are the unit
ideal, so the same formula is the selected identity of the two trivial
blow-ups. This also verifies compatibility with the chosen admissibility
isomorphism.
