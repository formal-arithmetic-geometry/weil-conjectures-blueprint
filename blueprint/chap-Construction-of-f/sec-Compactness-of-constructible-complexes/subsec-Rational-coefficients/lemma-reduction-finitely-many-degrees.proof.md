+++
kind = "proof"
of = "lemma-reduction-finitely-many-degrees"
order = 459
uses = ["theorem-enough-affine-weakly-contractible-objects", "proposition-exact-products", "corollary-ind-heart-b"]
+++
Cutting off the cohomology above degree $m$ is harmless for degree
reasons alone. To remove the cohomology below degree $m-d_C$ we use the
uniform bound: for bounded $K$ it kills the tail layer by layer, and for $K$ unbounded below we
write $K$ as the derived limit of its truncations and control the
resulting $\varprojlim^1$ term.

Replacing $K$ by $K[m]$, we may assume $m=0$. The truncation
$\tau_{>0}K$ lies in $D^{\geq1}$, and $C$ is a sheaf in degree $0$, so
there are no nonzero maps from $C$ to an object of $D^{\geq1}$. Hence
$\Hom(C,\tau_{>0}K[s])=0$ for
$s=0,-1$. In the long exact sequence of $\Hom(C,-)$ for the truncation
triangle $\tau_{\leq0}K\to K\to\tau_{>0}K\to$, these are the two groups
adjacent to $\Hom(C,K)$, and so
$\Hom(C,K)=\Hom(C,\tau_{\leq0}K)$. To remove the cohomology
in degrees $\leq-d_C-1$ from $K'=\tau_{\leq0}K$, we use the triangle
$\tau_{\leq-d_C-1}K'\to K'\to\tau_{\geq-d_C}K'\to$. It suffices to show that

$$
\Hom(C,L)=0\qquad
\text{for every }L\in\Dic(X,\Lambda)\text{ with }H^q(L)=0\text{ for }q>-d_C-1,
\tag{5.4}
$$

applied to $L=\tau_{\leq-d_C-1}K'$ and to $L=\tau_{\leq-d_C-1}K'[1]$.

We first prove (5.4) for bounded $L$. Such
an $L$ is a finite extension of its shifted cohomology
sheaves $H^q(L)[-q]$, and by the long exact Hom sequences it suffices
to show that each of them receives no nonzero map from $C$. A layer
$H^q(L)[-q]$ with $q\leq-d_C-1$ contributes
$\Hom(C,H^q(L)[-q])=\Ext^{-q}(C,H^qL)$. Since $-q>d_C$ and $H^q(L)$ is
ind-constructible, this group vanishes by
Corollary [corollary-ind-heart-b]. For $L$ unbounded
below we cannot argue in finitely many steps, and we use instead that
the derived category is left complete.

The pro-étale site has a basis of weakly contractible objects
(Theorem [theorem-enough-affine-weakly-contractible-objects]). For
this reason
Proposition [proposition-exact-products] applies: products of $\Lambda_X$-modules are
exact, products in $D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ are computed termwise, and

$$
L=R\varprojlim_n\tau_{\geq-n}L
$$

for every $L$. Concretely, if $L^\bullet$ is a complex representing $L$,
the limit is the derived inverse limit of the tower of good truncations
$\tau_{\geq-n}L^\bullet$ with their canonical transition maps. Since $\Hom(C,-)$ takes
products to products, the triangle defining $R\varprojlim$ yields the
Milnor exact sequence

$$
0\longrightarrow\varprojlim_n{}^1
\Hom(C,\tau_{\geq-n}L[-1])
\longrightarrow\Hom(C,L)
\longrightarrow\varprojlim_n\Hom(C,\tau_{\geq-n}L)
\longrightarrow0.
$$

Each $\tau_{\geq-n}L$ is bounded with cohomology in degrees $\leq-d_C-1$,
and hence the right-hand term vanishes by the bounded case. For the left-hand
term, the triangle

$$
H^{-n-1}(L)[n+1]\longrightarrow \tau_{\geq-n-1}L
\longrightarrow \tau_{\geq-n}L\longrightarrow H^{-n-1}(L)[n+2]
$$

gives an exact sequence

$$
\Ext^{n}(C,H^{-n-1}L)\to\Hom(C,\tau_{\geq-n-1}L[-1])\to\Hom(C,\tau_{\geq-n}L[-1])
\to\Ext^{n+1}(C,H^{-n-1}L).
$$

The outer terms vanish for $n>d_C$ by Corollary [corollary-ind-heart-b].
The transition maps are therefore isomorphisms for $n>d_C$, so the tower is
eventually constant and its $\varprojlim^1$ vanishes. This proves
(5.4).
