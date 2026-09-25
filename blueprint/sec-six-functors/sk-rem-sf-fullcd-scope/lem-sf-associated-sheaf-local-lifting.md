+++
id = "lem-sf-associated-sheaf-local-lifting"
kind = "lemma"
title = "Sections of an associated sheaf lift locally"
order = 2150
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site"]
+++
Let $P$ be a presheaf of $A$-modules on the
small étale site of a scheme $T$, that
is, on the site of [def-weil-pbc-etale-site], let
$P^{\#}$ be its associated sheaf and let $s\in P^{\#}(U)$ be a section over
an étale $U\to T$. Then there are an étale covering
$\lbrace U_i\to U\rbrace$ and elements $s_i\in P(U_i)$ with

$$
s|_{U_i}=\operatorname{im}(s_i)\qquad\text{in }P^{\#}(U_i)
$$

for every $i$, the map $P\to P^{\#}$ being the canonical one.

## Proof

The associated sheaf is produced from $P$ by the two-step plus construction

$$
P\longrightarrow P^{+}\longrightarrow P^{\#}=(P^{+})^{+},
$$

in which $P^{+}(U)$ is the set of equivalence classes of matching families in
$P$ over étale coverings of $U$, two families being equivalent when they
agree on a common refinement; the plus construction is the usual one attached
to the sheaf axiom of [def-weil-pbc-etale-sheaves], and $P^{\#}$ is a
sheaf.

Let $s\in P^{\#}(U)$ be given. It is the class of a matching family
$(t_j)$ over an étale covering $\lbrace U_j\to U\rbrace$ with
$t_j\in P^{+}(U_j)$, and the restriction of $s$ to $U_j$ is the image of
$t_j$ under $P^{+}\to(P^{+})^{+}$. Indeed, the restriction of the class of
a matching family over $\lbrace U_j\to U\rbrace$ to $U_j$ is represented by
the restricted family over the covering
$\lbrace U_j\times_UU_{j'}\to U_j\rbrace$ of $U_j$, and that family agrees on
this covering with the family whose member over $U_j$ is $t_j$, because the
original family is matching; two matching families that agree on a common
refinement represent the same element of $P^{+}(U_j)$.
Each $t_j\in P^{+}(U_j)$ is in turn the class of a matching family
$(s_{jk})$ over an étale covering $\lbrace U_{jk}\to U_j\rbrace$ with
$s_{jk}\in P(U_{jk})$, and the same argument shows that the image of
$t_j$ in $(P^{+})^{+}$ over $U_{jk}$ is the image of $s_{jk}$ under
$P\to P^{\#}$. Composing the two coverings gives an étale covering
$\lbrace U_{jk}\to U\rbrace$ with

$$
s|_{U_{jk}}=\operatorname{im}(s_{jk})\qquad\text{in }P^{\#}(U_{jk}),
$$

which is the assertion. No flatness, quasi-compactness or finiteness is used,
so the argument applies to the étale site of an arbitrary scheme.
