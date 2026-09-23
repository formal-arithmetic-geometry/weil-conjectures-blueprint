+++
id = "lemma-weil-pbc-stein-connectedness"
kind = "lemma"
title = "Stein connectedness for $\\mathbf P^1_A$"
order = 1604
uses = ["def-weil-pbc-strict-henselian-setup", "lemma-weil-pbc-spectral-restriction"]
+++
Every irreducible closed subset of $X$ meets $X_0$ in a connected nonempty
set. Consequently $\Gamma(X,F)\xrightarrow{\sim}\Gamma(X_0,F_0)$ for every
Zariski sheaf $F$.

## Proof

Fix an irreducible closed subset and give it the reduced closed-subscheme
structure $C\subseteq X$. The map $C\to S$ is proper. Its Stein
factorization gives $C\xrightarrow{u}\operatorname{Spec}B \xrightarrow{v}S$, with $A\to B$ integral and $u$ having geometrically
connected fibres. Since $(A,\mathfrak m)$ is henselian,
$(B,\mathfrak mB)$ is a henselian pair. The image
$D=v(\operatorname{Spec}B)$ is irreducible and closed because $C\to S$ is
proper. Henselian connectedness makes $D\cap V(\mathfrak m)$ connected and
nonempty. The map
$C\cap X_0\to D\cap V(\mathfrak m)$ is closed and surjective with connected
fibres, so the closed-surjection connected-fibre criterion makes
$C\cap X_0$ connected. This expands Tag
`0A0B`; the final equality of sections is Lemma
[lemma-weil-pbc-spectral-restriction].
