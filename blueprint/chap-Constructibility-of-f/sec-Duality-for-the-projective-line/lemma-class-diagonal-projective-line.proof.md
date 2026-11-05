+++
kind = "proof"
of = "lemma-class-diagonal-projective-line"
order = 552
+++
Let $x_0,x_1$ and $y_0,y_1$ be the pullbacks along $p_1$
and $p_2$ of the homogeneous coordinates of $\mathbf P^1_S$. Then
$\Delta$ is the zero locus of the section $x_0y_1-x_1y_0$ of
$p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)$. On the open where
$x_0$ and $y_0$ are invertible, in the affine coordinates
$x=x_1/x_0$ and $y=y_1/y_0$, this equation becomes $y-x$. It is a
nonzerodivisor, and the quotient
$\mathcal O_S[x,y]/(y-x)\simeq\mathcal O_S[x]$ is flat over $S$. The open
where $x_1$ and $y_1$ are invertible is treated in the same way, and these
two opens cover $\Delta$. Hence $\Delta$ is a relative effective Cartier
divisor, and it remains one after every base change.

To show $s_i=1$, note that both sides are endomorphisms of a sheaf
placed in degree zero. We have

$$
\Hom_{D((\mathbf P^1_S)_{\acute{e}t},A)}
(A_{\mathbf P^1_S},A_{\mathbf P^1_S})
=\Hom_{\operatorname{Mod}((\mathbf P^1_S)_{\acute{e}t},A)}
(A_{\mathbf P^1_S},A_{\mathbf P^1_S}),
$$

so $s_i$ is a morphism of sheaves and is determined by its geometric
stalks. By proper base change and the compatibility of $\delta$ and
$\operatorname{Tr}_{p_i}$ with base change, the stalk of (6.6) at a
geometric point $\bar x$ of $\mathbf P^1_S$ is computed on the fibre
$p_i^{-1}(\bar x)\simeq\mathbf P^1_{\bar x}$. On this fibre the equation $x_0y_1-x_1y_0$ restricts to a nonzero linear form, so the diagonal cuts out a single reduced point, whose line bundle is $\mathcal O(1)$.
By Lemma [lemma-cycle-class-cartier-divisor], the class of this point
composed with the unit is $c_1(\mathcal O(1))$. In turn, the trace $\operatorname{Tr}_p$ sends $c_1(\mathcal O(1))$ to $1$, since by
definition (6.5) it is the projection onto the summand of
(6.4) spanned by this class. Thus the stalk of $s_i$ at every
geometric point $\bar x$ sends $1$ to $1$, and so $s_i=1$.
