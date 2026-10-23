+++
kind  = "proof"
of    = "sk-p-central"
+++
We first construct the central matrix. Since the component group of $G$ is
finite ([sk-p-geometry]), we may choose $m>0$ with $F^m\in G^\circ$. By
[sk-p-product], we can write $F^m=ct$ with $c\in Z(G^\circ)^\circ$ and
$t\in H^\circ$. Choose representatives $g_1,\ldots,g_b$ of the components of
$G$ and set

$$
z=\prod_{j=1}^bg_jcg_j^{-1},\qquad N=mb.
$$

The factors lie in the abelian group $Z(G^\circ)^\circ$, and replacing
$g_j$ by $g_ju$ with $u\in G^\circ$ does not change the corresponding
factor. Therefore conjugation by an element of $G$ permutes the factors,
and $z$ is central in $G$. Since every commutator lies in $H$
([sk-i-restriction]), each factor has the same image as $c$ in $G/H$. As
$c\in HF^m$, it follows that $z\in HF^{mb}$, which gives $h$ and $N>0$.

Next we show that $\widetilde z=(h,N)$ is central in $\widetilde G$. The
commutator of $(h,N)$ with an element of $\widetilde G$ has degree zero,
and it maps to the identity matrix because $z$ is central. Since the
homomorphism to $G(\overline{\mathbf Q}_\ell)$ is injective in degree zero,
this commutator is trivial. The matrix $z$ also commutes with the action of
$W$ on every tensor construction.

Finally, by the stabilizer argument of [sk-i-restriction], every $W$-stable
subspace of an algebraic tensor construction is $G$-stable. Hence $z$ acts
on the $W$-stable subquotients and commutes with the action of $W$ on them.
On a simple subquotient, choose an eigenvalue $c$ of $z$. The corresponding
eigenspace is nonzero and $W$-stable, hence is the whole space, and so
$z=c\,\mathrm{id}$.
