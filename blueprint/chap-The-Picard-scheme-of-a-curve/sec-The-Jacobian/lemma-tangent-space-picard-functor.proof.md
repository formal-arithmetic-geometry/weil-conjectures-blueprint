+++
kind = "proof"
of = "lemma-tangent-space-picard-functor"
order = 1551
+++
Because $\varepsilon^2=0$, the map $a\mapsto1+\varepsilon a$ is a homomorphism,
and it gives an exact sequence of sheaves of groups on $X$

$$
0\longrightarrow\mathcal O_X\longrightarrow
\mathcal O_{X_\varepsilon}^\times\longrightarrow\mathcal O_X^\times
\longrightarrow1,
$$

split by the inclusion $\mathcal O_X^\times\subset
\mathcal O_{X_\varepsilon}^\times$. The schemes $X$ and
$X_\varepsilon$ have the same underlying space, so
$\operatorname{Pic}(X_\varepsilon)=H^1(X,\mathcal O_{X_\varepsilon}^\times)$.
Since the sequence is split, taking $H^1$ gives
$H^1(X,\mathcal O_{X_\varepsilon}^\times)=H^1(X,\mathcal O_X)\oplus\operatorname{Pic}(X)$,
in which the restriction map is the projection to the second summand.
Hence the kernel is $H^1(X,\mathcal O_X)$.
