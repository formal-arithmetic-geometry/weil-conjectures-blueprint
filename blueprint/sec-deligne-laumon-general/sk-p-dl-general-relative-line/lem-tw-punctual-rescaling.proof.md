+++
kind = "proof"
of = "lem-tw-punctual-rescaling"
uses = ["def-weil-punctual-weights"]
+++
The inclusion $X_y\hookrightarrow X_0$ is a closed immersion.
Thus a closed point $z$ of $X_y$ is the same closed point on
$X_0$, with the same residue field and the same local Frobenius
operator on the restricted stalk.
If $r=[\kappa(z):\kappa(y)]$, the tower of finite residue fields gives

$$
[\kappa(z):k_0]=mr,\qquad q_z=q^{mr}=(q^m)^r .
$$

Consequently an eigenvalue $\alpha$ on that stalk satisfies

$$
|\iota(\alpha)|=q_z^{w/2}=(q^m)^{rw/2},
$$

by [def-weil-punctual-weights] on $X_0$.
This is the same punctual weight condition over $\kappa(y)$.
No identification between the stalk at $z$ and a stalk at $y$
is involved.
