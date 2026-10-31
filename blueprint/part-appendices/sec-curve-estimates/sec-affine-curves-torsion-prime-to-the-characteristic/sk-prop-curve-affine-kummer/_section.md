+++
id = "sk-prop-curve-affine-kummer"
kind = "proposition"
title = "Cohomology of a smooth affine curve"
order = 917
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.injective_restrictH1", "AlgebraicGeometry.Scheme.EtaleTorsor.range_restrictH1_eq_ker_residueH1", "AlgebraicGeometry.IsConnectedCurve.sheafH_constantZMod_of_isAffine", "AlgebraicGeometry.IsConnectedCurve.natCard_sheafH_one_constantZMod_mul", "AlgebraicGeometry.IsConnectedCurve.bijective_fieldExtensionCohomologyMap_of_isAffine"]
uses = ["sk-prop-av-isogeny", "sk-prop-picard-pic-split", "sk-thm-curveestimate"]
tags = ["sketch"]
+++
Let $\overline C$ be a smooth proper connected curve of genus $g$
over an algebraically closed field $k$. Let
$U=\overline C\setminus D$, where $D$ is a finite nonempty set of
closed points, and let $n$ be invertible in $k$. There is a natural exact sequence

$$
0\longrightarrow H^1(\overline C,\mu_n)
\longrightarrow H^1(U,\mu_n)
\xrightarrow{\partial}(\mathbf Z/n)^D
\xrightarrow{\sum}\mathbf Z/n\longrightarrow0.
\tag{D.1}
$$

Moreover, $H^0(U,\mu_n)=\mu_n(k)$ and $H^q(U,\mu_n)=0$ for $q>1$.
The group $H^1(U,\mu_n)$ is noncanonically $(\mathbf Z/n)^{2g+\#D-1}$, and
the pullback maps on all these groups are isomorphisms under
algebraically closed extension.
