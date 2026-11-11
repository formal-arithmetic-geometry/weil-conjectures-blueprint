+++
id = "definition-real-sheaves--1"
kind = "definition"
title = "Real sheaves (1)"
name_showing = false
order = 1156001
aliases = ["bp-r354-1"]
lean = ["AlgebraicGeometry.WeilGroup.IsReal", "AlgebraicGeometry.WeilGroup.IsReal.map_conj_localEigenvalues", "AlgebraicGeometry.WeilGroup.isReal_of_map_conj_localEigenvalues", "AlgebraicGeometry.WeilSheaf.IsReal"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-perfect-complexes-geometric-point--6"]
+++
A Weil sheaf $\mathcal G$ is $\iota$-real if
$\iota\det(1-T\operatorname{Frob}_x\mid\mathcal G_{\bar x})$ has real coefficients for
every closed point; equivalently, the multiset of its complex
eigenvalues at each point is stable under complex conjugation.
