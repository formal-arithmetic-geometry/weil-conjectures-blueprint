+++
kind = "proof"
of = "sk-lem-curve-dense-open"
uses = ["sk-lem-curve-finite-support", "sk-lem-curve-normalization", "sk-prop-sf-comparison", "sk-lem-pbc-finite", "sk-thm-br"]
+++
The exact sequence is the sequence of classical sheaves associated to an
open and its closed complement. Its exactness can be checked on geometric
stalks on $C_{\mathrm{ét}}$, and we then pull it back. The last term has
finite sections and no positive cohomology ([sk-lem-curve-finite-support]),
and hence the long exact sequence yields

$$
\begin{split}
0\to H^0(C,j_!j^*F)\to H^0(C,F)\to H^0(Z,i^*F)\to{}\qquad\qquad\\
H^1(C,j_!j^*F)\to H^1(C,F)\to0,
\end{split}
$$

and isomorphisms in degrees at least two. If $F$ is killed by a prime
$\ell$, so are $j_!j^*F$ and $i_*i^*F$; then $F$ and $j_!j^*F$ fall
under the same assertions, and each of them transfers in both
directions: the vanishing assertions and $(C_8)$ through the
isomorphisms in degrees at least two (applied to $C$ and to each open
subset), finiteness through the exact sequence, whose term
$H^0(Z,i^*F)$ is finite, and the invariance assertions by the five
lemma, since the sequence is natural under field extension and its term
supported on $Z$ is unchanged. This is the only case used in the proof
of the theorem on the cohomology of curves (the curve package). For a
general constructible torsion $F$, both sides hold by that theorem. The five
lemma alone would not suffice there: if $F=j_!A\oplus B$ with $A$
$p$-primary and $B$ of torsion prime to $p$ and supported on $Z$, then
$j_!j^*F=j_!A$ is $p$-primary while $F$ is not, so $(C_3)$ for
$j_!j^*F$ does not follow from the assertions for $F$. See also (Stacks,
Tag 0GJA).

*Consequence.* If $j$ is dense, this lemma and the calculation for constant
$\mathbf F_\ell$ on $C$ via [sk-lem-curve-normalization] show that
$j_!\underline{\mathbf F_\ell}$ satisfies the assertions $(C_1)$–$(C_8)$ of
[def-weil-pbc-eight-curve-assertions]. An
arbitrary open is dense in the reduced union of the components it meets,
which is a closed subscheme of $C$. Apply the dense case there and pass back
to $C$, using that direct image along a finite morphism is exact (Stacks,
Tag 0A3Q) and does not change cohomology ([sk-lem-curve-finite-support]).
