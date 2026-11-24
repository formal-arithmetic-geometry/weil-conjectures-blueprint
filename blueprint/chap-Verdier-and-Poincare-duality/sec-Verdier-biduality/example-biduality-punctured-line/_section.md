+++
id = "example-biduality-punctured-line"
kind = "example"
title = "The dual of $j_!\\Lambda$ on the line"
order = 834
+++
Let $k$ be algebraically closed, $X=\mathbf A^1_k$, $i:0\to X$ the origin and
$j:U=\mathbf G_{m,k}\to X$ its complement, and take $\Lambda$ finite. The
sheaf $j_!\Lambda_U$ has stalk zero at $0$, but its dual does not. By
(10.3) for $j$ and $\href{@definition-verdier-dual-evaluation}{\omega_U}=\href{@definition-tate-twists}{\Lambda_U(1)}[2]$,

$$
\href{@definition-verdier-dual-evaluation}{\mathbb D_X(j_!\Lambda_U)}\simeq Rj_*\href{@definition-verdier-dual-evaluation}{\mathbb D_U\Lambda_U}
=Rj_*\href{@definition-tate-twists}{\Lambda_U(1)}[2],
$$

and by Example [example-closed-support] its stalk at $0$ is [$\Lambda(1)$](@definition-tate-twists)
in degree $-2$ and $\Lambda$ in degree $-1$. The term in degree $-1$ comes from
$R^1j_*\Lambda_U=i_*\href{@definition-tate-twists}{\Lambda(-1)}$. The same answer comes out of the triangle
$j_!\Lambda_U\to\Lambda_X\to i_*\Lambda\to$. Dualizing it, with
$\href{@definition-verdier-dual-evaluation}{\mathbb D_X\Lambda_X}=\href{@definition-tate-twists}{\Lambda_X(1)}[2]$ and
$\href{@definition-verdier-dual-evaluation}{\mathbb D_X(i_*\Lambda)}=i_*\href{@definition-verdier-dual-evaluation}{\mathbb D_0\Lambda}=i_*\Lambda$, gives a triangle

$$
i_*\Lambda\longrightarrow\href{@definition-tate-twists}{\Lambda_X(1)}[2]\longrightarrow
\href{@definition-verdier-dual-evaluation}{\mathbb D_X(j_!\Lambda_U)}\longrightarrow.
$$

On stalks at $0$ the first map, from degree $0$ to degree $-2$, is zero.
Hence the cone has [$\Lambda(1)$](@definition-tate-twists) in degree $-2$ and $\Lambda$ in degree $-1$.

Dualizing once more, [biduality](@theorem-verdier-biduality) predicts $\href{@definition-verdier-dual-evaluation}{\mathbb D_X}\href{@definition-verdier-dual-evaluation}{\mathbb D_X(j_!\Lambda_U)}
\simeq j_!\Lambda_U$, with zero stalk at $0$. In other words, the second dual
cancels the stalk that the first created. Here this follows from the two easy
cases. The map [$\delta$](@definition-verdier-dual-evaluation) is a morphism of triangles, and it is an isomorphism on $\Lambda_X$ and on $i_*\Lambda$, so by the five lemma it is an isomorphism on
$j_!\Lambda_U$. The argument used, however, that $\Lambda_U$ extends to the locally constant sheaf $\Lambda_X$. A locally constant $L$ on $U$ with nontrivial monodromy around $0$ has no such extension, and that is the case which needs the henselian
disc.
