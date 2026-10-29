+++
id = "lem-weil-pbc-constructible-change-of-ring"
kind = "lemma"
title = "Constructibility is unchanged under restriction of scalars between finite rings"
uses = ["def-weil-pbc-etale-constructible-sheaf", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.isConstructibleSheaf_restrictScalars_iff_of_finite"]
order = 1812
+++
Let $T$ be a scheme, $\varphi:\Lambda\to\Lambda'$ a homomorphism of finite commutative rings (for instance $\mathbf Z/n\to\mathbf Z/m$ for $m\mid n$), and $\mathcal G$ a sheaf of $\Lambda'_T$-modules on $T_{\Et}$ [def-weil-pbc-etale-site], [def-weil-pbc-etale-sheaves]; write $\varphi^*\mathcal G$ for $\mathcal G$ regarded as a sheaf of $\Lambda_T$-modules via $\varphi$. Then $\mathcal G$ is a constructible sheaf of $\Lambda'$-modules if and only if $\varphi^*\mathcal G$ is a constructible sheaf of $\Lambda$-modules [def-weil-pbc-etale-constructible-sheaf]. In particular a sheaf of $\mathbf Z/m$-modules, $m\mid n$, is constructible as a sheaf of $\mathbf Z/m$-modules iff it is as a sheaf of $\mathbf Z/n$-modules. (Ingredients: the same stratification serves for both, since inverse image along an immersion commutes with restriction of scalars; and, for sheaves of modules over a finite ring, being finite locally constant depends only on the underlying sheaf of sets, which $\varphi^*$ does not change.)
