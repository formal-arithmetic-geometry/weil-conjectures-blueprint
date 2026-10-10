+++
kind  = "proof"
of    = "lem-trf-open-tensor"
+++
For sheaves, internal Hom restricts to internal Hom on an open
localized site: on any object over $U$, both are morphisms on the
same slice site. Tensor–Hom adjunction and $j_!\dashv j^*$ of
[def-weil-extension-by-zero] give, for sheaves $P,M,N$,

$$
\begin{aligned}
\operatorname{Hom}(j_!P\otimes_A M,N)
&\simeq\operatorname{Hom}(P,j^*\mathcal Hom_A(M,N))\\
&\simeq\operatorname{Hom}(P,\mathcal Hom_A(j^*M,j^*N))\\
&\simeq\operatorname{Hom}(j_!(P\otimes_Aj^*M),N).
\end{aligned}
$$

Yoneda gives the underived tensor identity and its naturality.

Choose a K-flat representative $P^\bullet$ for $K$ as in
[def-weil-derived-tensor]. The same identity on complexes
shows that $j_!P^\bullet$ is K-flat. Indeed, for an acyclic
$Q^\bullet$, $j^*Q^\bullet$ is acyclic because inverse image is
exact ([def-weil-derived-pullback-tensor-hom]), so
$P^\bullet\otimes_Aj^*Q^\bullet$ and its exact extension by zero
are acyclic. Extension by zero commutes with direct sums, being a
left adjoint, and therefore commutes with the direct-sum
totalization of the tensor complex. The underived identity on
these representatives is the required derived identity.
