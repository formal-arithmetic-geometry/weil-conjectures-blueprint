+++
id = "lem-sc-zero-generic-acyclic"
kind = "lemma"
title = "Acyclicity of a sheaf with generically vanishing sections"
lean = ["AlgebraicGeometry.IsCurve.subsingleton_H_of_genericVanishing"]
order = 1429
uses = ["def-sc-curves", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "lem-weil-pbc-cohomology-filtered-colimit", "lem-weil-pbc-zero-dimensional-cohomology", "lemma-weil-pbc-finite-direct-image-exact"]
+++
Let $C$ be an integral separated
curve over an algebraically closed field,
and let $F$ be an abelian etale
sheaf on $C$ whose sections vanish generically in the following sense: for
every nonempty affine open $j_U:U\hookrightarrow C$ write
$u_U:F\to j_{U*}j_U^*F$ for the adjunction unit; every section of $F$ over an
etale $V\to C$ is, locally on $V$ for the etale topology, killed by $u_U$
for some nonempty affine open $U$. Then $H^q(C,F)=0$ for all $q>0$, in the
sense of [def-weil-pbc-etale-cohomology].
