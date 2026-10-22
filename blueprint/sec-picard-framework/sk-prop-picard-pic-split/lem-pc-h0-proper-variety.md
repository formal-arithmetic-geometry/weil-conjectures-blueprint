+++
id = "lem-pc-h0-proper-variety"
kind = "lemma"
title = "Global sections of a proper scheme"
lean = ["AlgebraicGeometry.Scheme.isField_globalSections_of_universallyClosed", "AlgebraicGeometry.Scheme.finite_globalSectionsRingHom_of_isProper", "AlgebraicGeometry.Scheme.GlobalSectionsBijective.of_geometricallyIntegral"]
order = 735
uses = ["def-pc-geometrically-irreducible", "def-pc-morphism-conventions", "def-pc-scheme", "lem-pc-coherent-hi", "lem-pc-finite-extension-alg-closed", "lem-pc-flat-base-change-cohom"]
+++
Let $k$ be a field and $X$ a proper scheme over $k$.

1. If $X$ is a variety over $k$ (e.g. connected and integral), then
$H^0(X,\mathcal{O}_X)$ is a finite field extension of $k$.
1. If $X$ is geometrically integral over $k$, then
$H^0(X,\mathcal{O}_X)=k$.
