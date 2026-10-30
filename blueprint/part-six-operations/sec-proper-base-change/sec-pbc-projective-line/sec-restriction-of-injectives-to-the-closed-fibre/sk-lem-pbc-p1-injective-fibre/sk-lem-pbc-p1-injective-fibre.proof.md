+++
kind = "proof"
of = "sk-lem-pbc-p1-injective-fibre"
uses = ["sk-thm-pbc-henselian-h0", "sk-lem-pbc-finite", "sk-rem-restriction-of-injectives-to-the-closed-fibre", "sk-rem-henselian-pairs-and-curves"]
+++
In degrees $q\geq2$ the claim follows from Gabber's theorem on
affine charts. In degree one, we lift classes to finite torsors over
$\mathbf P^1_R$, where they are killed by injectivity of $I$.

First consider an affine open $W=\operatorname{Spec}B$ of $\mathbf P^1_R$, and set
$J=\mathfrak mB$. The pair $(B,J)$ need not be henselian, so we pass
to its henselization $(B^h,JB^h)$. Then $B^h/JB^h=B/J$, and $B^h$ is the filtered colimit
of the étale $B$-algebras $B'$ equipped with
$B'/JB'\simeq B/J$. By Gabber's theorem (fact (i) above) and continuity of étale
cohomology we have

$$
H^q(W_0,I_0|_{W_0})
\simeq H^q(\operatorname{Spec}B^h,I|)
\simeq\varinjlim_{B'}H^q(\operatorname{Spec}B',I|).
\tag{4.10}
$$

The restriction of an injective sheaf to an étale object is injective,
because the restriction functor has an exact left adjoint, namely extension
by zero in the localized site. Thus every group on the right vanishes for
$q>0$.

The two standard affine charts $U,V\subset \mathbf P^1_R$ have affine intersection,
so by (4.10) the restriction of $I$
to each of $U_0$, $V_0$ and $(U\cap V)_0$ has no cohomology in positive
degrees. By the Mayer–Vietoris sequence on $\mathbf P^1_\kappa$, we
conclude that $H^q(\mathbf P^1_\kappa,I_0)=0$ for $q\geq2$. This is the case of two
charts in [Stacks, Tag 0A51](https://stacks.math.columbia.edu/tag/0A51). In degree one the same sequence only identifies
$H^1(\mathbf P^1_\kappa,I_0)$ with the cokernel of
$\Gamma(U_0,I_0)\oplus\Gamma(V_0,I_0)\to\Gamma((U\cap V)_0,I_0)$, and
nothing said so far shows that this cokernel vanishes.

It remains to treat a class $\xi\in H^1(\mathbf P^1_\kappa,I_0)$, and here we
follow [Stacks, Tag 0A5H](https://stacks.math.columbia.edu/tag/0A5H). Write $I$ as a filtered
colimit of constructible $\mathbf F_\ell$-sheaves. Pullback commutes with
this colimit, and so does $H^1$ on $\mathbf P^1_\kappa$, so $\xi$ is the image of a
class $\zeta\in H^1(\mathbf P^1_\kappa,G_0)$ for some constructible $G$ with a map
$G\to I$. Choose (4.8) and put
$P=\bigoplus_a(h_a)_*\underline{M_a}$. Since $I$ is injective, the map
$G\to I$ extends to $P\to I$. Let $\zeta'$ be the image of $\zeta$ in
$H^1(\mathbf P^1_\kappa,P_0)$.

By (4.9) and the Leray spectral sequence,

$$
H^1(\mathbf P^1_\kappa,P_0)
\simeq\bigoplus_a H^1((Y_a)_0,\underline{M_a}),\qquad
H^1(\mathbf P^1_R,P)\simeq\bigoplus_a H^1(Y_a,\underline{M_a}).
$$

Each $Y_a$ is proper over $R$, since it is finite over $\mathbf P^1_R$. Therefore,
by the comparison (4.7) for finite torsors, $\zeta'$
lifts to a class in $H^1(\mathbf P^1_R,P)$.
Its image in $H^1(\mathbf P^1_R,I)$ is zero because $I$ is injective. The commutative
square of restriction maps

$$
\begin{CD}
H^1(\mathbf P^1_R,P) @>>> H^1(\mathbf P^1_R,I)\\
@VVV @VVV\\
H^1(\mathbf P^1_\kappa,P_0) @>>> H^1(\mathbf P^1_\kappa,I_0)
\end{CD}
$$

shows that the image of $\zeta'$ in $H^1(\mathbf P^1_\kappa,I_0)$ is zero. Since
$G\to P\to I$ is the given map $G\to I$, this image is $\xi$, and hence
$\xi=0$.
