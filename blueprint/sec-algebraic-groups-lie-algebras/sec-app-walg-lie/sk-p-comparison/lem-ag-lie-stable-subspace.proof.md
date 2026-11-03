+++
kind  = "proof"
of    = "lem-ag-lie-stable-subspace"
+++
*$G$ is of finite type and irreducible.* By Cartier's theorem
[lem-ag-cartier-reduced], $G$ is smooth over $L$, so its local rings are
regular, and by [lem-wf-smooth-components-disjoint], applied on affine
opens, distinct irreducible components of $G$ do not meet. In the locally
Noetherian scheme $G$ the irreducible components are locally finite;
being pairwise disjoint, each of them is therefore open and closed. As $G$
is connected, it is irreducible. Choose an affine open $U_0\ni1$. For
$g\in G(L)$ the opens $U_0$ and $gU_0^{-1}$ (translations and inversion
are automorphisms of the scheme $G$, [lem-sc-translation-automorphism])
are nonempty, hence dense, so they meet in a closed point, which is an
$L$-point ([lem-wf-affine-nullstellensatz-vanishing]); thus $g\in U_0U_0$.
The open set $W=\bigcup_{u\in U_0(L)}uU_0$ lies in the image of
$U_0\times_LU_0$ under multiplication and contains every $L$-point. Its
closed complement contains no closed point; since a nonempty closed
subset of a scheme locally of finite type over $L$ contains a closed
point, the complement is empty. Hence $G$ is the image of the
quasi-compact scheme $U_0\times_LU_0$, so $G$ is quasi-compact and of
finite type over $L$.

*The stabilizer.* Choose a basis of $M$ whose first $u=\dim U$ vectors
span $U$, and write $r$ in block form
$\begin{pmatrix}a&b\\c&d\end{pmatrix}$, with $c$ the lower-left
$(\dim M-u)\times u$ block, whose entries are regular functions on $G$.
Let $S\subseteq G$ be the closed subscheme where $c$ vanishes. Its
$R$-points, for a commutative $L$-algebra $R$, are the $g\in G(R)$ such
that $r(g)$ is block upper triangular. Block upper triangular invertible
matrices form a subgroup and $r$ is a homomorphism of group schemes, so
$S$ is a closed subgroup scheme of $G$. Its Lie algebra consists of the
$X\in\mathfrak g$ such that the dual-number point $1+\varepsilon X$ lies
in $S$, that is, such that the lower-left block of
$r(1+\varepsilon X)=1+\varepsilon\,dr(X)$ vanishes:

$$
\operatorname{Lie}(S)=\{X\in\mathfrak g:dr(X)U\subseteq U\}.
$$

If $dr(X)U\subseteq U$ for all $X$, then
$\operatorname{Lie}(S)=\mathfrak g$. By [lem-ag-cartier-reduced],
$\dim S=\dim\operatorname{Lie}(S)=\dim\mathfrak g=\dim G$, and
[lem-ag-equal-dimension-subgroup] gives $S=G$. Hence $r(g)U\subseteq U$
for every $g\in G(L)$. Conversely, if $r(g)U\subseteq U$ for every
$g\in G(L)$, then the closed subscheme $S$ contains every $L$-point of
$G$. The $L$-points are dense in $G$, and $G$ is reduced, so $S=G$; hence
$\operatorname{Lie}(S)=\mathfrak g$ and every $dr(X)$ preserves $U$.

*Complement.* A connected closed matrix group $H$ over $L$ is a connected
group scheme of finite type over $L$, its Lie algebra computed by dual
numbers is $\operatorname{Lie}(H)$ of [def-wf-lie-algebra-derivation],
and an algebraic-group module is a rational representation; so the
complement is a special case. In the matrix language, the closed
subgroup $S=\{g\in H:r(g)U\subseteq U\}$ is reduced by
[lem-ag-cartier-reduced], has Lie algebra
$\{X\in\mathfrak h:dr(X)U\subseteq U\}$, and
[lem-wf-same-lie-closed-subgroup] replaces the dimension count above.
