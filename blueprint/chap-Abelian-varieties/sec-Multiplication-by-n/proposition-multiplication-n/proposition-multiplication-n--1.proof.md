+++
kind = "proof"
of = "proposition-multiplication-n--1"
order = 1503003
uses = ["lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n"]
+++
First suppose that $k$ is algebraically closed. Choose an ample
invertible sheaf $\mathcal L$ and put
$\mathcal N=\mathcal L\otimes[-1]^*\mathcal L$. By
[lemma-symmetric-ample-sheaf], $\mathcal N$ is symmetric and ample,
and [proposition-pullback-multiplication-n] gives
$[n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}$. If $[n]$ were not
locally quasi-finite, its non-quasi-finite locus would contain a closed
point $x$. The fibre through $x$ would have positive dimension and
would contain a nonempty proper closed subscheme $C$ of dimension one.
On $C$, the sheaf $\mathcal N$ remains ample, whereas
$(\mathcal N|_C)^{\otimes n^2}$ is trivial because $[n]$ is constant
on $C$. A positive tensor power of an ample invertible sheaf on such
a scheme cannot be trivial. This proves
`AlgebraicGeometry.locallyQuasiFinite_npow_id_of_isAlgClosed`.

For general $k$, local quasi-finiteness descends from the base change
to an algebraic closure. Since $[n]$ is proper, it is finite. Base
change along the identity section then shows that $A[n]$ is finite.
The scheme-theoretic image $Z$ of $[n]$ is a closed subscheme of $A$,
and the induced map $A\to Z$ is finite and surjective. Thus
$\dim Z=\dim A$. Since $A$ is integral by
[lemma-abelian-variety-commutative], the underlying closed subset of
$Z$ is all of $A$. Hence $[n]$ is surjective.

Put $r=\dim_k\Gamma(A[n],\mathcal O_{A[n]})$. Translation identifies
each fibre of $[n]$, after extension of its residue field, with a
base change of $A[n]$. Consequently all fibres have degree $r$.
The rank formula for a finite morphism of finite presentation to a
reduced scheme with constant fibre degree gives rank $r$ at every
point; this is `AlgebraicGeometry.IsIsogeny.finrank_eq`, applied using
`AlgebraicGeometry.isIsogeny_npow_id`.

Now choose $\mathcal N$ over $k$ as above. The degree formula for a
finite surjective pullback and the degree formula for tensor powers
give

$$
r\deg_{\mathcal N}(A)
=\deg_{[n]^*\mathcal N}(A)
=\deg_{\mathcal N^{\otimes n^2}}(A)
=n^{2g}\deg_{\mathcal N}(A).
$$

Here the two degree formulas are
`AlgebraicGeometry.Scheme.Hom.degree_pullback` and
`AlgebraicGeometry.Scheme.Hom.degree_tensorPow`.
Since $\deg_{\mathcal N}(A)>0$, cancellation gives $r=n^{2g}$.
This is `AlgebraicGeometry.isogenyDegree_npow_id`, and the definition
of the degree as the rank of the kernel gives the displayed formula.
