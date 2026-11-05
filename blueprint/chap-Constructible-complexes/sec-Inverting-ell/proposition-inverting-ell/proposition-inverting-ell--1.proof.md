+++
kind = "proof"
of = "proposition-inverting-ell--1"
order = 303001
uses = ["lemma-continuity-ext-out-constructible-complex"]
+++
After restriction of scalars, $F(L)$ is the sequential colimit

$$
L\xrightarrow{\ell}L\xrightarrow{\ell}L\xrightarrow{\ell}\cdots,
$$

whose first map to the colimit is the unit of the extension and
restriction of scalars adjunction. The needed sequential integral
strengthening of [lemma-continuity-ext-out-constructible-complex]
allows arbitrary bounded constructible integral sources, including torsion. It is
proved first for constructible sheaves, then for bounded complexes by
induction along truncation triangles. The stages of this sequence have
the common cohomological lower bound of $L$, so $\Hom(K,-)$ preserves
this colimit.

The equality $F(f)=F(g)$ gives equality of the adjoint maps from $K$
to this colimit. Two representatives of the same element of a filtered
colimit agree at a finite stage. The transition from stage zero to
stage $n$ is multiplication by $\ell^n$, which gives
$\ell^n f=\ell^n g$. For the last assertion, take $L=K$,
$f=\operatorname{id}_K$, and $g=0$.
