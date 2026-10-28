+++
kind  = "proof"
of    = "sk-lem-walg-normal-commutator"
+++
Multiplication and inversion are continuous for the Zariski topology, so
the closure of a subgroup is a subgroup. Since $\pi_1(U)$ is normal in
$W(U_0)$, conjugation by $\rho(W(U_0))$ preserves $H$. The normalizer of a
closed subgroup is closed, and so conjugation by $G$ preserves $H$ as well.
Since $W(U_0)/\pi_1(U)\simeq\mathbf Z$ is abelian, commutators of elements
of $\rho(W(U_0))$ lie in $\rho(\pi_1(U))$, and the commutator map
$G\times G\to\GL(V)$ is continuous, so the same holds on the closures.

For the complement:

*Density and stabilizers.* In a basis adapted to a subspace, the
stabilizer is cut out by the vanishing of one matrix block, so it is
closed and its points are exactly the elements preserving the subspace.
Containing a Zariski-dense subgroup, it contains the closure; the reverse
implication is restriction. The closures are algebraic groups: for
$a\in\Gamma$ left translation preserves $\Gamma$, so $aK=K$; for fixed
$y\in K$ the condition $xy\in K$ is closed and contains $\Gamma$, hence
$K$, giving $KK\subseteq K$; inversion is the same argument. Since
$K\times K$ is reduced by [lem-wf-affine-product-reduced], the vanishing principle there
turns these pointwise inclusions into regular group operations, and the
group identities are inherited from matrices.

*Rationality of the operations.* For a subquotient $A/B$ with
$B\subseteq A$ invariant under a dense subgroup, both are invariant under
the closure by the previous paragraph. In a basis adapted to
$B\subseteq A\subseteq M$ the matrix of $r(g)$ is block upper triangular;
the diagonal block at $A/B$ has regular entries, as does the corresponding
block of $r(g^{-1})$, so the induced action is a regular map to the
general linear group of the subquotient. A direct sum is block diagonal in
the original entries. In the tensor basis the entries are the products
$a_{ij}b_{uv}$; in the exterior basis they are the corresponding minors,
polynomials in the original entries, and the inverse is given by the same
formulas at $g^{-1}$. The determinant is the top exterior power on a
one-dimensional space, hence a rational character.

*Normality and commutators on $R$-points.* Write $A=k[x_{ij},\det^{-1}]$
and, for a subgroup $\Gamma\subseteq\GL_n(k)$, $I_\Gamma\subseteq A$ for the
ideal of functions vanishing on $\Gamma$; by [d-monodromy],
$G=V(I_{\rho(W)})$ and $H=V(I_{\rho(P)})$, and $\rho(P)\subseteq\rho(W)$
gives $I_{\rho(W)}\subseteq I_{\rho(P)}$, i.e. $H(R)\subseteq G(R)$ for every
$k$-algebra $R$. The kernel $P$ of the degree map is normal, and since
$\mathbf Z$ is abelian the degree map kills commutators, so
$[\rho(W),\rho(W)]\subseteq\rho(P)$. We show: if $\Delta\subseteq\Gamma$
are subgroups of $\GL_n(k)$ with $[\Gamma,\Gamma]\subseteq\Delta$, then
$aba^{-1}b^{-1}\in V(I_\Delta)(R)$ for all $a,b\in V(I_\Gamma)(R)$ and all $R$.
Let $f\in I_\Delta$ and let $F\in A\otimes_kA$ be the function
$F(a,b)=f(aba^{-1}b^{-1})$; it vanishes on $\Gamma\times\Gamma$. In
$A\otimes_k(A/I_\Gamma)$ write $\bar F=\sum_i\varphi_i\otimes\bar\psi_i$ with
$\bar\psi_1,\ldots,\bar\psi_m$ linearly independent. As $I_\Gamma$ is the
ideal of $\Gamma$, $A/I_\Gamma$ embeds in the functions on $\Gamma$, so there
are $b_1,\ldots,b_m\in\Gamma$ with $(\psi_i(b_j))$ invertible. For each $j$,
$\sum_i\varphi_i\,\psi_i(b_j)=F(-,b_j)$ vanishes on $\Gamma$, so lies in
$I_\Gamma$; inverting the matrix gives $\varphi_i\in I_\Gamma$. Hence
$F\in I_\Gamma\otimes A+A\otimes I_\Gamma$, so $F(a,b)=0$ for
$a,b\in V(I_\Gamma)(R)$. Applied to $\Gamma=\rho(W)$, $\Delta=\rho(P)$ this is
the commutator assertion, and normality of $H(R)$ in $G(R)$ follows from
$ghg^{-1}=(ghg^{-1}h^{-1})h$.

*Commutators as group schemes and the derived subgroup.* Let
$H\subseteq G$ be closed subgroup schemes of $\GL_n$ such that the
commutators of $G(R)$ lie in $H(R)$ for every $R$. Take $R$ the
coordinate ring of $G\times G$ and $a,b\in G(R)$ the two projections: their
commutator lies in $H(R)$, i.e. the commutator morphism $G\times G\to G$
factors through $H$. The commutator of any two points $a,b:X\to G$ is the
composite of $(a,b):X\to G\times G$ with this morphism, so it factors
through $H$: $H$ contains the commutators of $G$ as group schemes, and
then $H$ is normal in $G$ by $ghg^{-1}=(ghg^{-1}h^{-1})h$. A morphism to
$G=V(I)$ factors through $V(J)$, $J\supseteq I$, if and only if $J$ maps to
zero; so if $V(J)$ and $V(J')$ contain the commutators of $G$, so does
$V(J+J')$, and the sum of all Hopf ideals $J\supseteq I$ with this property
is a Hopf ideal (the Hopf conditions are additive) cutting out the
smallest closed subgroup scheme $[G,G]$ containing the commutators of $G$.
Thus $H$ contains the commutators of $G$ if and only if
$H\supseteq[G,G]$. For the monodromy pair, the previous paragraph supplies
the hypothesis.
