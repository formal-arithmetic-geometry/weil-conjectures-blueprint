+++
kind = "proof"
of = "det-sp-generic-divisor-constant"
uses = ["det-sp-thick-origin", "det-sp-defect-proper-smooth", "det-sp-defect-closed-vanishing"]
+++
The question is local at $\zeta$, and the smooth case of [det-sp-defect-proper-smooth] for open
immersions lets us shrink $X$; discard the other irreducible components of $X$ and $Z$. Normality
makes $X$ regular in codimension one, so the local ring at $\zeta$ is a discrete valuation ring.
After shrinking around $\zeta$, both $X$ and $Z_{\mathrm{red}}$ are smooth over $k$, and a local
equation $h$ of $Z_{\mathrm{red}}$ defines a smooth map $h\colon X\to\mathbf A^1$. In the discrete
valuation ring at $\zeta$ the defining equation of $Z$ has some order $m\geq1$, and its remaining
factor is a unit after shrinking. So on a further neighbourhood the ideal of $Z$ is $(h^m)$, that
is, $Z=h^{-1}V(x^m)$ schematically.

The smooth case of [det-sp-defect-proper-smooth] for $h$ and [det-sp-thick-origin] give

$$
C_{X,Z}(M_X)=C_{X,Z}(h^*M_{\mathbf A^1})\simeq h_Z^*C_{\mathbf A^1,V(x^m)}(M_{\mathbf A^1})=0
$$

there. Since $j_!j^*M_X=j_!M_U$, [det-sp-defect-closed-vanishing] gives
$C_{X,Z}(j_!M_U)\simeq C_{X,Z}(M_X)=0$ on the same neighbourhood.
