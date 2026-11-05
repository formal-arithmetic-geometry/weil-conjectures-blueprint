+++
kind = "proof"
of = "lemma-removing-finitely-many-points"
order = 1609
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-underived-base-change-map", "lemma-finite-morphisms", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms"]
+++
The third term of the exact sequence displayed above is supported on the finite set $Z$, so
by Lemma [lemma-sheaves-finite-support-finite-morphisms] it has finite sections and no
higher cohomology. Comparing the long exact sequences of $F$ and
$j_!j^*F$ then shows that each assertion passes in both directions.

The sheaf $j_!j^*F$ is again killed by $\ell$, so the hypotheses
on the coefficient prime are the same for both sheaves. Since the last
term of the exact sequence has no positive cohomology, the long exact
sequence yields

$$
\begin{split}
0\to H^0(C,j_!j^*F)\to H^0(C,F)\to H^0(Z,i^*F)\to{}\qquad\qquad\\
H^1(C,j_!j^*F)\to H^1(C,F)\to0,
\end{split}
$$

and isomorphisms in degrees at least two. Since the sequence is natural
under field extension and its term supported on $Z$ is unchanged,
the two long exact sequences show that the pullback maps
are isomorphisms for $F$ in all degrees if and only if they are
isomorphisms for $j_!j^*F$ in all degrees. For $(C_8)$, we apply the
degree-two identifications after restriction to every open subset of
$C$. See also [Stacks, [0GJA](https://stacks.math.columbia.edu/tag/0GJA)].
