+++
id = "lem-weil-pbc-cyclic-module-constant-reflection"
kind = "lemma"
title = "Forgetting cyclic module coefficients reflects constancy"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.cyclic_module_isConstant_of_forget"]
order = 1815
+++
Let $Y$ be a scheme [def-weil-pbc-scheme-conventions], $U$ an object of its small etale site [def-weil-pbc-etale-site], and $n\geq1$. Let $F$ be a sheaf of $\operatorname{ULift}(\mathbf Z/n)$-modules on the localized site $(Y_{\mathrm{et}})/U$ [def-weil-pbc-etale-sheaves]. If its underlying abelian sheaf is constant, then $F$ is constant as a module sheaf. No finiteness or nonemptiness hypothesis is imposed.
