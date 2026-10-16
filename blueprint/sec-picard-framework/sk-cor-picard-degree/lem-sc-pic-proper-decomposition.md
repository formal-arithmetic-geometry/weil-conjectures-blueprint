+++
id = "lem-sc-pic-proper-decomposition"
kind = "lemma"
title = "Structure of the Picard group of a proper curve"
lean = ["AlgebraicGeometry.Scheme.exists_mulEquiv_prod_ker_picDegreeHom"]
order = 894
uses = ["def-sc-curves", "def-sc-pic0", "def-sc-picard-group"]
+++
Let $C$ be a proper smooth connected curve over
algebraically closed $k$. The degree sequence

$$
0\longrightarrow\operatorname{Pic}^0(C)\longrightarrow
\operatorname{Pic}(C)\xrightarrow{\ \deg\ }\mathbf Z\longrightarrow0
$$

splits (the degree map is surjective since a $k$-rational point
gives a degree-one class), hence

$$
\operatorname{Pic}(C)\cong\mathbf Z\oplus\operatorname{Pic}^0(C).
$$
