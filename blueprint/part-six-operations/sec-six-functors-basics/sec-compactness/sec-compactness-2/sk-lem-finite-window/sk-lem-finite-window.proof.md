+++
kind = "proof"
of = "sk-lem-finite-window"
uses = ["sk-cor-ind-heart-ii", "sk-thm-pe-weakly-contractible-basis", "sk-prop-pe-products"]
+++
Replacing $K$ by $K[m]$, we may assume $m=0$. The truncation
$\tau_{>0}K$ lies in $D^{\geq1}$, so that $\Hom(C,\tau_{>0}K[s])=0$ for
$s=0,-1$. The truncation triangle for $\tau_{\leq0}$ then shows that
$\Hom(C,K)=\Hom(C,\tau_{\leq0}K)$. It remains to remove the cohomology
in degrees $\leq-d_C-1$ from $K'=\tau_{\leq0}K$. By the triangle
$\tau_{\leq-d_C-1}K'\to K'\to\tau_{\geq-d_C}K'\to$, it suffices to show that

$$
\Hom(C,L)=0\qquad
\text{for every }L\in\Dic(X,\Lambda)\text{ with }H^q(L)=0\text{ for }q>-d_C-1,
\tag{6.4}
$$

applied to $L=\tau_{\leq-d_C-1}K'$ and to $L=\tau_{\leq-d_C-1}K'[1]$.

If $L$ is bounded, (6.4) follows from the
finite filtration of $L$ by its cohomology sheaves, since a layer $H^q(L)[-q]$
with $q\leq-d_C-1$ contributes $\Ext^{-q}(C,H^qL)$, which vanishes by
Corollary [sk-cor-ind-heart-ii] since $-q>d_C$. For $L$ unbounded
below, we use that the derived category is left complete.

The pro-étale site has a basis of weakly contractible objects
(Theorem [sk-thm-pe-weakly-contractible-basis]), and hence
Proposition [sk-prop-pe-products] shows that products of $\Lambda_X$-modules are
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

The outer terms vanish for $n>d_C$ by Corollary [sk-cor-ind-heart-ii],
and so the transition maps are isomorphisms for $n>d_C$. Thus the tower is
eventually constant, and its $\varprojlim^1$ vanishes. This proves
(6.4), and hence the lemma.
