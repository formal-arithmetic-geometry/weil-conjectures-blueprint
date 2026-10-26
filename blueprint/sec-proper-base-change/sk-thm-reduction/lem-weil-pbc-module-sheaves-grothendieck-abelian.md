+++
id = "lem-weil-pbc-module-sheaves-grothendieck-abelian"
kind = "lemma"
title = "Sheaves of Lambda-modules on the small etale site form a Grothendieck abelian category"
lean = ["AlgebraicGeometry.Scheme.isGrothendieckAbelian_sheaf_smallEtaleTopology_moduleCat"]
order = 1947
uses = ["def-pc-scheme", "def-weil-pbc-etale-site", "def-weil-pbc-constant-sheaf", "def-weil-sheaf-of-modules-category", "def-sp-grothendieck-abelian", "def-weil-pbc-abelian-etale-sheaves"]
tags = ["stacks-03DA"]
+++
Let $T$ be a scheme [def-pc-scheme], $T_{\Et}$ its small etale site [def-weil-pbc-etale-site], $\Lambda$ a ring, $\Lambda_T$ the constant sheaf of rings with value $\Lambda$ on $T_{\Et}$ [def-weil-pbc-constant-sheaf], and $\Mod(T_{\Et},\Lambda)=\Mod(\Lambda_T)$ the category of sheaves of $\Lambda_T$-modules [def-weil-sheaf-of-modules-category]. Then $\Mod(T_{\Et},\Lambda)$ is a Grothendieck abelian category [def-sp-grothendieck-abelian]: it is abelian, it has all small colimits, filtered colimits in it are exact, and it has a generator. In particular (case $\Lambda=\mathbf Z$) the category $\Ab(T_{\Et})$ of abelian sheaves [def-weil-pbc-abelian-etale-sheaves] is Grothendieck abelian.
