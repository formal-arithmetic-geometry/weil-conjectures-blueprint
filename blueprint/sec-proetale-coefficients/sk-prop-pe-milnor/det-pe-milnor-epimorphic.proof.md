+++
kind = "proof"
of = "det-pe-milnor-epimorphic"
+++
*1.* Let $W$ be an affine weakly contractible object. The maps $t_n(W)$ are surjective
([det-pe-wc-sections-exact], whose proof only uses that $W$ is weakly contractible), and
$(\prod_nM_n)(W)=\prod_nM_n(W)$, products of sheaves being computed sectionwise. Given
$(a_n)\in\prod_nM_n(W)$, put $m_0=0$ and choose recursively $m_{n+1}\in M_{n+1}(W)$ with
$t_n(m_{n+1})=m_n-a_n$. Then $((1-T)(m))_n=m_n-t_n(m_{n+1})=a_n$. So $1-T$ is surjective on
every such $W$, i.e. the sequence $\prod_nM_n\xrightarrow{1-T}\prod_nM_n\to0$ is exact on
every $W$, and [det-pe-sections-conservative] shows that $1-T$ is an epimorphism of sheaves.

*2.* In each degree $i$ the sequence
$0\to\varprojlim_nK_n^i\to\prod_nK_n^i\xrightarrow{1-T}\prod_nK_n^i\to0$ is exact: the first
map is a kernel of $1-T$ (a family is in the kernel iff it is compatible with the
transitions), and $1-T$ is an epimorphism by 1 applied to the tower $(K_n^i)_n$. So
$0\to\varprojlim_nK_n\to\prod_nK_n\xrightarrow{1-T}\prod_nK_n\to0$ is a short exact sequence
of complexes, and its associated distinguished triangle in $D(X_{\mathrm{proét}},\Lambda)$ is
the displayed one. Countable products of sheaves of $\Lambda$-modules are exact
([det-pe-products-exact]), so the termwise product $\prod_nK_n$ is the product in the derived
category and the triangle exhibits $\varprojlim_nK_n$ as a homotopy limit. For a tower of
sheaves in degree $0$ this identifies $\varprojlim_nM_n$ with $R\varprojlim_nM_n$; compare
[det-pe-milnor-sequence], 2, where $R^1\varprojlim_nM_n=\coker(1-T)=0$ by 1.
