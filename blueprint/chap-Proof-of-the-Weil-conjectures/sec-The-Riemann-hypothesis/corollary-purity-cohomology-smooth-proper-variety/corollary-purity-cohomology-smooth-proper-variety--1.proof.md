+++
kind = "proof"
of = "corollary-purity-cohomology-smooth-proper-variety--1"
order = 1372002
uses = ["theorem-weights-rf-shriek", "proposition-forgetting-supports-composition", "theorem-poincare-duality-frobenius"]
+++
The constant Weil sheaf is punctually pure of weight zero, since its
local Frobenius is the identity. Viewed as a complex concentrated in
degree zero, it is therefore mixed of weights at most zero. Apply
Theorem [theorem-weights-rf-shriek] to the structure map
$X_0\to\operatorname{Spec}\mathbf F_q$. Taking global sections of the
cohomology sheaves on the point gives

$$
|\iota(\alpha)|\le q^{i/2}
$$

for every eigenvalue on $H_c^i(X,\overline{\mathbf Q}_\ell)$. Since
$X_0$ is proper, Proposition [proposition-forgetting-supports-composition]
identifies $H_c^i$ with $H^i$, compatibly with Frobenius. This gives the
same upper bound on ordinary cohomology.

Let $\alpha$ now be an eigenvalue on $H^i(X,\overline{\mathbf Q}_\ell)$.
It is nonzero, since Frobenius is invertible. Frobenius-compatible
Poincaré duality, as in Theorem [theorem-poincare-duality-frobenius],
identifies the eigenvalues in degree $2d-i$ with the numbers $q^d/\alpha$,
where $\alpha$ ranges over the eigenvalues in degree $i$. Applying the
upper bound in degree $2d-i$ gives

$$
\frac{q^d}{|\iota(\alpha)|}
=|\iota(q^d/\alpha)|
\le q^{(2d-i)/2}.
$$

Thus $|\iota(\alpha)|\ge q^{i/2}$, and the two inequalities give the
asserted equality.
