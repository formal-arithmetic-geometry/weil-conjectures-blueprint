+++
kind  = "proof"
of    = "lem-tw-punctual-rescaling"
+++
Let $z$ be a closed point of $X'_0$ and $x=\varphi(z)$, so that
$\kappa(x)\subseteq\kappa(z)$ are finite fields; put
$r=[\kappa(z):\kappa(x)]$, so $q_z=q_x^r$. The stalk of
$\varphi^*\mathcal F$ at a geometric point over $z$ is the stalk of
$\mathcal F$ at its image, and the local Frobenius of
$\varphi^*\mathcal F$ at $z$ is $F_x^r$. Every eigenvalue of $F_x^r$ is
of the form $\beta^r$ with $\beta$ an eigenvalue of $F_x$, and
$|\iota(\beta)|=q_x^{w/2}$ by [def-weil-punctual-weights] on $X_0$.
Consequently

$$
|\iota(\beta^r)|=q_x^{rw/2}=q_z^{w/2},
$$

which is the punctual weight condition at $z$.

In particular, let $h:X_0\to Y_0$ be a finite-type morphism of
finite-type $k_0$-schemes, let $y\in Y_0$ be a closed point with
$m=[\kappa(y):k_0]$, so $\kappa(y)\cong\mathbf F_{q^m}$, and set

$$
X_y:=X_0\times_{Y_0}\operatorname{Spec}\kappa(y).
$$

Applied to the closed immersion $X_y\hookrightarrow X_0$, a closed
point $z$ of $X_y$ is the same closed point on $X_0$, with the same
residue field and the same local Frobenius ($r=1$). If
$r'=[\kappa(z):\kappa(y)]$, then $q_z=q^{mr'}=(q^m)^{r'}$: residue
cardinalities do not depend on the base field. So the restriction
$\mathcal F|_{X_y}$ is punctually pure of weight $w$ relative to
$\kappa(y)$ as well.
