+++
id = "lem-weil-pbc-module-sheaves-grothendieck-abelian"
kind = "lemma"
title = "Sheaves of Lambda-modules on the small etale site form a Grothendieck abelian category"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site", "def-weil-pbc-constant-sheaf", "def-weil-sheaf-of-modules-category", "def-sp-grothendieck-abelian", "def-weil-pbc-abelian-etale-sheaves", "def-weil-presheaf-modules-sheafification"]
refines = "proof/lem-weil-pbc-grothendieck-spectral-sequence"
tags = ["sheaf-dag", "stacks-03DA"]
+++
Let $T$ be a scheme [def-pc-scheme], $T_{\Et}$ its small etale site [def-weil-pbc-etale-site], $\Lambda$ a commutative ring, $\Lambda_T$ the constant sheaf of rings with value $\Lambda$ on $T_{\Et}$ [def-weil-pbc-constant-sheaf], and $\Mod(T_{\Et},\Lambda)=\Mod(\Lambda_T)$ the category of sheaves of $\Lambda_T$-modules [def-weil-sheaf-of-modules-category]. Then $\Mod(T_{\Et},\Lambda)$ is a Grothendieck abelian category [def-sp-grothendieck-abelian]: it is abelian, it has all small colimits, filtered colimits in it are exact, and it has a generator, namely $\bigoplus_{U\in\mathcal S}j_{U!}\Lambda_U$, where $\mathcal S$ is a set of affine objects of $T_{\Et}$ such that every object of $T_{\Et}$ has a covering by members of $\mathcal S$, and $j_{U!}\Lambda_U$ is the extension by zero of $\Lambda_T|_U$ (Stacks 03DI), i.e. the sheafification [def-weil-presheaf-modules-sheafification] of the presheaf of $\Lambda_T$-modules $V\mapsto\bigoplus_{\varphi\in\mathrm{Mor}_{T_{\Et}}(V,U)}\Lambda_T(V)$. In particular (case $\Lambda=\mathbf Z$) the category $\Ab(T_{\Et})$ of abelian sheaves [def-weil-pbc-abelian-etale-sheaves] is Grothendieck abelian.
