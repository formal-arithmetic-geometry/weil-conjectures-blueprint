+++
id = "lemma-weil-pbc-cancellation"
kind = "lemma"
title = "Cancellation along a proper surjection"
lean = ["AlgebraicGeometry.Etale.HasInjectiveAcyclicity.of_comp", "AlgebraicGeometry.Etale.HasTorsionBaseChange.of_comp"]
order = 2049
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "def-weil-pbc-torsion-etale-sheaf"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an abelian group (every
element has finite additive order; for instance $\Lambda=\mathbf Z/n$). For a
morphism of schemes $f:X\to Y$ say that

- $f$ has *torsion base change* over $\Lambda$ if, for every cartesian square
  [def-weil-pbc-cartesian-square] with $f$ on the right and an arbitrary
  $g:Y'\to Y$ at the bottom, the derived exchange morphism
  [def-weil-pbc-derived-exchange] $g^{-1}Rf_*K\to Rf'_*g'^{-1}K$ is an
  isomorphism for every $K\in\Dplus(X_{\Et},\Lambda)$ whose cohomology sheaves
  are torsion [def-weil-pbc-torsion-etale-sheaf];
- $f$ has *injective acyclicity* over $\Lambda$ if, for every such square and
  every injective sheaf $I$ of $\Lambda$-modules on $X_{\Et}$ which is torsion,
  $R^qf'_*g'^{-1}I=0$ for $q>0$ [def-weil-pbc-direct-image].

Let $f:X\to Y$ be surjective and $h:Y\to Z$ arbitrary.

1. If $f$ has torsion base change and $hf$ has injective acyclicity over
   $\Lambda$, then $h$ has injective acyclicity over $\Lambda$.
2. If $f$ and $hf$ have torsion base change over $\Lambda$, then so does $h$.
