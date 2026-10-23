+++
id = "lemma-nagata-extend-admissible-blowup"
kind = "lemma"
title = "Property of the extended admissible blow-up, [stacks-project]"
order = 286
lean = ["AlgebraicGeometry.IsAdmissible.exists_extend", "AlgebraicGeometry.IsAdmissible.exists_extend_of_disjoint", "AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq_of_disjoint"]
uses = ["def-nagata-admissible-blowup", "def-nagata-extended-admissible-blowup", "def-nagata-extended-ideal", "def-nagata-global-blowup", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-flat-base-change"]
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
