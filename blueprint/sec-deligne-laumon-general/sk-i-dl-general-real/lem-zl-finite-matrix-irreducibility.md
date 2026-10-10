+++
id = "lem-zl-finite-matrix-irreducibility"
kind = "lemma"
title = "Absolute irreducibility has a finite matrix witness"
order = 2831
lean = ["Representation.exists_forall_isIrreducible_baseChange_of_congr"]
uses = ["lem-wf-schur-scalar", "p-real-integral"]
+++
Let $\mathcal O$ be a Noetherian local domain with maximal ideal
$\mathfrak m$ and fraction field $E$, and let $K\supseteq E$ be an
algebraically closed field. Let $\rho:\Pi\to\operatorname{GL}_E(V)$ be a
representation of a group $\Pi$ on an $n$-dimensional $E$-vector space
$V$, and let $b$ be a basis of $V$ in which every matrix $\rho(g)$ has
entries in $\mathcal O$. Assume that $V\otimes_E K$ is irreducible.
Then there is $N\geq1$ with the following property: if a subgroup
$\Pi'\subseteq\Pi$ contains, for every $g\in\Pi$, an element $h$ whose
matrix in $b$ is congruent to that of $g$ modulo $\mathfrak m^N$, then
$\Pi'$ acts absolutely irreducibly on $V$, i.e. $V\otimes_E K'$ is
irreducible under $\Pi'$ for every field $K'\supseteq E$.

## Proof

First recall the elementary matrix-algebra argument behind Burnside's
lemma. If a unital algebra $A\subset\operatorname{End}_k(W)$ acts
irreducibly on a finite-dimensional vector space over an algebraically
closed field, Schur's lemma [lem-wf-schur-scalar] says
$\operatorname{End}_A(W)=k$. For linearly independent
$w_1,\ldots,w_r$, induction on $r$ shows that
$A\to W^r$, $a\mapsto(aw_1,\ldots,aw_r)$, is onto.
For the induction, its image projects onto $W^{r-1}$. The kernel
in the last copy of $W$ is an $A$-submodule, hence is either
$W$ or zero. In the latter case the image is the graph of an
$A$-linear map $W^{r-1}\to W$; Schur's lemma makes that map
$(v_i)\mapsto\sum c_i v_i$. Applying it to the tuple furnished by
$1\in A$ contradicts the independence of the $w_i$.
Taking a basis of $W$ proves $A=\operatorname{End}_k(W)$.

Apply this to the span of $\rho(\Pi)$ after extending scalars from
$E$ to $K$: the $K$-span of the matrices $\rho(g)$ is all of
$\operatorname{End}_K(V\otimes_EK)$. Hence the $E$-span already has
dimension $n^2$, so choose $g_1,\ldots,g_{n^2}\in\Pi$ whose matrices
form an $E$-basis of $\operatorname{End}_E(V)$.

Write the matrices in the basis $b$; their entries lie in
$\mathcal O$. The determinant $\Delta$ of their $n^2$ vectorized
columns is a nonzero element of $\mathcal O$. Since $\mathcal O$ is a
Noetherian local domain, $\bigcap_N\mathfrak m^N=0$ by the Krull
intersection theorem, so choose $N\ge1$ with $\Delta\notin\mathfrak m^N$.
If $\Pi'$ is as in the statement, choose $h_j\in\Pi'$ whose matrices
are congruent to those of $g_j$ modulo $\mathfrak m^N$. Their column
determinant $\Delta'\in\mathcal O$ satisfies
$\Delta'\equiv\Delta\pmod{\mathfrak m^N}$, so $\Delta'\neq0$. Thus the
$E$-span of $\rho(\Pi')$ is again the whole matrix algebra. The same is
true after extending scalars to any field $K'\supseteq E$, which
excludes any nonzero proper $\Pi'$-invariant subspace of
$V\otimes_EK'$.

In the application, $E/\mathbf Q_\ell$ is finite, $\mathcal O=\mathcal O_E$,
and $\rho$ is a continuous representation of a profinite group.
Compactness of $\rho(\Pi)$ supplies a basis $b$ as required (as in
[p-real-integral]): for an initial lattice $L_0$, all its translates
lie in $\varpi_E^{-a}L_0$ for some $a$; their $\mathcal O_E$-span is a
finitely generated torsion-free module containing $L_0$, and hence is a
lattice $L$, stable under the whole group; take $b$ an
$\mathcal O_E$-basis of $L$. The congruence condition then says that
$\Pi'$ has the same image as $\Pi$ on $L/\varpi_E^NL$, and continuity
ensures that this reduction image is a finite quotient of $\Pi$.
