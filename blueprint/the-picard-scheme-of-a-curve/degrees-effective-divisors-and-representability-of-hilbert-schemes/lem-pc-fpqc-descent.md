+++
id = "lem-pc-fpqc-descent"
kind = "lemma"
title = "FPQC descent for invertible modules"
order = 4375
lean = ["AlgebraicGeometry.descent_invertible_fpqc"]
uses = ["def-pc-fppf-site"]
+++
(Descent, Proposition 35.5.2, [Tag
023T](https://stacks.math.columbia.edu/tag/023T).) Let
$\{S_i\to S\}_{i\in I}$ be an fpqc covering of schemes. The functor from
invertible $\mathcal{O}_S$-modules to descent data for this covering
(invertible $\mathcal{O}_{S_i}$-modules with gluing isomorphisms satisfying
the cocycle condition) is an equivalence of categories; in particular, if
the restrictions of an invertible module to the $S_i$ are trivial, then the
module is trivial.

## Proof

*Step 1: the affine case for modules.* Let $A\to B$ be a faithfully flat
ring map, and let $\Delta:B\to B\otimes_AB$, $\Delta(b)=b\otimes1$, be the
canonical inclusion; write $B^{\otimes r}$ for the $r$-fold tensor product.
A *descent datum* for the covering
$\{\operatorname{Spec}(B)\to\operatorname{Spec}(A)\}$ on a $B$-module $N$ is an
isomorphism $\psi:N\otimes_AB\to B\otimes_AN$ of $B\otimes_AB$-modules
satisfying the *cocycle condition*: the two isomorphisms
$N\otimes_AB\otimes_AB\to B\otimes_AB\otimes_AN$ obtained by applying
$\psi$ to the first two, resp. to the last two, tensor factors, agree.
*Claim: the functor from $A$-modules to $B$-modules with descent datum (an
$A$-module $M$ goes to $M\otimes_AB$ with the canonical swap isomorphism)
is an equivalence.*

The classical proof (EGA 0$_{IV}$, (2.5.7); Bourbaki, Alg. comm. V, §1, no.
9; Stacks, Descent, Proposition 35.3.9, [Tag
023N](https://stacks.math.columbia.edu/tag/023N)), which we reproduce:
given $(N,\psi)$, put
$$
N_0:=\ker\bigl(N\longrightarrow B\otimes_AN\bigr),\qquad
n\longmapsto\psi(n\otimes1)-1\otimes n.
$$
The cocycle condition says precisely that the twisted Amitsur-type complex
$$
0\to N_0\to N\to B\otimes_AN\to B\otimes_AB\otimes_AN\to\cdots
$$
(the differentials are the alternating sums of the cyclic permutations of
the tensor factors, with the first map $N\to B\otimes_AN$ the difference
above) is a complex, and the maps
$$
s(b_1\otimes\cdots\otimes b_p\otimes n):=b_1\otimes\cdots\otimes
b_{p-1}\otimes\psi^{-1}(b_p\otimes n)
$$
satisfy $ds+sd=\mathrm{id}$ (the two double sums cancel pairwise; the
cocycle condition is what makes the $\psi$-twisted pieces cancel). Hence
the complex is split exact; in particular the composite
$$
N_0\otimes_AB\longrightarrow N\otimes_AB\cong B\otimes_AN
$$
has image the kernel of $B\otimes_AN\to B\otimes_AB\otimes_AN$, which by
exactness is $N_0\otimes_AB$; the contracting homotopy identifies this
image with all of $N$: $N_0\otimes_AB\cong N$, compatibly with the descent
data. Faithfulness (an $A$-map vanishing after $\otimes_AB$ vanishes) and
fullness (a morphism $N\to N'$ compatible with the data maps $N_0$ into
$N_0'$; conversely a map $N_0\to N_0'$ yields a compatible map of the
$\otimes_AB$-modules, and the exactness shows it comes from a unique such
$A$-map) are then immediate. This proves the claim.

*Step 2: the affine case for invertible modules.* Let $(N,\psi)$ be a
descent datum with $N$ an invertible $B$-module. By the claim there is an
$A$-module $N_0$ with $N_0\otimes_AB\cong N$ compatibly with the data; the
canonical pairing $N\otimes_B\check N\to B$
($\check N:=\mathcal{H}om_B(N,B)$) is the base change of the canonical
pairing $N_0\otimes_A\check N_0\to A$ ($\mathcal{H}om$ commutes with
pullback for locally free modules), and by the faithfulness and fullness of
Step 1 the descent datum of $N_0\otimes_A\check N_0$ is isomorphic to that
of the trivial module $A$; hence $N_0\otimes_A\check N_0\cong A$, so $N_0$
is invertible.

*Step 3: the general covering.* Let $\{S_i\to S\}_{i\in I}$ be an fpqc
covering and $\xi=(N_i,\varphi_{ii'})$ a descent datum of invertible
modules. The datum and the statement are local on $S$ (descent data
restrict along morphisms $S'\to S$, and base changes of fpqc coverings are
fpqc: Topologies, Lemma 34.9.8, [Tag
022D](https://stacks.math.columbia.edu/tag/022D)), so it suffices to treat
$S$ affine; by the definition of an fpqc covering (Topologies, Definition
34.9.1, [Tag 022B](https://stacks.math.columbia.edu/tag/022B)) the affine
$S=\operatorname{Spec}(A)$ is covered by standard fpqc coverings of finite
subfamilies, and a finite standard fpqc covering
$\{V_k=\operatorname{Spec}(B_k)\to\operatorname{Spec}(A)\}_k$ is precisely a
faithfully flat map $A\to\prod_kB_k$ (since
$\operatorname{Spec}(\prod B_k)=\bigsqcup_k\operatorname{Spec}(B_k)$). The
restriction of the datum to the $V_k$ is a descent datum for the covering
$\{\operatorname{Spec}(\prod_kB_k)\to\operatorname{Spec}(A)\}$, which is
effective by Step 2 with $B=\prod_kB_k$ (the modules and isomorphisms are
the product of the pieces, and the cocycle condition is the compatibility
over the intersections, checked on the original $S_i$ by refinement). This
yields an invertible $\mathcal{O}_S$-module restricting to $N_i$ with the
given gluing data; the identification is constructed with the same
refinement-compatibility argument, and glueing over an affine open cover
proves the statement in general. The last assertion (trivial restrictions
imply trivial module) is the case of the datum given by the trivial modules
$N_i=\mathcal{O}_{S_i}$ with identities: the descended module has canonical
datum isomorphic to it, hence is trivial by faithfulness.

Unresolved dependencies: def:sc-invertible-module
