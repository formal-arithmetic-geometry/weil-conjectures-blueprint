+++
kind = "proof"
of = "sk-prop-curve-artin-schreier"
uses = ["sk-prop-sf-comparison", "sk-thm-br", "sk-thm-curveestimate", "sk-prop-curve-affine-kummer"]
+++
Write also $\varphi$ for the endomorphism $a\mapsto a^p$ of the sheaf
$\mathbf G_a$ on $C_{\acute{e}t}$. The Artin–Schreier sequence

$$
0\longrightarrow\mathbf F_p\longrightarrow\mathbf G_a
\xrightarrow{\varphi-1}\mathbf G_a\longrightarrow0
$$

is exact, since surjectivity is a local question and $T^p-T-a$ has
derivative $-1$. The étale cohomology of $\mathbf G_a$ is the
coherent cohomology of $\mathcal O_C$, since quasi-coherent sheaves have the
same cohomology on the étale and on the Zariski site, by faithfully
flat descent on affine opens and the Čech resolution. Coherent
cohomology of the curve $C$ vanishes in degrees above one, and since $C$ is proper,
$H^1(C,\mathcal O_C)$ is a finite-dimensional $k$-vector space.

The cohomology sequence is then determined by the following fact from linear
algebra. Let $\varphi$ be a Frobenius-linear endomorphism of a
finite-dimensional $k$-vector space $V$. Then $\varphi-1$ is surjective and
its kernel is the set of $k$-points of a finite étale scheme of
order $p^f$ with $f\leq\dim_k V$. To see this, we reduce along a finite
filtration to the part where $\varphi$ is nilpotent and the part where $\varphi$ is
bijective. On the nilpotent part, $\varphi-1$ is an automorphism given by an
additive polynomial. On a bijective part of dimension $f$, we choose a
basis, invert the matrix of $\varphi$, and write the equations of the fibres as

$$
x_i^p-\sum_j b_{ij}x_j=c_i\qquad(1\leq i\leq f),
$$

where $(b_{ij})$ is invertible. The coordinate algebra is free of
dimension $p^f$, with basis the monomials having each exponent less
than $p$. Since $p=0$ in $k$, the Jacobian matrix of these equations
is $-(b_{ij})$, which is invertible. Hence each fibre is finite
étale of degree $p^f$ and has $p^f$ points over the algebraically
closed field $k$ [Stacks, Tag 0A3L](https://stacks.math.columbia.edu/tag/0A3L). In particular every fibre is nonempty,
so $\varphi-1$ is surjective, and the kernel has $p^f$ elements.

We apply this to $H^0(C,\mathcal O_C)=k$ and to $H^1(C,\mathcal O_C)$. In the long
exact sequence associated to the Artin–Schreier sequence, surjectivity
of $\varphi-1$ on $H^0$ gives $H^1(C,\mathbf F_p)=\ker(\varphi-1)$ on
$H^1(C,\mathcal O_C)$, with the bound on its dimension, and surjectivity on
$H^1$ together with $H^2(C,\mathcal O_C)=0$ gives $H^q(C,\mathbf F_p)=0$ for
$q>1$.
Under an extension $k'/k$, flat base change for coherent cohomology identifies the
vector space and its Frobenius-linear map with their scalar
extensions. The kernel is a finite étale scheme, whose $k$-points
and $k'$-points agree, and hence the pullback map is an isomorphism
[Stacks, Tag 0HAN](https://stacks.math.columbia.edu/tag/0HAN), [Stacks, Tag 0A3P](https://stacks.math.columbia.edu/tag/0A3P). By Theorem [sk-prop-sf-comparison],
the statement carries over to $C_{\mathrm{pro}\acute{e}t}$.
