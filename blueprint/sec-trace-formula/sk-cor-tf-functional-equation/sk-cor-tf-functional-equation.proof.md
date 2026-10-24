+++
kind  = "proof"
of    = "sk-cor-tf-functional-equation"
+++
By [sk-thm-derived-duality] and [sk-thm-frobenius] with $K=\Ql$ and $X$
proper, cup product and the trace define a perfect pairing
$H^i\times H^{2d-i}\to\Ql(-d)$ with
$\langle F_ix,F_{2d-i}y\rangle=q^d\langle x,y\rangle$. Hence $F_{2d-i}$
is $q^d$ times the inverse transpose of $F_i$. Consequently $b_{2d-i}=b_i$, the
eigenvalues of $F_{2d-i}$ are the $q^d/\alpha$ for the eigenvalues
$\alpha$ of $F_i$, with multiplicities, and
$\det F_i\cdot\det F_{2d-i}=q^{db_i}$. Since $(-1)^i=(-1)^{2d-i}$,

$$
 D^2=\prod_i\bigl(\det F_i\cdot\det F_{2d-i}\bigr)^{(-1)^i}
 =q^{d\chi}.
$$

Since $F_i$ is invertible, its eigenvalues $\alpha$ are nonzero, and

$$
 \det\bigl(1-q^{-d}T^{-1}F_i\bigr)
 =\prod_\alpha\Bigl(-\frac{\alpha}{q^dT}\Bigr)\Bigl(1-\frac{q^d}{\alpha}T\Bigr)
 =(-1)^{b_i}\frac{\det F_i}{(q^dT)^{b_i}}\det\bigl(1-TF_{2d-i}\bigr).
$$

[sk-cor-tf-point-counting], with $H^i_c=H^i$ since $X_0$ is
proper, expresses $Z(X_0,T)$ as the product of the
$\det(1-TF_i)^{(-1)^{i+1}}$. We substitute $1/(q^dT)$ for $T$ and apply
the last display to each factor. Since $(-1)^i=(-1)^{2d-i}$, the factors
$\det(1-TF_{2d-i})^{(-1)^{i+1}}$ multiply to $Z(X_0,T)$, and the scalar
factors multiply to

$$
 (-1)^{\chi}D^{-1}(q^dT)^{\chi}=(-1)^{\chi}D\,T^{\chi},
$$

by $D^2=q^{d\chi}$.

For the complement, the first three assertions were shown above. For odd
$d$, graded commutativity of the cup product makes the perfect pairing on
$H^d$ alternating ([sk-thm-poincare-duality] (3)). A nondegenerate
alternating form over a field of characteristic $\neq2$ lives on a space of even dimension, so $b_d$ is even.
Pairing $i$ with $2d-i$ gives $\chi=2\sum_{i<d}(-1)^ib_i+(-1)^db_d$, hence
$\chi\equiv b_d\pmod2$ and $d\chi$ is even in both cases. Then
$\varepsilon=Dq^{-d\chi/2}$ satisfies $\varepsilon^2=1$.
