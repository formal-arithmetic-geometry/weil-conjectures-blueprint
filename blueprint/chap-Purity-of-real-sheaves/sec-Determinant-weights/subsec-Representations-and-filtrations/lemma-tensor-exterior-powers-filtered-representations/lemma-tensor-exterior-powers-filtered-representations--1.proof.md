+++
kind = "proof"
of = "lemma-tensor-exterior-powers-filtered-representations--1"
order = 1124004
uses = []
+++
First reduce the first tensor factor. For a stable subspace $C\subseteq V$,
suppose that $Q=S/(U\cap S)$ is a simple subquotient of $C\otimes_k V'$.
We argue by induction on the stable subspaces $C$, ordered by strict
inclusion. The case $C=0$ is impossible, since $Q$ is nonzero. Otherwise
choose a maximal proper stable subspace $D\subsetneq C$, so that $C/D$
is simple. Tensoring the quotient sequence gives an exact sequence

$$
D\otimes_k V'\xrightarrow{\iota}C\otimes_k V'
\xrightarrow{\pi}(C/D)\otimes_k V'\longrightarrow0.
$$

If $\operatorname{im}(\iota)\cap S\subseteq U$, the map $\pi$ identifies
$Q$ with $\pi(S)/\pi(U\cap S)$. Otherwise the image of
$\operatorname{im}(\iota)\cap S$ in the simple representation $Q$ is
nonzero and hence all of $Q$. Pulling $S$ and $U$ back along $\iota$
therefore presents $Q$ as a subquotient of $D\otimes_k V'$, to which the
induction hypothesis applies. This is
`Subrepresentation.exists_subquotient_tprod_equiv_of_subrepresentation`;
the quotient identifications use
`Subrepresentation.subquotientEquivOfIntertwiningMap`.

Taking $C=V$ gives
`Subrepresentation.exists_subquotient_tprod_left_equiv`: $Q$ is a
subquotient of $A\otimes_k V'$ for a simple subquotient $A$ of $V$.
Interchange the tensor factors, apply the same result to $V'$, and
interchange them back. Composing the resulting equivariant isomorphisms
gives a subquotient of $A\otimes_k B$ as asserted. This argument does
not construct a filtration or compare multiplicities.
