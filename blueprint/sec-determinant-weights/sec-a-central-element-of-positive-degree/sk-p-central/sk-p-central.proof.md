+++
kind = "proof"
of = "sk-p-central"
+++
We write a power of $\rho(s)$ as a central torus element times an
element of $H$, by Lemma [sk-p-product], and average
the torus part over the components of $G$ so that it becomes central
in all of $G$. Since the component group of
$G$ is finite (Lemma [sk-p-geometry]), we may choose
$m>0$ with $\rho(s)^m\in G^\circ$. By Lemma [sk-p-product], we
can write $\rho(s)^m=ct$ with $c\in Z(G^\circ)^\circ$ and $t\in H^\circ$.
Choose representatives $g_1,\ldots,g_b$ of the components of $G$ and
set

$$
z=\prod_{j=1}^bg_jcg_j^{-1},\qquad N=mb.
$$

The factors lie in the abelian group $Z(G^\circ)^\circ$, and replacing
$g_j$ by $g_ju$ with $u\in G^\circ$ does not change the corresponding
factor. Therefore conjugation by an element of $G$ permutes the
factors, and $z$ is central in $G$. Since every commutator lies in
$H$, each factor has the same image as $c$ in $G/H$. As $c\in H\rho(s)^m$,
it follows that $z\in H\rho(s)^{mb}$, which gives $h$ and $N=mb>0$.

Finally, we consider the action on tensor constructions. Since $z$ is
central in $G$, it commutes with the action of $W(U_0)$ on every tensor
construction. As noted after the definition of tensor constructions,
every $W(U_0)$-stable subspace of a tensor construction is $G$-stable. Hence $z$ acts on
the $W(U_0)$-stable subquotients and commutes with the action of $W(U_0)$ on
them. On a simple subquotient, an eigenspace of $z$ is nonzero and
$W(U_0)$-stable, hence is the whole space, and so $z$ acts by a scalar.
