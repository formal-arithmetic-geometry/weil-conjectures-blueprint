+++
id = "lem-weil-pbc-locally-constant-reduction"
kind = "lemma"
title = "Locally constant reduction and trace splitting"
order = 1710
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-r-group-filtration", "lem-weil-pbc-finite-stalk-formula"]
+++
Let $U$ be irreducible and let $G$ be a finite locally constant $\mathbf
F_r$-sheaf. There is a connected finite etale map $v:V\to U$ of degree prime
to $r$ such that $v^{-1}G$ has a filtration with constant $\mathbf
F_r$-quotients. The adjunction unit and trace satisfy

$$
 G\xrightarrow{\eta}v_*v^{-1}G
 \xrightarrow{\operatorname{tr}}G
   =\deg(v)\operatorname{id}_G,
$$

so $G$ is a direct summand of $v_*v^{-1}G$.

## Proof

Under the finite-etale correspondence, the finite locally constant $\mathbf
F_r$-sheaf $G$ on the irreducible $U$ corresponds to a finite etale
$U$-scheme, and the (profinite) monodromy group is the finite group $H$ acting
on the geometric stalk $G_{\bar u}$, acting through a finite quotient
associated with the correspondence. Let $H'$ be a Sylow $r$-subgroup of $H$,
of index prime to $r$, and let $v:V\to U$ be the corresponding connected
finite etale map of degree $[H:H']$; then the monodromy of $v^{-1}G$ is the
$r$-group $H'$, so the finite $r$-group filtration of
[lem-weil-pbc-finite-r-group-filtration] applied to the $H'$-module $G_{\bar
u}$ gives a filtration of $v^{-1}G$ with constant $\mathbf F_r$-quotients. At
a geometric point, the unit $G\to v_*v^{-1}G$ is the diagonal and the trace is
the sum over the finite fibre, by [lem-weil-pbc-finite-stalk-formula], so
their composite is $\deg(v)\operatorname{id}_G$ with
$\deg(v)\not\equiv0\pmod r$, and $G$ is a direct summand of $v_*v^{-1}G$.

Unresolved dependencies: lem:weil-pbc-finite-locally-constant-etale
