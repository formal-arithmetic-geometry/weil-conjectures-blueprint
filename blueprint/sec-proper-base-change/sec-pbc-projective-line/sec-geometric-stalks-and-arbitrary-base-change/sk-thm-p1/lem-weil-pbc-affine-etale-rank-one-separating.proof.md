+++
kind = "proof"
of = "lem-weil-pbc-affine-etale-rank-one-separating"
uses = ["def-weil-pbc-etale-sum-extension", "lem-weil-pbc-etale-inverse-image-restriction"]
+++
*Maps out of $G_U$.* For an affine etale $j_U:U\to X$, extension by zero is left adjoint to restriction to $U$ [def-weil-pbc-etale-sum-extension], restriction being the inverse image [lem-weil-pbc-etale-inverse-image-restriction], and the constant sheaf functor is left adjoint to global sections. Hence maps $G_U=j_{U!}\underline\Lambda_U\to F$ correspond, naturally in $F$, to $\Lambda$-linear maps $\Lambda\to F(U)$, i.e. to sections $x\in F(U)$ (the image of $1$). ([def-weil-pbc-etale-sum-extension], [lem-weil-pbc-etale-inverse-image-restriction]).

*Agreement on affine sections.* Suppose $f\circ h=g\circ h$ for all $U$ and all $h:G_U\to F$. For $x\in F(U)$ let $h_x$ correspond to $r\mapsto rx$; naturality of the correspondence shows that $f\circ h_x$ corresponds to $f_U(x)$, so $f_U(x)=g_U(x)$. Thus $f$ and $g$ agree on the sections over every affine object.

*All sections.* The affine etale objects are cover-dense in the small etale site (every etale $V\to X$ has a covering by affine opens, which are again etale over $X$). A section of a sheaf over $V$ is determined by its restrictions to such a covering, and $f$, $g$ commute with restrictions; so $f_V=g_V$ for all $V$ and $f=g$.
