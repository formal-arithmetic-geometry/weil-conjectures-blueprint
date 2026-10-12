+++
id = "lem-weil-pbc-constant-sheaf-geometric-stalk"
kind = "lemma"
title = "Geometric stalks of a constant etale sheaf"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site", "def-weil-pbc-sheafification", "def-weil-pbc-constant-sheaf", "def-weil-pbc-abelian-etale-sheaves", "def-weil-geometric-point", "def-weil-pbc-geometric-stalks", "def-weil-pbc-pointed-etale-neighbourhoods"]
tags = ["sheaf-dag", "stacks-03PT"]
+++
Let $T$ be a scheme [def-pc-scheme], $E$ an abelian group, and $\underline E$ the constant sheaf with value $E$ on the small etale site $T_{\Et}$ [def-weil-pbc-etale-site], i.e. the sheafification [def-weil-pbc-sheafification] of the constant presheaf $U\mapsto E$ (all restriction maps the identity), an object of $\Ab(T_{\Et})$ [def-weil-pbc-constant-sheaf], [def-weil-pbc-abelian-etale-sheaves]; write $\iota_U:E\to\underline E(U)$ for the component at $U$ of the canonical map from the constant presheaf to its sheafification. Let $\bar t:\operatorname{Spec}\Omega\to T$ be a geometric point [def-weil-geometric-point] and $\underline E_{\bar t}$ the stalk [def-weil-pbc-geometric-stalks]. Then the homomorphism $E\to\underline E_{\bar t}$ sending $e$ to the class of $\iota_T(e)$ at the pointed etale neighbourhood $(T,\bar t)$ is an isomorphism of abelian groups.
