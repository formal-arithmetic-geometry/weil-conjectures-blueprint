+++
kind = "proof"
of = "corollary-functional-equation--7"
order = 1045012
+++
Use the dual eigenvalues of Theorem [theorem-poincare-duality-frobenius--8] and the determinant relation of clause [corollary-functional-equation--6].

Now consider a single factor. Since $F_i$ is invertible, its
eigenvalues $\alpha$ are nonzero. Pulling $-\alpha/(q^dT)$ out of
each linear factor gives

$$
\det\bigl(1-q^{-d}T^{-1}F_i\bigr)
=\prod_\alpha\Bigl(-\frac{\alpha}{q^dT}\Bigr)\Bigl(1-\frac{q^d}{\alpha}T\Bigr)
=(-1)^{b_i}\frac{\det F_i}{(q^dT)^{b_i}}\det\bigl(1-TF_{2d-i}\bigr).
$$

By Corollary [corollary-point-counting-zeta-function], and since $H^i_c=H^i$ as $X_0$ is
proper, $Z(X_0,T)$ is the product of the
$\det(1-TF_i)^{(-1)^{i+1}}$. We substitute $1/(q^dT)$ for $T$ and apply
the last display to each factor. Since $(-1)^i=(-1)^{2d-i}$, the factors
$\det(1-TF_{2d-i})^{(-1)^{i+1}}$ multiply to $Z(X_0,T)$, and the scalar
factors multiply to

$$
(-1)^{\chi}D^{-1}(q^dT)^{\chi}=(-1)^{\chi}D\,T^{\chi},
$$

by $D^2=q^{d\chi}$. The second form of the equation is the definition
of $\varepsilon$.

*Source:* the proof of Corollary [corollary-functional-equation].
