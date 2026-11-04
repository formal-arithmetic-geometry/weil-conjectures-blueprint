+++
kind = "proof"
of = "theorem-purity-higher-direct-images-under"
order = 1364
uses = ["corollary-degreewise-duality-over-fields", "theorem-poincare-duality-frobenius", "theorem-direct-image-mixed-sheaf"]
+++
Since $f_0$ is proper, the definition of $Rf_{0!}$ by
compactification identifies it with $Rf_{0*}$. This identification
commutes with the base change maps that define the Weil structures,
which proves the first assertion.

Fix a closed point $y$. By proper base change, the stalk at $\bar y$
with its local Frobenius is $H^i(X_{\bar y},F)$. By
Theorem [theorem-direct-image-mixed-sheaf], $R^if_{0*}F$ is mixed
of weights at most $w+i$, so every eigenvalue $\alpha$ there
satisfies

$$
|\iota(\alpha)|\leq q_y^{(w+i)/2}.
$$

The opposite inequality comes from duality. The dual $F^\vee$ is
lisse of weight $-w$, so $F^\vee(d)$ has weight $-w-2d$. On the
smooth proper geometric fibre, Corollary [corollary-degreewise-duality-over-fields] and
Theorem [theorem-poincare-duality-frobenius] give a Frobenius-equivariant perfect
pairing

$$
H^i(X_{\bar y},F)\times
H^{2d-i}(X_{\bar y},F^\vee(d))\longrightarrow\overline{\mathbf Q}_\ell.
$$

Since the pairing is perfect and takes values in the trivial Weil
line, it identifies the second factor with the dual of the first as a
Frobenius module, so the eigenvalues on the second factor are the
$\alpha^{-1}$, with multiplicities. Applying
Theorem [theorem-direct-image-mixed-sheaf] once more, now to the
structure map of the fibre over $\kappa(y)$ and to $F^\vee(d)$, of
weight $-w-2d$, and to its cohomology in degree $2d-i$, we get

$$
|\iota(\alpha)|^{-1}
\leq q_y^{(-w-2d+2d-i)/2}=q_y^{(-w-i)/2}.
$$

The two inequalities give $|\iota(\alpha)|=q_y^{(w+i)/2}$ at every
closed point $y$. Every nonzero pure quotient in a mixed filtration of
$R^if_{0*}F$ has a nonzero stalk at some closed point, so its weight is
$w+i$. This proves the last assertion.
