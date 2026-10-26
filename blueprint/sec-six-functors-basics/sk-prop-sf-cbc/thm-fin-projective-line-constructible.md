+++
id = "thm-fin-projective-line-constructible"
kind = "theorem"
title = "Constructible coefficients on the projective line"
lean = ["AlgebraicGeometry.Etale.hasConstructibleDirectImages_projectiveLine"]
order = 2708
uses = ["cor-fin-projective-curve-finite-group", "def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "lem-fin-finite-morphism", "lem-fin-finite-over-projective", "lem-fin-finite-type-pushforward-embedding", "lem-weil-pbc-grothendieck-spectral-sequence", "sbc-def-coefficient-conventions", "thm-constructible-serre", "thm-sp-if-e1"]
+++
Let $S$ be of finite type
over $k$, and let $\Lambda$ be the finite ring killed by an
integer invertible in $k$ of [sbc-def-coefficient-conventions].
For every constructible
$\Lambda$-sheaf $F$ on $\mathbf P^1_S$, every
higher direct image
$R^q\pi_*F$, for $\pi:\mathbf P^1_S\to S$, is constructible.
