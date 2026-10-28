+++
kind  = "proof"
of    = "sk-prop-sf-pf-coherence"
+++
Naturality is that of the mate construction, which uses only the natural units
and counits. For $f=\mathrm{id}$ the two adjunctions are the identity
adjunction and the mate of the identity is the identity. In the pentagon both
sides are mates of the same composite of the two component mate constructions,
because the units and counits of composite adjunctions are the pasted ones and
pasting of mates is associative; the associativity of the derived tensor
product identifies the two tensor reassociations. Independence of the
compactification is the compatibility of the refinement comparisons with the
counits and with $j_!$, together with naturality and
prop:compactification-coherence. Compatibility with base change: choose
a compactification $f=p\circ j$ and base change it along $g$ to
$f'=p'\circ j'$, with $\bar g':\overline X'\to\overline X$ over $g$; by
[det-def-sf-exchanges] and [sk-prop-sf-comp-proper], $\operatorname{Ex}_!$
is the identification $L\bar g'^*j_!\cong j'_!Lg'^*$ followed by the
proper-base-change exchange $\operatorname{Ex}_*$ for $p$. On the $j_!$
factor both composites take values in the essential image of $j'_!$, where a
map is determined by its restriction to $X'$, and both restrict to the
identity. On the $p$ factor, for $M$ on $\overline X$:
$\operatorname{PF}_{p,M,L}$ is the transpose under $Lp^*\dashv Rp_*$ of
$\varepsilon_p\otimes1$ ($\varepsilon_p$ the counit) read through the
monoidality of $Lp^*$, and $\operatorname{Ex}_*$ is the mate of
$L\bar g'^*Lp^*\cong Lp'^*Lg^*$ under $Lp^*\dashv Rp_*$ and
$Lp'^*\dashv Rp'_*$; transposing the two composites
$Lg^*(Rp_*M\otimes^LL)\to Rp'_*(L\bar g'^*M\otimes^LLp'^*Lg^*L)$ under
$Lp'^*\dashv Rp'_*$ gives, by the pasting compatibility of mates
([sk-lem-sf-mate]) and the triangle identity for $p$, one and the same map
$Lp'^*Lg^*(Rp_*M\otimes^LL)\to L\bar g'^*M\otimes^LLp'^*Lg^*L$, namely
$L\bar g'^*\varepsilon_p\otimes1$ read through the monoidality isomorphisms;
so the two composites are mates of the same composite. (The same computation
with an arbitrary $L'\in\Dctf(Y',\Lambda)$ in place of $Lg^*L$ identifies
$\operatorname{PF}_{p'}\circ(\operatorname{Ex}_*\otimes1):
Lg^*Rp_*M\otimes^LL'\to Rp'_*(L\bar g'^*M\otimes^LLp'^*L')$ with the
transpose of $L\bar g'^*\varepsilon_p\otimes1$; this is the form used for the
symmetry of the relative product in [sk-thm-sf-kunneth-relative].) The
last clause is [det-prop-sf-pf-reduction], [sk-thm-sf-pf-field] and
[sk-thm-sf-pf-proetale].
