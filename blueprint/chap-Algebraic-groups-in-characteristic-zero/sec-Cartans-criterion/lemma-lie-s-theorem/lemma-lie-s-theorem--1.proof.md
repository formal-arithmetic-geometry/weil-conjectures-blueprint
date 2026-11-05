+++
kind = "proof"
of = "lemma-lie-s-theorem--1"
order = 1728002
uses = []
+++
The theorem `LieModule.exists_nontrivial_weightSpace_of_isSolvable`
gives a linear functional $\lambda$ for which the common eigenspace

$$
M_\lambda=\{m\in M:am=\lambda(a)m\text{ for all }a\in\mathfrak l\}
$$

is nonzero. Its proof first passes to the image of $\mathfrak l$ in
$\operatorname{End}(M)$, which is finite-dimensional. Induction on the
dimension of this image gives a common eigenspace for an ideal of
codimension one. The trace argument in
`LieModule.weightSpaceOfIsLieTower` shows that this eigenspace is stable
under the whole algebra, and the hypothesis on generalized eigenspaces
then gives an eigenvector for the remaining direction. Pulling the
weight back to $\mathfrak l$ gives the assertion about $M_\lambda$.

Choose $0\ne v\in M_\lambda$. For $a,b\in\mathfrak l$, the representation
identity gives

$$
\lambda([a,b])v=[a,b]v=a(bv)-b(av)
=\bigl(\lambda(b)\lambda(a)-\lambda(a)\lambda(b)\bigr)v=0.
$$

Since $v\ne0$, we have $\lambda([a,b])=0$. The derived algebra is the
linear span of these brackets, so linearity gives
$\lambda([\mathfrak l,\mathfrak l])=0$.
