+++
kind = "proof"
of = "sk-prop-smooth-proper-purity"
+++
Since $f_0$ is proper, the definition of $Rf_{0!}$ by
compactification identifies it with $Rf_{0*}$, and this
identification commutes with the base change maps that define the Weil
structures, which proves the first assertion.
By Theorem [sk-thm-dl-general-sheaf], $R^if_{0*}F$ is mixed of
weights at most $w+i$. Fix a closed point $y$. By proper base change, the stalk at $\bar y$ with
its local Frobenius is $H^i(X_{\bar y},F)$. Hence every eigenvalue
$\alpha$ there satisfies

$$
|\iota(\alpha)|\leq q_y^{(w+i)/2}.
$$

For the opposite inequality we use duality. The dual $F^\vee$ is
lisse of weight $-w$, and so $F^\vee(d)$ has weight $-w-2d$. On the
smooth proper geometric fibre, Corollary [sk-thm-derived-duality] and
Theorem [sk-thm-frobenius] give a Frobenius-equivariant perfect
pairing

$$
H^i(X_{\bar y},F)\times
H^{2d-i}(X_{\bar y},F^\vee(d))\longrightarrow \overline{\mathbf Q}_\ell.
$$

Since the pairing takes values in the trivial Weil line, the
eigenvalues on the second factor are the $\alpha^{-1}$, with
multiplicities. Applying Theorem [sk-thm-dl-general-sheaf] to the
structure map of the fibre over $\kappa(y)$ and to $F^\vee(d)$, we get

$$
|\iota(\alpha)|^{-1}
\leq q_y^{(-w-2d+2d-i)/2}=q_y^{(-w-i)/2}.
$$

Together the two inequalities show that
$|\iota(\alpha)|=q_y^{(w+i)/2}$ at every closed point $y$. Finally,
every nonzero pure quotient in a mixed filtration of $R^if_{0*}F$
has a nonzero stalk at some closed point, and therefore its weight is
$w+i$. This proves the last assertion.
