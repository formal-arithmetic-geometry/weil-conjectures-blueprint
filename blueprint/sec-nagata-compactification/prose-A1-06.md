+++
id = "prose-A1-06"
kind = "hidden"
title = "Strict transforms under a blow-up"
order = 127
+++
For a morphism $W\to T$ and a blow-up $T'\to T$, the strict
transform of $W$ is the closed subscheme of $W\times_TT'$ obtained
by removing the sections of its structure sheaf supported on the
inverse image of the exceptional divisor. Over a chart with equation $a$
on which $W\times_TT'$ is affine with ring $B$, the ring of the strict transform is

$$
B/\{b\in B:\ a^nb=0\text{ for some }n\geq0\}.
$$

If $U$ is the complement of the center, this is exactly the schematic
closure of $W_U$ in $W\times_TT'$, and this closure is what occurs in
the elimination of indeterminacy.
The strict transform is the blow-up of $W$ in the pulled-back ideal
[Stacks, Tag 080E](https://stacks.math.columbia.edu/tag/080E), and hence it is proper over $W$.

The proofs below produce blow-ups locally and one after another. The
next lemma lets us turn finitely many such local constructions into a
single admissible blow-up of $T$ that preserves $U$.
