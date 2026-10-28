+++
kind = "proof"
of = "sk-thm-iff"
uses = ["sk-def-exchange", "sk-thm-acyclicity", "sk-prop-pbc-degree-zero"]
+++
*(1) implies (2)* by placing $F$ in degree zero.

*(2) implies (3).* Suppose (2) holds and $I$ is an injective object of the
category of sheaves of $\Lambda$-modules. Then $Rf_*I=f_*I$ in
$D^+(Y_{\Et},\Lambda)$, so $R^qf_*I=0$ for $q>0$. Since $I$ is torsion, (2)
applies to it and gives $R^qf'_*g'^{-1}I\simeq g^{-1}R^qf_*I=0$ for $q>0$.
This proves (3).

*(3) implies (2).* Assume (3), and let $F$ be a sheaf of $\Lambda$-modules.
Choose an injective resolution $F\to I^\bullet$ in the category of sheaves of
$\Lambda$-modules. Its terms are torsion, since $\Lambda$ is. Exactness of
$g'^{-1}$ makes $g'^{-1}I^\bullet$ a resolution of $g'^{-1}F$, and (3) makes
its terms $f'_*$-acyclic. [sk-thm-acyclicity] therefore identifies
$f'_*g'^{-1}I^\bullet$ with $Rf'_*g'^{-1}F$. The complex $g^{-1}f_*I^\bullet$
computes $g^{-1}Rf_*F$ because inverse image is exact.
[sk-prop-pbc-degree-zero] gives an isomorphism

$$
g^{-1}f_*I^m\xrightarrow{\ \sim\ }f'_*g'^{-1}I^m
$$

in each degree. Naturality makes these into an isomorphism of complexes. The
resolution formula of [sk-def-exchange] identifies that isomorphism with the
derived exchange map for $F$ in $D^+(Y'_{\Et},\Lambda)$. This proves (2).

*(2) implies (1).* Let $K\in D^+(X_{\Et},\Lambda)$. If $K$ is bounded,
induction on its cohomological length using the canonical truncation
triangles and (2) proves that its exchange map is an isomorphism. In general
fix a degree $m$ and choose $N\geq m$. The complex $\tau_{\leq N}K$ is
bounded and has the desired comparison. Both functors $g^{-1}Rf_*$ and
$Rf'_*g'^{-1}$ send $D^{\geq N+1}(X_{\Et},\Lambda)$ into
$D^{\geq N+1}(Y'_{\Et},\Lambda)$, since inverse images are exact and derived
direct images are left $t$-exact. Applying them to

$$
\tau_{\leq N}K\longrightarrow K\longrightarrow\tau_{\geq N+1}K
\xrightarrow{+1}
$$

shows that comparison for $K$ in degree $m$ is the comparison for
$\tau_{\leq N}K$. It is an isomorphism. Since $m$ was arbitrary, (1)
follows.
