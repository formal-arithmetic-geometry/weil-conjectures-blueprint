+++
id = "lem-sc-sylow-module-filtration"
kind = "lemma"
title = "Sylow reduction of a finite torsion module"
lean = ["DiscreteModule.exists_isOpen_not_dvd_index_filtration", "Rep.exists_openSubgroup_primary_module_filtration"]
order = 1387
uses = ["def-exc-continuous-cohomology"]
+++
Let $G$ be a compact topological group (for instance a profinite group),
$\ell$ a prime, and $M$ a finite $\ell$-primary discrete continuous
$G$-module. There are an open subgroup $H\subset G$ of index prime to
$\ell$ and a finite filtration $0=F_0\subseteq F_1\subseteq\cdots\subseteq
F_n=M$ by $H$-stable subgroups whose successive quotients are trivial
$\mathbf F_\ell$-modules: $\ell F_{i+1}\subseteq F_i$ and $hx-x\in F_i$
for $h\in H$, $x\in F_{i+1}$.
