+++
kind  = "proof"
of    = "cor-wf-rank-one-punctual-purity-curve"
+++
Let $x\in|U_0|$ be closed and set
$d=[\kappa(x):\mathbf F_q]$. The local geometric-Frobenius operator of
[def-weil-local-frobenius-trace] is represented in the Weil group by
a conjugacy class $F_x$ of degree $d$ [p-real-operations], with degree as in
[def-wf-weil-group]. Because $\chi$ is one-dimensional, its value
on this class is well defined. The factorization of
[cor-wf-rank-one-degree-factorization-curve] gives its unique stalk
eigenvalue as

$$
\alpha_x=\chi(F_x)=\varepsilon(F_x)c^d.
$$

The character $\varepsilon$ has finite image, so
$\varepsilon(F_x)$ is a root of unity. By
[lem-tw-root-of-unity-modulus],
$|\iota(\varepsilon(F_x))|=1$. Therefore

$$
|\iota(\alpha_x)|=|\iota(c)|^d
=q^{d w_\iota(\chi)/2}
=|\kappa(x)|^{w_\iota(\chi)/2}.
$$

This is precisely the definition in [def-weil-punctual-weights].
If $s'=gs$ is another degree-one lift, then
$\chi(s')/\chi(s)=\chi(g)$ is a root of unity by
[thm-wf-rank-one-finite-geometric-image-curve]; hence its complex
modulus is one and the displayed weight does not depend on $s$.
