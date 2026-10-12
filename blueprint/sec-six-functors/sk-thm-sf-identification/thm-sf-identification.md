+++
id = "thm-sf-identification"
kind = "theorem"
title = "The pairing is the duality isomorphism"
order = 2526
uses = ["def-sf-cup", "def-sf-orientation", "def-sf-pairing", "def-sf-pf", "lem-sf-detection", "lem-sf-mate", "lem-sf-tensor-hom", "lem-sf-twist-interchange", "thm-sf-global-duality"]
+++
In the setting of [def-sf-pairing] — so $X$ satisfies the hypotheses of
[thm-sf-global-duality]: $X$ is proper, or $X=X_0\times_{k_0}k$ with $X_0$
smooth, separated of finite type and geometrically connected, and no
properness is required in the latter case — suppose in addition that $K$ is
perfect over $\Lambda_X$ and that the orientation of
[def-sf-orientation] is fixed. Then the tensor–internal-Hom adjoint of
$\beta_K$ is the canonical isomorphism

$$
b_K^\sharp:\ R\Gamma\bigl(X,K^\vee(d)\bigr)[2d]\xrightarrow{\ \sim\ }
R\operatorname{Hom}_\Lambda\bigl(R\Gamma_c(X,K),\Lambda\bigr)
$$

in the point category $D^b_c(s,\Lambda)$, and its inverse is the global
duality isomorphism of [thm-sf-global-duality] followed by the
identification $\mathbb D_XK\cong K^\vee(d)[2d]$ induced by the orientation.
In particular $\beta_K$ is perfect. If $X$ is proper and
$\Lambda\in\{A_{E,n},E,\overline{\mathbf Q}_\ell\}$, its degreewise form
gives perfect pairings

$$
\langle-,-\rangle_i:H_c^i(X,K)\times H^{2d-i}\bigl(X,K^\vee(d)\bigr)
\longrightarrow\Lambda\qquad(i\in\mathbf Z),
$$

the line-valued form being $H_c^i(X,K)\times H^{2d-i}(X,K^\vee)\to \Lambda(-d)$.
