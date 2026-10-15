+++
kind = "proof"
of = "sk-lem-curve-dense-open"
uses = ["sk-lem-curve-finite-support", "sk-lem-curve-normalization", "sk-prop-sf-comparison"]
+++
The exact sequence is the open–closed sequence of classical sheaves; it can be
checked on geometric stalks on $C_{\mathrm{ét}}$ and then pulled back. The
last term has finite sections and no positive cohomology
([sk-lem-curve-finite-support]), so the long exact sequence gives

$$
\begin{split}
0\to H^0(C,j_!j^*F)\to H^0(C,F)\to H^0(Z,i^*F)\to{}\qquad\qquad\\
H^1(C,j_!j^*F)\to H^1(C,F)\to0,
\end{split}
$$

and isomorphisms in degrees at least two. The sequence is natural under field
extension and its point term is unchanged, so the five lemma gives the
equivalence of the invariance assertions. For $(C_8)$ apply the same
identifications in degree two to each open subset of $C$. See also (Stacks,
Tag 0GJA).

*Consequence.* In particular $j_!\underline{\mathbf F_r}$ satisfies the
assertions $(C_1)$–$(C_8)$ when $j$ is dense, by [sk-lem-curve-normalization]
and the constant calculation. For an arbitrary open, apply this on the
reduced union of the components it meets, which is a closed subscheme, and
use exactness of finite direct image. Alternatively, shrink to the dense
regular open of the normalization and use [sk-lem-curve-finite-support];
this is the route of (Stacks, Tag 0A3Q).
