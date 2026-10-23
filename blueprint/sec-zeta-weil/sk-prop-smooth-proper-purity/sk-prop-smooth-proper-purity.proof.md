+++
kind  = "proof"
of    = "sk-prop-smooth-proper-purity"
+++
Since $f_0$ is proper, the definition of $Rf_{0!}$ by
compactification identifies it with $Rf_{0*}$ ([sk-prop-sf-comp-proper]),
and this identification commutes with the base-change maps that define the
Weil structures.

By [sk-thm-dl-general-sheaf], $R^if_{0*}F$ is mixed of
weights at most $w+i$. Fix a closed point $y$ and put
$q_y=\#\kappa(y)$. By proper base change ([sk-thm-sfb-proper-base-change]),
the stalk at $\bar y$ with its local Frobenius is $H^i(X_{\bar y},F)$. Thus
every eigenvalue $\alpha$ there satisfies

$$
 |\iota(\alpha)|\leq q_y^{(w+i)/2}.
$$

For the opposite inequality we use duality. The dual $F^\vee$ is
lisse of weight $-w$, and so $F^\vee(d)$ has weight $-w-2d$. On the
smooth proper geometric fibre, [sk-thm-derived-duality] and
[sk-thm-frobenius] give a Frobenius-equivariant perfect pairing

$$
 H^i(X_{\bar y},F)\times
 H^{2d-i}(X_{\bar y},F^\vee(d))\longrightarrow\overline{\mathbf Q}_\ell.
$$

Since the pairing takes values in the trivial Weil line, the
eigenvalues on the second factor are the $\alpha^{-1}$, with
multiplicities. Applying [sk-thm-dl-general-sheaf] to the
structure map of the fibre over $\kappa(y)$ and to $F^\vee(d)$, we get

$$
 |\iota(\alpha)|^{-1}
 \leq q_y^{(-w-2d+2d-i)/2}=q_y^{(-w-i)/2}.
$$

Together the two inequalities give
$|\iota(\alpha)|=q_y^{(w+i)/2}$ at every closed point $y$. Finally,
every nonzero pure quotient in a mixed filtration of $R^if_{0*}F$
has a nonzero stalk at some closed point, and so its weight is $w+i$.
This proves the last assertion.

For the complement: by proper base change the geometric stalks of
$R^if_{0*}F$ are the $H^i(X_{\bar y},F)$, and smoothness of $f_0$ makes
them locally constant in $\bar y$ by smooth base change
([sk-thm-smooth-base-change]), applied to the finite levels of a lattice
of $F$ étale-locally on $Y_0$ and passed to the limit.
