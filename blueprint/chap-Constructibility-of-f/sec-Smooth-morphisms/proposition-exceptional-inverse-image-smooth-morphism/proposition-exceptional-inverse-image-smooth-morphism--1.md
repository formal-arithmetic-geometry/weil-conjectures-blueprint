+++
id = "proposition-exceptional-inverse-image-smooth-morphism--1"
kind = "proposition"
title = "Smooth duality on an affine chart"
order = 561002
aliases = ["bp-r169-1"]
lean = ["AlgebraicGeometry.Etale.satisfiesSmoothDuality_chart"]
uses = ["definition-relative-dualizing-complex", "theorem-existence-exceptional-inverse-image"]
+++
Let $f:X\to S$ be a morphism, let $u:U\hookrightarrow X$ and
$v:V\hookrightarrow S$ be affine open subschemes with $f(U)\subset V$, and
suppose that
$$
fu=vp_de,\qquad e:U\longrightarrow\mathbf A^d_V
$$
with $e$ étale. Let $A$ be finite commutative with exponent invertible on $V$,
and suppose that $h=fu$ admits a compactification.

Assume the following two assertions: for every compactifiable étale morphism
$a$, the complex $\omega_a$ is isomorphic to the tensor unit and its canonical tensor maps
are isomorphisms; for every affine-space projection over an affine base where
the exponent of $A$ is invertible, its dualizing complex is a locally constant
rank-one sheaf shifted by twice the relative dimension and its canonical
tensor maps are isomorphisms.

Then there is a locally constant sheaf $L_U$ of $A$-modules on $U_{\acute{e}t}$,
with every geometric stalk isomorphic to $A$, such that
$$
\omega_h\simeq L_U[2d].
$$
For every $N\in D(S_{\acute{e}t},A)$ the canonical map
$$
\omega_h\otimes_A^{\mathbf L}h^*N\longrightarrow h^!N
$$
is an isomorphism.
