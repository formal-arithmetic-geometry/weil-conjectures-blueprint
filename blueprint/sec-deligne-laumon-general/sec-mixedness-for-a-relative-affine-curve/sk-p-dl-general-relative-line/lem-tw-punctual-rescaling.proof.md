+++
kind = "proof"
of = "lem-tw-punctual-rescaling"
uses = ["def-weil-punctual-weights"]
+++
Let $x'$ be a closed point of $X'_0$ and $x=\varphi(x')$, a closed point
of $X_0$, and put $r=[\kappa(x'):\kappa(x)]$, so that $q_{x'}=q_x^r$. A
geometric point $\bar x'$ over $x'$ maps to a geometric point $\bar x$
over $x$, and $(\varphi^*\mathcal F)_{\bar x'}=\mathcal F_{\bar x}$; under
this identification the local Frobenius $F_{x'}$ of the induced Weil
structure acts as $F_x^r$. Hence the eigenvalues of $F_{x'}$ are the
$\alpha^r$, with $\alpha$ an eigenvalue of $F_x$ on $\mathcal F_{\bar x}$,
and $|\iota(\alpha^r)|=q_x^{rw/2}=q_{x'}^{w/2}$ by
[def-weil-punctual-weights] on $X_0$. So $\varphi^*\mathcal F$ is
punctually $\iota$-pure of weight $w$.

*Rescaling.* The weight condition at a closed point $z$ uses only
$q_z=\#\kappa(z)$, not the base field. For the fibre
$X_y\hookrightarrow X_0$ over a closed point $y$ of a base, with
$[\kappa(y):k_0]=m$, the inclusion is a closed immersion.
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
