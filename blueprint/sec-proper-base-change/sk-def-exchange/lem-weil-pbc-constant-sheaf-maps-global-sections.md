+++
id = "lem-weil-pbc-constant-sheaf-maps-global-sections"
kind = "lemma"
title = "Morphisms out of a constant sheaf are maps into global sections"
uses = ["def-weil-pbc-constant-sheaf", "def-weil-pbc-sheafification"]
lean = ["CategoryTheory.constantSheafAdj"]
tags = ["sheaf-dag", "mathlib", "stacks-0H7J"]
+++
Let $\mathcal C$ be a site with a final object $X$, and let $\mathcal A$ be the category of sets or of commutative rings (a category of values in which sheafification [def-weil-pbc-sheafification] exists). For an object $E$ of $\mathcal A$ let $\underline E$ be the constant sheaf [def-weil-pbc-constant-sheaf], with $c_E:E\to\underline E(X)$ the map sending $e$ to the image of the constant section $e$ of the constant presheaf. Then for every sheaf $\mathcal F$ on $\mathcal C$ with values in $\mathcal A$ the map $\operatorname{Hom}(\underline E,\mathcal F)\to\operatorname{Hom}_{\mathcal A}(E,\mathcal F(X))$, $\varphi\mapsto\varphi_X\circ c_E$, is a bijection, natural in $\mathcal F$ (and in $E$); that is, $E\mapsto\underline E$ is left adjoint to $\mathcal F\mapsto\mathcal F(X)=\Gamma(\mathcal C,\mathcal F)$.
