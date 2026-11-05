+++
kind = "proof"
of = "proposition-milnor-sequence"
order = 92
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "theorem-existence-contractible-covers", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "corollary-evaluation-weakly-contractible-objects", "proposition-exact-products"]
+++
Everything follows from the triangle (2.1). Indeed, for a tower of
modules, $R\varprojlim_nM_n$ is the fibre of a map between two sheaves in
degree $0$, so it has cohomology only in degrees $0$ and $1$, namely the
kernel and the cokernel of $1-T$. Here the kernel is $\varprojlim_nM_n$, and
the cokernel is $R^1\varprojlim_nM_n$, which proves the first two
assertions. Similarly, for a tower of complexes, the long exact cohomology sequence
of (2.1) reads

$$
\prod_nH^{q-1}(K_n)\xrightarrow{1-T}\prod_nH^{q-1}(K_n)
\to H^q(R\varprojlim_nK_n)\to\prod_nH^q(K_n)\xrightarrow{1-T}\prod_nH^q(K_n),
$$

where we used that by Proposition [proposition-exact-products] the cohomology of each
product is the product of the cohomology sheaves. The cokernel on the left
is $R^1\varprojlim_nH^{q-1}(K_n)$ and the kernel on the right is
$\varprojlim_nH^q(K_n)$, which gives (2.2).

Suppose now that the transition maps of a tower of modules are
epimorphisms. We show that $1-T$ is an epimorphism; then
$R^1\varprojlim_nM_n=0$ and the derived limit is $\varprojlim_nM_n$. By
Corollary [corollary-evaluation-weakly-contractible-objects] it suffices to check surjectivity on sections
over every weakly contractible $W$, where the maps $t_n$ are surjective.
Given $(a_n)$, choose $m_0$ arbitrarily and then, recursively, $m_{n+1}$
with $t_n(m_{n+1})=m_n-a_n$. Then $(1-T)(m_n)_n=(a_n)_n$. See
[Stacks, [0947](https://stacks.math.columbia.edu/tag/0947)].
