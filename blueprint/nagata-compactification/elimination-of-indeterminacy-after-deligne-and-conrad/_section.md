+++
id = "elimination-of-indeterminacy-after-deligne-and-conrad"
kind = "section"
title = "Elimination of indeterminacy after Deligne and Conrad"
order = 378
+++
This section is the formalized route to
[lemma-nagata-elimination-indeterminacy] (Stacks Tag 081S), which the
modification layer consumes: the common modification, the graph extension and
the isomorphism near the closure of a boundary piece are all built from its
construction [def-nagata-elimination-indeterminacy]. Both stand at the end of
this section, after Conrad's Theorem 2.4 that proves them. It follows Deligne's notes as
written up by Conrad
[ConradNagata]: two blow-up lemmas of Deligne
(*Lemme* 0.2 and *Lemme* 0.3, which are Lemmas 1.4 and 1.5 of
*loc. cit.*), and then Conrad's Theorem 2.4 (Deligne's
*Théorème* 1.2, Nagata's Theorem 3.2): a rational map to a separated
finite-type target becomes defined, in the precise sense of a quasi-domination,
after a single admissible blow-up of the source. The proof is a chain of four
special cases, the last of which uses Zariski's Main Theorem to replace an
arbitrary target by a quasi-affine one.

The Stacks Project's route through Raynaud–Gruson flattening by blow-up
(Stacks Tags 0815, 081R, 081P, 081L) is not the formalized one and is not
recorded; see the route remark closing this section. This section is formalized: most statements
below carry a non-empty `\lean` field naming the declaration that realizes
them, up to Conrad's Theorem 2.4 itself
(`AlgebraicGeometry.exists_admissibleBlowup_extend_partialSection`) and its
$U=V$ corollary.

Throughout, $S$ is a quasi-compact and quasi-separated base scheme and all
fibre products of $S$-schemes are taken over $S$ unless another base is
displayed. We freely use the affine blow-up charts of
[def-nagata-blowup-chart-ring]: for an ideal $I\subseteq A$ and $s\in I$
we write

$$
U(s)=\operatorname{Spec}\bigl(A[I/s]\bigr)
\subseteq\operatorname{Bl}_I(\operatorname{Spec}A),
$$

the open locus on which the extended ideal $I\cdot\mathcal O$ is invertible
with global basis $s$; by
[prop-nagata-affine-blowup-chart-cover] these charts, taken over a
generating set of $I$, cover the blow-up.
