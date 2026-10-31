+++
id = "sk-prop-curve-artin-schreier"
kind = "proposition"
title = "$p$-torsion on a smooth proper curve in characteristic $p$"
order = 921
lean = ["AlgebraicGeometry.Scheme.nonempty_addEquiv_sheafH_zero_constantZMod", "AlgebraicGeometry.IsCurve.exists_constantZMod_one_frobenius_baseChange_model", "AlgebraicGeometry.isZero_etaleCohomology_constantZMod_of_one_lt_of_charP", "AlgebraicGeometry.IsCurve.finite_sheafH_constantModSheaf_of_isProper", "AlgebraicGeometry.IsCurve.bijective_cohomologyMap_constantModSheaf_of_isProper"]
uses = ["sk-prop-av-isogeny", "sk-prop-sf-comparison"]
tags = ["sketch"]
+++
Let $C$ be a smooth proper connected curve of genus $g$ over an
algebraically closed field of characteristic $p>0$, and let $\varphi$ be
the Frobenius-linear endomorphism of $H^1(C,\mathcal O_C)$ induced by
$a\mapsto a^p$ on $\mathcal O_C$. Then

$$
H^0(C,\mathbf F_p)=\mathbf F_p,\qquad
H^1(C,\mathbf F_p)=
\ker(\varphi-1:H^1(C,\mathcal O_C)\to H^1(C,\mathcal O_C)),
$$

and $H^q(C,\mathbf F_p)=0$ for $q>1$. The group $H^1(C,\mathbf F_p)$
is finite, of $\mathbf F_p$-dimension at most $g$, and its pullback map
is an isomorphism under algebraically closed extension.
