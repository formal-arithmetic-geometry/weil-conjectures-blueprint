+++
id = "lem-weil-pbc-fpqc-finer-than-etale"
kind = "lemma"
title = "Every small etale covering family is an fpqc covering"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.fpqcCover_of_smallEtaleCover"]
+++
Let $T$ be a scheme [def-pc-scheme], and let $(f_i:U_i\to U)$ be any covering family in its small etale site $T_{\mathrm{Et}}$ [def-weil-pbc-etale-site]. Then $(f_i)_i$ is an fpqc covering of $U$ `AlgebraicGeometry.Scheme.fpqcPrecoverage` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/Fpqc.lean)): each $f_i$ is flat, and for every affine open $V\subseteq U$ there are finitely many indices $i_j$ and affine opens $V_j\subseteq U_{i_j}$ whose images under $f_{i_j}$ have union exactly $V$.
