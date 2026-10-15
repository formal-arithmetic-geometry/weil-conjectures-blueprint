+++
kind = "proof"
of = "det-thm-int-restriction-glue"
+++
(1) Boundedness and constructibility of the reduction $M\otimes^{\mathbf L}\mathbf F_{E,X}$
are local for a finite open cover, exactly as in the rational case
([det-thm-restriction-glue](1)), since restriction commutes with reduction.
Derived completeness is local: let
$C=\operatorname{cone}(M\to R\varprojlim_n M\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$.
Restriction $u_\alpha^*$ to an open is exact, commutes with reduction modulo
$\pi_E^n$ and with $R\varprojlim$ (it has an exact left adjoint
$u_{\alpha!}$, so it preserves K-injectives, and it commutes with products).
So $u_\alpha^*C$ is the corresponding cone for $M|_{U_\alpha}$, which is zero.
Restrictions to the members of an open cover are jointly conservative, so
$C=0$ and $M$ is derived complete.

(2) As in [det-thm-restriction-local], choose finitely many affine opens
$v:V\hookrightarrow Y$, $u:U\hookrightarrow X$ with $f(U)\subset V$ covering $X$
and closed immersions $i:U\hookrightarrow\mathbf A^d_V$ over $V$, with
$p:\mathbf A^d_V\to V$. Compatibility of compactly supported direct images
with composition and uniqueness of right adjoints give $u^!\simeq u^*$ for
open immersions and $u^*f^!\simeq i^!p^!v^*$ as functors
$\Loc(\Dbc(Y,\mathcal O_E))\to\Loc(\Dbc(U,\mathcal O_E))$. For
$K\in\Dbc(Y,\mathcal O_E)$: $v^*K\in\Dbc$; $p^!v^*K\in\Dbc$ by
[det-thm-int-restriction-line]; $i^!p^!v^*K\in\Dbc$ by
[det-thm-int-restriction-closed]. So $u^*f^!K\in\Dbc(U,\mathcal O_E)$ on each
member of the cover, and $f^!K\in\Dbc(X,\mathcal O_E)$ by (1). Finally
$Rf_!$ maps $\Dbc(X,\mathcal O_E)$ into $\Dbc(Y,\mathcal O_E)$
([sk-prop-int-brown]), and the inclusions
$\Dbc(-,\mathcal O_E)\subset\Loc(\Dbc(-,\mathcal O_E))$ are full, so the Hom
bijections of the adjunction restrict.
