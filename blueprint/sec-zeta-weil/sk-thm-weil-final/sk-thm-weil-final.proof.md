+++
kind  = "proof"
of    = "sk-thm-weil-final"
+++
The first assertion follows from [sk-cor-tf-point-counting] and
[sk-thm-intfactors], and the second is the purity
statement for all complex embeddings in that theorem.
Frobenius-equivariant Poincaré duality, already used in
[sk-cor-tf-functional-equation], matches the eigenvalues in
degrees $i$ and $2d-i$ as $\alpha$ and $q^d/\alpha$, and hence
$b_i=b_{2d-i}$. Independence of $\ell$ follows from $b_i=\deg P_i$.

If $X$ is connected, a global section of its constant sheaf is
constant, so $H^0(X,\Ql)=\Ql$ with Frobenius acting as the identity.
The trace map and duality identify $H^{2d}(X,\Ql)$ with $\Ql(-d)$
([sk-cor-trace]), on which Frobenius acts by $q^d$. This proves the
assertions in degrees $0$ and $2d$; when $d=0$, the two descriptions concern
the same group.

For the functional equation, apply
[sk-cor-tf-functional-equation] with
$D=\prod_i\det(F_i)^{(-1)^i}$. It shows that $D^2=q^{d\chi}$ and that
the coefficient of $T^\chi$ is $(-1)^\chi D$.
The equalities $b_i=b_{2d-i}$ give $\chi\equiv b_d\pmod2$. When $d$ is
odd, graded commutativity makes the perfect pairing on the middle
cohomology alternating, so $b_d$ is even (the complement of
[sk-cor-tf-functional-equation]). Thus $d\chi$ is always even.
Put $\varepsilon=(-1)^\chi Dq^{-d\chi/2}$, whose square is one.
The resulting formula is an identity in $\mathbf Q(T)$, because the
zeta function is rational over $\mathbf Q$ and the scalar
$\varepsilon q^{d\chi/2}$ is a rational number.

The complement is the eigenvalue matching above, transported to the $P_i$ by
$P_i=P_{i,\ell}$.
