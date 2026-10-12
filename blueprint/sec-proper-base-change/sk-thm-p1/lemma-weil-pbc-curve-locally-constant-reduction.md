+++
id = "lemma-weil-pbc-curve-locally-constant-reduction"
kind = "lemma"
title = "Locally constant sheaf reduction"
order = 1184
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-finite-l-group-filtration", "lemma-weil-pbc-finite-stalk-formula", "thm-galois-lc-etale"]
+++
Let $U$ be irreducible and let $G$ be a finite locally constant sheaf of
$\mathbf F_\ell$-vector spaces on $U_{\Et}$. There is a connected finite
etale $v:V\to U$ of degree prime to $\ell$ such that $v^{-1}G$ has a
filtration by subsheaves with constant $\mathbf F_\ell$-quotients. The
adjunction unit and the trace satisfy

$$
 G\xrightarrow{\eta}v_*v^{-1}G
 \xrightarrow{\operatorname{tr}}G
   =\deg(v)\operatorname{id}_G,
$$

so $G$ is a direct summand of $v_*v^{-1}G$.
