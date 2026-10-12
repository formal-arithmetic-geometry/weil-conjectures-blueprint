+++
id = "lem-weil-pbc-sheafification-geometric-stalk"
kind = "lemma"
title = "The geometric stalk of a sheafification is the stalk of the presheaf"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site", "def-weil-geometric-point", "def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-category-colimit", "def-weil-pbc-geometric-stalks", "def-weil-pbc-sheafification", "def-weil-pbc-abelian-etale-sheaves"]
lean = ["CategoryTheory.GrothendieckTopology.Point.presheafToSheafCompSheafFiberIso"]
tags = ["sheaf-dag", "mathlib", "stacks-03PT"]
+++
Let $T$ be a scheme [def-pc-scheme], $T_{\Et}$ its small etale site [def-weil-pbc-etale-site] and $\bar t:\operatorname{Spec}\Omega\to T$ a geometric point [def-weil-geometric-point], with category of pointed etale neighbourhoods $\mathcal N_{\bar t}$ [def-weil-pbc-pointed-etale-neighbourhoods]. For a presheaf of abelian groups $\mathcal F$ on $T_{\Et}$ (a contravariant functor from $T_{\Et}$ to abelian groups) define its stalk $\mathcal F_{\bar t}=\varinjlim_{(U,\bar u)\in\mathcal N_{\bar t}^{\mathrm{op}}}\mathcal F(U)$ [def-weil-pbc-category-colimit], with coprojections $s\mapsto(\text{class of }s\text{ at }(U,\bar u))$ (for a sheaf this is the stalk of [def-weil-pbc-geometric-stalks]). Let $\theta:\mathcal F\to\mathcal F^\#$ be the sheafification [def-weil-pbc-sheafification], $\mathcal F^\#\in\Ab(T_{\Et})$ [def-weil-pbc-abelian-etale-sheaves]. Then the homomorphism $\theta_{\bar t}:\mathcal F_{\bar t}\to(\mathcal F^\#)_{\bar t}$ induced by $\theta$, sending the class of $s\in\mathcal F(U)$ at $(U,\bar u)$ to the class of $\theta_U(s)$ at $(U,\bar u)$, is an isomorphism of abelian groups.
