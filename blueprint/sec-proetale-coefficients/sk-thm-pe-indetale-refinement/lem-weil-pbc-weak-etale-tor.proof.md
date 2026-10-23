+++
kind  = "proof"
of    = "lem-weil-pbc-weak-etale-tor"
+++
For $B$-modules $M,N$ we first show

$$
 \operatorname{Tor}^B_i(M,N)=
 B\otimes_{B\otimes_AB}\operatorname{Tor}^A_i(M,N).
$$

Take free $B$-module resolutions $P\to M$, $Q\to N$, in nonnegative
homological degrees. They are flat resolutions over $A$, by the flatness
condition in [def-weil-pbc-ind-etale-algebra]. The double complex
$P\otimes_AQ$ therefore computes $\operatorname{Tor}^A(M,N)$. The two factors
give it an action of $B\otimes_AB$. Tensoring over that ring with $B$ is
exact, by the other flatness condition. It commutes with homology and
identifies the double complex with $P\otimes_BQ$, which computes the left
side. This proves the formula. In 1, $\operatorname{Tor}^A_1$ vanishes
identically, hence so does $\operatorname{Tor}^B_1$, and every $B$-module is
flat. In 2, the hypothesis means $\operatorname{Tor}^A_2$ vanishes identically,
since $\operatorname{Tor}_2(M,A/I)=\operatorname{Tor}_1(M,I)$ and flatness of a
module is tested on finitely generated ideals; hence
$\operatorname{Tor}^B_2$ vanishes, and every finitely generated ideal of $B$ is
flat.
