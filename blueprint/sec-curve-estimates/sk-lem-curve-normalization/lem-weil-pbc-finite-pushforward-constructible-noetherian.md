+++
id = "lem-weil-pbc-finite-pushforward-constructible-noetherian"
kind = "lemma"
title = "Finite pushforward preserves constructibility on Noetherian schemes"
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.lowerStar_of_isFinite"]
order = 1488
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-pushforward-generic-constructible", "lem-weil-pbc-noetherian-finite-components", "lemma-weil-pbc-finite-exchange"]
+++
Let $\Lambda$ be a finite commutative ring, let $U$ be a Noetherian scheme, let
$h:V\to U$ be a finite morphism, and let $E$ be a constructible etale sheaf of
$\Lambda$-modules on $V$. Then its direct image $h_*E$ is a constructible etale
sheaf of $\Lambda$-modules on $U$.
