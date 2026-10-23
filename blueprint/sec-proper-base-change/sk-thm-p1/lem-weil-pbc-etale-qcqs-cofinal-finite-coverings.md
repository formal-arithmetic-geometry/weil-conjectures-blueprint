+++
id = "lem-weil-pbc-etale-qcqs-cofinal-finite-coverings"
kind = "lemma"
title = "Cofinal finite affine etale coverings of a quasi-compact quasi-separated etale object"
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Etale.exists_affine_refinement", "AlgebraicGeometry.Scheme.mem_smallEtaleTopology_iff", "AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace"]
order = 1740
+++
Let $U$ be a quasi-compact and quasi-separated scheme [def-weil-pbc-scheme-conventions], viewed as an object of its small étale site [def-weil-pbc-etale-site]. For every jointly surjective family of étale morphisms $(T_a\to U)_{a\in A}$ there are a finite set $B$, indices $a(b)\in A$, and affine schemes $V_b$ with étale maps $V_b\to U$, each factoring through $T_{a(b)}\to U$, such that $(V_b\to U)_{b\in B}$ is jointly surjective and every fibre product $V_b\times_UV_{b'}$ is quasi-compact. Equivalently, finite affine étale coverings with quasi-compact pairwise fibre products form a cofinal system of coverings of $U$.
