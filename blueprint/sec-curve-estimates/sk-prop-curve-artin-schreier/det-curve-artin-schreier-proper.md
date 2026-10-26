+++
id = "det-curve-artin-schreier-proper"
kind = "proposition"
title = "Artin–Schreier computation on a smooth proper curve"
lean = ["AlgebraicGeometry.Scheme.nonempty_addEquiv_sheafH_zero_constantZMod", "AlgebraicGeometry.IsCurve.exists_constantZMod_one_frobenius_baseChange_model", "AlgebraicGeometry.isZero_etaleCohomology_constantZMod_of_one_lt_of_charP", "AlgebraicGeometry.IsCurve.bijective_cohomologyMap_constantModSheaf_of_isProper", "LinearMap.Frobenius.finite_fixedPoints", "LinearMap.Frobenius.natCard_fixedPoints_le"]
order = 1438
uses = ["def-sc-field-extension"]
+++
Let $k$ be algebraically closed of characteristic $p>0$ and $C$ a smooth
proper connected curve over $k$. Then:

1. $H^0(C_{\mathrm{ét}},\mathbf F_p)\cong\mathbf F_p$ and
   $H^q(C_{\mathrm{ét}},\mathbf F_p)=0$ for $q\geq2$.
2. There are a finite-dimensional $k$-vector space $V$ and a $p$-linear map
   $F:V\to V$ such that
   $H^1(C_{\mathrm{ét}},\mathbf F_p)\cong V^F=\ker(F-1:V\to V)$. In
   particular $H^1(C_{\mathrm{ét}},\mathbf F_p)$ is finite, of order at most
   $p^{\dim_kV}$.
3. For an extension $k\subseteq k'$ of algebraically closed fields, let
   $F'$ be the $p$-linear map of $k'\otimes_kV$ with
   $F'(1\otimes v)=1\otimes F(v)$. Then
   $H^1((C_{k'})_{\mathrm{ét}},\mathbf F_p)\cong(k'\otimes_kV)^{F'}$, and
   under these identifications the pullback map is $v\mapsto1\otimes v$.
   The pullback maps $\rho^q_{k'/k}(C,\mathbf F_p)$ of
   [def-sc-field-extension] are isomorphisms for all $q$.
