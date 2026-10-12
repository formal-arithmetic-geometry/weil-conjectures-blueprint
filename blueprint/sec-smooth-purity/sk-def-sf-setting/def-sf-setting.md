+++
id = "def-sf-setting"
kind = "remark"
title = "Coefficients and sites"
order = 1794
lean = ["AlgebraicGeometry.Etale.DerivedCategoryBoundedConstructible", "AlgebraicGeometry.Etale.DerivedCategory.boundedConstructibleFiniteTor", "AlgebraicGeometry.Etale.constantComplex"]
+++
Fix the global finite-field datum $(p,a,q,k_0,k)$ with $k=\overline{\mathbf F}_q$, a prime $\ell\neq p$, a finite extension $E/\Ql$ with valuation ring
$\mathcal O_E$ and uniformizer $\varpi_E$, an integer $n\ge1$, and put
$A_{E,n}=\mathcal O_E/\varpi_E^n$. The *coefficient stages* are
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, with constructibility, finite Tor
amplitude, constructible intervals and Tate twists. At a finite stage, for a
scheme $X$, $D^b_c(X,\Lambda)$ is the full subcategory of the derived category
of sheaves of $\Lambda$-modules on the small étale site of $X$ consisting of the
bounded complexes with constructible cohomology sheaves,
$D^b_{ctf}(X,\Lambda)\subseteq D^b_c(X,\Lambda)$ consists of those of finite Tor
amplitude, and the constant complex $\Lambda_X$ is the constant sheaf $\Lambda$
placed in degree $0$, the unit of $\otimes^L_\Lambda$.
Morphisms are separated of finite type.
