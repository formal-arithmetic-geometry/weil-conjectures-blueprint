+++
kind = "proof"
of = "det-sp-zero-section-vanishing"
uses = ["det-sp-defect-closed-vanishing", "det-sp-zero-section-cartier", "det-sp-defect-proper-smooth", "det-sp-zero-section-affine-space"]
+++
By [det-sp-defect-closed-vanishing], replace $L$ by $j_!j^*L$, so that $i^*L=0$. By
[det-sp-zero-section-cartier], $C_{X,Z}(L)\simeq Rb_{Z*}C_{X',b^{-1}Z}(b^*L)$ for the blow-up
$b\colon X'\to X$ along $Z$, and $b^{-1}Z$ is an effective Cartier divisor. So it suffices to treat
the case where $Z$ is an effective Cartier divisor.

The assertion is local: the smooth case of [det-sp-defect-proper-smooth] for open immersions
identifies the restriction of $C_{X,Z}(L)$ to an open $V\subset X$ with $C_{V,Z\cap V}(L|_V)$. Take
$X$ affine with $Z=V(h)$ for a function $h$. Choose algebra generators for $\mathcal O(X)$ and
append $h$ as the last coordinate. This gives a closed immersion

$$
a:X\hookrightarrow\mathbf A^n,\qquad Z=a^{-1}(\mathbf A^{n-1}\times\{0\})
$$

schematically. The proper case of [det-sp-defect-proper-smooth] gives
$C_{\mathbf A^n,\mathbf A^{n-1}\times\{0\}}(a_*L)\simeq a_{Z*}C_{X,Z}(L)$, the left side vanishes by
[det-sp-zero-section-affine-space], and the closed direct image $a_{Z*}$ is faithful. Hence
$C_{X,Z}(L)=0$.
