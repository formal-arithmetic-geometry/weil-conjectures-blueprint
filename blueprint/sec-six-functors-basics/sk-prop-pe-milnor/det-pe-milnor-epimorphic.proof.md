+++
kind = "proof"
of = "det-pe-milnor-epimorphic"
+++
Let $W$ be an affine weakly contractible object. The maps $t_n(W)$ are surjective (part 3 of
[det-pe-weak-contractible-equivalences]), and $(\prod_nM_n)(W)=\prod_nM_n(W)$
([det-pe-sections-limits-colimits]). Given $(a_n)\in\prod_nM_n(W)$, put $m_0=0$ and choose
recursively $m_{n+1}\in M_{n+1}(W)$ with $t_n(m_{n+1})=m_n-a_n$. Then
$((1-T)(m))_n=m_n-t_n(m_{n+1})=a_n$. So $1-T$ is surjective on every such $W$, i.e. the sequence
$\prod_nM_n\xrightarrow{1-T}\prod_nM_n\to0$ is exact on every $W$, and
[det-pe-sections-conservative] shows that $1-T$ is an epimorphism of sheaves. By [det-pe-milnor-sequence], 2,
$R^1\varprojlim_nM_n=\coker(1-T)=0$ and $R^p\varprojlim_nM_n=0$ for $p\neq0,1$, so
$R\varprojlim_nM_n$ has cohomology only in degree $0$, equal to $\varprojlim_nM_n$; the
inclusion of $\varprojlim_nM_n=\ker(1-T)$ in degree $0$ of the two-term complex is
therefore a quasi-isomorphism.
