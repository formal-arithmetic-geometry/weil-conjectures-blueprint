+++
kind  = "proof"
of    = "lem-trf-exceptional-internal-hom-exchange"
+++
By the stratified internal-Hom preservation
[det-thm-sf-ctf-stability-internal-hom], whose proof does not use biduality,
$R\mathcal Hom_A(c^*M,c^!N)$ and $R\mathcal Hom_A(M,N)$ lie in
$D^b_{ctf}$, so $c^!R\mathcal Hom_A(M,N)$ is defined by the constructible
Brown adjunction $c_!\dashv c^!$ of [sk-thm-existence]. Test only against
$P\in D^b_{ctf}(C,A)$, or the established localizing category. The
tensor–internal-Hom adjunction of [def-weil-derived-pullback-tensor-hom], the
Brown adjunction and the earlier projection formula [sk-thm-sf-pf-proetale]
give the chain

$$
\begin{aligned}
\operatorname{Hom}_C\bigl(P,R\mathcal Hom_A(c^*M,c^!N)\bigr)
&\cong\operatorname{Hom}_Z\bigl(c_!\bigl(P\otimes_A^Lc^*M\bigr),N\bigr)\\
&\cong\operatorname{Hom}_Z\bigl(c_!P\otimes_A^LM,N\bigr)\\
&\cong\operatorname{Hom}_C\bigl(P,c^!R\mathcal Hom_A(M,N)\bigr).
\end{aligned}
$$

Every arrow is natural in $P$, so the Yoneda lemma gives an isomorphism, and
it is the canonical comparison defined by evaluation and the counit.
Naturality in $M$ and $N$, and compatibility with shifts and distinguished
triangles, are the corresponding properties of the adjunctions and of the
projection formula.
