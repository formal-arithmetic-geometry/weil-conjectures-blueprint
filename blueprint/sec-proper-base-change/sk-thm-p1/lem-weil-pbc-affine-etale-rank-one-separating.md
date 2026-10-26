+++
id = "lem-weil-pbc-affine-etale-rank-one-separating"
kind = "lemma"
title = "Affine etale rank-one extensions separate module-valued sheaves"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sum-extension"]
lean = ["AlgebraicGeometry.Scheme.affine_etale_rankOne_isSeparating"]
order = 1709
+++
Let $X$ be a scheme, $X_{\mathrm{Et}}$ its small etale site [def-weil-pbc-etale-site], and $\Lambda$ a commutative ring. In the category of sheaves valued in $\mathrm{Mod}(\Lambda)$ [def-weil-pbc-etale-sheaves], the family $G_U=j_{U!}\underline{\Lambda}_U$, indexed by all affine objects $j_U:U\to X$ of this site, is separating: for every $f,g:F\to F^{\prime}$, if $f\circ h=g\circ h$ for every $U$ and every $h:G_U\to F$, then $f=g$. Here extension by zero is [def-weil-pbc-etale-sum-extension] and $\underline\Lambda_U$ is the constant sheaf with value $\Lambda$ on $U_{\mathrm{Et}}$. The site, index family, coefficients and Hom sets use universe $u+1$ above the base-scheme universe $u$. No quasi-compactness, quasi-separatedness or finiteness of the ring is assumed.
