+++
id = "lem-weil-pbc-comparison-sections"
kind = "lemma"
title = "Sections of the comparison inverse image"
order = 1351
uses = ["def-weil-pbc-cover-cech", "def-weil-pbc-ind-etale-basis", "def-weil-pbc-inverse-image", "def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-etale-finite-data-descent", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-ind-etale-basis", "lem-weil-pbc-ind-etale-stability"]
+++
Let $X$ be affine, let $F$ be an etale module sheaf, and write a basis object
as $U=\varprojlim_i U_i$ with $U_i/X$ affine etale of finite presentation.
Then naturally

$$
 (\nu_X^*F)(U)=\Gamma(U_{\Et},F|_U)
             =\varinjlim_i F(U_i).
$$

The restriction $F|_U$ is the scheme inverse image. The same section formula
holds for sheaves of sets.
