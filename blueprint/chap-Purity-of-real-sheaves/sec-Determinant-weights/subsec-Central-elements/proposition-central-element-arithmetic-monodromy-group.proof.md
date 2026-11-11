+++
kind = "proof"
of = "proposition-central-element-arithmetic-monodromy-group"
order = 1142
uses = ["lemma-identity-component"]
+++
We write a power of $\rho(s)$ as a central torus element times an
element of $H$, by Lemma [lemma-identity-component], and average
the torus part over the components of $G$ so that it becomes central
in all of $G$. The factors from $H$ that accumulate in this
process are collected in $h$; their determinants are roots of unity, so they do not affect
determinant weights (see Lemma [lemma-determinant-weight-from-central-scalar] below). Note that the
direct sum $V$ of the $V_i$ is again semisimple, so
Lemma [lemma-identity-component] applies to it.

Since the component group of
$G$ is finite (Lemma [lemma-connected-components-images-homomorphisms]), we may choose
$m>0$ with $\rho(s)^m\in G^\circ$. By Lemma [lemma-identity-component], we
can write $\rho(s)^m=ct$ with $c\in Z(G^\circ)^\circ$ and $t\in H^\circ$.
Choose representatives $g_1,\ldots,g_b$ of the components of $G$ and
set

$$
z=\prod_{j=1}^bg_jcg_j^{-1},\qquad N=mb.
$$

The element $c$ is central in $G^\circ$ but perhaps not in $G$, since
the other components may conjugate it nontrivially. The product $z$ of its
conjugates, one for each component, is however central in $G$.
Indeed, the factors lie in the abelian group $Z(G^\circ)^\circ$, and since replacing
$g_j$ by $g_ju$ with $u\in G^\circ$ does not change the corresponding
factor, conjugation by an element of $G$ permutes the
factors. Next, every commutator lies in $H$, so each factor has the same image
as $c$ in $G/H$. Since $c\in H\rho(s)^m$, we get $z\in H\rho(s)^{mb}$, which
gives $h$ and $N=mb>0$.

Being central in $G$, the element $z$ commutes with the action of $W(U_0)$ on
tensor constructions. Moreover, as noted after the definition of tensor constructions,
every $W(U_0)$-stable subspace of a tensor construction is $G$-stable. Hence
$z$ acts on the $W(U_0)$-stable subquotients and commutes with the action of
$W(U_0)$ on them. On a simple subquotient, therefore, an eigenspace of $z$ is nonzero and
$W(U_0)$-stable, hence is the whole space; in other words, $z$ acts by a scalar.
