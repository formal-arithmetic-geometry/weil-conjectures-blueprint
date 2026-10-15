+++
id = "lem-weil-pbc-geometric-point-open-or-closed"
kind = "lemma"
title = "A field-valued point lies on the open part or on the closed complement"
uses = ["def-weil-pbc-scheme-conventions", "def-weil-scheme-morphism-properties"]
lean = ["AlgebraicGeometry.existsUnique_fac_or_fac_of_range_eq_compl"]
+++
Let $X$ be a scheme [def-weil-pbc-scheme-conventions], let $j:U\hookrightarrow X$ be an open immersion `AlgebraicGeometry.IsOpenImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/OpenImmersion.lean)) and $i:Z\hookrightarrow X$ a closed immersion [def-weil-scheme-morphism-properties] with $i(Z)=X\setminus j(U)$ as sets. Let $K$ be a field and $s:\operatorname{Spec}K\to X$ a morphism of schemes (for instance a geometric point `AlgebraicGeometry.Scheme.SpecToEquivOfField, IsAlgClosed` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean))), and let $x\in X$ be the image of the unique point of $\operatorname{Spec}K$. Then exactly one of the following holds: (a) $x\in j(U)$, and there is a unique morphism $t:\operatorname{Spec}K\to U$ with $j\circ t=s$; (b) $x\in i(Z)$, and there is a unique morphism $t:\operatorname{Spec}K\to Z$ with $i\circ t=s$. In particular a geometric point $\bar x$ of $X$ whose image lies in $i(Z)$ is $i\circ\bar z$ for a unique geometric point $\bar z$ of $Z$ (with the same field), and one whose image lies in $j(U)$ is $j\circ\bar u$ for a unique geometric point $\bar u$ of $U$.
