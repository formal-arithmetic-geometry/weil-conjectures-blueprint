+++
id = "example-internal-hom-affine-line"
kind = "example"
title = "Internal Hom on the affine line"
order = 627
+++
Over an algebraically closed $k$, let $j:U=\mathbf G_{m,k}\hookrightarrow
X=\mathbf A^1_k$ and let $i$ be the inclusion of the origin. The
[localization sequence](@proposition-extension-zero-restriction-closed-subscheme) $0\to j_!\Lambda_U\to\Lambda_X\to i_*\Lambda\to0$
shows that $\Lambda_X$ is built from $j_!\Lambda_U$ and $i_*\Lambda$, and the
formula above computes $\cHom$ out of each piece. By
Example [example-closed-support],

$$
\cHom(j_!\Lambda_U,\Lambda_X)=Rj_*\Lambda_U,
\qquad
\cHom(i_*\Lambda,\Lambda_X)=i_*\href{@theorem-existence-exceptional-inverse-image}{i^!\Lambda_X}\simeq i_*\href{@definition-tate-twists}{\Lambda(-1)}[-2].
$$

The first has $\mathcal H^0=\Lambda_X$ and $\mathcal H^1=i_*\href{@definition-tate-twists}{\Lambda(-1)}$. In
the second, the local Ext sheaves from the skyscraper sheaf $i_*\Lambda$ to
the constant sheaf vanish except in degree two. Both results are
[constructible](@definition-constructible-sheaves) but not [lisse](@definition-lisse-sheaves). The first is computed by a nonproper direct
image, and the second by [$i^!$](@theorem-existence-exceptional-inverse-image).
