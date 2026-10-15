+++
kind = "proof"
of = "sk-lem-finite-window"
uses = ["sk-cor-ind-heart-ii", "sk-thm-pe-weakly-contractible-basis", "sk-prop-pe-products", "sk-prop-pe-left-complete", "sk-prop-pe-milnor"]
+++
Replacing $K$ by $K[m]$ we may assume $m=0$. The truncation $\tau_{>0}K$ lies in $\D^{\geq1}$, so
$\Hom(C,\tau_{>0}K[s])=0$ for $s=0,-1$, and the truncation triangle for $\tau_{\leq0}$ shows that
$\Hom(C,K)=\Hom(C,\tau_{\leq0}K)$. It remains to remove the cohomology in degrees $\leq-d_C-1$ from
$K'=\tau_{\leq0}K$. By the triangle $\tau_{\leq-d_C-1}K'\to K'\to\tau_{\geq-d_C}K'\to$, it suffices to
show the lower tail vanishing

$$
\Hom(C,L)=0\qquad\text{for every }L\in\Dic(X,\Lambda)\text{ with }H^q(L)=0\text{ for }q>-d_C-1,
$$

applied to $L=\tau_{\leq-d_C-1}K'$ and to $L=\tau_{\leq-d_C-1}K'[1]$ ([det-finite-window-reduction]).

If $L$ is bounded, the lower tail vanishing follows from the finite filtration of $L$ by its cohomology
sheaves: a layer $H^q(L)[-q]$ with $q\leq-d_C-1$ contributes $\Ext^{-q}(C,H^qL)$, which vanishes by
[sk-cor-ind-heart-ii] since $-q>d_C$ ([det-finite-window-bounded]). For $L$ unbounded below we use that
the derived category is left complete.

The pro-étale site has a basis of weakly contractible objects ([sk-thm-pe-weakly-contractible-basis]),
so [sk-prop-pe-products] shows that products of $\Lambda_X$-modules are exact, products in
$\D(X_{\mathrm{proét}},\Lambda)$ are computed termwise, and

$$
L=R\varprojlim_n\tau_{\geq-n}L
$$

for every $L$ ([sk-prop-pe-left-complete]). Concretely, choose a complex $L^\bullet$ representing $L$;
the limit is the derived inverse limit of the tower of good truncations $\tau_{\geq-n}L^\bullet$ with
their canonical transition maps. Since $\Hom(C,-)$ takes products to products, the triangle defining
$R\varprojlim$ gives the Milnor exact sequence

$$
0\longrightarrow\varprojlim_n{}^1\Hom(C,\tau_{\geq-n}L[-1])\longrightarrow\Hom(C,L)
\longrightarrow\varprojlim_n\Hom(C,\tau_{\geq-n}L)\longrightarrow0.
$$

Each $\tau_{\geq-n}L$ is bounded with cohomology in degrees $\leq-d_C-1$, so the right-hand term
vanishes by the bounded case. For the left-hand term, the triangle

$$
H^{-n-1}(L)[n+1]\longrightarrow\tau_{\geq-n-1}L\longrightarrow\tau_{\geq-n}L\longrightarrow H^{-n-1}(L)[n+2]
$$

shows that the transition map $\Hom(C,\tau_{\geq-n-1}L[-1])\to\Hom(C,\tau_{\geq-n}L[-1])$ sits between
$\Ext^{n}(C,H^{-n-1}L)$ and $\Ext^{n+1}(C,H^{-n-1}L)$. Both vanish for $n>d_C$ by [sk-cor-ind-heart-ii].
So the tower is eventually constant, and the $\varprojlim^1$ of an eventually constant tower is zero: in
the description of $\varprojlim^1$ as the cokernel of $1-\mathrm{shift}$ on the product, one solves the
equation successively along the constant tail and then along the finitely many earlier terms. This
proves the lower tail vanishing, and hence the lemma ([det-finite-window-unbounded]).
