+++
kind = "proof"
of = "det-thm-restriction-local"
+++
*Existence of charts.* $Y$ is quasi-compact, so it is covered by finitely
many affine opens $V_\beta$; each $f^{-1}(V_\beta)$ is quasi-compact and is
covered by finitely many affine opens $U_{\beta\alpha}$. Since $f$ is of finite
type, $\mathcal O(U_{\beta\alpha})$ is a finitely generated
$\mathcal O(V_\beta)$-algebra; a choice of $d$ generators gives a surjection
$\mathcal O(V_\beta)[t_1,\dots,t_d]\to\mathcal O(U_{\beta\alpha})$, i.e. a
closed immersion $U_{\beta\alpha}\hookrightarrow\mathbf A^d_{V_\beta}$ over
$V_\beta$.

*The factorization.* For an open immersion $w$, $Rw_!=w_!$ is left adjoint to
$w^*$ on the localizing categories, so $w^!\simeq w^*$. Using the composition
isomorphisms $(gh)^!\simeq h^!g^!$ of [sk-lem-sf-mate],

$$
u^*f^!\simeq u^!f^!\simeq(fu)^!=(vpi)^!\simeq i^!p^!v^!\simeq i^!p^!v^*.
$$

*Constructibility.* Let $K\in\Dbc(Y,\Lambda)$. Then $v^*K\in\Dbc(V,\Lambda)$.
By [sk-cor-affine-space-rational], $p^!v^*K\simeq p^*v^*K(d)[2d]$ lies in
$\Dbc(\mathbf A^d_V,\Lambda)$. By [sk-prop-closed-adjoint-constructible],
$i^!$ maps $\Dbc(\mathbf A^d_V,\Lambda)$ into $\Dbc(U,\Lambda)$. Hence
$u^*f^!K\in\Dbc(U,\Lambda)$.
