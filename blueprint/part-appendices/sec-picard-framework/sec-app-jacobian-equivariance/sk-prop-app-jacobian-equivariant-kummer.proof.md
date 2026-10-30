+++
kind = "proof"
of = "sk-prop-app-jacobian-equivariant-kummer"
uses = ["sk-prop-sf-comparison", "sk-prop-jacobian-descent"]
+++
We compute on the étale site. The result is transported to the
pro-étale site by Theorem [sk-prop-sf-comparison], and
since that comparison is natural, it preserves all the maps and Galois
actions below. The Kummer sequence gives

$$
0\longrightarrow
H^0(C,\mathbf G_m)/\ell^n
\longrightarrow H^1(C,\mu_{\ell^n})
\longrightarrow\operatorname{Pic}(C)[\ell^n]
\longrightarrow0.
$$

The first term vanishes because
$H^0(C,\mathbf G_m)=\bar k^{\times}$ is divisible. Since the degree map
takes values in the torsion-free group $\mathbf Z$, we have
$\operatorname{Pic}(C)[\ell^n]=\operatorname{Pic}^0(C)[\ell^n]$, and
Proposition [sk-prop-jacobian-descent] identifies this
group with $J_0[\ell^n](\bar k)$. The map induced by
$\mu_{\ell^n}\to\mathbf G_m$ and the identification of
Proposition [sk-prop-jacobian-descent] are natural in the
curve and in the field, and hence Galois-equivariant.

To check the transition maps, we map the Kummer sequence for
$\ell^{n+1}$ to that for $\ell^n$ by $[\ell]$ on the first
$\mathbf G_m$ and by the identity on the second. On the kernels this is
$z\mapsto z^\ell$, and on the Picard group it sends an invertible sheaf
to its $\ell$-th tensor power, which is $[\ell]$ on $J_0$. Therefore the
displayed isomorphisms identify the two inverse systems, including
their transition maps.
