+++
id = "lem-weil-pbc-etale-qcqs-cofinal-finite-coverings"
kind = "lemma"
title = "Cofinal finite affine etale coverings of a quasi-compact quasi-separated etale object"
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.etale_qcqs_cofinal_finite_affine_coverings"]
source = "literature/stacks-project/etale-cohomology.tex, Etale Cohomology, Section 59.51, Tag 03Q4 (label section-colimit), first paragraph, using Topologies, Lemma Tag 0218 (label lemma-etale-affine) and Sites, Lemma Tag 0738 (label lemma-directed-colimits-sections)"
+++
Let $U$ be a quasi-compact and quasi-separated scheme [def-weil-pbc-scheme-conventions], viewed as an object of its small etale site [def-weil-pbc-etale-site]. For every jointly surjective family of etale morphisms $(T_a\to U)_{a\in A}$, there are a finite set $B$, indices $a(b)\in A$, and affine schemes $V_b$ with etale maps $V_b\to U$, each factoring through $T_{a(b)}\to U$, such that $(V_b\to U)_{b\in B}$ is jointly surjective and every fibre product $V_b\times_UV_{b'}$ is quasi-compact. Equivalently, finite affine etale coverings with quasi-compact pairwise fibre products form a cofinal system of coverings of $U$. This is the refinement used in Etale Cohomology, Section 59.51, Tag 03Q4, for Sites, Lemma Tag 0738.
