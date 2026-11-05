+++
id = "example-biduality-punctured-line"
kind = "example"
title = "The dual of $j_!\\Lambda$ on the line"
order = 833
+++
Let $k$ be algebraically closed, $X=\mathbf A^1_k$, $i:0\to X$ the origin and
$j:U=\mathbf G_{m,k}\to X$ its complement, and take $\Lambda$ finite. The
sheaf $j_!\Lambda_U$ has stalk zero at $0$, but its dual does not. By
(10.3) for $j$ and $\omega_U=\Lambda_U(1)[2]$,

$$
\mathbb D_X(j_!\Lambda_U)\simeq Rj_*\mathbb D_U\Lambda_U
=Rj_*\Lambda_U(1)[2],
$$

and by Example [example-closed-support] its stalk at $0$ is $\Lambda(1)$
in degree $-2$ and $\Lambda$ in degree $-1$. The term in degree $-1$ comes from
$R^1j_*\Lambda_U=i_*\Lambda(-1)$. The same answer comes out of the triangle
$j_!\Lambda_U\to\Lambda_X\to i_*\Lambda\to$. Dualizing it, with
$\mathbb D_X\Lambda_X=\Lambda_X(1)[2]$ and
$\mathbb D_X(i_*\Lambda)=i_*\mathbb D_0\Lambda=i_*\Lambda$, gives a triangle

$$
i_*\Lambda\longrightarrow\Lambda_X(1)[2]\longrightarrow
\mathbb D_X(j_!\Lambda_U)\longrightarrow.
$$

On stalks at $0$ the first map, from degree $0$ to degree $-2$, is zero.
Hence the cone has $\Lambda(1)$ in degree $-2$ and $\Lambda$ in degree $-1$.

Dualizing once more, biduality predicts $\mathbb D_X\mathbb D_X(j_!\Lambda_U)
\simeq j_!\Lambda_U$, with zero stalk at $0$. In other words, the second dual
cancels the stalk that the first created. Here this follows from the two easy
cases. The map $\delta$ is a morphism of triangles, and it is an isomorphism on $\Lambda_X$ and on $i_*\Lambda$, so by the five lemma it is an isomorphism on
$j_!\Lambda_U$. The argument used, however, that $\Lambda_U$ extends to the locally constant sheaf $\Lambda_X$. A locally constant $L$ on $U$ with nontrivial monodromy around $0$ has no such extension, and that is the case which needs the henselian
disc.
