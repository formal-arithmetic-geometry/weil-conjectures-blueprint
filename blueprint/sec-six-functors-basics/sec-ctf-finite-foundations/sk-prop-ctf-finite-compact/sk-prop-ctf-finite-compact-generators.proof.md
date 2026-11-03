+++
kind = "proof"
of = "det-ctf-finite-compact-generators"
+++
*Thick and small.* Constructibility and finite Tor amplitude are preserved by shifts, cones and direct
summands, so $\Dctf(X,A)$ is thick. It is a full subcategory of the essentially small bounded constructible
category, so it is essentially small; choose a small skeleton $G$.

*Generation.* If $K\in\Loc(\Dctf(X,A))$ has $\Hom(C[n],K)=0$ for all $C\in G$, $n\in\mathbf Z$, then the objects
$M$ with $\Hom(M[n],K)=0$ for all $n$ form a localizing subcategory containing $\Dctf(X,A)$, hence containing
$K$; so $\mathrm{id}_K=0$. With [det-ctf-finite-compact-proetale], $G$ is a set of compact generators.

*Compact objects.* In a compactly generated triangulated category with a set $G$ of compact generators
closed under shifts, the compact objects are exactly the direct summands of finite extensions of objects of
$G$, i.e. the thick closure of $G$ (Stacks, Tag 09SN; the key step, Stacks, Tag 09SM, is that a map from a
compact object to a sum, or to a homotopy colimit of finite extensions of generators, factors through a
finite stage). The thick closure of $G$ is $\Dctf(X,A)$, since this is thick and contains $G$, and every
object of it is isomorphic to one in $G$. Hence $\Loc(\Dctf(X,A))^c=\Dctf(X,A)$.
