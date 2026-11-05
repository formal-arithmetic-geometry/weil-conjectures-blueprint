+++
id = "proposition-cohomology-smooth-affine-curve"
kind = "proposition"
title = "Cohomology of a smooth affine curve"
order = 1584
lean = ["AlgebraicGeometry.Scheme.gysinH2_eq_zero_iff", "AlgebraicGeometry.Scheme.residueSequence_exact"]
uses = ["lemma-stability", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image"]
+++
Let $\overline C$ be a smooth proper connected curve of genus $g$
over an algebraically closed field $k$.  Let
$U=\overline C\setminus D$, where $D$ is a finite nonempty set of
closed points, and let $n$ be invertible in $k$.  There is a natural exact sequence

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
