+++
id = "lem-weil-pbc-geometric-point-open-or-closed"
kind = "lemma"
title = "A field-valued point lies on the open part or on the closed complement"
uses = ["def-weil-pbc-scheme-conventions", "def-weil-scheme-morphism-properties"]
lean = ["AlgebraicGeometry.existsUnique_fac_or_fac_of_range_eq_compl", "AlgebraicGeometry.IsClosedImmersion.existsUnique_fac_of_field", "AlgebraicGeometry.IsOpenImmersion.lift_fac", "AlgebraicGeometry.disjoint_range_of_range_eq_compl"]
order = 1804
+++
Let $X$ be a scheme [def-weil-pbc-scheme-conventions], let $j:U\hookrightarrow X$ be an open immersion and $i:Z\hookrightarrow X$ a closed immersion [def-weil-scheme-morphism-properties] with $i(Z)=X\setminus j(U)$ as sets. Let $K$ be a field and $s:\operatorname{Spec}K\to X$ a morphism of schemes (for instance a geometric point), and let $x\in X$ be the image of the unique point of $\operatorname{Spec}K$. Then exactly one of the following holds: (a) $x\in j(U)$, and there is a unique morphism $t:\operatorname{Spec}K\to U$ with $j\circ t=s$; (b) $x\in i(Z)$, and there is a unique morphism $t:\operatorname{Spec}K\to Z$ with $i\circ t=s$. In particular a geometric point $\bar x$ of $X$ whose image lies in $i(Z)$ is $i\circ\bar z$ for a unique geometric point $\bar z$ of $Z$ (with the same field), and one whose image lies in $j(U)$ is $j\circ\bar u$ for a unique geometric point $\bar u$ of $U$.
