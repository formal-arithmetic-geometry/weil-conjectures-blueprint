+++
kind = "proof"
of = "det-sp-zero-section-affine-space"
uses = ["det-sp-defect-closed-vanishing", "det-sp-generic-divisor", "det-sp-defect-proper-smooth", "det-sp-constant-family-conservative"]
+++
Induct on $n\geq1$. By [det-sp-defect-closed-vanishing] we may replace $L$ by $j_!j^*L$ and assume
$L|_Z=0$. The scheme $X$ is normal and $Z$ is a principal divisor, so [det-sp-generic-divisor]
shows that the closure $Y$ of the support of $C_{X,Z}(L)$ is a proper closed subset of the
hyperplane $Z$. For $n=1$ the hyperplane is a point, $Y$ is empty, and the assertion follows.

For $n>1$, choose a line $\lambda$ in the vector space $Z$ such that the linear projection
$q\colon X\to X'=X/\lambda\simeq\mathbf A^{n-1}$ is finite on $Y$. To see existence, choose the
projective point $\mathbf P(\lambda)$ outside the part at infinity of the projective closure of $Y$
in $\mathbf P(Z\oplus k)$; the projection is then finite on $Y$ by the usual proof of linear Noether
normalization. Set $Z'=Z/\lambda$, a coordinate hyperplane in $X'$, so that $Z=q^{-1}(Z')$.
Compactify the $\lambda$-direction:

$$
\bar q:\bar X=\mathbf P^1\times X'\longrightarrow X',\qquad
\bar Z=\bar q^{-1}(Z'),\qquad
v:X\hookrightarrow\bar X,\qquad \bar L=v_!L,
$$

and let $\bar q_Z\colon\bar Z\to Z'$ be the restriction of $\bar q$. Since $\bar q$ is proper and
$\bar Z=\bar q^{-1}(Z')$ schematically, the proper case of [det-sp-defect-proper-smooth] and the
induction hypothesis for $(X',Z')$ give

$$
R\bar q_{Z*}C_{\bar X,\bar Z}(\bar L)\simeq C_{X',Z'}(R\bar q_*\bar L)=0.
$$

The smooth case of [det-sp-defect-proper-smooth] for the open immersion $v$ identifies the
restriction of $C_{\bar X,\bar Z}(\bar L)$ to $Z$ with $C_{X,Z}(L)$. Hence
$C_{\bar X,\bar Z}(\bar L)$ is supported on $Y\cup(\bar Z\setminus Z)$. This closed subset is finite
over $Z'$: $Y$ is finite over $Z'$ and therefore closed in $\bar Z$, and $\bar Z\setminus Z$ is the
infinity section of $\bar Z\to Z'$. By [det-sp-constant-family-conservative],
$C_{\bar X,\bar Z}(\bar L)=0$, and restriction to $Z$ gives $C_{X,Z}(L)=0$.
