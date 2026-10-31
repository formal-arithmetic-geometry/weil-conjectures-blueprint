+++
kind = "proof"
of = "sk-lem-curve-dense-open"
uses = ["sk-lem-curve-finite-support", "sk-lem-curve-normalization", "sk-prop-sf-comparison", "sk-lem-pbc-finite", "sk-thm-br"]
+++
The exact sequence is the sequence of classical sheaves associated to an
open and its closed complement. Its exactness can be checked on
geometric stalks on $C_{\acute{e}t}$, and we then pull it back. The last term
has finite sections and no positive cohomology, and hence the long exact
sequence yields

$$
\begin{split}
0\to H^0(C,j_!j^*F)\to H^0(C,F)\to H^0(Z,i^*F)\to{}\qquad\qquad\\
H^1(C,j_!j^*F)\to H^1(C,F)\to0,
\end{split}
$$

and isomorphisms in degrees at least two. The sequence is natural
under field extension and its term supported on $Z$ is unchanged.
The two long exact sequences therefore show that the pullback maps
are isomorphisms for $F$ in all degrees if and only if they are
isomorphisms for $j_!j^*F$ in all degrees. For $(C_8)$, we apply the
degree-two identifications after restriction to every open subset of
$C$. If $\ell F=0$, then $j_!j^*F$ is also killed by $\ell$, so
removing $Z$ does not change the coefficient prime. See also
[Stacks, Tag 0GJA](https://stacks.math.columbia.edu/tag/0GJA).
