+++
kind = "proof"
of = "proposition-h-1-curve-tate-module--1"
order = 1565003
uses = []
+++
The Kummer sequence on $X_{\acute{e}t}$ gives

$$
0\longrightarrow\Gamma(X,\mathcal O_X)^\times/m
\longrightarrow H^1(X_{\acute{e}t},\mu_m)
\longrightarrow\operatorname{Pic}(X)[m]\longrightarrow0.
$$

Properness makes $\Gamma(X,\mathcal O_X)$ a finite $\Omega$-algebra.
Since $\Omega$ is algebraically closed and $m$ is invertible, every unit
of this algebra is an $m$th power. Thus the first term vanishes.
In Lean, `AlgebraicGeometry.Scheme.injective_sheafHMap_kernelι_one`
proves injectivity of the map to $H^1(X_{\acute{e}t},\mathbf G_m)$, and
`AlgebraicGeometry.Scheme.mem_torsionBy_iff_exists_sheafHMap_kernelι_one`
identifies its image with the torsion subgroup, using the canonical
Picard isomorphism
`AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroupAddEquiv`.

For an automorphism $f$, restriction on cohomology commutes with
$\mu_m\to\mathbf G_m$. Under the Picard isomorphism, restriction on
$H^1(X_{\acute{e}t},\mathbf G_m)$ is pullback of line bundles. This gives
the second assertion. Finally, the composite
$\mu_m\hookrightarrow\mu_{m'}\to\mathbf G_m$ is the original inclusion
$\mu_m\to\mathbf G_m$; functoriality of $H^1$ gives the last assertion.
