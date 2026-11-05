+++
kind = "proof"
of = "proposition-h-1-curve-tate-module"
order = 1569
uses = ["lemma-rigidification-along-section", "lemma-twisting-h-0-1-h"]
+++
The isomorphism comes from the Kummer sequence and the identification
of the preceding proposition. The point is that both are compatible with
the Galois action and with the transition maps. Then they pass to the
inverse limit.

We compute on the étale site and transport the result to the
pro-étale site by Theorem [theorem-bounded-below-cohomology-comparison].
Since that comparison is natural, it preserves all the maps and Galois
actions below. The Kummer sequence gives

$$
0\longrightarrow
H^0(C,\mathbf G_m)/\ell^n
\longrightarrow H^1(C,\mu_{\ell^n})
\longrightarrow\operatorname{Pic}(C)[\ell^n]
\longrightarrow0.
$$

The first term vanishes. Indeed, $C$ is proper and connected, so
$H^0(C,\mathbf G_m)=\bar k^{\times}$, and this group is divisible. For the
last term, note that the degree map takes values in the torsion-free group $\mathbf Z$, so
$\operatorname{Pic}(C)[\ell^n]=\operatorname{Pic}^0(C)[\ell^n]$, and
Proposition [proposition-jacobian-over-ground-field] identifies this
group with $J_0[\ell^n](\bar k)$. It remains to check Galois equivariance. The map induced by
$\mu_{\ell^n}\to\mathbf G_m$ and the identification of
Proposition [proposition-jacobian-over-ground-field] are natural in the
curve and in the field, and hence Galois-equivariant.

To check the transition maps, we map the Kummer sequence for
$\ell^{n+1}$ to that for $\ell^n$ by $[\ell]$ on the first
$\mathbf G_m$ and by the identity on the second. On the kernels this is
$z\mapsto z^\ell$. On the Picard group it sends an invertible sheaf
to its $\ell$-th tensor power, which is $[\ell]$ on $J_0$. Therefore the
displayed isomorphisms identify the two inverse systems, including
their transition maps.
