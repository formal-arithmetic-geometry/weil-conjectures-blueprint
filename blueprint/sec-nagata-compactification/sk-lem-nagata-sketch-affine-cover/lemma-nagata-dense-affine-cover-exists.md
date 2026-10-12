+++
id = "lemma-nagata-dense-affine-cover-exists"
kind = "lemma"
title = "Existence of a finite affine cover with dense total intersection"
order = 325
lean = ["AlgebraicGeometry.exists_isAffineOpen_cover_genericPoints_subset", "AlgebraicGeometry.exists_isAffineOpen_iSup_eq_top_and_genericPoints_subset_iInter", "dense_iInf_of_genericPoints_subset"]
uses = ["def-weil-pbc-scheme-conventions", "lemma-nagata-affine-neighbourhood-generic-points"]
+++
Let $X$ be a quasi-compact scheme with finitely many irreducible
components $Z_1,\dots,Z_r$, with generic points $\eta_j$. Then there is a
finite affine open covering $X=U_1\cup\dots\cup U_m$ such that
$\eta_j\in U_i$ for all $i$ and $j$; in particular the total intersection

$$
U:=U_1\cap\dots\cap U_m
$$

is dense in $X$. More generally, in any scheme the intersection of finitely
many open subsets each of which contains the generic points of all
irreducible components is dense.
